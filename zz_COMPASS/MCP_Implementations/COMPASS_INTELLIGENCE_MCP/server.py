#!/usr/bin/env python3
"""
COMPASS Intelligence MCP Server
================================
The brain of the Compass Writing Ecosystem.

Provides tools for:
1. Knowledge Graph -> Mermaid transformation (visualize your novel's structure)
2. Chapter text -> structured entity extraction (feed the Knowledge Graph)
3. Prompt engineering pattern management (XML tags, CoT, context pinning, few-shots)
4. Pipeline orchestration helpers

This MCP transforms data BETWEEN other MCPs:
  Chapter Text -> [THIS MCP] -> Structured Entities -> Knowledge Graph Memory
  Knowledge Graph Memory -> [THIS MCP] -> Mermaid Syntax -> Mermaid MCP
"""

import json
import os
import re
from pathlib import Path
from typing import Any
from datetime import datetime
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("compass-intelligence")

# Data paths
DATA_DIR = Path(__file__).parent / "data"
PROMPTS_DIR = DATA_DIR / "prompts"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
PROMPTS_DIR.mkdir(exist_ok=True)

# ============================================================
# PROMPT PATTERN STORAGE
# ============================================================

PATTERNS_FILE = DATA_DIR / "prompt_patterns.json"

def load_patterns() -> dict:
    """Load prompt engineering patterns from JSON"""
    if not PATTERNS_FILE.exists():
        default = {
            "xml_tags": {
                "character_extraction": "<character_extraction>\nFor EACH character who appears, speaks, or is referenced:\n- name, role, emotional_state, key_actions, key_dialogue\n- relationships_shown with evidence\n- observations (traits, behaviors, details)\n</character_extraction>",
                "location_extraction": "<location_extraction>\nFor EACH location or setting:\n- name, physical_description, atmosphere\n- narrative_function, characters_present\n- observations\n</location_extraction>",
                "event_extraction": "<event_extraction>\nFor EACH significant plot beat:\n- name, description, characters_involved\n- location, chapter_position, consequences\n- observations\n</event_extraction>",
                "theme_extraction": "<theme_extraction>\nFor EACH theme expressed or developed:\n- name, how_expressed, characters_connected\n- development_stage (introduced/developing/challenged/deepened/resolved)\n- observations\n</theme_extraction>",
                "plot_thread_extraction": "<plot_thread_extraction>\nFor EACH plot thread advanced or introduced:\n- name, status, description\n- connected_characters, observations\n</plot_thread_extraction>",
                "craft_extraction": "<craft_extraction>\nFor NOTABLE prose techniques:\n- technique, example (brief quote)\n- effect on reader, observations\n</craft_extraction>",
                "system_context": "<system_context>\nYou are a literary intelligence extraction system.\nExtract every narratively significant element into structured categories.\nBe thorough but precise. Only extract what is ACTUALLY in the text.\nUse Chain of Thought reasoning for each category.\n</system_context>",
                "reference_context": "<reference_context>\nPin the following for cross-reference:\n- Story_Bible/ (character DNA, plot DNA, world DNA)\n- Previous Knowledge Graph entities\n</reference_context>"
            },
            "chain_of_thought": {
                "character_analysis": "Step 1: Identify all characters mentioned.\nStep 2: For each character, note their actions and dialogue.\nStep 3: Analyze emotional state and motivation.\nStep 4: Map relationships shown in this passage.\nStep 5: Compare against established character DNA for consistency.",
                "plot_analysis": "Step 1: Identify the main plot beats in this chapter.\nStep 2: Determine chapter position (opening/rising/climax/falling/closing).\nStep 3: Trace cause-and-effect chains.\nStep 4: Identify what this chapter sets up for future chapters.\nStep 5: Check against established plot threads for continuity.",
                "theme_analysis": "Step 1: What themes are present in this chapter?\nStep 2: How are they expressed (through character, setting, action, dialogue)?\nStep 3: Are any themes in tension with each other?\nStep 4: Has a theme deepened, been challenged, or resolved?\nStep 5: Which characters embody or oppose each theme?"
            },
            "context_pinning": {
                "novel_context": "Always pin: Story_Bible/, Character DNA files, Plot DNA, World DNA, previous Knowledge Graph state.",
                "chapter_context": "Pin: Previous chapter summary, current chapter file, next chapter outline (if exists).",
                "character_context": "Pin: Character's full DNA profile, all scenes they appear in, relationship map."
            },
            "few_shot_examples": {
                "character_extraction_example": "INPUT: 'Nick leaned against the doorframe, his guitar case hanging from one hand like a question mark.'\nOUTPUT: {\n  \"name\": \"Nick Johnson\",\n  \"physical_details\": \"Leaning posture, carrying guitar case\",\n  \"emotional_state\": \"Uncertain, tentative — guitar case 'like a question mark'\",\n  \"observations\": [\"Guitar is extension of identity\", \"Body language shows uncertainty\", \"Simile suggests seeking something\"]\n}",
                "event_extraction_example": "INPUT: 'The first chord rang out across the lake, and every kid at Camp Winnipesaukee stopped.'\nOUTPUT: {\n  \"name\": \"Nick's Breakthrough Performance\",\n  \"description\": \"Nick plays guitar at camp, enters flow state, captivates audience\",\n  \"chapter_position\": \"climax\",\n  \"consequences\": \"Establishes natural talent, sets up music as identity\"\n}"
            }
        }
        save_patterns(default)
        return default
    with open(PATTERNS_FILE, 'r') as f:
        return json.load(f)


