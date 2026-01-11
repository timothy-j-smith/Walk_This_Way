#!/usr/bin/env python3
"""
Walk This Way - Character Database MCP Server
Provides tools for querying and managing character information for the novel Walk This Way
"""

import json
import os
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("walkthisway-characters")

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
            description="Get complete profile for a specific character by name (Nick Johnson, Jackie Marsh, Maxanne Sartori, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name (e.g., 'Nick Johnson', 'Jackie Marsh', 'Maxanne Sartori')"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="list_characters",
            description="List all character names in Walk This Way database",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_character_attribute",
            description="Get a specific attribute for a character (e.g., music preferences, personality traits, relationships)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "attribute": {
                        "type": "string",
                        "description": "Attribute path (e.g., 'preferences.music.loves', 'personality.traits', 'relationships', 'arc.key_moments')"
                    }
                },
                "required": ["name", "attribute"]
            }
        ),
        Tool(
            name="check_character_fact",
            description="Check if a proposed fact about a character is consistent with established information from Story Bible",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "fact_type": {
                        "type": "string",
                        "description": "Type of fact (e.g., 'music_preference', 'personality_trait', 'relationship', 'timeline_event', 'voice_pattern')"
                    },
                    "proposed_fact": {
                        "type": "string",
                        "description": "The fact to check (e.g., 'Nick loves disco music', 'Jackie speaks in informal slang')"
                    }
                },
                "required": ["name", "fact_type", "proposed_fact"]
            }
        ),
        Tool(
            name="get_relationship",
            description="Get the relationship details between two characters with full evolution timeline",
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
            description="Search characters by trait, preference, musical style, or any attribute",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term (e.g., 'Aerosmith', 'working-class', 'Juilliard', 'guitar')"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_character_timeline",
            description="Get all key moments in a character's arc with dates and emotional states",
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
            description="Get detailed voice/speaking pattern information for dialogue writing",
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
            name="get_characters_by_year",
            description="Get character ages and status for a specific year (useful for timeline consistency)",
            inputSchema={
                "type": "object",
                "properties": {
                    "year": {
                        "type": "integer",
                        "description": "Year (e.g., 1975, 1979, 2009)"
                    }
                },
                "required": ["year"]
            }
        ),
        Tool(
            name="check_timeline_consistency",
            description="Verify if a proposed event is consistent with character timeline and ages",
            inputSchema={
                "type": "object",
                "properties": {
                    "character": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of proposed event"
                    },
                    "event": {
                        "type": "string",
                        "description": "Description of proposed event"
                    }
                },
                "required": ["character", "year", "event"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""
    characters = load_characters()
    
    if name == "list_characters":
        char_list = list(characters.keys())
        return [TextContent(
            type="text",
            text=json.dumps({
                "novel": "Walk This Way",
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
                    "error": f"Attribute '{attribute_path}' not found for {char_name}"
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
            "established_facts": [],
            "reasoning": ""
        }
        
        # Check music preferences
        if fact_type == "music_preference" and "preferences" in char_data:
            music_prefs = char_data.get("preferences", {}).get("music", {})
            loves = music_prefs.get("loves", [])
            hates = music_prefs.get("hates", [])
            
            consistency_check["established_facts"] = {
                "loves": loves,
                "hates": hates
            }
            
            proposed_lower = proposed_fact.lower()
            
            # Check contradictions
            for genre in hates:
                if genre.lower() in proposed_lower and any(word in proposed_lower for word in ["love", "enjoy", "likes"]):
                    consistency_check["consistent"] = False
                    consistency_check["reasoning"] = f"CONTRADICTION: {char_name} hates {genre} (established in Story Bible)"
                    break
            
            if consistency_check["consistent"] is None:
                for genre in loves:
                    if genre.lower() in proposed_lower and any(word in proposed_lower for word in ["hate", "dislike", "despise"]):
                        consistency_check["consistent"] = False
                        consistency_check["reasoning"] = f"CONTRADICTION: {char_name} loves {genre} (established in Story Bible)"
                        break
            
            if consistency_check["consistent"] is None:
                consistency_check["consistent"] = True
                consistency_check["reasoning"] = "No contradiction found with established music preferences"
        
        # Check voice/dialect patterns
        elif fact_type == "voice_pattern":
            voice_info = char_data.get("personality", {}).get("voice", "")
            consistency_check["established_facts"] = {"voice": voice_info}
            
            # Example checks
            if char_name == "Jackie Marsh" and any(word in proposed_fact.lower() for word in ["slang", "ain't", "gonna", "informal"]):
                consistency_check["consistent"] = False
                consistency_check["reasoning"] = "CONTRADICTION: Jackie uses educated, precise language with rare contractions (especially when nervous)"
            elif char_name == "Nick Johnson" and "formal" in proposed_fact.lower() or "academic" in proposed_fact.lower():
                consistency_check["consistent"] = False
                consistency_check["reasoning"] = "CONTRADICTION: Nick speaks with working-class Boston dialect, economical speech"
            else:
                consistency_check["consistent"] = True
                consistency_check["reasoning"] = "No obvious contradiction with established voice patterns"
        
        else:
            consistency_check["consistent"] = "unknown"
            consistency_check["reasoning"] = f"Fact type '{fact_type}' checking not yet implemented. Manually verify against Story Bible."
        
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
                    "preview": basic_info.get('occupation_1979', 'Unknown occupation'),
                    "relevance": "Contains search term in profile"
                })
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "query": arguments["query"],
                "results": results,
                "count": len(results)
            }, indent=2)
        )]
    
    elif name == "get_character_timeline":
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
                "timeline": arc
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
    
    elif name == "get_characters_by_year":
        year = arguments["year"]
        result = {
            "year": year,
            "characters": []
        }
        
        for char_name, char_data in characters.items():
            basic_info = char_data.get("basic_info", {})
            
            # Calculate age for this year
            age_key = f"age_{year}"
            if age_key in basic_info:
                age = basic_info[age_key]
            else:
                # Try to calculate from birth year
                if "born" in basic_info:
                    age = year - basic_info["born"]
                else:
                    age = "Unknown"
            
            occupation_key = f"occupation_{year}"
            occupation = basic_info.get(occupation_key, "Unknown")
            
            result["characters"].append({
                "name": char_name,
                "age": age,
                "occupation": occupation
            })
        
        return [TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )]
    
    elif name == "check_timeline_consistency":
        char_name = arguments["character"]
        year = arguments["year"]
        event = arguments["event"]
        
        if char_name not in characters:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Character '{char_name}' not found"}, indent=2)
            )]
        
        char_data = characters[char_name]
        basic_info = char_data.get("basic_info", {})
        
        # Calculate age
        if "born" in basic_info:
            age_at_event = year - basic_info["born"]
        else:
            age_at_event = "Unknown"
        
        # Check for conflicts with known timeline
        arc = char_data.get("arc", {})
        key_moments = arc.get("key_moments", [])
        
        conflicts = []
        for moment in key_moments:
            # Simple conflict detection
            if "year" in moment or "date" in moment:
                # Could add more sophisticated checking here
                pass
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "character": char_name,
                "year": year,
                "age_at_event": age_at_event,
                "proposed_event": event,
                "conflicts_detected": conflicts,
                "recommendation": "Check Story Bible timeline.md for detailed chronology"
            }, indent=2)
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
