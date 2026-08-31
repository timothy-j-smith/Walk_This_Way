import asyncio
import contextlib
import importlib.util
import io
import json
import runpy
import subprocess
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
AUTHOR_ROOT = MCP_ROOT / "AUTHOR_ENGINES"
AUTHOR_SERVER_PATH = AUTHOR_ROOT / "author_server.py"
STYLE_SERVER_PATH = MCP_ROOT / "STYLE_EMULATION_MCP" / "server.py"


class FakeMcpValue:
    def __init__(self, **values):
        self.__dict__.update(values)


class FakeTransport:
    def __init__(self):
        self.entered = False
        self.exited = False

    async def __aenter__(self):
        self.entered = True
        return "read-stream", "write-stream"

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.exited = True


class FakeServer:
    instances = []

    def __init__(self, name):
        self.name = name
        self.run_calls = []
        self.transports = []
        self.instances.append(self)

    def list_tools(self):
        return lambda function: function

    def call_tool(self):
        return lambda function: function

    def create_initialization_options(self):
        return "initialization-options"

    async def run(self, read_stream, write_stream, initialization_options):
        self.run_calls.append(
            (read_stream, write_stream, initialization_options)
        )


def build_fake_mcp_modules():
    transports = []

    def stdio_server():
        transport = FakeTransport()
        transports.append(transport)
        return transport

    mcp_module = types.ModuleType("mcp")
    server_module = types.ModuleType("mcp.server")
    stdio_module = types.ModuleType("mcp.server.stdio")
    types_module = types.ModuleType("mcp.types")

    server_module.Server = FakeServer
    server_module.stdio = stdio_module
    stdio_module.stdio_server = stdio_server
    types_module.TextContent = FakeMcpValue
    types_module.Tool = FakeMcpValue
    mcp_module.server = server_module

    modules = {
        "mcp": mcp_module,
        "mcp.server": server_module,
        "mcp.server.stdio": stdio_module,
        "mcp.types": types_module,
    }
    return modules, transports


def load_server_module(path, module_name, argv=None):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {path}")

    module = importlib.util.module_from_spec(spec)
    fake_modules, _ = build_fake_mcp_modules()
    command_line = argv or [str(path)]
    with (
        patch.dict(sys.modules, fake_modules),
        patch.object(sys, "argv", command_line),
    ):
        spec.loader.exec_module(module)
    return module


def execute_server(path, argv=None):
    fake_modules, transports = build_fake_mcp_modules()
    output = io.StringIO()
    command_line = argv or [str(path)]
    with (
        patch.dict(sys.modules, fake_modules),
        patch.object(sys, "argv", command_line),
        contextlib.redirect_stdout(output),
    ):
        runpy.run_path(str(path), run_name="__main__")
    return output.getvalue(), transports


class AuthorEngineTests(unittest.TestCase):
    def setUp(self):
        FakeServer.instances.clear()

    def test_every_author_knowledge_base_passes_the_server_selftest(self):
        data_files = sorted((AUTHOR_ROOT / "data").glob("*.json"))
        self.assertGreater(len(data_files), 0)

        for data_file in data_files:
            with self.subTest(author=data_file.stem):
                result = subprocess.run(
                    [
                        sys.executable,
                        str(AUTHOR_SERVER_PATH),
                        "--author",
                        data_file.stem,
                        "--selftest",
                    ],
                    cwd=REPOSITORY_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, msg=result.stderr)
                self.assertIn(
                    f"engine loaded ({data_file.name})",
                    result.stdout,
                )

    def test_author_tools_route_to_the_expected_payloads_and_defaults(self):
        module = load_server_module(
            AUTHOR_SERVER_PATH,
            "test_author_engine",
            [str(AUTHOR_SERVER_PATH), "--author", "king"],
        )

        tools = asyncio.run(module.list_tools())
        self.assertEqual(
            [tool.name for tool in tools],
            ["king_guide", "king_imagine", "king_craft", "king_revise"],
        )

        guide = asyncio.run(
            module.call_tool("king_guide", {"section": "pitfalls"})
        )
        guide_payload = json.loads(guide[0].text)
        self.assertEqual(guide_payload["engine"], "Stephen King")
        self.assertEqual(guide_payload["pitfalls"], module.KB["pitfalls"])
        self.assertNotIn("signature_moves", guide_payload)

        imagine = asyncio.run(
            module.call_tool("king_imagine", {"text": "A boy finds a tape."})
        )
        imagine_payload = json.loads(imagine[0].text)
        self.assertEqual(imagine_payload["liberty_level"], "nice")
        self.assertEqual(imagine_payload["mode"], "CREATE (Architecture)")
        self.assertEqual(
            imagine_payload["student_input"],
            "A boy finds a tape.",
        )

        revise = asyncio.run(module.call_tool("king_revise", {}))
        revise_payload = json.loads(revise[0].text)
        self.assertEqual(revise_payload["liberty_level"], "professional")
        self.assertEqual(revise_payload["student_input"], "(none provided - ask for it)")
        self.assertIn("pitfalls", revise_payload)

        unknown = asyncio.run(module.call_tool("king_missing", {}))
        self.assertEqual(unknown[0].text, "Unknown tool: king_missing")


class StyleEmulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_server_module(
            STYLE_SERVER_PATH,
            "test_style_emulation",
        )

    def test_committee_data_loads_and_author_aliases_are_normalized(self):
        for key in self.module.COMMITTEE:
            with self.subTest(author=key):
                knowledge_base = self.module.load_kb(key)
                self.assertNotIn("error", knowledge_base)
                self.assertEqual(knowledge_base["key"], key)
                self.assertTrue(knowledge_base["name"])

        aliased = self.module.load_kb("  Stephen King  ")
        self.assertEqual(aliased["key"], "king")
        self.assertEqual(aliased["name"], "Stephen King")

        unknown = self.module.load_kb("not-on-the-committee")
        self.assertEqual(unknown["available"], sorted(self.module.COMMITTEE))
        self.assertIn("Unknown master", unknown["error"])

    def test_style_metrics_are_deterministic_for_empty_and_punctuated_text(self):
        empty = self.module.measure_style("")
        self.assertEqual(
            {
                key: empty[key]
                for key in (
                    "word_count",
                    "sentence_count",
                    "avg_sentence_length",
                    "dialogue_spans",
                    "unique_words",
                )
            },
            {
                "word_count": 0,
                "sentence_count": 0,
                "avg_sentence_length": 0.0,
                "dialogue_spans": 0,
                "unique_words": 0,
            },
        )
        self.assertNotIn("lexical_diversity", empty)

        measured = self.module.measure_style('Run fast. "Not yet!" Run fast?')
        self.assertEqual(measured["word_count"], 6)
        self.assertEqual(measured["sentence_count"], 3)
        self.assertEqual(measured["avg_sentence_length"], 2.0)
        self.assertEqual(measured["dialogue_spans"], 1)
        self.assertEqual(measured["unique_words"], 4)
        self.assertEqual(measured["lexical_diversity"], 0.667)

    def test_style_tool_routes_preserve_material_and_report_metric_deltas(self):
        scene = asyncio.run(
            self.module.call_tool(
                "emulate_scene",
                {"author": "king", "text": "Nick held the cassette."},
            )
        )
        scene_payload = json.loads(scene[0].text)
        self.assertEqual(scene_payload["student_material"], "Nick held the cassette.")
        self.assertFalse(scene_payload["keep_the_emulation"])
        self.assertEqual(scene_payload["never"], self.module.NEVER)
        self.assertEqual(
            scene_payload["close_with"],
            "Want me to do this in another master's voice for comparison?",
        )

        rejected = asyncio.run(
            self.module.call_tool(
                "emulate_scene",
                {"author": "unknown", "text": "Do not transform this."},
            )
        )
        rejected_payload = json.loads(rejected[0].text)
        self.assertIn("Unknown master", rejected_payload["error"])
        self.assertNotIn("student_material", rejected_payload)

        comparison = asyncio.run(
            self.module.call_tool(
                "analyze_style_match",
                {
                    "your_text": "One two. Three four.",
                    "target_text": "One two three four.",
                    "target_author": "Target",
                },
            )
        )
        comparison_payload = json.loads(comparison[0].text)
        self.assertEqual(comparison_payload["target_author"], "Target")
        self.assertEqual(
            comparison_payload["deltas"],
            {
                "avg_sentence_length": -2.0,
                "lexical_diversity": 0.0,
                "dialogue_spans": 0,
            },
        )


class MfaServerStartupTests(unittest.TestCase):
    def setUp(self):
        FakeServer.instances.clear()

    def test_servers_run_over_stdio_without_protocol_noise(self):
        cases = (
            (
                AUTHOR_SERVER_PATH,
                [str(AUTHOR_SERVER_PATH), "--author", "king"],
                "king-engine",
            ),
            (
                STYLE_SERVER_PATH,
                [str(STYLE_SERVER_PATH)],
                "style-emulation",
            ),
        )

        for path, argv, expected_name in cases:
            with self.subTest(server=expected_name):
                FakeServer.instances.clear()
                stdout, transports = execute_server(path, argv)

                self.assertEqual(stdout, "")
                self.assertEqual(len(FakeServer.instances), 1)
                server = FakeServer.instances[0]
                self.assertEqual(server.name, expected_name)
                self.assertEqual(
                    server.run_calls,
                    [
                        (
                            "read-stream",
                            "write-stream",
                            "initialization-options",
                        )
                    ],
                )
                self.assertEqual(len(transports), 1)
                self.assertTrue(transports[0].entered)
                self.assertTrue(transports[0].exited)


if __name__ == "__main__":
    unittest.main()
