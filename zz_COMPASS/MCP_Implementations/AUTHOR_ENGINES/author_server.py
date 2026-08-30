#!/usr/bin/env python3
"""
AUTHOR ENGINES MCP — generic private tutoring server.
PRIVATE & CONFIDENTIAL — Timothy's personal MFA program. Educational use only.

One codebase serves every author engine. Each mcp.json entry passes --author <key>;
the server loads data/<key>.json and registers four author-prefixed tools:
  <key>_guide    — return craft KB slices (writing DNA, moves, pitfalls, prompts)
  <key>_imagine  — CREATE mode   (A: Architecture)   default liberty: Nice
  <key>_craft    — TRANSFORM mode (B: Brick)          default liberty: Neutral
  <key>_revise   — EDIT mode     (S+H: Scalpel&Hose)  default liberty: Professional

Two-layer model: this server routes and returns KB slices + teaching instructions;
the host model does the teaching. NICE != DISHONEST.
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--author", required=True, help="author key, e.g. russo")
parser.add_argument("--selftest", action="store_true", help="load KB, print OK, exit")
ARGS = parser.parse_args()

KEY = ARGS.author
DATA_FILE = Path(__file__).parent / "data" / f"{KEY}.json"

try:
    KB = json.loads(DATA_FILE.read_text(encoding="utf-8"))
except FileNotFoundError:
    sys.exit(f"ERROR: knowledge base not found: {DATA_FILE}")

META = KB.get("meta", {})
NAME = META.get("name", KEY.title())
FOCUS = META.get("focus_work", "")

if ARGS.selftest:
    print(f"OK — {NAME} engine loaded ({DATA_FILE.name}); focus: {FOCUS}; "
          f"dna={len(KB.get('writing_dna', []))} moves={len(KB.get('signature_moves', []))} "
          f"prompts={len(KB.get('tutor_prompts', []))}")
    sys.exit(0)

from mcp.server import Server                      # noqa: E402
from mcp.types import Tool, TextContent            # noqa: E402
import mcp.server.stdio                            # noqa: E402

app = Server(f"{KEY}-engine")

LIBERTY = {
    "nice": "NICE: name what is alive first, then concrete upgrades. No inflation.",
    "neutral": "NEUTRAL: works/fails because X. One revision focus. Direct.",
    "professional": "PROFESSIONAL: prioritized failure modes, revision plan, honest score if asked.",
}

SHARED_GUIDELINES = KB.get("guidelines", {
    "honesty_protocol": "No inflated ratings. Tone changes; truth does not.",
    "absh_awareness": "Respect Architecture -> Brick -> Scalpel -> Hose. The Brick is wet: never edit during Brick.",
    "voice_intactness": "Always end with the single question: is the voice that came through still intact?",
    "fair_use": "Paraphrase and craft labels only. No bulk reproduction of copyrighted text.",
})


def payload(mode: str, liberty: str, user_input: str, extra: dict) -> str:
    out = {
        "engine": NAME,
        "focus_work": FOCUS,
        "mode": mode,
        "liberty_level": liberty,
        "liberty_instruction": LIBERTY.get(liberty, LIBERTY["neutral"]),
        "teaching_instructions": (
            f"You are tutoring Timothy through {NAME}'s craft (focus: {FOCUS}). "
            "Use the KB slices below as the craft frame. Teach with specifics, quote his "
            "lines back, propose concrete revisions using <<Agent note: ...>> notation. "
            "This is his private MFA program - craft education, never pastiche-for-publication."
        ),
        "writing_dna": KB.get("writing_dna", []),
        "guidelines": SHARED_GUIDELINES,
        "student_input": user_input or "(none provided - ask for it)",
    }
    out.update(extra)
    return json.dumps(out, indent=2, ensure_ascii=False)


@app.list_tools()
async def list_tools() -> list[Tool]:
    text_arg = {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "Seed idea, excerpt, or chapter text"},
            "liberty": {"type": "string", "enum": ["nice", "neutral", "professional"],
                        "description": "Override the default liberty level"},
        },
    }
    return [
        Tool(
            name=f"{KEY}_guide",
            description=f"{NAME} craft guide - writing DNA, signature moves, pitfalls, tutor "
                        f"prompts and project applications drawn from {FOCUS}. Optional "
                        f"'section' narrows the slice.",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {"type": "string",
                                "description": "Optional: writing_dna | signature_moves | "
                                               "tutor_prompts | pitfalls | apply_to_projects | focus_deep"}
                },
            },
        ),
        Tool(
            name=f"{KEY}_imagine",
            description=f"CREATE mode (A: Architecture). Seed idea -> situation, structure and "
                        f"stakes through {NAME}'s lens. Default liberty: Nice.",
            inputSchema=text_arg,
        ),
        Tool(
            name=f"{KEY}_craft",
            description=f"TRANSFORM mode (B: Brick support). Excerpt -> surgical improvement in "
                        f"{NAME}'s craft frame. Default liberty: Neutral.",
            inputSchema=text_arg,
        ),
        Tool(
            name=f"{KEY}_revise",
            description=f"EDIT mode (S+H: Scalpel & Hose). Passage/chapter -> deep pass: cut what "
                        f"fails, add only what is missing. Default liberty: Professional.",
            inputSchema=text_arg,
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    args = arguments or {}
    text = args.get("text", "")

    if name == f"{KEY}_guide":
        section = args.get("section")
        if section and section in KB:
            body = {"engine": NAME, "focus_work": FOCUS, section: KB[section],
                    "guidelines": SHARED_GUIDELINES}
        else:
            body = {"engine": NAME, "focus_work": FOCUS,
                    "writing_dna": KB.get("writing_dna", []),
                    "signature_moves": KB.get("signature_moves", []),
                    "focus_deep": KB.get("focus_deep", {}),
                    "tutor_prompts": KB.get("tutor_prompts", []),
                    "pitfalls": KB.get("pitfalls", []),
                    "apply_to_projects": KB.get("apply_to_projects", {}),
                    "guidelines": SHARED_GUIDELINES}
        return [TextContent(type="text", text=json.dumps(body, indent=2, ensure_ascii=False))]

    if name == f"{KEY}_imagine":
        lib = args.get("liberty", "nice")
        return [TextContent(type="text", text=payload("CREATE (Architecture)", lib, text, {
            "focus_deep": KB.get("focus_deep", {}),
            "task": "Build situation, stakes and structure from the seed. Map, not fence."}))]

    if name == f"{KEY}_craft":
        lib = args.get("liberty", "neutral")
        return [TextContent(type="text", text=payload("TRANSFORM (Brick support)", lib, text, {
            "signature_moves": KB.get("signature_moves", []),
            "task": "Surgical improvement of the excerpt. Specific lines, concrete rewrites."}))]

    if name == f"{KEY}_revise":
        lib = args.get("liberty", "professional")
        return [TextContent(type="text", text=payload("EDIT (Scalpel & Hose)", lib, text, {
            "signature_moves": KB.get("signature_moves", []),
            "pitfalls": KB.get("pitfalls", []),
            "tutor_prompts": KB.get("tutor_prompts", []),
            "task": "Deep pass. Scalpel: cut with rationale. Hose: add ONLY what is missing. "
                    "End with the voice-intactness question."}))]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await app.run(read, write, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
