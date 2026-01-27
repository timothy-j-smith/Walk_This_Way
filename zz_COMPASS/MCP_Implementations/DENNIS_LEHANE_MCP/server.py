#!/usr/bin/env python3
"""
Dennis Lehane MCP Server - PRIVATE & CONFIDENTIAL
Style analysis tool specifically for "Walk This Way"
"""

import json
import os
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("dennis-lehane-style")

# Data file path
DATA_DIR = Path(__file__).parent / "data"
LEHANE_DATA_FILE = DATA_DIR / "lehane_analysis.json"

def load_lehane_data() -> dict:
    """Load Dennis Lehane analysis data from JSON file"""
    if not LEHANE_DATA_FILE.exists():
        return {}
    with open(LEHANE_DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Dennis Lehane style analysis tools"""
    return [
        Tool(
            name="get_lehane_style_guide",
            description="Get Dennis Lehane's style guide including Boston grit, visceral descriptions, sentence rhythm, dialogue patterns, and thematic elements. Use this to understand Lehane's authentic voice for 'Walk This Way'.",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Optional: Specific category (e.g., 'loss_of_innocence_theme', 'boston_grit', 'visceral_descriptions', 'dialogue_patterns', 'sentence_rhythm')"
                    }
                }
            }
        ),
        Tool(
            name="analyze_lehane_technique",
            description="Analyze a specific Lehane writing technique and how to apply it to 'Walk This Way'. Examples: 'loss of innocence', 'silence/unspoken themes', 'class distinctions', 'visceral descriptions'.",
            inputSchema={
                "type": "object",
                "properties": {
                    "technique": {
                        "type": "string",
                        "description": "The technique to analyze (e.g., 'loss of innocence', 'boston grit', 'visceral descriptions')"
                    },
                    "application": {
                        "type": "string",
                        "description": "Optional: How to apply to 'Walk This Way' (e.g., 'Nick's character', 'Jackie's dialogue', 'Maxanne's narration')"
                    }
                },
                "required": ["technique"]
            }
        ),
        Tool(
            name="get_lehane_examples",
            description="Get specific examples of Lehane's techniques from Mystic River and Gone Baby Gone, with analysis of how they work and how to apply similar techniques to 'Walk This Way'.",
            inputSchema={
                "type": "object",
                "properties": {
                    "technique_type": {
                        "type": "string",
                        "description": "Type of technique (e.g., 'dialogue', 'description', 'theme', 'structure')"
                    }
                }
            }
        ),
        Tool(
            name="compare_to_lehane_style",
            description="Compare a passage from 'Walk This Way' to Lehane's style, identifying what matches and what needs adjustment to achieve authentic Lehane voice.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to compare to Lehane's style"
                    },
                    "focus": {
                        "type": "string",
                        "description": "Optional: What to focus on (e.g., 'dialogue', 'description', 'rhythm', 'themes')"
                    }
                },
                "required": ["text"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    data = load_lehane_data()
    
    if not data:
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "Dennis Lehane analysis data not found",
                "path": str(LEHANE_DATA_FILE),
                "suggestion": "Verify data file exists at the specified path"
            }, indent=2)
        )]
    
    if name == "get_lehane_style_guide":
        category = arguments.get("category")
        if category:
            result = data.get(category, {})
            if result:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "category": category,
                        "data": result
                    }, indent=2)
                )]
            else:
                available = list(data.keys())
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Category '{category}' not found",
                        "available_categories": available
                    }, indent=2)
                )]
        else:
            # Return overview
            return [TextContent(
                type="text",
                text=json.dumps({
                    "metadata": data.get("metadata", {}),
                    "available_categories": list(data.keys()),
                    "summary": "Dennis Lehane style guide for 'Walk This Way' - PRIVATE & CONFIDENTIAL"
                }, indent=2)
            )]
    
    elif name == "analyze_lehane_technique":
        technique = arguments.get("technique", "").lower()
        application = arguments.get("application", "")
        
        # Search for technique in data
        results = []
        for category, content in data.items():
            if category == "metadata":
                continue
            if isinstance(content, dict):
                for key, value in content.items():
                    if technique in str(key).lower() or technique in str(value).lower():
                        results.append({
                            "category": category,
                            "section": key,
                            "content": value
                        })
        
        if results:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "technique": technique,
                    "application": application if application else "General application to 'Walk This Way'",
                    "findings": results[:5]  # Limit to top 5
                }, indent=2)
            )]
        else:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "technique": technique,
                    "message": "Technique not found in analysis data",
                    "suggestion": "Try: 'loss of innocence', 'boston grit', 'visceral descriptions', 'dialogue', 'themes'"
                }, indent=2)
            )]
    
    elif name == "get_lehane_examples":
        technique_type = arguments.get("technique_type", "").lower()
        
        examples = []
        for category, content in data.items():
            if category == "metadata":
                continue
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, dict) and "examples" in value:
                        for example in value.get("examples", []):
                            if technique_type in str(example).lower() or not technique_type:
                                examples.append({
                                    "category": category,
                                    "section": key,
                                    "example": example
                                })
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "technique_type": technique_type if technique_type else "all",
                "examples": examples[:10]  # Limit to top 10
            }, indent=2)
        )]
    
    elif name == "compare_to_lehane_style":
        text = arguments.get("text", "")
        focus = arguments.get("focus", "")
        
        # Load relevant style data
        style_guide = {}
        if focus:
            # Get specific category
            for category in data.keys():
                if focus.lower() in category.lower():
                    style_guide[category] = data[category]
        else:
            # Get key style elements
            for key in ["loss_of_innocence_theme", "boston_grit", "visceral_descriptions", "dialogue_patterns", "sentence_rhythm"]:
                if key in data:
                    style_guide[key] = data[key]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "text_analyzed": text[:200] + "..." if len(text) > 200 else text,
                "focus": focus if focus else "comprehensive",
                "lehane_style_reference": style_guide,
                "comparison": "Compare the provided text to Lehane's style elements above. Identify: 1) What matches Lehane's style, 2) What needs adjustment, 3) Specific recommendations for achieving authentic Lehane voice."
            }, indent=2)
        )]
    
    else:
        return [TextContent(
            type="text",
            text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2)
        )]

if __name__ == "__main__":
    import mcp.server.stdio
    mcp.server.stdio.stdio_server(app)
