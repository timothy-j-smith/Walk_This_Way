import asyncio
import importlib.util
import json
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
AUTHOR_SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "AUTHOR_ENGINES"
    / "author_server.py"
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


def load_author_server():
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
        "test_author_engine_liberty_server",
        AUTHOR_SERVER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {AUTHOR_SERVER_PATH}")

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
        patch.object(
            sys,
            "argv",
            [str(AUTHOR_SERVER_PATH), "--author", "king"],
        ),
    ):
        spec.loader.exec_module(module)
    return module


class AuthorEngineLibertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_author_server()

    def test_explicit_liberty_overrides_each_tool_default(self):
        cases = (
            ("king_imagine", "professional"),
            ("king_craft", "nice"),
            ("king_revise", "neutral"),
        )

        for tool_name, liberty in cases:
            with self.subTest(tool=tool_name, liberty=liberty):
                result = asyncio.run(
                    self.module.call_tool(
                        tool_name,
                        {"text": "Test passage.", "liberty": liberty},
                    )
                )
                payload = json.loads(result[0].text)

                self.assertEqual(payload["liberty_level"], liberty)
                self.assertEqual(
                    payload["liberty_instruction"],
                    self.module.LIBERTY[liberty],
                )
                self.assertEqual(payload["student_input"], "Test passage.")


if __name__ == "__main__":
    unittest.main()