def save_patterns(patterns: dict) -> None:
    """Save prompt engineering patterns"""
    with open(PATTERNS_FILE, 'w') as f:
        json.dump(patterns, f, indent=2)


# ============================================================
# MERMAID GENERATION HELPERS
# ============================================================

def sanitize_id(name: str) -> str:
    """Convert entity name to valid Mermaid node ID"""
    return re.sub(r'[^a-zA-Z0-9]', '_', name).strip('_')


def truncate(text: str, max_len: int = 50) -> str:
    """Truncate text for Mermaid labels"""
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "..."


def entities_to_mermaid(entities: list, relations: list,
                        filter_type: str = None,
                        style: str = "full") -> str:
    """
    Transform Knowledge Graph entities/relations into Mermaid diagram syntax.

    Args:
        entities: List of {name, entityType, observations[]}
        relations: List of {from, to, relationType}
        filter_type: Optional entity type to filter (e.g., "character")
        style: "full" (with observations) or "simple" (names only)
    """
    # Color mapping by entity type
    colors = {
        "character": "#e74c3c",
        "location": "#1abc9c",
        "event": "#3498db",
        "plot_thread": "#9b59b6",
        "theme": "#f39c12",
        "craft_note": "#2ecc71",
        "world_rule": "#e67e22",
        "research": "#95a5a6",
        "system": "#7f8c8d"
    }

    # Group entities by type
    groups = {}
    entity_names = set()
    for e in entities:
        etype = e.get("entityType", "other")
        if filter_type and etype != filter_type:
            continue
        if etype not in groups:
            groups[etype] = []
        groups[etype].append(e)
        entity_names.add(e["name"])

    # Build Mermaid syntax
    lines = ["graph TD"]

    # Subgraph labels
    subgraph_labels = {
        "character": "Characters",
        "location": "Locations",
        "event": "Key Events",
        "plot_thread": "Plot Threads",
        "theme": "Themes",
        "craft_note": "Craft Notes",
        "world_rule": "World Rules",
        "research": "Research",
        "system": "System"
    }

    for etype, ents in groups.items():
        label = subgraph_labels.get(etype, etype.replace("_", " ").title())
        lines.append(f"  subgraph {sanitize_id(label)}[\"{label}\"]")
        for e in ents:
            node_id = sanitize_id(e["name"])
            if style == "full" and e.get("observations"):
                first_obs = truncate(e["observations"][0], 40)
                # Escape quotes for Mermaid
                first_obs = first_obs.replace('"', "'")
                lines.append(f'    {node_id}["{e["name"]}<br/>{first_obs}"]')
            else:
                lines.append(f'    {node_id}["{e["name"]}"]')
        lines.append("  end")

    # Add relations (only between entities in scope)
    for r in relations:
        from_name = r.get("from", "")
        to_name = r.get("to", "")
        if from_name in entity_names and to_name in entity_names:
            from_id = sanitize_id(from_name)
            to_id = sanitize_id(to_name)
            rel = r.get("relationType", "relates_to")
            lines.append(f'  {from_id} -->|{rel}| {to_id}')

    # Add style directives
    for etype, ents in groups.items():
        color = colors.get(etype, "#95a5a6")
        for e in ents:
            node_id = sanitize_id(e["name"])
            lines.append(f"  style {node_id} fill:{color},color:#fff")

    return "\n".join(lines)


