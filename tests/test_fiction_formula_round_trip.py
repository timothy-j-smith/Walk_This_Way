import asyncio
import importlib.util
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "FICTION_REVERSE_ENGINEERING_MCP"
    / "server.py"
)
BUNDLED_FORMULA_TITLE = "Walk This Way Chapter 15 Landslide"


class FakeMcpValue:
    def __init__(self, **values):
        self.__dict__.update(values)


class FakeServer:
    def __init__(self, name):
        self.name = name

    def list_tools(self):
        return lambda function: function

    def call_tool(self):
        return lambda function: function


def load_server_module():
    spec = importlib.util.spec_from_file_location(
        "test_fiction_reverse_engineering_server",
        SERVER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {SERVER_PATH}")

    mcp_module = types.ModuleType("mcp")
    server_module = types.ModuleType("mcp.server")
    stdio_module = types.ModuleType("mcp.server.stdio")
    types_module = types.ModuleType("mcp.types")

    server_module.Server = FakeServer
    server_module.stdio = stdio_module
    types_module.TextContent = FakeMcpValue
    types_module.Tool = FakeMcpValue
    mcp_module.server = server_module

    module = importlib.util.module_from_spec(spec)
    with patch.dict(
        sys.modules,
        {
            "mcp": mcp_module,
            "mcp.server": server_module,
            "mcp.server.stdio": stdio_module,
            "mcp.types": types_module,
        },
    ):
        spec.loader.exec_module(module)
    return module


class FictionFormulaRoundTripTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_server_module()

    def call_tool(self, name, arguments):
        result = asyncio.run(self.module.call_tool(name, arguments))
        return json.loads(result[0].text)

    def test_bundled_formula_is_discoverable_and_usable_for_pacing(self):
        available = self.call_tool("list_available_formulas", {})
        bundled = next(
            formula
            for formula in available["formulas"]
            if formula["title"] == BUNDLED_FORMULA_TITLE
        )

        self.assertEqual(bundled["author"], "Timothy J. Smith")
        self.assertEqual(bundled["genre"], "literary fiction")

        pacing = self.call_tool(
            "analyze_pacing",
            {
                "text": "The room stayed quiet.",
                "target_formula": BUNDLED_FORMULA_TITLE,
            },
        )

        self.assertEqual(
            pacing["comparison"],
            {
                "your_tension": "low",
                "bestseller_tension": "low",
                "match": True,
            },
        )

    def test_generated_formula_can_be_listed_and_reused(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            original_formulas_directory = self.module.FORMULAS_DIR
            self.module.FORMULAS_DIR = Path(temporary_directory)
            self.addCleanup(
                setattr,
                self.module,
                "FORMULAS_DIR",
                original_formulas_directory,
            )

            created = self.call_tool(
                "reverse_engineer_novel",
                {
                    "text": '"Wait," Nick said. Then he ran.',
                    "title": "Round Trip Formula",
                    "author": "Regression Test",
                    "genre": "literary fiction",
                },
            )
            available = self.call_tool("list_available_formulas", {})
            pacing = self.call_tool(
                "analyze_pacing",
                {
                    "text": "Then he ran.",
                    "target_formula": "Round Trip Formula",
                },
            )

        self.assertEqual(created["status"], "success")
        self.assertEqual(created["novel"], "Round Trip Formula by Regression Test")
        self.assertEqual(available["total_formulas"], 1)
        self.assertEqual(
            available["formulas"][0]["title"],
            "Round Trip Formula",
        )
        self.assertIn("comparison", pacing)
        self.assertEqual(
            pacing["comparison"]["match"],
            pacing["comparison"]["your_tension"]
            == pacing["comparison"]["bestseller_tension"],
        )


if __name__ == "__main__":
    unittest.main()
