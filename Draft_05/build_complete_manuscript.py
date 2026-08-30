#!/usr/bin/env python3
"""Combine Draft_05 chapters into a print-ready manuscript."""

from __future__ import annotations

import re
from pathlib import Path

DRAFT_DIR = Path(__file__).resolve().parent

CHAPTERS = [
    # (number, filename, caps_title, toc_display_title)
    (1, "Chapter_01_Wish_You_Were_Here.txt", "WISH YOU WERE HERE", "Wish You Were Here"),
    (2, "Chapter_02_Draw_the_Line.txt", "DRAW THE LINE", "Draw the Line"),
    (3, "Chapter_03_Killer_Queen.txt", "KILLER QUEEN", "Killer Queen"),
    (4, "Chapter_04_More_Than_a_Feeling.txt", "MORE THAN A FEELING", "More Than a Feeling"),
    (5, "Chapter_05_Schools_Out.txt", "SCHOOL'S OUT", "School's Out"),
    (6, "Chapter_06_With_a_Little_Help_From_My_Friends.txt", "WITH A LITTLE HELP FROM MY FRIENDS", "With a Little Help From My Friends"),
    (7, "Chapter_07_Bohemian_Rhapsody.txt", "BOHEMIAN RHAPSODY", "Bohemian Rhapsody"),
    (8, "Chapter_08_Mama_Kin.txt", "MAMA KIN", "Mama Kin"),
    (9, "Chapter_09_Just_What_I_Needed.txt", "JUST WHAT I NEEDED", "Just What I Needed"),
    (10, "Chapter_10_Dream_On.txt", "DREAM ON", "Dream On"),
    (11, "Chapter_11_Radio_Radio.txt", "RADIO, RADIO", "Radio, Radio"),
    (12, "Chapter_12_Summer_Breeze.txt", "SUMMER BREEZE", "Summer Breeze"),
    (13, "Chapter_13_Breakdown.txt", "BREAKDOWN", "Breakdown"),
    (14, "Chapter_14_Baba_ORiley.txt", "BABA O'RILEY", "Baba O'Riley"),
    (15, "Chapter_15_Landslide.txt", "LANDSLIDE", "Landslide"),
    (16, "Chapter_16_Running_on_Empty.txt", "RUNNING ON EMPTY", "Running on Empty"),
    (17, "Chapter_17_Bridge_Over_Troubled_Water.txt", "BRIDGE OVER TROUBLED WATER", "Bridge Over Troubled Water"),
    (18, "Chapter_18_Rock_n_Roll_Fantasy.txt", "ROCK 'N' ROLL FANTASY", "Rock 'n' Roll Fantasy"),
    (19, "Chapter_19_Born_to_Run.txt", "BORN TO RUN", "Born to Run"),
    (20, "Chapter_20_Hotel_California.txt", "HOTEL CALIFORNIA", "Hotel California"),
    (21, "Chapter_21_Another_Brick_in_the_Wall.txt", "ANOTHER BRICK IN THE WALL", "Another Brick in the Wall"),
    (22, "Chapter_22_Wont_Get_Fooled_Again.txt", "WON'T GET FOOLED AGAIN", "Won't Get Fooled Again"),
    (23, "Chapter_23_Working_Class_Hero.txt", "WORKING CLASS HERO", "Working Class Hero"),
    (24, "Chapter_24_Light_My_Fire.txt", "LIGHT MY FIRE", "Light My Fire"),
    (25, "Chapter_25_Night_Moves.txt", "NIGHT MOVES", "Night Moves"),
    (26, "Chapter_26_Father_and_Son.txt", "FATHER AND SON", "Father and Son"),
    (27, "Chapter_27_Turn_the_Page.txt", "TURN THE PAGE", "Turn the Page"),
    (28, "Chapter_28_Rhiannon.txt", "RHIANNON", "Rhiannon"),
    (29, "Chapter_29_Rock_and_Roll_All_Nite.txt", "ROCK AND ROLL ALL NITE", "Rock and Roll All Nite"),
    (30, "Chapter_30_Silver_Springs.txt", "SILVER SPRINGS", "Silver Springs"),
    (31, "Chapter_31_Thunder_Road.txt", "THUNDER ROAD", "Thunder Road"),
    (32, "Chapter_32_Barracuda.txt", "BARRACUDA", "Barracuda"),
    (33, "Chapter_33_Somebody_to_Love.txt", "SOMEBODY TO LOVE", "Somebody to Love"),
    (34, "Chapter_34_Train_Kept_A_Rollin.txt", "TRAIN KEPT A-ROLLIN'", "Train Kept A-Rollin'"),
    (35, "Chapter_35_Go_Your_Own_Way.txt", "GO YOUR OWN WAY", "Go Your Own Way"),
    (36, "Chapter_36_Stairway_to_Heaven.txt", "STAIRWAY TO HEAVEN", "Stairway to Heaven"),
    (37, "Chapter_37_The_Boys_Are_Back_in_Town.txt", "THE BOYS ARE BACK IN TOWN", "The Boys Are Back in Town"),
    (38, "Chapter_38_Sweet_Emotion.txt", "SWEET EMOTION", "Sweet Emotion"),
    (39, "Chapter_39_Free_Bird.txt", "FREE BIRD", "Free Bird"),
    (40, "Chapter_40_Comfortably_Numb.txt", "COMFORTABLY NUMB", "Comfortably Numb"),
    (41, "Chapter_41_Walk_This_Way.txt", "WALK THIS WAY", "Walk This Way"),
]