# ============================================================
# CHAPTER EXTRACTION HELPERS
# ============================================================

def generate_extraction_prompt(chapter_text: str, extraction_types: list = None) -> str:
    """
    Generate a structured XML-tagged extraction prompt for a chapter.
    This prompt is designed to be sent to Claude for processing.
    """
    patterns = load_patterns()

    if extraction_types is None:
        extraction_types = ["characters", "locations", "events",
                          "themes", "plot_threads", "craft"]

    prompt_parts = []

    # System context
    prompt_parts.append(patterns["xml_tags"].get("system_context", ""))
    prompt_parts.append("")

    # Reference context
    prompt_parts.append(patterns["xml_tags"].get("reference_context", ""))
    prompt_parts.append("")

    # Input
    prompt_parts.append("<input>")
    prompt_parts.append(chapter_text[:500] + "..." if len(chapter_text) > 500
                       else chapter_text)
    prompt_parts.append("</input>")
    prompt_parts.append("")

    # Extraction instructions
    prompt_parts.append("<extraction_instructions>")

    type_mapping = {
        "characters": "character_extraction",
        "locations": "location_extraction",
        "events": "event_extraction",
        "themes": "theme_extraction",
        "plot_threads": "plot_thread_extraction",
        "craft": "craft_extraction"
    }

    for i, ext_type in enumerate(extraction_types, 1):
        tag_key = type_mapping.get(ext_type)
        if tag_key and tag_key in patterns["xml_tags"]:
            prompt_parts.append(f"\nSTEP {i}: {ext_type.upper()} EXTRACTION")
            prompt_parts.append(patterns["xml_tags"][tag_key])

    prompt_parts.append("</extraction_instructions>")
    prompt_parts.append("")

    # Chain of Thought guidance
    prompt_parts.append("<chain_of_thought>")
    for cot_type in ["character_analysis", "plot_analysis", "theme_analysis"]:
        if cot_type in patterns["chain_of_thought"]:
            prompt_parts.append(f"\n{cot_type.upper()}:")
            prompt_parts.append(patterns["chain_of_thought"][cot_type])
    prompt_parts.append("</chain_of_thought>")
    prompt_parts.append("")

    # Output format
    prompt_parts.append("<output_format>")
    prompt_parts.append("Return structured JSON with:")
    prompt_parts.append('  "entities": [{"name": "...", "entityType": "...", "observations": [...]}]')
    prompt_parts.append('  "relations": [{"from": "...", "to": "...", "relationType": "..."}]')
    prompt_parts.append("Use active voice for relation types.")
    prompt_parts.append("</output_format>")

    return "\n".join(prompt_parts)


