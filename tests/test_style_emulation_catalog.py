import asyncio
import importlib.util
import json
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "STYLE_EMULATION_MCP"
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


def load_server():
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
        "test_style_emulation_catalog_server",
        SERVER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {SERVER_PATH}")

    module = importlib.util.module_from_spec(spec)
    with patch.dict(
        sys.modules,
        {
            "mcp": mcp,
            "mcp.server": server,
            "mcp.server.stdio": stdio,
            "mcp.types": mcp_types,
        },
    ):
        spec.loader.exec_module(module)
    return module


class StyleEmulationCatalogTests(unittest.TestCase):
    def test_list_masters_returns_complete_sorted_committee_with_signatures(self):
        module = load_server()

        result = asyncio.run(module.call_tool("list_masters", {}))
        body = json.loads(result[0].text)
        rows = body["committee"]

        self.assertEqual(
            [row["key"] for row in rows],
            sorted(module.COMMITTEE),
        )
        self.assertTrue(all(row["has_engine"] for row in rows))

        rows_by_key = {row["key"]: row for row in rows}
        for key, signature in module.SIGNATURES.items():
            with self.subTest(master=key):
                self.assertEqual(rows_by_key[key]["name"], signature["name"])
                self.assertEqual(
                    rows_by_key[key]["primary_move"],
                    signature["primary_move"],
                )

        self.assertEqual(
            body["five_core_signatures"],
            list(module.SIGNATURES),
        )
        self.assertIn("One master per output", body["note"])


if __name__ == "__main__":
    unittest.main()
