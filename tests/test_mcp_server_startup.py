import io
import json
import runpy
import sys
import types
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
SERVER_PATHS = (
    MCP_ROOT / "CURSOR_WORKFLOW_ORCHESTRATOR_MCP" / "server.py",
    MCP_ROOT / "DENNIS_LEHANE_MCP" / "server.py",
    MCP_ROOT / "FICTION_REVERSE_ENGINEERING_MCP" / "server.py",
    MCP_ROOT / "PROFESSIONAL_EDITOR_MCP" / "server.py",
)
READ_STREAM = object()
WRITE_STREAM = object()
TRANSPORTS = []


class FakeServer:
    instances = []

    def __init__(self, name):
        self.name = name
        self.initialization_options = object()
        self.run_calls = []
        self.instances.append(self)

    def list_tools(self):
        return lambda function: function

    def call_tool(self):
        return lambda function: function

    def create_initialization_options(self):
        return self.initialization_options

    async def run(self, read_stream, write_stream, initialization_options):
        self.run_calls.append(
            (read_stream, write_stream, initialization_options)
        )


class FakeMcpValue:
    def __init__(self, **values):
        self.__dict__.update(values)


class FakeTransport:
    def __init__(self):
        self.entered = False
        self.exited = False

    async def __aenter__(self):
        self.entered = True
        return READ_STREAM, WRITE_STREAM

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.exited = True


def fake_stdio_server():
    transport = FakeTransport()
    TRANSPORTS.append(transport)
    return transport


def mcp_stubs():
    mcp = types.ModuleType("mcp")
    server = types.ModuleType("mcp.server")
    stdio = types.ModuleType("mcp.server.stdio")
    mcp_types = types.ModuleType("mcp.types")

    server.Server = FakeServer
    stdio.stdio_server = fake_stdio_server
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


def execute_server(path):
    output = io.StringIO()
    with (
        patch.dict(sys.modules, mcp_stubs()),
        patch.object(Path, "mkdir", return_value=None),
        redirect_stdout(output),
    ):
        module_globals = runpy.run_path(str(path), run_name="__main__")
    return module_globals, output.getvalue()


class McpServerStartupTests(unittest.TestCase):
    def setUp(self):
        FakeServer.instances.clear()
        TRANSPORTS.clear()

    def test_server_scripts_open_stdio_and_run_the_mcp_application(self):
        for server_path in SERVER_PATHS:
            with self.subTest(server=server_path.parent.name):
                FakeServer.instances.clear()
                TRANSPORTS.clear()

                _, stdout = execute_server(server_path)

                self.assertEqual(stdout, "")
                self.assertEqual(len(FakeServer.instances), 1)
                app = FakeServer.instances[0]
                self.assertEqual(
                    app.run_calls,
                    [(READ_STREAM, WRITE_STREAM, app.initialization_options)],
                )
                self.assertEqual(len(TRANSPORTS), 1)
                self.assertTrue(TRANSPORTS[0].entered)
                self.assertTrue(TRANSPORTS[0].exited)

    def test_servers_resolve_workspace_paths_from_their_own_location(self):
        for directory in (
            "CURSOR_WORKFLOW_ORCHESTRATOR_MCP",
            "FICTION_REVERSE_ENGINEERING_MCP",
        ):
            with self.subTest(server=directory):
                module_globals, _ = execute_server(
                    MCP_ROOT / directory / "server.py"
                )

                self.assertEqual(
                    module_globals["PROJECT_ROOT"],
                    REPOSITORY_ROOT,
                )

    def test_orchestrator_usage_log_has_a_real_utc_timestamp(self):
        module_globals, _ = execute_server(SERVER_PATHS[0])

        with TemporaryDirectory() as temporary_directory:
            log_path = Path(temporary_directory) / "usage.jsonl"
            log_usage = module_globals["log_usage"]
            log_usage.__globals__["USAGE_LOG_PATH"] = log_path
            log_usage("analyze_context", {"task": "test"})

            log_entry = json.loads(log_path.read_text(encoding="utf-8"))

        timestamp = datetime.fromisoformat(log_entry["timestamp"])
        self.assertEqual(timestamp.utcoffset(), timezone.utc.utcoffset(timestamp))
        self.assertEqual(log_entry["action"], "analyze_context")
        self.assertEqual(log_entry["details"], {"task": "test"})


if __name__ == "__main__":
    unittest.main()
