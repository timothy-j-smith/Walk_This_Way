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
    / "WalkThisWay_Character_MCP"
    / "server.py"
)


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
    mcp_module = types.ModuleType("mcp")
    server_module = types.ModuleType("mcp.server")
    stdio_module = types.ModuleType("mcp.server.stdio")
    types_module = types.ModuleType("mcp.types")

    server_module.Server = FakeServer
    server_module.stdio = stdio_module
    types_module.TextContent = FakeMcpValue
    types_module.Tool = FakeMcpValue
    mcp_module.server = server_module

    fake_modules = {
        "mcp": mcp_module,
        "mcp.server": server_module,
        "mcp.server.stdio": stdio_module,
        "mcp.types": types_module,
    }
    spec = importlib.util.spec_from_file_location(
        "test_walk_this_way_character_server",
        SERVER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {SERVER_PATH}")

    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, fake_modules):
        spec.loader.exec_module(module)
    return module


class WalkThisWayCharacterMcpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_server_module()

    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        fixture_path = Path(self.temporary_directory.name) / "characters.json"
        fixture_path.write_text(
            json.dumps(
                {
                    "Nick Johnson": {
                        "basic_info": {
                            "born": 1960,
                            "age_1975": 13,
                            "occupation_1975": "Student",
                        },
                        "personality": {
                            "voice": "Working-class Boston dialect",
                        },
                        "preferences": {
                            "music": {
                                "loves": ["Aerosmith"],
                                "hates": ["disco"],
                            }
                        },
                        "relationships": {},
                    },
                    "Jackie Marsh": {
                        "basic_info": {
                            "born": 1962,
                            "occupation_1975": "Student",
                        },
                        "personality": {
                            "voice": "Educated, precise language",
                        },
                        "relationships": {
                            "Nick Johnson": {
                                "type": "best friend turned rival",
                            }
                        },
                    },
                }
            ),
            encoding="utf-8",
        )
        self.module.CHARACTERS_FILE = fixture_path

    def tearDown(self):
        self.temporary_directory.cleanup()

    def call_tool(self, name, arguments):
        content = asyncio.run(self.module.call_tool(name, arguments))
        return json.loads(content[0].text)

    def test_nested_attribute_lookup_and_missing_path(self):
        found = self.call_tool(
            "get_character_attribute",
            {
                "name": "Nick Johnson",
                "attribute": "preferences.music.loves",
            },
        )
        self.assertEqual(found["value"], ["Aerosmith"])

        missing = self.call_tool(
            "get_character_attribute",
            {
                "name": "Nick Johnson",
                "attribute": "preferences.music.favorite_song",
            },
        )
        self.assertEqual(
            missing["error"],
            "Attribute 'preferences.music.favorite_song' not found for Nick Johnson",
        )

    def test_fact_checks_reject_established_music_and_voice_contradictions(self):
        cases = (
            (
                "Nick Johnson",
                "music_preference",
                "Nick loves disco",
                "Nick Johnson hates disco",
            ),
            (
                "Nick Johnson",
                "music_preference",
                "Nick despises Aerosmith",
                "Nick Johnson loves Aerosmith",
            ),
            (
                "Jackie Marsh",
                "voice_pattern",
                "Jackie speaks in informal slang",
                "Jackie uses educated, precise language",
            ),
            (
                "Nick Johnson",
                "voice_pattern",
                "Nick sounds academic and formal",
                "Nick speaks with working-class Boston dialect",
            ),
        )

        for character, fact_type, proposed_fact, expected_reason in cases:
            with self.subTest(character=character, proposed_fact=proposed_fact):
                result = self.call_tool(
                    "check_character_fact",
                    {
                        "name": character,
                        "fact_type": fact_type,
                        "proposed_fact": proposed_fact,
                    },
                )
                self.assertFalse(result["consistent"])
                self.assertIn(expected_reason, result["reasoning"])

    def test_relationship_lookup_falls_back_to_reverse_profile(self):
        result = self.call_tool(
            "get_relationship",
            {
                "character1": "Nick Johnson",
                "character2": "Jackie Marsh",
            },
        )

        self.assertEqual(
            result["relationship"],
            {"type": "best friend turned rival"},
        )
        self.assertEqual(result["character1"], "Jackie Marsh")
        self.assertEqual(result["character2"], "Nick Johnson")
        self.assertEqual(
            result["note"],
            "Relationship found in Jackie Marsh's profile",
        )

    def test_year_lookup_prefers_recorded_age_then_calculates_from_birth_year(self):
        result = self.call_tool("get_characters_by_year", {"year": 1975})
        characters = {
            character["name"]: character
            for character in result["characters"]
        }

        self.assertEqual(characters["Nick Johnson"]["age"], 13)
        self.assertEqual(characters["Jackie Marsh"]["age"], 13)
        self.assertEqual(
            characters["Nick Johnson"]["occupation"],
            "Student",
        )


if __name__ == "__main__":
    unittest.main()
