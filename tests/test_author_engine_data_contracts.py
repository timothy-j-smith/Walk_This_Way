import ast
import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MCP_ROOT = REPOSITORY_ROOT / "zz_COMPASS" / "MCP_Implementations"
AUTHOR_DATA_ROOT = MCP_ROOT / "AUTHOR_ENGINES" / "data"
STYLE_ROOT = MCP_ROOT / "STYLE_EMULATION_MCP"
STYLE_SERVER_PATH = STYLE_ROOT / "server.py"
SIGNATURES_PATH = STYLE_ROOT / "signatures.json"

REQUIRED_COLLECTIONS = {
    "writing_dna": list,
    "signature_moves": list,
    "focus_deep": dict,
    "tutor_prompts": list,
    "pitfalls": list,
    "apply_to_projects": dict,
    "guidelines": dict,
}
REQUIRED_GUIDELINES = {
    "honesty_protocol",
    "absh_awareness",
    "voice_intactness",
    "fair_use",
}
REQUIRED_SIGNATURE_FIELDS = {
    "name",
    "primary_move",
    "sentence_shape",
    "body_signature",
    "closing_image",
}


def read_committee() -> dict[str, str | None]:
    tree = ast.parse(
        STYLE_SERVER_PATH.read_text(encoding="utf-8"),
        filename=str(STYLE_SERVER_PATH),
    )
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "COMMITTEE"
                for target in node.targets
            )
        ):
            committee = ast.literal_eval(node.value)
            if not isinstance(committee, dict):
                raise TypeError("COMMITTEE must be a dictionary")
            return committee
    raise AssertionError("COMMITTEE assignment not found")


class AuthorEngineDataContractTests(unittest.TestCase):
    def test_every_author_engine_has_complete_tutoring_data(self):
        data_paths = sorted(AUTHOR_DATA_ROOT.glob("*.json"))
        self.assertGreater(len(data_paths), 0)

        names = set()
        for data_path in data_paths:
            with self.subTest(author=data_path.stem):
                data = json.loads(data_path.read_text(encoding="utf-8"))
                meta = data.get("meta")

                self.assertIsInstance(meta, dict)
                self.assertIsInstance(meta.get("name"), str)
                self.assertTrue(meta["name"].strip())
                self.assertIsInstance(meta.get("focus_work"), str)
                self.assertTrue(meta["focus_work"].strip())
                self.assertNotIn(meta["name"], names)
                names.add(meta["name"])

                for key, expected_type in REQUIRED_COLLECTIONS.items():
                    self.assertIsInstance(data.get(key), expected_type)
                    self.assertTrue(data[key], msg=f"{key} must not be empty")

                self.assertTrue(
                    REQUIRED_GUIDELINES.issubset(data["guidelines"]),
                    msg="Required educational safeguards are missing",
                )

    def test_style_committee_matches_author_engine_files(self):
        committee = read_committee()
        data_paths = sorted(AUTHOR_DATA_ROOT.glob("*.json"))
        data_filenames = {path.name for path in data_paths}
        data_keys = {path.stem for path in data_paths}
        engine_entries = {
            key: filename
            for key, filename in committee.items()
            if filename is not None
        }

        self.assertEqual(set(engine_entries), data_keys)
        self.assertEqual(set(engine_entries.values()), data_filenames)
        self.assertEqual(
            {key for key, filename in committee.items() if filename is None},
            {"lehane"},
        )

    def test_quick_signatures_reference_committee_members(self):
        committee = read_committee()
        signatures = json.loads(SIGNATURES_PATH.read_text(encoding="utf-8"))

        self.assertTrue(signatures)
        self.assertTrue(set(signatures).issubset(committee))
        for key, signature in signatures.items():
            with self.subTest(author=key):
                self.assertIsInstance(signature, dict)
                self.assertTrue(REQUIRED_SIGNATURE_FIELDS.issubset(signature))
                for field in REQUIRED_SIGNATURE_FIELDS:
                    self.assertIsInstance(signature[field], str)
                    self.assertTrue(signature[field].strip())


if __name__ == "__main__":
    unittest.main()