# ============================================================
# TOOL DEFINITIONS
# ============================================================

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Compass Intelligence tools"""
    return [
        # === MERMAID VISUALIZATION ===
        Tool(
            name="kg_to_mermaid",
            description="Transform Knowledge Graph entities and relations into Mermaid diagram syntax. Feed the output to the Mermaid MCP's generate_mermaid_diagram tool to create a visual diagram. Accepts the JSON output from Knowledge Graph Memory's read_graph tool.",
            inputSchema={
                "type": "object",
                "properties": {
                    "entities": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Array of entities from Knowledge Graph Memory read_graph (each has name, entityType, observations[])"
                    },
                    "relations": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Array of relations from Knowledge Graph Memory read_graph (each has from, to, relationType)"
                    },
                    "filter_type": {
                        "type": "string",
                        "description": "Optional: filter to show only one entity type (character, location, event, theme, plot_thread, craft_note)"
                    },
                    "style": {
                        "type": "string",
                        "enum": ["full", "simple"],
                        "description": "full = show first observation as subtitle; simple = names only. Default: full"
                    }
                },
                "required": ["entities", "relations"]
            }
        ),

        # === CHAPTER EXTRACTION ===
        Tool(
            name="generate_extraction_prompt",
            description="Generate an XML-tagged extraction prompt for analyzing a chapter. The generated prompt uses XML tags, Chain of Thought, and few-shot patterns to structure the extraction. Send the returned prompt to Claude along with the chapter text for structured entity extraction.",
            inputSchema={
                "type": "object",
                "properties": {
                    "chapter_text": {
                        "type": "string",
                        "description": "The chapter text to analyze (or first 500 chars as preview)"
                    },
                    "extraction_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Which types to extract: characters, locations, events, themes, plot_threads, craft. Default: all."
                    }
                },
                "required": ["chapter_text"]
            }
        ),

        Tool(
            name="text_to_kg_entities",
            description="Parse structured extraction text (from Claude's response to an extraction prompt) into Knowledge Graph compatible entities and relations. Accepts JSON with 'entities' and 'relations' arrays and validates them for Knowledge Graph Memory format.",
            inputSchema={
                "type": "object",
                "properties": {
                    "extraction_json": {
                        "type": "string",
                        "description": "JSON string containing extracted entities and relations"
                    }
                },
                "required": ["extraction_json"]
            }
        ),

        # === PROMPT ENGINEERING PATTERNS ===
        Tool(
            name="get_prompt_pattern",
            description="Retrieve a stored prompt engineering pattern by category and name. Categories: xml_tags, chain_of_thought, context_pinning, few_shot_examples.",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["xml_tags", "chain_of_thought", "context_pinning", "few_shot_examples"],
                        "description": "Pattern category"
                    },
                    "name": {
                        "type": "string",
                        "description": "Pattern name within the category. Use 'list' to see all available patterns."
                    }
                },
                "required": ["category"]
            }
        ),

        Tool(
            name="save_prompt_pattern",
            description="Save a new prompt engineering pattern or update an existing one. Use this to build your library of XML tags, Chain of Thought templates, context pinning strategies, and few-shot examples.",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["xml_tags", "chain_of_thought", "context_pinning", "few_shot_examples"],
                        "description": "Pattern category"
                    },
                    "name": {
                        "type": "string",
                        "description": "Pattern name (e.g., 'dialogue_analysis', 'pacing_check')"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "The pattern content (XML tag template, CoT steps, context pin spec, or few-shot example)"
                    }
                },
                "required": ["category", "name", "pattern"]
            }
        ),

        Tool(
            name="list_all_patterns",
            description="List all stored prompt engineering patterns organized by category. Shows category names and pattern names (not full content).",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),

        # === PIPELINE STATUS ===
        Tool(
            name="pipeline_status",
            description="Show the status of the Compass Intelligence Pipeline: what's been extracted, what's in the Knowledge Graph, what's been visualized, and what chapters still need processing.",
            inputSchema={
                "type": "object",
                "properties": {
                    "chapters_dir": {
                        "type": "string",
                        "description": "Path to the chapters directory to check (default: Active_Draft_2/)"
                    }
                }
            }
        ),

        Tool(
            name="get_pipeline_help",
            description="Get step-by-step instructions for using the full Compass Intelligence Pipeline: from chapter analysis to Knowledge Graph population to Mermaid visualization.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""

    # ─── KG TO MERMAID ───
    if name == "kg_to_mermaid":
        entities = arguments.get("entities", [])
        relations = arguments.get("relations", [])
        filter_type = arguments.get("filter_type")
        style = arguments.get("style", "full")

        mermaid_syntax = entities_to_mermaid(entities, relations,
                                             filter_type=filter_type,
                                             style=style)

        stats = {}
        for e in entities:
            etype = e.get("entityType", "other")
            if filter_type and etype != filter_type:
                continue
            stats[etype] = stats.get(etype, 0) + 1

        return [TextContent(
            type="text",
            text=json.dumps({
                "mermaid_syntax": mermaid_syntax,
                "stats": {
                    "entities_by_type": stats,
                    "total_entities": sum(stats.values()),
                    "total_relations": len(relations),
                    "filter_applied": filter_type
                },
                "next_step": "Send the mermaid_syntax to the Mermaid MCP's generate_mermaid_diagram tool with theme='dark' and outputType='file'"
            }, indent=2)
        )]

    # ─── GENERATE EXTRACTION PROMPT ───
    elif name == "generate_extraction_prompt":
        chapter_text = arguments.get("chapter_text", "")
        extraction_types = arguments.get("extraction_types")

        prompt = generate_extraction_prompt(chapter_text, extraction_types)

        return [TextContent(
            type="text",
            text=json.dumps({
                "extraction_prompt": prompt,
                "extraction_types": extraction_types or ["characters", "locations", "events", "themes", "plot_threads", "craft"],
                "instructions": "Send this prompt along with the full chapter text to Claude for structured extraction. The response should be JSON with 'entities' and 'relations' arrays.",
                "next_step": "After extraction, use text_to_kg_entities to validate, then write to Knowledge Graph Memory using create_entities and create_relations."
            }, indent=2)
        )]

    # ─── TEXT TO KG ENTITIES ───
    elif name == "text_to_kg_entities":
        extraction_json = arguments.get("extraction_json", "")

        try:
            data = json.loads(extraction_json)
        except json.JSONDecodeError as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Invalid JSON: {str(e)}",
                    "hint": "The extraction_json should be a valid JSON string with 'entities' and 'relations' arrays."
                }, indent=2)
            )]

        entities = data.get("entities", [])
        relations = data.get("relations", [])

        # Validate entities
        valid_entities = []
        issues = []
        for i, e in enumerate(entities):
            if not e.get("name"):
                issues.append(f"Entity {i}: missing 'name'")
                continue
            if not e.get("entityType"):
                issues.append(f"Entity {i} ({e['name']}): missing 'entityType'")
                continue
            if not e.get("observations") or not isinstance(e["observations"], list):
                issues.append(f"Entity {i} ({e['name']}): missing or invalid 'observations' (must be array of strings)")
                continue
            # Ensure observations are strings
            e["observations"] = [str(o) for o in e["observations"]]
            valid_entities.append(e)

        # Validate relations
        valid_relations = []
        entity_names = {e["name"] for e in valid_entities}
        for i, r in enumerate(relations):
            if not r.get("from") or not r.get("to") or not r.get("relationType"):
                issues.append(f"Relation {i}: missing required field (from, to, relationType)")
                continue
            if r["from"] not in entity_names:
                issues.append(f"Relation {i}: 'from' entity '{r['from']}' not in extracted entities")
            if r["to"] not in entity_names:
                issues.append(f"Relation {i}: 'to' entity '{r['to']}' not in extracted entities")
            valid_relations.append(r)

        return [TextContent(
            type="text",
            text=json.dumps({
                "valid_entities": valid_entities,
                "valid_relations": valid_relations,
                "validation_issues": issues,
                "summary": {
                    "entities_valid": len(valid_entities),
                    "entities_invalid": len(entities) - len(valid_entities),
                    "relations_valid": len(valid_relations),
                    "relations_invalid": len(relations) - len(valid_relations)
                },
                "next_step": "Use Knowledge Graph Memory's create_entities with valid_entities and create_relations with valid_relations."
            }, indent=2)
        )]

    # ─── GET PROMPT PATTERN ───
    elif name == "get_prompt_pattern":
        patterns = load_patterns()
        category = arguments.get("category", "")
        pattern_name = arguments.get("name", "list")

        if category not in patterns:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Category '{category}' not found",
                    "available_categories": list(patterns.keys())
                }, indent=2)
            )]

        if pattern_name == "list" or not pattern_name:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "category": category,
                    "available_patterns": list(patterns[category].keys()),
                    "count": len(patterns[category])
                }, indent=2)
            )]

        if pattern_name not in patterns[category]:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Pattern '{pattern_name}' not found in '{category}'",
                    "available_patterns": list(patterns[category].keys())
                }, indent=2)
            )]

        return [TextContent(
            type="text",
            text=json.dumps({
                "category": category,
                "name": pattern_name,
                "pattern": patterns[category][pattern_name]
            }, indent=2)
        )]

    # ─── SAVE PROMPT PATTERN ───
    elif name == "save_prompt_pattern":
        patterns = load_patterns()
        category = arguments.get("category", "")
        pattern_name = arguments.get("name", "")
        pattern_content = arguments.get("pattern", "")

        if category not in patterns:
            patterns[category] = {}

        is_update = pattern_name in patterns[category]
        patterns[category][pattern_name] = pattern_content
        save_patterns(patterns)

        return [TextContent(
            type="text",
            text=json.dumps({
                "action": "updated" if is_update else "created",
                "category": category,
                "name": pattern_name,
                "message": f"Pattern '{pattern_name}' {'updated' if is_update else 'saved'} in '{category}'"
            }, indent=2)
        )]

    # ─── LIST ALL PATTERNS ───
    elif name == "list_all_patterns":
        patterns = load_patterns()

        summary = {}
        total = 0
        for category, items in patterns.items():
            summary[category] = {
                "patterns": list(items.keys()),
                "count": len(items)
            }
            total += len(items)

        return [TextContent(
            type="text",
            text=json.dumps({
                "prompt_engineering_library": summary,
                "total_patterns": total,
                "categories": list(patterns.keys())
            }, indent=2)
        )]

    # ─── PIPELINE STATUS ───
    elif name == "pipeline_status":
        chapters_dir = arguments.get("chapters_dir", "Active_Draft_2/")
        workspace = Path(__file__).parent.parent.parent.parent

        # Check for chapter files
        chapters_path = workspace / chapters_dir
        chapter_files = []
        if chapters_path.exists():
            for f in sorted(chapters_path.iterdir()):
                if f.suffix in ['.txt', '.md'] and 'Chapter' in f.name:
                    chapter_files.append(f.name)

        # Check patterns
        patterns = load_patterns()
        pattern_count = sum(len(v) for v in patterns.values())

        return [TextContent(
            type="text",
            text=json.dumps({
                "pipeline_status": {
                    "chapters_found": len(chapter_files),
                    "chapter_files": chapter_files,
                    "chapters_dir": str(chapters_dir),
                    "prompt_patterns_stored": pattern_count,
                    "pattern_categories": list(patterns.keys())
                },
                "pipeline_steps": {
                    "1_read_chapter": "Read chapter file",
                    "2_generate_prompt": "Call generate_extraction_prompt with chapter text",
                    "3_extract": "Send extraction prompt to Claude for structured extraction",
                    "4_validate": "Call text_to_kg_entities to validate extraction",
                    "5_write_kg": "Write to Knowledge Graph Memory (create_entities + create_relations)",
                    "6_visualize": "Call kg_to_mermaid, then send to Mermaid MCP"
                },
                "commands_available": [
                    "/knowledge-graph-visualize - Generate Mermaid from KG",
                    "/chapter-to-kg <file> - Full extraction pipeline"
                ]
            }, indent=2)
        )]

    # ─── PIPELINE HELP ───
    elif name == "get_pipeline_help":
        return [TextContent(
            type="text",
            text=json.dumps({
                "compass_intelligence_pipeline": {
                    "overview": "Transform novel chapters into a visual knowledge graph in 6 steps.",
                    "steps": [
                        {
                            "step": 1,
                            "name": "Read Chapter",
                            "tool": "Read the chapter file",
                            "mcp": "Filesystem / direct file read"
                        },
                        {
                            "step": 2,
                            "name": "Generate Extraction Prompt",
                            "tool": "generate_extraction_prompt",
                            "mcp": "compass-intelligence (this MCP)",
                            "description": "Creates an XML-tagged, Chain-of-Thought extraction prompt"
                        },
                        {
                            "step": 3,
                            "name": "Extract Intelligence",
                            "tool": "Send prompt + chapter to Claude",
                            "mcp": "Claude AI (the assistant itself)",
                            "description": "Claude reads the chapter and returns structured JSON"
                        },
                        {
                            "step": 4,
                            "name": "Validate Extraction",
                            "tool": "text_to_kg_entities",
                            "mcp": "compass-intelligence (this MCP)",
                            "description": "Validates extracted entities/relations for KG format"
                        },
                        {
                            "step": 5,
                            "name": "Write to Knowledge Graph",
                            "tool": "create_entities + create_relations",
                            "mcp": "Knowledge Graph Memory MCP",
                            "description": "Persists extracted intelligence as graph nodes and edges"
                        },
                        {
                            "step": 6,
                            "name": "Visualize",
                            "tool": "kg_to_mermaid -> generate_mermaid_diagram",
                            "mcp": "compass-intelligence + Mermaid MCP",
                            "description": "Transforms KG to Mermaid syntax, renders as diagram"
                        }
                    ],
                    "cursor_commands": {
                        "/chapter-to-kg <file>": "Runs steps 1-6 automatically",
                        "/kg-viz": "Runs step 6 only (visualize current KG)",
                        "/kg-viz characters": "Visualize only characters and their relations"
                    },
                    "prompt_engineering_tools": {
                        "get_prompt_pattern": "Retrieve stored XML tags, CoT templates, few-shot examples",
                        "save_prompt_pattern": "Add new patterns to your library",
                        "list_all_patterns": "See everything in your prompt engineering library"
                    }
                }
            }, indent=2)
        )]

    return [TextContent(
        type="text",
        text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2)
    )]


async def main():
    """Run the Compass Intelligence MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
