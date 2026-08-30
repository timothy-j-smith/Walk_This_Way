#!/usr/bin/env python3
"""
Style Emulation MCP — PRIVATE MFA tutoring companion.
Educational use only. Not for publication.

Two-layer model: this server loads the Author Engine KB + the five-master
signature table and returns a teaching packet. The host model writes the
emulation. Timothy reads it, then writes his own version.
"""

import json
import re
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

HERE = Path(__file__).resolve().parent
ENGINES = HERE.parent / "AUTHOR_ENGINES" / "data"
LEHANE_FILE = HERE.parent / "DENNIS_LEHANE_MCP" / "data" / "lehane_analysis.json"
SIGNATURES = json.loads((HERE / "signatures.json").read_text(encoding="utf-8"))

COMMITTEE = {
    "ondaatje": "ondaatje.json",
    "dickey": "dickey.json",
    "king": "king.json",
    "robinson": "robinson.json",
    "kesey": "kesey.json",
    "russo": "russo.json",
    "mccarthy": "mccarthy.json",
    "goldman": "goldman.json",
    "chbosky": "chbosky.json",
    "tartt": "tartt.json",
    "proulx": "proulx.json",
    "whitehead": "whitehead.json",
    "houston": "houston.json",
    "ludlum": "ludlum.json",
    "harris": "harris.json",
    "lehane": None,
}

NEVER = [
    "Never emulate a voice outside the Author MCP committee unless Timothy approves a new engine.",
    "Never run style emulation in a finished-chapter polish pass. Learning, not editing.",
    "Never inflate quality. Name the move. Phantom Cowboy applies.",
    "Never keep the emulation as the draft. Timothy writes his own version after.",
    "Never blend two masters in one output.",
    "Never change scene, characters, or plot. Only the voice.",
]

PROCEDURE = [
    "Read the target Author MCP first (KB slices below). Memory drift produces pastiche.",
    "Apply only ONE master's lens.",
    "Render the SAME material Timothy provided.",
    "Tag the specific craft moves after the prose. That list is the educational payload.",
    "If asked, save as style-emulation_{author}_{date}.txt for print.",
    "Close with: Want me to do this in another master's voice for comparison?",
]

app = Server("style-emulation")


def measure_style(text: str) -> dict[str, Any]:
    """Quantitative cousin of the lost NLTK analyzer — no Anthropic required."""
    words = re.findall(r"[A-Za-z']+", text)
    sents = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    quotes = len(re.findall(r'"[^"]+"', text))
    out: dict[str, Any] = {
        "word_count": len(words),
        "sentence_count": len(sents),
        "avg_sentence_length": round(len(words) / max(len(sents), 1), 2),
        "dialogue_spans": quotes,
        "unique_words": len(set(w.lower() for w in words)),
    }
    if words:
        out["lexical_diversity"] = round(out["unique_words"] / len(words), 3)
    try:
        import textstat
        out["flesch_kincaid_grade"] = textstat.flesch_kincaid_grade(text)
        out["reading_ease"] = textstat.flesch_reading_ease(text)
    except Exception as exc:
        out["textstat"] = f"unavailable ({exc})"
    return out


def load_kb(key: str) -> dict[str, Any]:
    key = key.lower().strip()
    aliases = {"stephen king": "king", "james dickey": "dickey",
               "michael ondaatje": "ondaatje", "dennis lehane": "lehane",
               "marilynne robinson": "robinson"}
    key = aliases.get(key, key)
    if key not in COMMITTEE:
        return {"error": f"Unknown master '{key}'", "available": sorted(COMMITTEE)}
    if key == "lehane":
        if not LEHANE_FILE.exists():
            return {"error": "Lehane analysis file missing", "key": key}
        raw = json.loads(LEHANE_FILE.read_text(encoding="utf-8"))
        return {
            "key": key,
            "name": "Dennis Lehane",
            "focus_work": "Mystic River / Gone Baby Gone",
            "writing_dna": list(raw.keys())[:8],
            "signature_moves": SIGNATURES.get("lehane", {}),
            "source": str(LEHANE_FILE),
        }
    path = ENGINES / COMMITTEE[key]
    if not path.exists():
        return {"error": f"Author engine missing: {path}", "key": key}
    kb = json.loads(path.read_text(encoding="utf-8"))
    meta = kb.get("meta", {})
    return {
        "key": key,
        "name": meta.get("name", key.title()),
        "focus_work": meta.get("focus_work", ""),
        "writing_dna": kb.get("writing_dna", []),
        "signature_moves": kb.get("signature_moves", []),
        "tutor_prompts": kb.get("tutor_prompts", []),
        "pitfalls": kb.get("pitfalls", []),
        "focus_deep": kb.get("focus_deep", {}),
        "quick_signature": SIGNATURES.get(key, {}),
        "source": str(path),
    }


def packet(form: str, key: str, material: str, extra: dict[str, Any]) -> str:
    kb = load_kb(key)
    if "error" in kb:
        return json.dumps(kb, indent=2)
    out = {
        "form": form,
        "private_mfa": True,
        "keep_the_emulation": False,
        "engine": kb.get("name"),
        "focus_work": kb.get("focus_work"),
        "quick_signature": kb.get("quick_signature") or kb.get("signature_moves"),
        "writing_dna": kb.get("writing_dna"),
        "signature_moves": kb.get("signature_moves") if isinstance(kb.get("signature_moves"), list) else None,
        "tutor_prompts": kb.get("tutor_prompts", []),
        "pitfalls": kb.get("pitfalls", []),
        "student_material": material or "(none — ask for it)",
        "procedure": PROCEDURE,
        "never": NEVER,
        "teaching_instructions": (
            f"You are tutoring Timothy through {kb.get('name')}'s craft. "
            "Write the requested emulation of HIS material only. "
            "Then tag the moves. Then stop. He will write his own version. "
            "Do not praise the emulation. Name what the master did."
        ),
        "close_with": "Want me to do this in another master's voice for comparison?",
    }
    out.update(extra)
    return json.dumps(out, indent=2, ensure_ascii=False)


