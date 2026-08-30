import json
import subprocess
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_CONFIG_PATH = REPOSITORY_ROOT / ".cursor" / "mcp.json"
SETUP_PATH = REPOSITORY_ROOT / ".cursor" / "setup.sh"
LEGACY_SERVER_NAMES = (
    "stephen_king",
    "dennis_lehane",
    "walk_this_way_character",
)


class McpDependencyCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = json.loads(MCP_CONFIG_PATH.read_text(encoding="utf-8"))
        cls.server_configs = config["mcpServers"]

    def test_registered_legacy_servers_constrain_mcp_to_version_1(self):
        for server_name in LEGACY_SERVER_NAMES:
            with self.subTest(server=server_name):
                server_config = self.server_configs[server_name]
                interpreter = REPOSITORY_ROOT / server_config["command"]
                server_path = REPOSITORY_ROOT / server_config["args"][0]

                self.assertEqual(
                    interpreter.parent.parent,
                    server_path.parent / "venv",
                )
                requirements_path = server_path.parent / "requirements.txt"
                requirements = [
                    line.strip()
                    for line in requirements_path.read_text(
                        encoding="utf-8"
                    ).splitlines()
                    if line.strip() and not line.lstrip().startswith("#")
                ]
                self.assertEqual(requirements, ["mcp<2"])

    def test_setup_has_compatible_fallback_and_import_smoke_test(self):
        setup_script = SETUP_PATH.read_text(encoding="utf-8")

        self.assertIn('"mcp<2"', setup_script)
        self.assertIn("runpy.run_path('$dir/server.py')", setup_script)
        for server_name in LEGACY_SERVER_NAMES:
            server_config = self.server_configs[server_name]
            server_directory = str(
                Path(server_config["args"][0]).parent
            )
            with self.subTest(server=server_name):
                self.assertIn(f'"{server_directory}"', setup_script)

    def test_registered_legacy_servers_import_in_configured_venvs(self):
        for server_name in LEGACY_SERVER_NAMES:
            with self.subTest(server=server_name):
                server_config = self.server_configs[server_name]
                interpreter = REPOSITORY_ROOT / server_config["command"]
                server_path = server_config["args"][0]

                self.assertTrue(
                    interpreter.is_file(),
                    msg=f"Run .cursor/setup.sh to create {interpreter}",
                )
                result = subprocess.run(
                    [
                        str(interpreter),
                        "-c",
                        (
                            "import runpy; "
                            f"runpy.run_path({server_path!r})"
                        ),
                    ],
                    cwd=REPOSITORY_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    msg=result.stderr,
                )


if __name__ == "__main__":
    unittest.main()
