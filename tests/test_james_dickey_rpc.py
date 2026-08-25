import json
import subprocess
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = (
    REPOSITORY_ROOT
    / "zz_COMPASS"
    / "MCP_Implementations"
    / "JAMES_DICKEY_MCP"
    / "server.py"
)


def run_server(requests: list[str]) -> list[dict]:
    result = subprocess.run(
        [sys.executable, str(SERVER_PATH)],
        input="\n".join(requests) + "\n",
        capture_output=True,
        check=True,
        encoding="utf-8",
        timeout=5,
    )
    return [json.loads(line) for line in result.stdout.splitlines()]


class JamesDickeyRpcTests(unittest.TestCase):
    def test_stdio_supports_initialize_list_and_normalized_tool_call(self):
        responses = run_server(
            [
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {},
                    }
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "tools/list",
                        "params": {},
                    }
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 3,
                        "method": "tools/call",
                        "params": {
                            "name": "dickey_revise",
                            "arguments": {
                                "text": "He crossed the river.",
                                "mode": " EDIT ",
                                "liberty": " PROFESSIONAL ",
                                "focus": "aftermath",
                            },
                        },
                    }
                ),
            ]
        )

        self.assertEqual(len(responses), 3)
        self.assertEqual(
            responses[0]["result"]["serverInfo"]["name"],
            "james-dickey-deliverance",
        )
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2024-11-05")
        self.assertEqual(
            [tool["name"] for tool in responses[1]["result"]["tools"]],
            ["dickey_imagine", "dickey_craft", "dickey_revise"],
        )

        tool_result = responses[2]["result"]
        self.assertFalse(tool_result["isError"])
        brief = tool_result["content"][0]["text"]
        self.assertIn("mode=edit | liberty=professional", brief)
        self.assertIn("**User focus:** aftermath", brief)
        self.assertIn("He crossed the river.", brief)

    def test_stdio_returns_json_rpc_errors_and_ignores_notifications(self):
        responses = run_server(
            [
                "{not json",
                "[]",
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "method": "notifications/initialized",
                        "params": {},
                    }
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 4,
                        "method": "unknown/method",
                        "params": {},
                    }
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 5,
                        "method": "tools/call",
                        "params": {"name": "unknown_tool", "arguments": {}},
                    }
                ),
            ]
        )

        self.assertEqual(
            [response["error"]["code"] for response in responses],
            [-32700, -32600, -32601, -32602],
        )
        self.assertEqual([response["id"] for response in responses], [None, None, 4, 5])


if __name__ == "__main__":
    unittest.main()
