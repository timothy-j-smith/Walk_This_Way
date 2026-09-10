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
SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "CURSOR_WORKFLOW_ORCHESTRATOR_MCP"
    / "server.py"
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


def load_server_module():
    mcp = types.ModuleType("mcp")
    server = types.ModuleType("mcp.server")
    stdio = types.ModuleType("mcp.server.stdio")
    mcp_types = types.ModuleType("mcp.types")

    server.Server = FakeServer
    server.stdio = stdio
    mcp.server = server
    mcp_types.Tool = FakeMcpValue
    mcp_types.TextContent = FakeMcpValue

    spec = importlib.util.spec_from_file_location(
        "test_orchestrator_config_server",
        SERVER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {SERVER_PATH}")

    module = importlib.util.module_from_spec(spec)
    with (
        patch.dict(
            sys.modules,
            {
                "mcp": mcp,
                "mcp.server": server,
                "mcp.server.stdio": stdio,
                "mcp.types": mcp_types,
            },
        ),
        patch.object(Path, "mkdir", return_value=None),
    ):
        spec.loader.exec_module(module)
    return module


class OrchestratorMcpConfigTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = TemporaryDirectory()
        temporary_root = Path(self.temporary_directory.name)
        self.config_path = temporary_root / "mcp.json"
        self.log_path = temporary_root / "usage.jsonl"
        self.initial_config = {
            "metadata": {"schema": 1},
            "mcpServers": {
                "alpha": {
                    "command": "alpha-command",
                    "disabled": True,
                    "env": {"KEEP": "unchanged"},
                },
                "beta": {
                    "command": "beta-command",
                    "disabled": False,
                },
            },
        }
        self.config_path.write_text(
            json.dumps(self.initial_config),
            encoding="utf-8",
        )
        self.module = load_server_module()
        self.module.MCP_CONFIG_PATH = self.config_path
        self.module.USAGE_LOG_PATH = self.log_path

    def tearDown(self):
        self.temporary_directory.cleanup()

    def call_tool(self, name, arguments):
        response = asyncio.run(self.module.call_tool(name, arguments))
        return json.loads(response[0].text)

    def read_config(self):
        return json.loads(self.config_path.read_text(encoding="utf-8"))

    def read_log(self):
        return [
            json.loads(line)
            for line in self.log_path.read_text(encoding="utf-8").splitlines()
        ]

    def test_enable_changes_only_requested_servers_and_reports_unknowns(self):
        result = self.call_tool(
            "enable_mcps",
            {"mcp_names": ["alpha", "missing"]},
        )

        expected_config = self.initial_config | {
            "mcpServers": {
                **self.initial_config["mcpServers"],
                "alpha": {
                    **self.initial_config["mcpServers"]["alpha"],
                    "disabled": False,
                },
            }
        }
        self.assertEqual(self.read_config(), expected_config)
        self.assertEqual(
            result,
            {
                "success": True,
                "enabled": ["alpha"],
                "not_found": ["missing"],
                "message": "Enabled 1 MCP(s). Restart Cursor for changes to take effect.",
            },
        )

        log_entry = self.read_log()[0]
        self.assertEqual(log_entry["action"], "enable_mcps")
        self.assertEqual(log_entry["details"]["mcp_names"], ["alpha", "missing"])
        self.assertEqual(log_entry["details"]["result"], result)

    def test_disable_changes_only_requested_servers_and_reports_unknowns(self):
        result = self.call_tool(
            "disable_mcps",
            {"mcp_names": ["beta", "missing"]},
        )

        expected_config = self.initial_config | {
            "mcpServers": {
                **self.initial_config["mcpServers"],
                "beta": {
                    **self.initial_config["mcpServers"]["beta"],
                    "disabled": True,
                },
            }
        }
        self.assertEqual(self.read_config(), expected_config)
        self.assertEqual(
            result,
            {
                "success": True,
                "disabled": ["beta"],
                "not_found": ["missing"],
                "message": "Disabled 1 MCP(s). Restart Cursor for changes to take effect.",
            },
        )

        log_entry = self.read_log()[0]
        self.assertEqual(log_entry["action"], "disable_mcps")
        self.assertEqual(log_entry["details"]["mcp_names"], ["beta", "missing"])
        self.assertEqual(log_entry["details"]["result"], result)


if __name__ == "__main__":
    unittest.main()
