import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "AUTHOR_ENGINES"
    / "author_server.py"
)


def run_author_server(*arguments: str, cwd: str | None = None):
    return subprocess.run(
        [sys.executable, str(SERVER_PATH), *arguments],
        capture_output=True,
        cwd=cwd,
        encoding="utf-8",
        timeout=5,
    )


class AuthorEngineCliTests(unittest.TestCase):
    def test_selftest_resolves_author_data_outside_repository(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = run_author_server(
                "--author",
                "king",
                "--selftest",
                cwd=temporary_directory,
            )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertIn("OK — Stephen King engine loaded (king.json)", result.stdout)
        self.assertIn("dna=", result.stdout)
        self.assertIn("moves=", result.stdout)
        self.assertIn("prompts=", result.stdout)

    def test_invalid_author_configuration_fails_before_server_startup(self):
        missing_argument = run_author_server()
        self.assertEqual(missing_argument.returncode, 2)
        self.assertIn(
            "the following arguments are required: --author",
            missing_argument.stderr,
        )
        self.assertEqual(missing_argument.stdout, "")

        missing_author = run_author_server(
            "--author",
            "not-a-configured-author",
            "--selftest",
        )
        self.assertEqual(missing_author.returncode, 1)
        self.assertIn(
            "ERROR: knowledge base not found:",
            missing_author.stderr,
        )
        self.assertIn(
            "data/not-a-configured-author.json",
            missing_author.stderr,
        )
        self.assertEqual(missing_author.stdout, "")


if __name__ == "__main__":
    unittest.main()
