#!/usr/bin/env python3
"""
Stephen King MCP Server — "The Writer's Toolbox"
PRIVATE & CONFIDENTIAL

A craft philosophy educational engine built on King's On Writing,
organized in 3-3-3 architecture: 3 Tools × 3 Modes × 3 Liberty Levels.

Tools:
  king_imagine  — Situations, stakes, fear, planning (Architecture)
  king_craft    — Voice, pacing, telepathy, building (Brick)
  king_revise   — Cutting and adding (Scalpel & Hose)

Modes:
  create    — Idea → story (default: nice)
  transform — Draft → better draft (default: neutral)
  edit      — Chapters → mastery (default: professional)

Liberty Levels:
  nice         — Encouraging but honest
  neutral      — Direct and balanced
  professional — Rigorous, numerical, no hand-holding
"""

import json
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

app = Server("stephen-king-toolbox")

DATA_DIR = Path(__file__).parent / "data"
KING_DATA_FILE = DATA_DIR / "king_analysis.json"

VALID_MODES = {"create", "transform", "edit"}
VALID_LEVELS = {"nice", "neutral", "professional"}
MODE_DEFAULTS = {"create": "nice", "transform": "neutral", "edit": "professional"}


def load_king_data() -> dict:
    """Load the King craft knowledge base."""
    if not KING_DATA_FILE.exists():
        return {}
    with open(KING_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_liberty(mode: str, level: str | None) -> str:
    """Resolve the liberty level, falling back to the mode's smart default."""
    if level and level in VALID_LEVELS:
        return level
    return MODE_DEFAULTS.get(mode, "neutral")


def format_liberty_voice(level: str, content: dict) -> dict:
    """Wrap response content with the appropriate liberty-level voice framing."""
    levels = content.pop("_liberty_levels", None)
    if levels is None:
        data = load_king_data()
        levels = data.get("liberty_levels", {})

    level_info = levels.get(level, {})
    content["liberty_level"] = {
        "level": level,
        "voice": level_info.get("voice", ""),
        "critical_rule": level_info.get("critical_rule", ""),
    }
    return content


def build_imagine_response(data: dict, idea: str, mode: str, level: str, context: str) -> dict:
    """Build a response for king_imagine — the Architecture tool."""
    situation = data.get("situation_over_plot", {})
    fear = data.get("fear_and_stakes", {})
    philosophy = data.get("core_philosophy", {}).get("principles", {})
    absh = data.get("absh_mapping", {}).get("architecture", {})
    settings = data.get("creative_settings", {}).get("king_imagine", {})

    fear_categories = []
    for fc in fear.get("fear_categories", []):
        fear_categories.append({
            "type": fc.get("type", ""),
            "technique": fc.get("technique", ""),
        })

    response = {
        "tool": "king_imagine",
        "mode": mode,
        "absh_phase": "A — Architecture",
        "idea": idea,
        "context": context if context else "No additional context provided",
        "creative_settings": settings,
        "situation_philosophy": {
            "core": situation.get("core_statement", ""),
            "principles": situation.get("principles", []),
            "scene_test": situation.get("scene_test", ""),
        },
        "situation_examples": situation.get("examples", {}),
        "fear_and_stakes": {
            "core": fear.get("core_statement", ""),
            "categories": fear_categories,
        },
        "key_principles": {
            "story_is_king": philosophy.get("story_is_king", {}).get("statement", ""),
            "character_drives_plot": philosophy.get("character_drives_plot", {}).get("statement", ""),
            "fear_of_beginning": philosophy.get("fear_of_beginning", {}).get("statement", ""),
        },
        "guidance": _imagine_guidance(level, idea),
        "_liberty_levels": data.get("liberty_levels", {}),
    }

    return format_liberty_voice(level, response)


def _imagine_guidance(level: str, idea: str) -> list[str]:
    """Generate level-appropriate guidance for the imagine tool."""
    base = [
        "Start with a SITUATION, not a plot. Put characters in a predicament.",
        "What is the central fear? Make it specific and concrete.",
        "Who are the characters? What do they want? What are they afraid of?",
        "What's the 'what if?' that makes this compelling?",
    ]
    if level == "nice":
        return [f"This idea has energy. Let's build on it."] + base + [
            "Don't worry about structure yet — let the situation breathe.",
            "Trust the idea. The story is already there; your job is excavation."
        ]
    elif level == "professional":
        return base + [
            "Rate the situation on a 1-10 scale. Be honest.",
            "Identify the weakest element and propose a specific fix.",
            "What would King cut from this concept? What would he add?"
        ]
    return base + [
        "What works about this situation? What needs sharpening?",
        "Is the fear specific enough? Can you name it in one sentence?"
    ]


def build_craft_response(data: dict, text: str, focus: str, mode: str, level: str) -> dict:
    """Build a response for king_craft — the Brick tool."""
    telepathy = data.get("telepathy_engine", {})
    voice = data.get("voice_craft", {})
    pacing = data.get("pacing_mastery", {})
    toolbox = data.get("writers_toolbox", {})
    absh = data.get("absh_mapping", {}).get("brick", {})
    settings = data.get("creative_settings", {}).get("king_craft", {})

    focus_data = {}
    if focus:
        focus_lower = focus.lower()
        if "voice" in focus_lower or "dialogue" in focus_lower:
            focus_data = voice
        elif "pacing" in focus_lower or "rhythm" in focus_lower:
            focus_data = pacing
        elif "telepathy" in focus_lower or "description" in focus_lower:
            focus_data = telepathy
        elif "toolbox" in focus_lower:
            focus_data = toolbox

    response = {
        "tool": "king_craft",
        "mode": mode,
        "absh_phase": "B — Brick",
        "text_analyzed": text[:300] + "..." if len(text) > 300 else text,
        "focus": focus if focus else "comprehensive",
        "creative_settings": settings,
        "telepathy_check": {
            "signal_elements": telepathy.get("signal", {}).get("elements", []),
            "noise_elements": telepathy.get("noise", {}).get("elements", []),
            "quality_formula": telepathy.get("quality_formula", ""),
        },
        "voice_craft": {
            "blue_collar": voice.get("blue_collar_authenticity", {}).get("techniques", [])[:3],
            "period_voice": voice.get("period_specific_voice", {}).get("techniques", [])[:3],
            "child_teen": voice.get("child_teen_pov", {}).get("techniques", [])[:3],
        },
        "pacing_check": {
            "page_turner": pacing.get("page_turner_technique", {}).get("techniques", [])[:3],
            "sentence_rhythm": pacing.get("sentence_rhythm", {}).get("techniques", [])[:3],
        },
        "focus_detail": focus_data if focus_data else "No specific focus — reviewing all craft elements",
        "guidance": _craft_guidance(level, focus),
        "_liberty_levels": data.get("liberty_levels", {}),
    }

    return format_liberty_voice(level, response)


def _craft_guidance(level: str, focus: str) -> list[str]:
    """Generate level-appropriate guidance for the craft tool."""
    base = [
        "Check the telepathy: is the image clear? Maximum signal, minimum noise.",
        "Check the voice: does it sound like a real person or a writer performing?",
        "Check the pacing: does every sentence earn its place?",
    ]
    if level == "nice":
        return ["There's real craft here. Let's sharpen it."] + base
    elif level == "professional":
        return base + [
            "Rate the telepathy clarity on 1-10.",
            "Identify every adverb. Justify each one or cut it.",
            "Find the passive voice. Rewrite in active.",
            "Where is the prose performing instead of communicating?"
        ]
    return base + [
        "What's working? What's noise? Be specific."
    ]


def build_revise_response(data: dict, text: str, mode: str, level: str, focus: str) -> dict:
    """Build a response for king_revise — the Scalpel & Hose tool."""
    revision = data.get("revision_philosophy", {})
    hard_rules = data.get("hard_rules", {}).get("rules", [])
    guidelines = data.get("agent_guidelines", {})
    settings_key = f"king_revise_{mode}"
    settings = data.get("creative_settings", {}).get(settings_key, {})

    scalpel_targets = revision.get("scalpel_king_cuts", {}).get("targets", [])
    hose_targets = revision.get("hose_king_additions", {}).get("targets", [])

    response = {
        "tool": "king_revise",
        "mode": mode,
        "absh_phase": "S + H — Scalpel & Hose",
        "text_analyzed": text[:500] + "..." if len(text) > 500 else text,
        "revision_focus": focus if focus else "comprehensive",
        "creative_settings": settings,
        "kings_formula": revision.get("kings_formula", ""),
        "scalpel_targets": scalpel_targets,
        "hose_targets": hose_targets,
        "closed_door_open_door": revision.get("closed_door_open_door", {}),
        "inline_notes": guidelines.get("inline_notes", {}),
        "honesty_protocol": guidelines.get("honesty_protocol", {}).get("core_rule", ""),
        "guidance": _revise_guidance(level, mode),
        "_liberty_levels": data.get("liberty_levels", {}),
    }

    if mode == "edit":
        response["hard_rules_checklist"] = [
            f"Rule {r['number']}: {r['rule']}" for r in hard_rules
        ]
        response["rating_scale"] = guidelines.get("honesty_protocol", {}).get("rating_scale", {})
        response["neurodiversity_notes"] = guidelines.get("neurodiversity_informed", {}).get("general", [])

    return format_liberty_voice(level, response)


def _revise_guidance(level: str, mode: str) -> list[str]:
    """Generate level-appropriate guidance for the revise tool."""
    if mode == "create":
        base = [
            "This is early-stage revision — shape the clay, don't polish it yet.",
            "Focus on situation clarity and character motivation first.",
            "Is the central fear specific and concrete?",
        ]
    elif mode == "transform":
        base = [
            "Quick targeted improvement — in, out, better.",
            "Apply the Scalpel: cut adverbs, passive voice, overwriting.",
            "Apply the Hose: add one specific sensory detail, one money sentence.",
        ]
    else:
        base = [
            "Full editorial treatment. Hold nothing back.",
            "Rate on 1-10 scale. Be honest — the Phantom Cowboy lesson applies.",
            "Group changes by category: pacing, voice, telepathy, etc.",
            "Provide a revision plan with specific, actionable steps.",
            "Use <<Agent note>> inline for editorial commentary.",
        ]

    if level == "nice":
        return ["Let's find what's strong and build from there."] + base
    elif level == "professional":
        return base + [
            "No flattery. Rate what the prose earns, not what the author hopes.",
            "Identify the top 3 failures. Provide the fix for each.",
        ]
    return base


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List the 3 King MCP tools."""
    return [
        Tool(
            name="king_imagine",
            description=(
                "Architecture phase: develop situations, stakes, and fear from a seed idea. "
                "Modes: create (default nice), transform (default neutral), edit (default professional). "
                "Override liberty level with: nice, neutral, professional."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "idea": {
                        "type": "string",
                        "description": "The seed idea, situation, image, or concept to develop",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["create", "transform", "edit"],
                        "description": "Workflow mode (default: create)",
                    },
                    "liberty_level": {
                        "type": "string",
                        "enum": ["nice", "neutral", "professional"],
                        "description": "Feedback delivery level (default: mode's smart default)",
                    },
                    "context": {
                        "type": "string",
                        "description": "Optional context: genre, characters, setting, constraints",
                    },
                },
                "required": ["idea"],
            },
        ),
        Tool(
            name="king_craft",
            description=(
                "Brick phase: refine voice, pacing, telepathy, and prose building. "
                "Analyzes text through King's craft lens — signal vs noise, authentic voice, rhythm. "
                "Focus areas: voice, dialogue, pacing, rhythm, telepathy, description, toolbox."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to analyze and improve",
                    },
                    "focus": {
                        "type": "string",
                        "description": "Optional focus area: voice, dialogue, pacing, rhythm, telepathy, description, toolbox",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["create", "transform", "edit"],
                        "description": "Workflow mode (default: transform)",
                    },
                    "liberty_level": {
                        "type": "string",
                        "enum": ["nice", "neutral", "professional"],
                        "description": "Feedback delivery level (default: mode's smart default)",
                    },
                },
                "required": ["text"],
            },
        ),
        Tool(
            name="king_revise",
            description=(
                "Scalpel & Hose phase: cutting and adding. "
                "Create mode: shape early material. Transform mode: quick targeted polish. "
                "Edit mode: full editorial treatment with rating, revision plan, and inline notes. "
                "Applies King's '2nd draft = 1st draft minus 10%' formula."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to revise",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["create", "transform", "edit"],
                        "description": "Workflow mode (default: edit)",
                    },
                    "liberty_level": {
                        "type": "string",
                        "enum": ["nice", "neutral", "professional"],
                        "description": "Feedback delivery level (default: mode's smart default)",
                    },
                    "focus": {
                        "type": "string",
                        "description": "Optional revision focus: scalpel, hose, adverbs, passive_voice, pacing, dialogue, all",
                    },
                },
                "required": ["text"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Route tool calls to the appropriate handler."""
    data = load_king_data()

    if not data:
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "King craft knowledge base not found",
                "path": str(KING_DATA_FILE),
                "suggestion": "Verify data/king_analysis.json exists",
            }, indent=2),
        )]

    if name == "king_imagine":
        idea = arguments.get("idea", "")
        mode = arguments.get("mode", "create")
        if mode not in VALID_MODES:
            mode = "create"
        level = resolve_liberty(mode, arguments.get("liberty_level"))
        context = arguments.get("context", "")

        result = build_imagine_response(data, idea, mode, level, context)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "king_craft":
        text = arguments.get("text", "")
        focus = arguments.get("focus", "")
        mode = arguments.get("mode", "transform")
        if mode not in VALID_MODES:
            mode = "transform"
        level = resolve_liberty(mode, arguments.get("liberty_level"))

        result = build_craft_response(data, text, focus, mode, level)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "king_revise":
        text = arguments.get("text", "")
        mode = arguments.get("mode", "edit")
        if mode not in VALID_MODES:
            mode = "edit"
        level = resolve_liberty(mode, arguments.get("liberty_level"))
        focus = arguments.get("focus", "")

        result = build_revise_response(data, text, mode, level, focus)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    return [TextContent(
        type="text",
        text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2),
    )]


async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
