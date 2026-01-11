#!/usr/bin/env python3
"""
COMPASS Writing System - Character Database MCP Server Template
Universal character database server for any fiction novel
"""

import json
import os
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("compass-characters")

# Data file path
DATA_DIR = Path(__file__).parent / "data"
CHARACTERS_FILE = DATA_DIR / "characters.json"

def load_characters() -> dict:
    """Load character database from JSON file"""
    if not CHARACTERS_FILE.exists():
        return {}
    with open(CHARACTERS_FILE, 'r') as f:
        return json.load(f)

def save_characters(characters: dict) -> None:
    """Save character database to JSON file"""
    DATA_DIR.mkdir(exist_ok=True)
    with open(CHARACTERS_FILE, 'w') as f:
        json.dump(characters, f, indent=2)

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available character database tools"""
    return [
        Tool(
            name="get_character",
            description="Get complete profile for a specific character by name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name (case-sensitive, full name preferred)"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="list_characters",
            description="List all character names in the database",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_character_attribute",
            description="Get a specific attribute for a character (supports nested paths like 'preferences.music.loves')",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "attribute": {
                        "type": "string",
                        "description": "Attribute path using dot notation (e.g., 'personality.traits', 'relationships.OTHER_CHARACTER', 'arc.key_moments')"
                    }
                },
                "required": ["name", "attribute"]
            }
        ),
        Tool(
            name="check_character_fact",
            description="Check if a proposed fact about a character is consistent with established information",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "fact_type": {
                        "type": "string",
                        "description": "Type of fact being checked (e.g., 'preference', 'personality_trait', 'relationship', 'timeline_event', 'voice_pattern', 'skill', 'goal')"
                    },
                    "proposed_fact": {
                        "type": "string",
                        "description": "The fact to check for consistency (e.g., 'loves classical music', 'speaks formally', 'is enemies with CHARACTER_X')"
                    }
                },
                "required": ["name", "fact_type", "proposed_fact"]
            }
        ),
        Tool(
            name="get_relationship",
            description="Get the relationship details between two characters including evolution over time",
            inputSchema={
                "type": "object",
                "properties": {
                    "character1": {
                        "type": "string",
                        "description": "First character name"
                    },
                    "character2": {
                        "type": "string",
                        "description": "Second character name"
                    }
                },
                "required": ["character1", "character2"]
            }
        ),
        Tool(
            name="search_characters",
            description="Search characters by trait, preference, occupation, or any attribute",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term (searches across all character data)"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_character_arc",
            description="Get complete character arc with all key moments and development",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="get_character_voice",
            description="Get voice and speaking patterns for authentic dialogue writing",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="get_all_relationships",
            description="Get all relationships for a specific character",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="compare_characters",
            description="Compare two characters across specified attributes (useful for contrast, conflict, or parallels)",
            inputSchema={
                "type": "object",
                "properties": {
                    "character1": {
                        "type": "string",
                        "description": "First character name"
                    },
                    "character2": {
                        "type": "string",
                        "description": "Second character name"
                    },
                    "attributes": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of attributes to compare (e.g., ['personality.traits', 'preferences.music', 'background.education']). If omitted, compares major attributes."
                    }
                },
                "required": ["character1", "character2"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""
    characters = load_characters()
    
    # Filter out template notes if present
    if "_TEMPLATE_NOTES" in characters:
        del characters["_TEMPLATE_NOTES"]
    
    if name == "list_characters":
        char_list = list(characters.keys())
        return [TextContent(
            type="text",
            text=json.dumps({
                "characters": char_list,
                "count": len(char_list)
            }, indent=2)
        )]
    
    elif name == "get_character":
        char_name = arguments["name"]
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Character '{char_name}' not found",
                    "available_characters": list(characters.keys())
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps(characters[char_name], indent=2)
        )]
    
    elif name == "get_character_attribute":
        char_name = arguments["name"]
        attribute_path = arguments["attribute"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        # Navigate nested attribute path
        char_data = characters[char_name]
        try:
            for key in attribute_path.split('.'):
                char_data = char_data[key]
            
            return [TextContent(
                type="text",
                text=json.dumps({
                    "character": char_name,
                    "attribute": attribute_path,
                    "value": char_data
                }, indent=2)
            )]
        except (KeyError, TypeError):
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Attribute '{attribute_path}' not found for {char_name}",
                    "suggestion": "Check available attributes in character profile"
                }, indent=2)
            )]
    
    elif name == "check_character_fact":
        char_name = arguments["name"]
        fact_type = arguments["fact_type"]
        proposed_fact = arguments["proposed_fact"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        char_data = characters[char_name]
        
        consistency_check = {
            "character": char_name,
            "fact_type": fact_type,
            "proposed_fact": proposed_fact,
            "consistent": None,
            "established_facts": {},
            "reasoning": ""
        }
        
        # Generic preference checking
        if "preference" in fact_type:
            preferences = char_data.get("preferences", {})
            consistency_check["established_facts"] = preferences
            
            proposed_lower = proposed_fact.lower()
            
            # Check across all preference categories
            for category, prefs in preferences.items():
                if isinstance(prefs, dict):
                    loves = prefs.get("loves", [])
                    hates = prefs.get("hates", [])
                    
                    # Check for contradictions
                    for item in hates:
                        if isinstance(item, str) and item.lower() in proposed_lower:
                            if any(word in proposed_lower for word in ["love", "enjoy", "like", "prefer"]):
                                consistency_check["consistent"] = False
                                consistency_check["reasoning"] = f"CONTRADICTION: Character hates {item} (category: {category})"
                                break
                    
                    if consistency_check["consistent"] is False:
                        break
                    
                    for item in loves:
                        if isinstance(item, str) and item.lower() in proposed_lower:
                            if any(word in proposed_lower for word in ["hate", "dislike", "despise"]):
                                consistency_check["consistent"] = False
                                consistency_check["reasoning"] = f"CONTRADICTION: Character loves {item} (category: {category})"
                                break
            
            if consistency_check["consistent"] is None:
                consistency_check["consistent"] = True
                consistency_check["reasoning"] = "No contradiction found with established preferences"
        
        # Voice pattern checking
        elif "voice" in fact_type or "speech" in fact_type:
            voice = char_data.get("personality", {}).get("voice", "")
            consistency_check["established_facts"] = {"voice": voice}
            consistency_check["consistent"] = "manual_review"
            consistency_check["reasoning"] = f"Voice pattern: {voice}. Manually verify proposed dialogue fits this pattern."
        
        else:
            consistency_check["consistent"] = "manual_review"
            consistency_check["reasoning"] = f"Fact type '{fact_type}' requires manual verification against character profile"
        
        return [TextContent(
            type="text",
            text=json.dumps(consistency_check, indent=2)
        )]
    
    elif name == "get_relationship":
        char1 = arguments["character1"]
        char2 = arguments["character2"]
        
        if char1 not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char1}' not found"}, indent=2)
            )]
        
        relationships = characters[char1].get("relationships", {})
        if char2 not in relationships:
            # Try reverse lookup
            if char2 in characters:
                reverse_relationships = characters[char2].get("relationships", {})
                if char1 in reverse_relationships:
                    return [TextContent(
                        type="text",
                        text=json.dumps({
                            "character1": char2,
                            "character2": char1,
                            "relationship": reverse_relationships[char1],
                            "note": f"Relationship found in {char2}'s profile"
                        }, indent=2)
                    )]
            
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"No relationship documented between {char1} and {char2}"
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "character1": char1,
                "character2": char2,
                "relationship": relationships[char2]
            }, indent=2)
        )]
    
    elif name == "search_characters":
        query = arguments["query"].lower()
        results = []
        
        for char_name, char_data in characters.items():
            char_str = json.dumps(char_data).lower()
            if query in char_str:
                basic_info = char_data.get('basic_info', {})
                results.append({
                    "name": char_name,
                    "occupation": basic_info.get('occupation', 'Unknown'),
                    "relevance": "Contains search term"
                })
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "query": arguments["query"],
                "results": results,
                "count": len(results)
            }, indent=2)
        )]
    
    elif name == "get_character_arc":
        char_name = arguments["name"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        arc = characters[char_name].get("arc", {})
        return [TextContent(
            type="text",
            text=json.dumps({
                "character": char_name,
                "arc": arc
            }, indent=2)
        )]
    
    elif name == "get_character_voice":
        char_name = arguments["name"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        personality = characters[char_name].get("personality", {})
        voice_info = {
            "character": char_name,
            "voice": personality.get("voice", "Not documented"),
            "traits": personality.get("traits", []),
            "quirks": personality.get("quirks", [])
        }
        
        return [TextContent(
            type="text",
            text=json.dumps(voice_info, indent=2)
        )]
    
    elif name == "get_all_relationships":
        char_name = arguments["name"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        relationships = characters[char_name].get("relationships", {})
        return [TextContent(
            type="text",
            text=json.dumps({
                "character": char_name,
                "relationships": relationships,
                "count": len(relationships)
            }, indent=2)
        )]
    
    elif name == "compare_characters":
        char1 = arguments["character1"]
        char2 = arguments["character2"]
        attributes = arguments.get("attributes", ["personality.traits", "preferences", "background.education"])
        
        if char1 not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char1}' not found"}, indent=2)
            )]
        if char2 not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char2}' not found"}, indent=2)
            )]
        
        comparison = {
            "character1": char1,
            "character2": char2,
            "comparisons": []
        }
        
        for attr_path in attributes:
            char1_data = characters[char1]
            char2_data = characters[char2]
            
            try:
                for key in attr_path.split('.'):
                    char1_data = char1_data[key]
                    char2_data = char2_data[key]
                
                comparison["comparisons"].append({
                    "attribute": attr_path,
                    char1: char1_data,
                    char2: char2_data
                })
            except (KeyError, TypeError):
                comparison["comparisons"].append({
                    "attribute": attr_path,
                    "error": f"Attribute not found in one or both characters"
                })
        
        return [TextContent(
            type="text",
            text=json.dumps(comparison, indent=2)
        )]
    
    return [TextContent(
        type="text",
        text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2)
    )]

async def main():
    """Run the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