ACTS = [
    (
        "ACT I",
        "TOYS IN THE ATTIC",
        range(1, 16),
    ),
    (
        "ACT II",
        "A NIGHT AT THE OPERA",
        range(16, 28),
    ),
    (
        "ACT III",
        "IN THROUGH THE OUT DOOR",
        range(28, 42),
    ),
]

ACT_HEADER_RE = re.compile(
    r"^ACT\s+[IVX]+:\s*.+$",
    re.IGNORECASE | re.MULTILINE,
)
CHAPTER_HEADER_RE = re.compile(
    r'^CHAPTER\s+\d+:\s*["\u201c].*?["\u201d].*$',
    re.IGNORECASE | re.MULTILINE,
)
HORIZONTAL_RULE_RE = re.compile(r"^---+\s*$", re.MULTILINE)


def chapter_lookup() -> dict[int, tuple[str, str, str]]:
    return {num: (caps, fname, toc) for num, fname, caps, toc in CHAPTERS}


def clean_chapter_body(raw: str) -> list[str]:
    """Return prose paragraphs with leading/trailing whitespace stripped."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = ACT_HEADER_RE.sub("", text)
    text = CHAPTER_HEADER_RE.sub("", text)
    text = HORIZONTAL_RULE_RE.sub("", text)

    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n+", text):
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if not lines:
            continue
        paragraphs.append(" ".join(lines))

    return paragraphs


def load_chapter_paragraphs(filename: str) -> list[str]:
    path = DRAFT_DIR / filename
    return clean_chapter_body(path.read_text(encoding="utf-8"))


def indent_paragraph(text: str, indent: str = "\t") -> str:
    return f"{indent}{text}"


def build_markdown() -> str:
    parts: list[str] = []

    parts.append(
        """<!--
  PRINT INSTRUCTIONS
  1. Open this file in a browser (drag into Chrome/Safari) or import into Word.
  2. File → Print (or Cmd+P). Enable "Background graphics" if titles look plain.
  3. Margins: 1 inch recommended. Page numbers appear at bottom center.
-->

