import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_BUILDER_PATH = (
    REPOSITORY_ROOT / "Draft_05" / "build_complete_manuscript.py"
)


def load_manuscript_builder():
    spec = importlib.util.spec_from_file_location(
        "test_manuscript_builder_safety",
        MANUSCRIPT_BUILDER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {MANUSCRIPT_BUILDER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ManuscriptBuilderSafetyTests(unittest.TestCase):
    def test_main_warns_when_header_cleanup_leaves_an_empty_chapter(self):
        module = load_manuscript_builder()
        headers_only = (
            "ACT I: TOYS IN THE ATTIC\n\n"
            'CHAPTER 1: "WISH YOU WERE HERE"\n\n'
            "---\n"
        )

        with TemporaryDirectory() as temporary_directory:
            draft_dir = Path(temporary_directory)
            (draft_dir / "empty_chapter.txt").write_text(
                headers_only,
                encoding="utf-8",
            )
            output = io.StringIO()
            with (
                patch.object(module, "DRAFT_DIR", draft_dir),
                patch.object(
                    module,
                    "CHAPTERS",
                    [
                        (
                            1,
                            "empty_chapter.txt",
                            "WISH YOU WERE HERE",
                            "Wish You Were Here",
                        )
                    ],
                ),
                patch.object(
                    module,
                    "ACTS",
                    [("ACT I", "TOYS IN THE ATTIC", range(1, 2))],
                ),
                redirect_stdout(output),
            ):
                module.main()

            self.assertEqual(module.clean_chapter_body(headers_only), [])
            self.assertIn(
                "WARNING: Chapter 1 has no paragraphs after cleaning",
                output.getvalue(),
            )
            self.assertTrue(
                (draft_dir / "Walk_This_Way_Draft_05_COMPLETE.md").is_file()
            )
            self.assertTrue(
                (draft_dir / "Walk_This_Way_Draft_05_COMPLETE.txt").is_file()
            )


if __name__ == "__main__":
    unittest.main()
