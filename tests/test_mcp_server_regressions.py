import asyncio
import contextlib
import importlib.util
import io
import json
import runpy
import sys
import tempfile
import types
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
SERVER_NAMES = (
    "PROFESSIONAL_EDITOR_MCP",
    "DENNIS_LEHANE_MCP",
    "FICTION_REVERSE_ENGINEERING_MCP",
    "CURSOR_WORKFLOW_ORCHESTRATOR_MCP",
)


def build_fake_mcp_modules():
    state = types.SimpleNamespace(contexts=[], servers=[])

    class FakeStdioContext:
        def __init__(self):
            self.entered = False
            self.exited = False

        async def __aenter__(self):
            self.entered = True
            return "read-stream", "write-stream"

        async def __aexit__(self, exc_type, exc_value, traceback):
            self.exited = True

    class FakeServer:
        def __init__(self, name):
            self.name = name
            self.run_calls = []
            state.servers.append(self)

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

    class FakeMcpType:
        def __init__(self, **values):
            self.__dict__.update(values)

    def stdio_server():
        context = FakeStdioContext()
        state.contexts.append(context)
        return context

    mcp_module = types.ModuleType("mcp")
    server_module = types.ModuleType("mcp.server")
    stdio_module = types.ModuleType("mcp.server.stdio")
    types_module = types.ModuleType("mcp.types")

    server_module.Server = FakeServer
    server_module.stdio = stdio_module
    stdio_module.stdio_server = stdio_server
    types_module.TextContent = FakeMcpType
    types_module.Tool = FakeMcpType
    mcp_module.server = server_module

    modules = {
        "mcp": mcp_module,
        "mcp.server": server_module,
        "mcp.server.stdio": stdio_module,
        "mcp.types": types_module,
    }
    return modules, state


def load_server_module(server_directory: str):
    server_path = MCP_ROOT / server_directory / "server.py"
    module_name = f"test_{server_directory.lower()}_server"
    spec = importlib.util.spec_from_file_location(module_name, server_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {server_path}")
    module = importlib.util.module_from_spec(spec)
    fake_modules, _ = build_fake_mcp_modules()
    with patch.dict(sys.modules, fake_modules):
        spec.loader.exec_module(module)
    return module


class McpServerStartupTests(unittest.TestCase):
    def test_fixed_servers_use_async_stdio_entrypoint_without_stdout_noise(self):
        for server_directory in SERVER_NAMES:
            with self.subTest(server=server_directory):
                server_path = MCP_ROOT / server_directory / "server.py"
                fake_modules, state = build_fake_mcp_modules()
                stdout = io.StringIO()

                with patch.dict(sys.modules, fake_modules):
                    with contextlib.redirect_stdout(stdout):
                        runpy.run_path(str(server_path), run_name="__main__")

                self.assertEqual(
                    stdout.getvalue(),
                    "",
                    msg=f"{server_directory} wrote non-protocol text to stdout",
                )
                self.assertEqual(len(state.contexts), 1)
                self.assertTrue(state.contexts[0].entered)
                self.assertTrue(state.contexts[0].exited)
                self.assertEqual(len(state.servers), 1)
                self.assertEqual(
                    state.servers[0].run_calls,
                    [
                        (
                            "read-stream",
                            "write-stream",
                            "initialization-options",
                        )
                    ],
                )


class McpServerInvariantTests(unittest.TestCase):
    def test_project_roots_resolve_to_repository(self):
        for server_directory in (
            "FICTION_REVERSE_ENGINEERING_MCP",
            "CURSOR_WORKFLOW_ORCHESTRATOR_MCP",
        ):
            with self.subTest(server=server_directory):
                module = load_server_module(server_directory)
                self.assertEqual(module.PROJECT_ROOT.resolve(), REPOSITORY_ROOT)

    def test_orchestrator_usage_log_has_utc_timestamp(self):
        module = load_server_module("CURSOR_WORKFLOW_ORCHESTRATOR_MCP")

        with tempfile.TemporaryDirectory() as temporary_directory:
            log_path = Path(temporary_directory) / "usage.jsonl"
            module.USAGE_LOG_PATH = log_path
            module.log_usage("test-action", {"source": "regression-test"})

            entry = json.loads(log_path.read_text(encoding="utf-8"))

        timestamp = datetime.fromisoformat(entry["timestamp"])
        self.assertEqual(timestamp.utcoffset(), timedelta(0))
        self.assertEqual(entry["action"], "test-action")
        self.assertEqual(entry["details"], {"source": "regression-test"})


class FictionReverseEngineeringAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_server_module("FICTION_REVERSE_ENGINEERING_MCP")

    def call_tool(self, name, arguments):
        response = asyncio.run(self.module.call_tool(name, arguments))
        return json.loads(response[0].text)

    def test_empty_analysis_paths_return_zero_metrics(self):
        structure = self.module.analyze_structure("")
        pacing = self.module.analyze_pacing("")
        dialogue = self.module.extract_dialogue_patterns("")

        for metric in (
            "total_words",
            "total_sentences",
            "total_paragraphs",
            "total_dialogue",
            "plot_points",
            "avg_sentence_length",
            "dialogue_percentage",
        ):
            with self.subTest(metric=metric):
                self.assertEqual(structure[metric], 0)
        self.assertEqual(structure["chapter_count"], 1)
        self.assertEqual(pacing["tension_frequency"], 0)
        self.assertEqual(pacing["reveal_frequency"], 0)
        self.assertEqual(pacing["dialogue_frequency"], 0)
        self.assertEqual(pacing["avg_sentence_length"], 0)
        self.assertEqual(pacing["sentence_variation"], 0)
        self.assertEqual(dialogue["total_dialogue"], 0)
        self.assertEqual(dialogue["avg_dialogue_length"], 0)

    def test_chapter_parser_preserves_boundaries_and_selection(self):
        text = (
            "CHAPTER 1\n"
            "When Nick ran. He stopped.\n\n"
            "Act 2\n"
            "The room held still. However, he stayed."
        )

        all_chapters = self.call_tool("find_chapter_formula", {"text": text})
        second_chapter = self.call_tool(
            "find_chapter_formula",
            {"text": text, "chapter_num": 2},
        )

        self.assertEqual(all_chapters["total_chapters"], 2)
        self.assertEqual(len(all_chapters["chapter_formulas"]), 2)
        self.assertTrue(all_chapters["chapter_formulas"][0]["has_hook"])
        self.assertTrue(all_chapters["chapter_formulas"][1]["has_cliffhanger"])
        self.assertEqual(second_chapter["chapter"], 2)
        self.assertEqual(second_chapter["formula"]["word_count"], 7)
        self.assertFalse(second_chapter["formula"]["has_hook"])
        self.assertTrue(second_chapter["formula"]["has_cliffhanger"])


if __name__ == "__main__":
    unittest.main()
