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


class McpServerValidationTests(unittest.TestCase):
    def test_unknown_bestseller_returns_available_formulas(self):
        module = load_server_module("FICTION_REVERSE_ENGINEERING_MCP")

        with tempfile.TemporaryDirectory() as temporary_directory:
            module.FORMULAS_DIR = Path(temporary_directory)
            result = asyncio.run(
                module.call_tool(
                    "compare_to_bestseller",
                    {
                        "your_text": "Nick waited.",
                        "bestseller_title": "Missing Formula",
                    },
                )
            )

        body = json.loads(result[0].text)
        self.assertEqual(
            body["error"],
            "Formula not found for 'Missing Formula'",
        )
        self.assertEqual(body["available_formulas"], [])
        self.assertEqual(
            body["hint"],
            "Run reverse_engineer_novel first to create a formula",
        )


if __name__ == "__main__":
    unittest.main()
