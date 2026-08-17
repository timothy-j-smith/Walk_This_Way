import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
SERVER_NAMES = {
    "PROFESSIONAL_EDITOR_MCP": "professional-editor",
    "DENNIS_LEHANE_MCP": "dennis-lehane-style",
    "FICTION_REVERSE_ENGINEERING_MCP": "fiction-reverse-engineering",
    "CURSOR_WORKFLOW_ORCHESTRATOR_MCP": "cursor-workflow-orchestrator",
}


def load_server_module(server_directory: str):
    server_path = MCP_ROOT / server_directory / "server.py"
    module_name = f"test_{server_directory.lower()}_server"
    spec = importlib.util.spec_from_file_location(module_name, server_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {server_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class McpServerStartupTests(unittest.TestCase):
    def test_fixed_servers_complete_initialize_handshake(self):
        initialize_request = json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "regression-test",
                        "version": "1.0",
                    },
                },
            }
        )

        for server_directory, expected_name in SERVER_NAMES.items():
            with self.subTest(server=server_directory):
                server_path = MCP_ROOT / server_directory / "server.py"
                completed = subprocess.run(
                    [sys.executable, str(server_path)],
                    input=f"{initialize_request}\n",
                    capture_output=True,
                    check=False,
                    cwd=REPOSITORY_ROOT,
                    text=True,
                    timeout=10,
                )

                self.assertEqual(
                    completed.returncode,
                    0,
                    msg=f"{server_directory} failed to start:\n{completed.stderr}",
                )
                output_lines = [
                    line for line in completed.stdout.splitlines() if line.strip()
                ]
                self.assertTrue(
                    output_lines,
                    msg=f"{server_directory} returned no initialize response",
                )

                responses = []
                for line in output_lines:
                    try:
                        responses.append(json.loads(line))
                    except json.JSONDecodeError as error:
                        self.fail(
                            f"{server_directory} corrupted stdout with "
                            f"non-JSON protocol output: {line!r} ({error})"
                        )

                initialize_response = next(
                    (response for response in responses if response.get("id") == 1),
                    None,
                )
                self.assertIsNotNone(
                    initialize_response,
                    msg=f"{server_directory} did not answer initialize",
                )
                self.assertEqual(
                    initialize_response["result"]["serverInfo"]["name"],
                    expected_name,
                )


class McpServerInvariantTests(unittest.TestCase):
    def test_project_roots_resolve_to_repository(self):
        for server_directory in (
            "FICTION_REVERSE_ENGINEERING_MCP",
            "CURSOR_WORKFLOW_ORCHESTRATOR_MCP",
        ):
            with self.subTest(server=server_directory):
                module = load_server_module(server_directory)
                self.assertEqual(module.PROJECT_ROOT.resolve(), REPOSITORY_ROOT)

    def test_orchestrator_usage_log_has_utc_timestamp(self):
        module = load_server_module("CURSOR_WORKFLOW_ORCHESTRATOR_MCP")

        with tempfile.TemporaryDirectory() as temporary_directory:
            log_path = Path(temporary_directory) / "usage.jsonl"
            module.USAGE_LOG_PATH = log_path
            module.log_usage("test-action", {"source": "regression-test"})

            entry = json.loads(log_path.read_text(encoding="utf-8"))

        timestamp = datetime.fromisoformat(entry["timestamp"])
        self.assertEqual(timestamp.utcoffset(), timedelta(0))
        self.assertEqual(entry["action"], "test-action")
        self.assertEqual(entry["details"], {"source": "regression-test"})


if __name__ == "__main__":
    unittest.main()
