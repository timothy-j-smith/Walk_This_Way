import asyncio
import importlib.util
import json
import sys
import types
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
AUTHOR_SERVER_PATH = MCP_ROOT / "AUTHOR_ENGINES" / "author_server.py"
STYLE_SERVER_PATH = MCP_ROOT / "STYLE_EMULATION_MCP" / "server.py"
MANUSCRIPT_BUILDER_PATH = (
    REPOSITORY_ROOT / "Draft_05" / "build_complete_manuscript.py"
)


class FakeServer:
    def __init__(self, name):
        self.name = name

    def list_tools(self):
        return lambda function: function

    def call_tool(self):
        return lambda function: function


class FakeMcpValue:
    def __init__(self, **values):
        self.__dict__.update(values)


def fake_mcp_modules():
    mcp = types.ModuleType("mcp")
    server = types.ModuleType("mcp.server")
    stdio = types.ModuleType("mcp.server.stdio")
    mcp_types = types.ModuleType("mcp.types")

    server.Server = FakeServer
    server.stdio = stdio
    mcp.server = server
    mcp_types.Tool = FakeMcpValue
    mcp_types.TextContent = FakeMcpValue

    return {
        "mcp": mcp,
        "mcp.server": server,
        "mcp.server.stdio": stdio,
        "mcp.types": mcp_types,
    }


def load_module(module_name, path, argv=None, stub_mcp=False):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    modules = fake_mcp_modules() if stub_mcp else {}
    command_line = argv or [str(path)]
    with (
        patch.dict(sys.modules, modules),
        patch.object(sys, "argv", command_line),
    ):
        spec.loader.exec_module(module)
    return module


def result_body(results):
    return json.loads(results[0].text)


class AuthorEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(
            "test_author_engine",
            AUTHOR_SERVER_PATH,
            [str(AUTHOR_SERVER_PATH), "--author", "king"],
            stub_mcp=True,
        )

    def test_registered_tools_route_to_the_expected_default_modes(self):
        tools = asyncio.run(self.module.list_tools())
        self.assertEqual(
            [tool.name for tool in tools],
            ["king_guide", "king_imagine", "king_craft", "king_revise"],
        )

        cases = (
            ("king_imagine", "CREATE (Architecture)", "nice"),
            ("king_craft", "TRANSFORM (Brick support)", "neutral"),
            ("king_revise", "EDIT (Scalpel & Hose)", "professional"),
        )
        for tool_name, mode, liberty in cases:
            with self.subTest(tool=tool_name):
                body = result_body(
                    asyncio.run(self.module.call_tool(tool_name, {}))
                )
                self.assertEqual(body["mode"], mode)
                self.assertEqual(body["liberty_level"], liberty)
                self.assertEqual(
                    body["student_input"],
                    "(none provided - ask for it)",
                )

    def test_guide_slices_known_sections_and_rejects_unknown_tools(self):
        guide = result_body(
            asyncio.run(
                self.module.call_tool(
                    "king_guide",
                    {"section": "pitfalls"},
                )
            )
        )
        self.assertIn("pitfalls", guide)
        self.assertNotIn("signature_moves", guide)

        unknown = asyncio.run(
            self.module.call_tool("king_not_a_tool", None)
        )
        self.assertEqual(unknown[0].text, "Unknown tool: king_not_a_tool")


class StyleEmulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(
            "test_style_emulation",
            STYLE_SERVER_PATH,
            stub_mcp=True,
        )

    def test_style_metrics_are_deterministic_with_optional_readability(self):
        textstat = types.ModuleType("textstat")
        textstat.flesch_kincaid_grade = lambda text: 4.25
        textstat.flesch_reading_ease = lambda text: 88.5

        with patch.dict(sys.modules, {"textstat": textstat}):
            metrics = self.module.measure_style(
                'Hello there. "Run now!" Run now?'
            )

        self.assertEqual(
            metrics,
            {
                "word_count": 6,
                "sentence_count": 3,
                "avg_sentence_length": 2.0,
                "dialogue_spans": 1,
                "unique_words": 4,
                "lexical_diversity": 0.667,
                "flesch_kincaid_grade": 4.25,
                "reading_ease": 88.5,
            },
        )

    def test_master_aliases_load_and_unknown_masters_return_choices(self):
        king = self.module.load_kb(" Stephen King ")
        self.assertEqual(king["key"], "king")
        self.assertEqual(king["name"], "Stephen King")
        self.assertEqual(
            king["quick_signature"]["primary_move"],
            "Ordinary made holy. Working-class register taken seriously",
        )

        unknown = self.module.load_kb("not-a-master")
        self.assertEqual(unknown["error"], "Unknown master 'not-a-master'")
        self.assertIn("lehane", unknown["available"])

    def test_tool_routing_preserves_material_and_reports_metric_deltas(self):
        packet = result_body(
            asyncio.run(
                self.module.call_tool(
                    "emulate_paragraph",
                    {"author": "king", "text": "The original line."},
                )
            )
        )
        self.assertEqual(packet["engine"], "Stephen King")
        self.assertEqual(packet["student_material"], "The original line.")
        self.assertFalse(packet["keep_the_emulation"])

        textstat = types.ModuleType("textstat")
        textstat.flesch_kincaid_grade = lambda text: 0
        textstat.flesch_reading_ease = lambda text: 0
        with patch.dict(sys.modules, {"textstat": textstat}):
            comparison = result_body(
                asyncio.run(
                    self.module.call_tool(
                        "analyze_style_match",
                        {
                            "your_text": "One short sentence.",
                            "target_text": "One. Two.",
                            "target_author": "Target",
                        },
                    )
                )
            )

        self.assertEqual(comparison["target_author"], "Target")
        self.assertEqual(
            comparison["deltas"]["avg_sentence_length"],
            2.0,
        )
        self.assertEqual(
            comparison["deltas"]["lexical_diversity"],
            0.0,
        )


class ManuscriptBuilderTests(unittest.TestCase):
    def test_builders_strip_source_headers_and_escape_markdown_prose(self):
        module = load_module(
            "test_manuscript_builder",
            MANUSCRIPT_BUILDER_PATH,
        )
        source = (
            "ACT I: SOURCE TITLE\r\n\r\n"
            "CHAPTER 1: \u201cSOURCE CHAPTER\u201d\r\n\r\n"
            "A & <B>.\r\nline two\r\n\r\n"
            "---\r\n\r\n"
            "Second paragraph."
        )

        with TemporaryDirectory() as temporary_directory:
            draft_dir = Path(temporary_directory)
            (draft_dir / "chapter.txt").write_text(
                source,
                encoding="utf-8",
            )
            with (
                patch.object(module, "DRAFT_DIR", draft_dir),
                patch.object(
                    module,
                    "CHAPTERS",
                    [(1, "chapter.txt", "OUTPUT TITLE", "Output Title")],
                ),
                patch.object(
                    module,
                    "ACTS",
                    [("ACT I", "TEST ACT", range(1, 2))],
                ),
            ):
                markdown = module.build_markdown()
                plain_text = module.build_plain_text()

        self.assertIn("Chapter 1 \u2014 \"Output Title\"", markdown)
        self.assertIn(
            "<p>A &amp; &lt;B&gt;. line two</p>",
            markdown,
        )
        self.assertNotIn("SOURCE CHAPTER", markdown)
        self.assertIn('\tA & <B>. line two', plain_text)
        self.assertEqual(
            plain_text.count('CHAPTER 1: "OUTPUT TITLE"'),
            1,
        )
        self.assertNotIn("---", plain_text)


if __name__ == "__main__":
    unittest.main()