<style>
@page {
  size: letter;
  margin: 1in;
  @bottom-center {
    content: counter(page);
    font-family: "Times New Roman", Times, serif;
    font-size: 11pt;
    color: #333;
  }
}
body {
  font-family: "Times New Roman", Times, serif;
  font-size: 12pt;
  line-height: 1.5;
  color: #000;
  max-width: 6.5in;
  margin: 0 auto;
}
.title-page {
  page-break-after: always;
  text-align: center;
  padding-top: 2.5in;
}
.title-page h1 {
  font-size: 28pt;
  font-weight: bold;
  letter-spacing: 0.08em;
  margin: 0 0 0.4in 0;
  text-transform: uppercase;
}
.title-page .subtitle {
  font-size: 14pt;
  font-style: italic;
  margin: 0 0 1.2in 0;
}
.title-page .draft {
  font-size: 12pt;
  margin: 0.15in 0;
}
.title-page .author {
  font-size: 14pt;
  margin-top: 1.5in;
}
.toc-page {
  page-break-after: always;
}
.toc-page h2 {
  text-align: center;
  font-size: 16pt;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin: 0 0 0.35in 0;
}
.toc-act {
  font-weight: bold;
  text-transform: uppercase;
  margin: 0.22in 0 0.08in 0;
  font-size: 11pt;
}
.toc-entry {
  margin: 0.04in 0 0.04in 0.25in;
  font-size: 11pt;
}
.chapter-break {
  page-break-before: always;
}
.chapter-heading {
  text-align: center;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 14pt;
  letter-spacing: 0.04em;
  margin: 0 0 0.35in 0;
}
.prose p {
  text-indent: 0.5in;
  margin: 0;
  padding: 0;
  text-align: justify;
}
.prose p:first-child {
  text-indent: 0;
}
@media print {
  body { max-width: none; margin: 0; }
}
</style>
"""
    )

    parts.append('<div class="title-page">')
    parts.append("<h1>Walk This Way</h1>")
    parts.append('<p class="subtitle">A Novel</p>')
    parts.append('<p class="draft">Draft 05</p>')
    parts.append('<p class="draft">June 2026</p>')
    parts.append('<p class="author">Timothy</p>')
    parts.append("</div>")

    parts.append('<div class="toc-page">')
    parts.append("<h2>Table of Contents</h2>")
    lookup = chapter_lookup()
    for act_label, act_subtitle, chapter_range in ACTS:
        parts.append(f'<p class="toc-act">{act_label}: {act_subtitle}</p>')
        for num in chapter_range:
            _, _, display = lookup[num]
            parts.append(
                f'<p class="toc-entry">Chapter {num} — "{display}"</p>'
            )
    parts.append("</div>")

    for num, filename, title, toc_display in CHAPTERS:
        paragraphs = load_chapter_paragraphs(filename)
        parts.append('<div class="chapter-break">')
        parts.append(
            f'<p class="chapter-heading">Chapter {num}: "{title}"</p>'
        )
        parts.append('<div class="prose">')
        for para in paragraphs:
            escaped = (
                para.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            parts.append(f"<p>{escaped}</p>")
        parts.append("</div>")
        parts.append("</div>")

    return "\n".join(parts) + "\n"


def build_plain_text() -> str:
    lines: list[str] = []
    form_feed = "\f"

    lines.append("WALK THIS WAY")
    lines.append("A Novel")
    lines.append("")
    lines.append("Draft 05")
    lines.append("June 2026")
    lines.append("")
    lines.append("Timothy")
    lines.append(form_feed)

    lines.append("TABLE OF CONTENTS")
    lines.append("")
    lookup = chapter_lookup()
    for act_label, act_subtitle, chapter_range in ACTS:
        lines.append(f"{act_label}: {act_subtitle}")
        for num in chapter_range:
            _, _, display = lookup[num]
            lines.append(f"  Chapter {num} — \"{display}\"")
        lines.append("")
    lines.append(form_feed)

    for num, filename, title, toc_display in CHAPTERS:
        paragraphs = load_chapter_paragraphs(filename)
        lines.append(f"CHAPTER {num}: \"{title}\"")
        lines.append("")
        for para in paragraphs:
            lines.append(indent_paragraph(para))
        lines.append(form_feed)

    return "\n".join(lines).rstrip("\f") + "\n"


def main() -> None:
    md_path = DRAFT_DIR / "Walk_This_Way_Draft_05_COMPLETE.md"
    txt_path = DRAFT_DIR / "Walk_This_Way_Draft_05_COMPLETE.txt"

    md_path.write_text(build_markdown(), encoding="utf-8")
    txt_path.write_text(build_plain_text(), encoding="utf-8")

    md_words = len(md_path.read_text(encoding="utf-8").split())
    txt_words = len(txt_path.read_text(encoding="utf-8").split())
    print(f"Wrote {md_path.name} ({md_words:,} words)")
    print(f"Wrote {txt_path.name} ({txt_words:,} words)")

    for num, filename, title, toc_display in CHAPTERS:
        paras = load_chapter_paragraphs(filename)
        if not paras:
            print(f"WARNING: Chapter {num} has no paragraphs after cleaning")


if __name__ == "__main__":
    main()
