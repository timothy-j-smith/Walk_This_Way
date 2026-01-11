#!/usr/bin/env python3
"""
COMPASS Writing System - Writing Guides MCP Server
Comprehensive fiction writing reference database with author advice, techniques, and principles
"""

import json
import os
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("compass-writing-guides")

# Data file path
DATA_DIR = Path(__file__).parent / "data"
GUIDES_FILE = DATA_DIR / "writing_guides.json"

def load_guides() -> dict:
    """Load writing guides database from JSON file"""
    if not GUIDES_FILE.exists():
        return {}
    with open(GUIDES_FILE, 'r') as f:
        return json.load(f)

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available writing guides tools"""
    return [
        Tool(
            name="get_author_advice",
            description="Get writing advice and principles from a specific author (e.g., 'Stephen King', 'Anne Lamott', 'Brandon Sanderson')",
            inputSchema={
                "type": "object",
                "properties": {
                    "author": {
                        "type": "string",
                        "description": "Author name (e.g., 'Stephen King', 'Anne Lamott')"
                    },
                    "topic": {
                        "type": "string",
                        "description": "Optional: Filter by specific topic (e.g., 'adverbs', 'dialogue', 'character')"
                    }
                },
                "required": ["author"]
            }
        ),
        Tool(
            name="get_topic_guidance",
            description="Get comprehensive guidance on a writing topic (e.g., 'dialogue', 'pacing', 'character_development', 'prose_style', 'atmosphere', 'point_of_view', 'show_dont_tell', 'revision')",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Writing topic name"
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="get_author_style",
            description="Get detailed author style guide (prose style, narrative technique, themes, signature moves, use cases). Available authors: Stephen King, Richard Russo, Dennis Lehane, Donna Tartt, J.D. Salinger, Annie Proulx, Cormac McCarthy, Colson Whitehead",
            inputSchema={
                "type": "object",
                "properties": {
                    "author": {
                        "type": "string",
                        "description": "Author name"
                    }
                },
                "required": ["author"]
            }
        ),
        Tool(
            name="get_quote",
            description="Get inspirational writing quotes. Can filter by author or search by keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "author": {
                        "type": "string",
                        "description": "Optional: Filter by author name"
                    },
                    "keyword": {
                        "type": "string",
                        "description": "Optional: Search for quotes containing keyword"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_technique",
            description="Get techniques for a specific aspect of writing (e.g., 'pacing_techniques', 'dialogue_techniques', 'character_techniques', 'prose_techniques', 'atmosphere_techniques')",
            inputSchema={
                "type": "object",
                "properties": {
                    "technique_type": {
                        "type": "string",
                        "description": "Type of technique (e.g., 'pacing_techniques', 'dialogue_techniques')"
                    }
                },
                "required": ["technique_type"]
            }
        ),
        Tool(
            name="get_genre_guidance",
            description="Get genre-specific writing guidance (e.g., 'literary_fiction', 'crime_mystery', 'horror_supernatural', 'coming_of_age')",
            inputSchema={
                "type": "object",
                "properties": {
                    "genre": {
                        "type": "string",
                        "description": "Genre name"
                    }
                },
                "required": ["genre"]
            }
        ),
        Tool(
            name="search_guides",
            description="Search across all writing guides (authors, topics, quotes, techniques) by keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search keyword or phrase"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_authors",
            description="List all available authors with writing advice",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="list_topics",
            description="List all available writing topics",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_writing_tip",
            description="Get a quick writing tip on a specific topic or from a specific author",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Optional: Topic (e.g., 'dialogue', 'pacing', 'character')"
                    },
                    "author": {
                        "type": "string",
                        "description": "Optional: Author name"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_methodology",
            description="Get writing methodology/philosophy guidance (e.g., 'scalpel_hose', 'compass_advanced_tools', 'json_prompts')",
            inputSchema={
                "type": "object",
                "properties": {
                    "methodology": {
                        "type": "string",
                        "description": "Methodology name (e.g., 'scalpel_hose', 'compass_advanced_tools', 'json_prompts')"
                    },
                    "section": {
                        "type": "string",
                        "description": "Optional: Specific section (e.g., 'process', 'character_depth_hierarchy', 'core_systems')"
                    }
                },
                "required": ["methodology"]
            }
        ),
        Tool(
            name="list_methodologies",
            description="List all available writing methodologies and philosophies",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""
    guides = load_guides()
    
    if not guides:
        return [TextContent(
            type="text",
            text=json.dumps({"error": "Writing guides database not found or empty"}, indent=2)
        )]
    
    if name == "get_author_advice":
        author_name = arguments.get("author", "")
        topic_filter = arguments.get("topic")
        
        authors = guides.get("authors", {})
        if author_name not in authors:
            available = list(authors.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Author '{author_name}' not found",
                    "available_authors": available
                }, indent=2)
            )]
        
        author_data = authors[author_name]
        result = {
            "author": author_name,
            "source": author_data.get("source", ""),
            "core_philosophy": author_data.get("core_philosophy", ""),
            "principles": []
        }
        
        principles = author_data.get("principles", [])
        if topic_filter:
            principles = [p for p in principles if topic_filter.lower() in p.get("topic", "").lower()]
            result["filtered_by_topic"] = topic_filter
        
        result["principles"] = principles
        
        return [TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )]
    
    elif name == "get_topic_guidance":
        topic_name = arguments.get("topic", "")
        
        topics = guides.get("topics", {})
        if topic_name not in topics:
            available = list(topics.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Topic '{topic_name}' not found",
                    "available_topics": available
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "topic": topic_name,
                **topics[topic_name]
            }, indent=2)
        )]
    
    elif name == "get_author_style":
        author_name = arguments.get("author", "")
        
        styles = guides.get("author_styles", {})
        if author_name not in styles:
            available = list(styles.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Author style '{author_name}' not found",
                    "available_authors": available
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "author": author_name,
                **styles[author_name]
            }, indent=2)
        )]
    
    elif name == "get_quote":
        author_filter = arguments.get("author", "")
        keyword = arguments.get("keyword", "")
        
        quotes = guides.get("quotes", {})
        results = []
        
        # Search in specific author quotes
        if author_filter:
            author_quotes = quotes.get(author_filter.lower().replace(" ", "_"), [])
            if keyword:
                author_quotes = [q for q in author_quotes if keyword.lower() in q.get("quote", "").lower() or keyword.lower() in q.get("context", "").lower()]
            results.extend([{**q, "author": author_filter} for q in author_quotes])
        # Search in general quotes
        else:
            general_quotes = quotes.get("general_writing", [])
            if keyword:
                general_quotes = [q for q in general_quotes if keyword.lower() in q.get("quote", "").lower() or keyword.lower() in q.get("context", "").lower()]
            results.extend(general_quotes)
            
            # Also search all author quotes if no author filter
            if not author_filter and not keyword:
                for author_key, author_quotes in quotes.items():
                    if author_key != "general_writing":
                        author_name = author_key.replace("_", " ").title()
                        results.extend([{**q, "author": author_name} for q in author_quotes])
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "quotes": results,
                "count": len(results)
            }, indent=2)
        )]
    
    elif name == "get_technique":
        technique_type = arguments.get("technique_type", "")
        
        techniques = guides.get("techniques", {})
        if technique_type not in techniques:
            available = list(techniques.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Technique type '{technique_type}' not found",
                    "available_techniques": available
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "technique_type": technique_type,
                "techniques": techniques[technique_type]
            }, indent=2)
        )]
    
    elif name == "get_genre_guidance":
        genre_name = arguments.get("genre", "")
        
        genres = guides.get("genre_guidance", {})
        if genre_name not in genres:
            available = list(genres.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Genre '{genre_name}' not found",
                    "available_genres": available
                }, indent=2)
            )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "genre": genre_name,
                **genres[genre_name]
            }, indent=2)
        )]
    
    elif name == "search_guides":
        query = arguments.get("query", "").lower()
        
        results = {
            "query": query,
            "matches": {
                "authors": [],
                "topics": [],
                "quotes": [],
                "techniques": []
            }
        }
        
        # Search authors
        for author_name, author_data in guides.get("authors", {}).items():
            author_str = json.dumps(author_data).lower()
            if query in author_str:
                results["matches"]["authors"].append(author_name)
        
        # Search topics
        for topic_name, topic_data in guides.get("topics", {}).items():
            topic_str = json.dumps(topic_data).lower()
            if query in topic_str:
                results["matches"]["topics"].append(topic_name)
        
        # Search quotes
        for author_key, quote_list in guides.get("quotes", {}).items():
            for quote_data in quote_list:
                quote_str = json.dumps(quote_data).lower()
                if query in quote_str:
                    results["matches"]["quotes"].append({
                        "quote": quote_data.get("quote", "")[:100] + "...",
                        "author": quote_data.get("author", author_key.replace("_", " ").title())
                    })
        
        # Search techniques
        for tech_type, tech_list in guides.get("techniques", {}).items():
            tech_str = " ".join(tech_list).lower()
            if query in tech_str:
                results["matches"]["techniques"].append(tech_type)
        
        total_matches = sum(len(v) for v in results["matches"].values())
        results["total_matches"] = total_matches
        
        return [TextContent(
            type="text",
            text=json.dumps(results, indent=2)
        )]
    
    elif name == "list_authors":
        authors = guides.get("authors", {})
        author_styles = guides.get("author_styles", {})
        
        all_authors = list(set(list(authors.keys()) + list(author_styles.keys())))
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "authors": sorted(all_authors),
                "count": len(all_authors),
                "with_advice": list(authors.keys()),
                "with_styles": list(author_styles.keys())
            }, indent=2)
        )]
    
    elif name == "list_topics":
        topics = guides.get("topics", {})
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "topics": list(topics.keys()),
                "count": len(topics),
                "descriptions": {k: v.get("description", "") for k, v in topics.items()}
            }, indent=2)
        )]
    
    elif name == "get_writing_tip":
        topic = arguments.get("topic", "")
        author = arguments.get("author", "")
        
        # If author specified, get a principle from that author
        if author:
            authors = guides.get("authors", {})
            if author in authors:
                principles = authors[author].get("principles", [])
                if topic:
                    principles = [p for p in principles if topic.lower() in p.get("topic", "").lower()]
                if principles:
                    selected = principles[0]
                    return [TextContent(
                        type="text",
                        text=json.dumps({
                            "tip": selected.get("quote", ""),
                            "explanation": selected.get("explanation", ""),
                            "author": author,
                            "topic": selected.get("topic", "")
                        }, indent=2)
                    )]
        
        # If topic specified, get guidance from that topic
        if topic:
            topics = guides.get("topics", {})
            if topic in topics:
                topic_data = topics[topic]
                principles = topic_data.get("principles", [])
                if principles:
                    return [TextContent(
                        type="text",
                        text=json.dumps({
                            "tip": principles[0] if isinstance(principles[0], str) else principles[0].get("principle", ""),
                            "topic": topic,
                            "description": topic_data.get("description", "")
                        }, indent=2)
                    )]
        
        # Default: return a general tip
        return [TextContent(
            type="text",
            text=json.dumps({
                "tip": "Read a lot and write a lot. - Stephen King",
                "explanation": "The only way to become a better writer is through consistent practice. Read widely across genres to understand what works, and write regularly to develop your craft.",
                "author": "Stephen King"
            }, indent=2)
        )]
    
    elif name == "get_methodology":
        methodology_name = arguments.get("methodology", "")
        section = arguments.get("section", "")
        
        methodologies = guides.get("methodologies", {})
        if methodology_name not in methodologies:
            available = list(methodologies.keys())
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Methodology '{methodology_name}' not found",
                    "available_methodologies": available
                }, indent=2)
            )]
        
        methodology_data = methodologies[methodology_name]
        
        if section:
            if section in methodology_data:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "methodology": methodology_name,
                        "section": section,
                        "content": methodology_data[section]
                    }, indent=2)
                )]
            else:
                available_sections = list(methodology_data.keys())
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Section '{section}' not found in {methodology_name}",
                        "available_sections": available_sections
                    }, indent=2)
                )]
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "methodology": methodology_name,
                **methodology_data
            }, indent=2)
        )]
    
    elif name == "list_methodologies":
        methodologies = guides.get("methodologies", {})
        
        methodology_list = []
        for key, value in methodologies.items():
            methodology_list.append({
                "name": key,
                "title": value.get("name", key),
                "description": value.get("description", ""),
                "source": value.get("source", "")
            })
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "methodologies": methodology_list,
                "count": len(methodology_list)
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