@app.list_tools()
async def list_tools() -> list[Tool]:
    author_arg = {
        "type": "object",
        "properties": {
            "author": {
                "type": "string",
                "description": "Master key: ondaatje, dickey, king, lehane, robinson, russo, kesey, ...",
            },
            "text": {
                "type": "string",
                "description": "Scene description or Timothy's draft",
            },
        },
        "required": ["author", "text"],
    }
    return [
        Tool(
            name="list_masters",
            description="List the Style Emulation committee (Author Engines + five-master signatures).",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="get_master_signature",
            description="Quick-reference signature plus Author Engine KB for one master. Read this before emulating.",
            inputSchema={
                "type": "object",
                "properties": {
                    "author": {"type": "string", "description": "Master key, e.g. ondaatje"},
                },
                "required": ["author"],
            },
        ),
        Tool(
            name="emulate_paragraph",
            description="Form A: one paragraph (80-200 words) in one master's voice. Learning only.",
            inputSchema=author_arg,
        ),
        Tool(
            name="emulate_opening_lines",
            description="Form B: three candidate opening lines in one master's voice, each tagged.",
            inputSchema=author_arg,
        ),
        Tool(
            name="emulate_scene",
            description="Form C: re-render Timothy's 1-2 paragraph draft (300-800 words) plus see-what-I-see notes.",
            inputSchema=author_arg,
        ),
        Tool(
            name="style_emulation_rules",
            description="Protocol, never-rules, and how this differs from Fiction Reverse Engineering.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="extract_style_profile",
            description="Quantitative style metrics for a passage (sentence length, dialogue, reading level). Learning/diagnostic only.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Passage to measure"},
                    "author_name": {"type": "string", "description": "Optional label, e.g. Lehane sample"},
                },
                "required": ["text"],
            },
        ),
        Tool(
            name="analyze_style_match",
            description="Compare two passages by metrics (your text vs a target sample). Not a polish pass.",
            inputSchema={
                "type": "object",
                "properties": {
                    "your_text": {"type": "string"},
                    "target_text": {"type": "string", "description": "Target author's sample"},
                    "target_author": {"type": "string"},
                },
                "required": ["your_text", "target_text"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    args = arguments or {}
    author = args.get("author", "")
    text = args.get("text", "")

    if name == "list_masters":
        rows = []
        for key in sorted(COMMITTEE):
            sig = SIGNATURES.get(key, {})
            rows.append({
                "key": key,
                "name": sig.get("name") or key,
                "primary_move": sig.get("primary_move", "See Author Engine"),
                "has_engine": True,
            })
        body = {
            "committee": rows,
            "five_core_signatures": list(SIGNATURES.keys()),
            "note": "One master per output. Read get_master_signature before emulating.",
        }
        return [TextContent(type="text", text=json.dumps(body, indent=2, ensure_ascii=False))]

    if name == "get_master_signature":
        return [TextContent(type="text", text=json.dumps(load_kb(author), indent=2, ensure_ascii=False))]

    if name == "emulate_paragraph":
        return [TextContent(type="text", text=packet(
            "A. SINGLE PARAGRAPH (80-200 words)",
            author,
            text,
            {"task": "One paragraph in the master's voice. Tag the move(s)."},
        ))]

    if name == "emulate_opening_lines":
        return [TextContent(type="text", text=packet(
            "B. OPENING LINE (3 candidates)",
            author,
            text,
            {"task": "Three opening lines. Tag each: withholds, plants, body-first, time-pool, etc."},
        ))]

    if name == "emulate_scene":
        return [TextContent(type="text", text=packet(
            "C. SCENE EMULATION (300-800 words) + see-what-I-see",
            author,
            text,
            {"task": "Same scene, master's voice, then a companion list of moves vs Timothy's original."},
        ))]

    if name == "extract_style_profile":
        body = {
            "label": args.get("author_name") or "sample",
            "metrics": measure_style(text),
            "note": "Metrics only. For voice translation use emulate_paragraph / emulate_scene.",
        }
        return [TextContent(type="text", text=json.dumps(body, indent=2))]

    if name == "analyze_style_match":
        yours = measure_style(args.get("your_text", ""))
        target = measure_style(args.get("target_text", ""))
        body = {
            "target_author": args.get("target_author") or "target",
            "yours": yours,
            "target": target,
            "deltas": {
                k: round(yours.get(k, 0) - target.get(k, 0), 3)
                for k in ("avg_sentence_length", "lexical_diversity", "dialogue_spans")
                if isinstance(yours.get(k), (int, float)) and isinstance(target.get(k), (int, float))
            },
            "note": "Diagnostic. Do not force the draft to match the numbers.",
        }
        return [TextContent(type="text", text=json.dumps(body, indent=2))]

    if name == "style_emulation_rules":
        body = {
            "what_this_is": "Generative companion to Fiction Reverse Engineering.",
            "reverse_engineering": "Measures the formula.",
            "style_emulation": "Produces prose IN the formula so Timothy can see the lesson and write his own.",
            "procedure": PROCEDURE,
            "never": NEVER,
            "protocol_file": str(HERE / "PROTOCOL.md"),
        }
        return [TextContent(type="text", text=json.dumps(body, indent=2))]

    return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]


async def main() -> None:
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
