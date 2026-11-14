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


def load_style_server():
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
        "test_style_emulation_lehane_server",
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


class StyleEmulationLehaneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_style_server()

    def test_full_name_alias_loads_the_special_lehane_adapter(self):
        knowledge = self.module.load_kb(" Dennis Lehane ")

        self.assertEqual(knowledge["key"], "lehane")
        self.assertEqual(knowledge["name"], "Dennis Lehane")
        self.assertIn("loss_of_innocence_theme", knowledge["writing_dna"])
        self.assertEqual(
            knowledge["signature_moves"]["primary_move"],
            "Class as plot engine; revelation discipline",
        )
        self.assertTrue(Path(knowledge["source"]).is_file())

    def test_emulation_packet_uses_lehane_analysis_and_preserves_input(self):
        result = asyncio.run(
            self.module.call_tool(
                "emulate_paragraph",
                {"author": "lehane", "text": "The original material."},
            )
        )
        packet = json.loads(result[0].text)

        self.assertEqual(packet["engine"], "Dennis Lehane")
        self.assertEqual(packet["student_material"], "The original material.")
        self.assertEqual(
            packet["quick_signature"]["primary_move"],
            "Class as plot engine; revelation discipline",
        )
        self.assertFalse(packet["keep_the_emulation"])
        self.assertNotIn("error", packet)


if __name__ == "__main__":
    unittest.main()
