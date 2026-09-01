import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = REPOSITORY_ROOT / "Draft_05" / "build_complete_manuscript.py"


def load_builder_module():
    spec = importlib.util.spec_from_file_location(
        "draft_05_manuscript_builder",
        BUILDER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {BUILDER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ManuscriptBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = load_builder_module()

    def test_clean_chapter_body_removes_headers_and_normalizes_paragraphs(self):
        raw = (
            "ACT I: TOYS IN THE ATTIC\r\n\r\n"
            'CHAPTER 1: “WISH YOU WERE HERE”\r\n\r\n'
            "---\r\n\r\n"
            "  First line of prose.  \r\n"
            "Second line of the same paragraph.\r\n\r\n\r\n"
            "Final paragraph.\r"
        )

        self.assertEqual(
            self.builder.clean_chapter_body(raw),
            [
                "First line of prose. Second line of the same paragraph.",
                "Final paragraph.",
            ],
        )

    def test_main_builds_html_and_plain_text_from_isolated_chapters(self):
        chapters = [
            (1, "chapter_01.txt", "TEST CHAPTER", "Test Chapter"),
        ]
        acts = [
            ("ACT I", "TEST ACT", range(1, 2)),
        ]

        with tempfile.TemporaryDirectory() as temporary_directory:
            draft_directory = Path(temporary_directory)
            (draft_directory / "chapter_01.txt").write_text(
                'CHAPTER 1: "OLD TITLE"\n\n'
                "Rock & roll <loud>.\n"
                "Still the same paragraph.\n\n"
                "Second paragraph.\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with (
                patch.object(self.builder, "DRAFT_DIR", draft_directory),
                patch.object(self.builder, "CHAPTERS", chapters),
                patch.object(self.builder, "ACTS", acts),
                contextlib.redirect_stdout(stdout),
            ):
                self.builder.main()

            markdown = (
                draft_directory / "Walk_This_Way_Draft_05_COMPLETE.md"
            ).read_text(encoding="utf-8")
            plain_text = (
                draft_directory / "Walk_This_Way_Draft_05_COMPLETE.txt"
            ).read_text(encoding="utf-8")

        self.assertIn("ACT I: TEST ACT", markdown)
        self.assertIn('Chapter 1 — "Test Chapter"', markdown)
        self.assertIn('Chapter 1: "TEST CHAPTER"', markdown)
        self.assertIn(
            "<p>Rock &amp; roll &lt;loud&gt;. "
            "Still the same paragraph.</p>",
            markdown,
        )
        self.assertNotIn("OLD TITLE", markdown)

        self.assertIn("ACT I: TEST ACT", plain_text)
        self.assertIn('CHAPTER 1: "TEST CHAPTER"', plain_text)
        self.assertIn(
            "\tRock & roll <loud>. Still the same paragraph.",
            plain_text,
        )
        self.assertNotIn("OLD TITLE", plain_text)
        self.assertEqual(plain_text.count("\f"), 2)
        self.assertNotIn("WARNING:", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
