import json
import os
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_CONFIG_PATH = REPOSITORY_ROOT / ".cursor" / "mcp.json"
SETUP_PATH = REPOSITORY_ROOT / ".cursor" / "setup.sh"
LEGACY_SERVER_NAMES = (
    "stephen_king",
    "dennis_lehane",
    "walk_this_way_character",
)
LEGACY_SERVER_DIRECTORIES = (
    "zz_COMPASS/MCP_Implementations/STEPHEN_KING_MCP",
    "zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP",
    "zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP",
)


def create_setup_fixture(root: Path) -> tuple[Path, Path]:
    setup_path = root / ".cursor" / "setup.sh"
    setup_path.parent.mkdir(parents=True)
    setup_path.write_text(
        SETUP_PATH.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    fake_bin = root / "fake-bin"
    fake_bin.mkdir()
    python3_path = fake_bin / "python3"
    python3_path.write_text(
        "#!/usr/bin/env bash\n"
        "if [[ \"$1\" == \"-c\" ]]; then\n"
        "  echo '3.12'\n"
        "  exit 0\n"
        "fi\n"
        "exit 99\n",
        encoding="utf-8",
    )
    python3_path.chmod(0o755)

    command_log = root / "commands.log"
    for directory in LEGACY_SERVER_DIRECTORIES:
        server_root = root / directory
        bin_path = server_root / "venv" / "bin"
        bin_path.mkdir(parents=True)
        (server_root / "server.py").write_text("", encoding="utf-8")

        pip_path = bin_path / "pip"
        pip_path.write_text(
            "#!/usr/bin/env bash\n"
            f"printf '%s|pip|%s\\n' {directory!r} \"$*\" >> \"$COMMAND_LOG\"\n",
            encoding="utf-8",
        )
        pip_path.chmod(0o755)

        python_path = bin_path / "python"
        python_path.write_text(
            "#!/usr/bin/env bash\n"
            f"server_directory={directory!r}\n"
            "printf '%s|python|%s\\n' \"$server_directory\" \"$*\" "
            ">> \"$COMMAND_LOG\"\n"
            "if [[ \"${FAIL_IMPORT_FOR:-}\" == \"$server_directory\" ]]; then\n"
            "  exit 23\n"
            "fi\n",
            encoding="utf-8",
        )
        python_path.chmod(0o755)

    for directory in (
        LEGACY_SERVER_DIRECTORIES[0],
        LEGACY_SERVER_DIRECTORIES[2],
    ):
        (root / directory / "requirements.txt").write_text(
            "mcp<2\n",
            encoding="utf-8",
        )

    return setup_path, command_log


def run_setup_fixture(
    root: Path,
    setup_path: Path,
    command_log: Path,
    fail_import_for: str = "",
) -> tuple[subprocess.CompletedProcess[str], list[str]]:
    environment = os.environ.copy()
    environment.update(
        {
            "COMMAND_LOG": str(command_log),
            "FAIL_IMPORT_FOR": fail_import_for,
            "PATH": f"{root / 'fake-bin'}:{environment['PATH']}",
        }
    )
    result = subprocess.run(
        ["bash", str(setup_path)],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    commands = (
        command_log.read_text(encoding="utf-8").splitlines()
        if command_log.exists()
        else []
    )
    return result, commands


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

    def test_setup_executes_requirements_fallback_and_import_branches(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            setup_path, command_log = create_setup_fixture(root)
            result, commands = run_setup_fixture(
                root,
                setup_path,
                command_log,
            )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        for directory in LEGACY_SERVER_DIRECTORIES:
            with self.subTest(server=directory):
                self.assertIn(
                    f"{directory}|pip|install -q --upgrade pip",
                    commands,
                )
                self.assertIn(
                    (
                        f"{directory}|python|-c import runpy; "
                        f"runpy.run_path('{directory}/server.py')"
                    ),
                    commands,
                )

        self.assertIn(
            (
                f"{LEGACY_SERVER_DIRECTORIES[0]}|pip|install -q -r "
                f"{LEGACY_SERVER_DIRECTORIES[0]}/requirements.txt"
            ),
            commands,
        )
        self.assertIn(
            (
                f"{LEGACY_SERVER_DIRECTORIES[1]}|pip|install -q "
                "mcp<2"
            ),
            commands,
        )

    def test_setup_stops_when_a_server_import_fails(self):
        failing_directory = LEGACY_SERVER_DIRECTORIES[1]
        unvisited_directory = LEGACY_SERVER_DIRECTORIES[2]

        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            setup_path, command_log = create_setup_fixture(root)
            result, commands = run_setup_fixture(
                root,
                setup_path,
                command_log,
                fail_import_for=failing_directory,
            )

        self.assertEqual(result.returncode, 23)
        self.assertTrue(
            any(
                command.startswith(f"{failing_directory}|python|")
                for command in commands
            )
        )
        self.assertFalse(
            any(
                command.startswith(f"{unvisited_directory}|")
                for command in commands
            )
        )


if __name__ == "__main__":
    unittest.main()
