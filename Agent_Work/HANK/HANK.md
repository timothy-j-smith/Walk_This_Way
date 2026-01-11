# Fiction Writing with MCP Servers: Complete Implementation Guide

**Vision:** MCP for Fiction Writing

**Why Unique:** Most fiction writers use software or memory, but this approach treats fiction writing as a data problem, enabling structured manipulation of characters, events, and world rules.

---

## System Architecture

```text
┌─────────────────────────────────────────────┐
│           CURSOR IDE (Writing Environment)   │
│                                              │
│  ┌──────────────────────────────────────┐  │
│  │   Your Prose (Markdown Chapters)      │  │
│  └──────────────────────────────────────┘  │
│                    ↕                         │
│              AI Assistant (Claude)           │
│                    ↕                         │
│  ┌─────────────────────────────────────────┐│
│  │        MCP Protocol Layer               ││
│  └─────────────────────────────────────────┘│
└───────────────────┬─────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
  ┌─────▼──────┐         ┌─────▼──────┐
  │ Character  │         │ Timeline   │
  │ MCP Server │         │ MCP Server │
  └─────┬──────┘         └─────┬──────┘
        │                       │
  ┌─────▼──────┐         ┌─────▼──────┐
  │characters  │         │ events     │
  │.json       │         │.json       │
  └────────────┘         └────────────┘
```

### Five Envisioned MCP Servers

#### 1. **Character Database Server** (Implemented Below)

- Character profiles, traits, preferences
- Relationship mapping
- Character arc tracking
- Consistency checking

#### 2. **Timeline & Continuity Server** (Future)

- Chronological event tracking
- Location tracking by time
- Character knowledge states
- Temporal validation

#### 3. **World Rules & Lore Server** (Future)

- Setting details
- Technology/magic systems
- Organizations and locations
- Rule enforcement

#### 4. **Plot Structure & Pacing Server** (Future)

- Plot thread tracking
- Structural analysis
- Pacing metrics
- Setup/payoff tracking

#### 5. **Dialogue & Voice Consistency Server** (Future)

- Speech pattern analysis
- Voice modeling per character
- Vocabulary consistency
- Dialogue authenticity checking

---

## Why MCP Over Markdown Files

### The Fundamental Difference

**Markdown + @ References:**

- AI *interprets* documentation
- Probabilistic understanding
- Limited by context window
- No guarantees

**MCP Servers:**

- AI *executes* deterministic queries
- Structured data returns
- Not context-limited
- Guaranteed accuracy for structured facts

### Concrete Example

**Question:** "Has Sarah ever been to Chicago?"

**Markdown Approach:**

```text
User: @characters.md @timeline.md Has Sarah been to Chicago?
AI: *Scans files, interprets content*
Response: "I don't see any mention of Chicago" (might miss it)
```

**MCP Approach:**

```text
User: Has Sarah been to Chicago?
AI: *Calls character-database MCP*
Tool: query_character_locations("Sarah")
Response: {
  "locations": [
    {"city": "Chicago", "chapter": 17, "page": 203, "context": "Conference"}
  ]
}
AI: "Yes, Sarah visited Chicago in Chapter 17, page 203 for a conference"
```

### Key Advantages

1. **Precision**: Exact answers from database, not probabilistic interpretation
1. **Scale**: Works across 10 books, not limited by context window
1. **Validation**: Can enforce consistency rules programmatically
1. **Computation**: Can perform calculations (timelines, distances, relationships)
1. **Persistence**: Data structure persists independently of AI conversations
1. **Evolution**: Can add sophistication (ML models, pattern recognition) later

---

## Implementation: Character Database MCP Server

### Complete File Structure

```text
character-mcp-server/
├── server.py              # Main MCP server implementation
├── data/
│   └── characters.json    # Character database
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

### File 1: `requirements.txt`

```txt
mcp
```

### File 2: `data/characters.json`

```json
{
  "Sarah Chen": {
    "basic_info": {
      "age": 28,
      "occupation": "Cryptography PhD student",
      "physical": {
        "height": "5'7\"",
        "eyes": "green",
        "hair": "black, shoulder-length",
        "distinctive": "Taps fingers when thinking"
      }
    },
    "personality": {
      "traits": [
        "analytical",
        "stubborn", 
        "protective of friends",
        "distrustful of authority"
      ],
      "voice": "Direct, uses short sentences when emotional, technical metaphors",
      "quirks": [
        "Taps fingers when thinking",
        "Quotes movies when nervous"
      ]
    },
    "preferences": {
      "music": {
        "loves": ["rock", "punk", "classical"],
        "hates": ["disco", "country"]
      },
      "food": {
        "loves": ["Thai food", "black coffee"],
        "hates": ["sweet drinks"]
      }
    },
    "background": {
      "education": "MIT undergrad, Stanford PhD program",
      "family": "Estranged from mother, close to younger brother",
      "history": "Discovered encryption vulnerability that exposed corporate fraud"
    },
    "relationships": {
      "Dr. Martinez": {
        "type": "mentor",
        "status": "complicated - discovers his betrayal",
        "evolution": "Trusting → Suspicious → Confrontational"
      },
      "Alex": {
        "type": "best friend",
        "status": "loyal",
        "evolution": "Steady support throughout"
      }
    },
    "arc": {
      "starting_state": "Naive, trusts authority figures",
      "key_moments": [
        {
          "chapter": 3,
          "event": "Discovers encrypted files",
          "change": "First seeds of doubt"
        },
        {
          "chapter": 7,
          "event": "Confronts Martinez",
          "change": "Realizes she's on her own"
        }
      ],
      "ending_state": "Independent, trusts her own judgment"
    },
    "first_appearance": {
      "chapter": 1,
      "page": 3
    },
    "last_updated": "2026-01-08"
  },
  "Dr. Martinez": {
    "basic_info": {
      "age": 55,
      "occupation": "Professor, former NSA analyst",
      "physical": {
        "height": "6'1\"",
        "eyes": "brown",
        "hair": "gray, well-groomed",
        "distinctive": "Always wears bow ties"
      }
    },
    "personality": {
      "traits": [
        "charismatic",
        "manipulative",
        "patient",
        "calculating"
      ],
      "voice": "Professorial, uses academic language to deflect, never raises voice",
      "quirks": [
        "Adjusts bow tie when lying",
        "Uses Latin phrases"
      ]
    },
    "preferences": {
      "music": {
        "loves": ["opera", "jazz"],
        "hates": ["modern pop"]
      }
    },
    "background": {
      "education": "Harvard PhD",
      "family": "Divorced, estranged daughter",
      "history": "Left NSA under mysterious circumstances"
    },
    "relationships": {
      "Sarah Chen": {
        "type": "mentee",
        "status": "antagonist",
        "evolution": "Mentoring → Manipulating → Confrontational"
      }
    },
    "arc": {
      "starting_state": "Respected mentor figure",
      "key_moments": [
        {
          "chapter": 7,
          "event": "Confrontation with Sarah",
          "change": "Mask slips, reveals true nature"
        }
      ],
      "ending_state": "Exposed antagonist"
    },
    "first_appearance": {
      "chapter": 2,
      "page": 18
    }
  }
}
```

### File 3: `server.py`

```python
#!/usr/bin/env python3
"""
Character Database MCP Server
Provides tools for querying and managing fiction characters
"""

import json
import os
from pathlib import Path
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("character-database")

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
                        "description": "Character name (case-sensitive)"
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
            description="Get a specific attribute for a character (e.g., personality, preferences, relationships)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Character name"
                    },
                    "attribute": {
                        "type": "string",
                        "description": "Attribute path (e.g., 'preferences.music', 'personality.traits', 'relationships')"
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
                        "description": "Type of fact (e.g., 'music_preference', 'personality_trait', 'relationship')"
                    },
                    "proposed_fact": {
                        "type": "string",
                        "description": "The fact to check (e.g., 'loves disco music', 'is shy and withdrawn')"
                    }
                },
                "required": ["name", "fact_type", "proposed_fact"]
            }
        ),
        Tool(
            name="get_relationship",
            description="Get the relationship details between two characters",
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
            description="Search characters by trait, preference, or attribute",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term (e.g., 'stubborn', 'loves rock music', 'MIT')"
                    }
                },
                "required": ["query"]
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
        
        # Navigate nested attribute path (e.g., "preferences.music")
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
        
        # Check consistency based on fact type
        consistency_check = {
            "character": char_name,
            "fact_type": fact_type,
            "proposed_fact": proposed_fact,
            "consistent": None,
            "established_facts": [],
            "reasoning": ""
        }
        
        # Example checks for music preferences
        if fact_type == "music_preference" and "preferences" in char_data:
            music_prefs = char_data.get("preferences", {}).get("music", {})
            loves = music_prefs.get("loves", [])
            hates = music_prefs.get("hates", [])
            
            consistency_check["established_facts"] = {
                "loves": loves,
                "hates": hates
            }
            
            # Simple keyword matching (could be more sophisticated)
            proposed_lower = proposed_fact.lower()
            
            # Check against hates
            for genre in hates:
                if genre.lower() in proposed_lower and ("love" in proposed_lower or "enjoy" in proposed_lower):
                    consistency_check["consistent"] = False
                    consistency_check["reasoning"] = f"Contradicts established fact: {char_name} hates {genre}"
                    break
            
            # Check against loves
            if consistency_check["consistent"] is None:
                for genre in loves:
                    if genre.lower() in proposed_lower and ("hate" in proposed_lower or "dislike" in proposed_lower):
                        consistency_check["consistent"] = False
                        consistency_check["reasoning"] = f"Contradicts established fact: {char_name} loves {genre}"
                        break
            
            if consistency_check["consistent"] is None:
                consistency_check["consistent"] = True
                consistency_check["reasoning"] = "No contradiction found with established preferences"
        
        else:
            consistency_check["consistent"] = "unknown"
            consistency_check["reasoning"] = f"Fact type '{fact_type}' checking not yet implemented"
        
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
            # Convert character data to searchable string
            char_str = json.dumps(char_data).lower()
            if query in char_str:
                results.append({
                    "name": char_name,
                    "preview": f"{char_data.get('basic_info', {}).get('occupation', 'Unknown occupation')}"
                })
        
        return [TextContent(
            type="text",
            text=json.dumps({
                "query": arguments["query"],
                "results": results,
                "count": len(results)
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
```

### File 4: `README.md`

```markdown
# Character Database MCP Server

MCP server for managing fiction character databases.

## Features
- Store character profiles (personality, preferences, relationships, arc)
- Query character details
- Check fact consistency
- Search characters by attributes

## Tools Available
1. `list_characters` - Get all character names
2. `get_character` - Full character profile
3. `get_character_attribute` - Specific attribute (e.g., music preferences)
4. `check_character_fact` - Verify consistency
5. `get_relationship` - Relationship between two characters
6. `search_characters` - Find characters by trait

## Data Format
See `data/characters.json` for structure.
```

---

## Setup Instructions

### Step 1: Create Directory Structure

```bash
mkdir -p ~/character-mcp-server/data
cd ~/character-mcp-server
```

### Step 2: Create All Files

Create the following files with the content provided above:

- `server.py`
- `data/characters.json`
- `requirements.txt`
- `README.md`

### Step 3: Make Server Executable

```bash
chmod +x server.py
```

### Step 4: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Install MCP
pip install mcp
```

### Step 5: Test Server (Optional)

```bash
python server.py
# Should start without errors (will wait for input)
# Press Ctrl+C to stop
```

### Step 6: Configure Cursor

#### Option A: Cursor Settings UI

1. Open Cursor
1. Go to Settings (Cmd+, or Ctrl+,)
1. Search for "MCP"
1. Click "Edit Config" or "Add MCP Server"
1. Add server configuration

#### Option B: Manual Config File

**Mac/Linux:** `~/.cursor/mcp_settings.json`
**Windows:** `%APPDATA%\Cursor\mcp_settings.json`

```json
{
  "mcpServers": {
    "character-database": {
      "command": "python",
      "args": [
        "/Users/YOUR_USERNAME/character-mcp-server/server.py"
      ],
      "env": {}
    }
  }
}
```

**If using virtual environment:**

```json
{
  "mcpServers": {
    "character-database": {
      "command": "/Users/YOUR_USERNAME/character-mcp-server/venv/bin/python",
      "args": [
        "/Users/YOUR_USERNAME/character-mcp-server/server.py"
      ]
    }
  }
}
```

**Important:** Replace `/Users/YOUR_USERNAME/` with your actual path!

### Step 7: Restart Cursor

- Completely quit Cursor
- Reopen Cursor
- MCP server will initialize on startup

### Step 8: Verify Installation

In Cursor, try this prompt:

```text
Use the character-database MCP to list all available characters.
```

Expected result: `["Sarah Chen", "Dr. Martinez"]`

### Step 9: Test All Tools

#### A. List characters

```text
Call list_characters from character-database MCP
```

#### B. Get character profile

```text
Get Sarah Chen's complete profile using character-database MCP
```

#### C. Get specific attribute

```text
What music does Sarah Chen love? Use character-database MCP
```

#### D. Check consistency

```text
Check if this is consistent: "Sarah Chen loves disco music"
Use check_character_fact from character-database MCP
```

#### E. Get relationship

```text
What's the relationship between Sarah Chen and Dr. Martinez?
Use character-database MCP
```

#### F. Search characters

```text
Find characters who went to MIT using character-database MCP
```

---

## Usage Workflow

### During Chapter Writing

#### Scenario 1: Drafting with Character Context

```text
I'm writing Chapter 8 where Sarah is at a rock concert.
Use character-database MCP to get Sarah's music preferences,
then draft a scene showing her genuine enjoyment.
```

#### Scenario 2: Consistency Checking

```text
I just wrote: "Sarah smiled, remembering the disco nights 
with her mother."

Check if this contradicts established facts using 
character-database MCP.
```

#### Scenario 3: Relationship Development

```text
Get Sarah and Dr. Martinez's relationship details from 
character-database MCP. I need to write their confrontation 
maintaining consistency with their evolution.
```

### Updating Character Database

**As you write, update `data/characters.json`:**

- Add new characters
- Update character arcs after key moments
- Record new relationships
- Track preference discoveries

**Example workflow:**

1. Write Chapter 5
1. Discover Sarah has a new trait through writing
1. Add trait to `data/characters.json`
1. Future chapters can query this trait
1. Consistency maintained automatically

---

## Future MCP Servers

### Timeline MCP Server (Next Priority)

**Purpose:** Track events chronologically, validate temporal logic

**Tools to implement:**

- `add_event(date, event, characters_involved, location)`
- `get_timeline(start_date, end_date)`
- `get_character_location(character, date)`
- `validate_scene_timing(proposed_events)`
- `check_knowledge_state(character, fact, chapter)`

**Data structure:**

```json
{
  "events": [
    {
      "date": "2024-03-15",
      "time": "14:30",
      "event": "Sarah discovers encrypted files",
      "location": "University Lab",
      "characters": ["Sarah Chen"],
      "chapter": 3,
      "consequences": ["Sarah begins investigation"]
    }
  ]
}
```

### World Rules MCP Server

**Purpose:** Maintain consistency in fictional world mechanics

**Tools to implement:**

- `get_location_details(location_name)`
- `check_technology_rules(proposed_usage)`
- `get_organization_info(org_name)`
- `validate_world_logic(proposed_event)`

### Plot Structure MCP Server

**Purpose:** Track narrative structure and pacing

**Tools to implement:**

- `get_plot_threads(status)` (active/resolved/abandoned)
- `analyze_pacing(chapter_range)`
- `check_setup_payoff(element)`
- `suggest_next_beat(current_chapter)`

### Dialogue Voice MCP Server

**Purpose:** Maintain character voice consistency

**Tools to implement:**

- `analyze_dialogue(character, proposed_line)`
- `get_speech_patterns(character)`
- `check_vocabulary_fit(character, word)`

---

## Critical Assessment

### What's Genuinely Possible

**✅ Definitely Achievable:**

- Character database with structured queries
- Timeline validation
- World rules enforcement
- Basic consistency checking
- Cross-project data persistence

**⚠️ Challenging But Doable:**

- Semantic consistency checking (requires LLM calls)
- Voice pattern analysis (statistical methods)
- Relationship graph visualization
- Pattern recognition across chapters

**❓ Experimental:**

- "Learning" MCPs that improve over time
- Deep narrative structure analysis
- Predictive plot suggestions

### Advantages vs. Markdown

**MCP Wins:**

1. Structured queries (deterministic results)
1. Validation logic (programmatic enforcement)
1. Scale (not limited by context window)
1. Computation (can calculate, analyze, graph)

**Markdown Wins:**

1. Ease of setup (lower barrier)
1. Human readability (quick reference)
1. Flexibility (unstructured notes)
1. Lower maintenance

### Critical Success Factors

**For this to work well, you need:**

1. ✅ Engineering enjoyment (not a chore)
1. ✅ Technical capability (can build/debug)
1. ✅ Systematic thinking (architect mindset)
1. ✅ Long-term project (10 books = ROI)
1. ✅ Patience for setup (20-40 hour investment)

**Risks to manage:**

1. ⚠️ Over-engineering before writing
1. ⚠️ Rigid systems constraining creativity
1. ⚠️ MCP protocol changes requiring updates
1. ⚠️ Complexity exceeding benefit

### Recommended Approach

**Phase 1 (Weeks 1-2):** Build character MCP only

- Implement basic server
- Test with sample characters
- Write one chapter using it
- **Validate value before proceeding**

**Phase 2 (During Book 1):** Expand as needed

- Add timeline MCP if temporal issues emerge
- Build tools for actual pain points
- Don't solve hypothetical problems

**Phase 3 (Between Books):** Sophistication

- After Book 1, assess what mattered
- Build advanced features based on experience
- Refine architecture for Books 2-10

---

## Why Nobody's Doing This Yet

1. **MCP is very new** (late 2024 release)
1. **Fiction writers aren't typically engineers**
1. **Intersection is rare** (technical + serious fiction)
1. **Problem space is hard** (narrative consistency is complex)
1. **Unproven approach** (you're pioneering this)

**This is an opportunity, not a red flag.** You're exploring genuinely novel territory.

---

## Conclusion

This system is **genuinely possible and could work exceptionally well** for someone with your specific profile:

- Technical sophistication
- Systematic mindset
- Long-term writing ambitions (10 books)
- Enjoys engineering as much as writing
- Hobby context (time investment acceptable)

**Key insight:** MCP servers provide **computational precision** that markdown files cannot. As your fictional universe grows across 10 books, this architectural advantage compounds.

**Critical recommendation:** Start small, validate value incrementally, build sophistication based on real needs rather than hypothetical ones.

**The future vision:** A personal "story universe infrastructure" that scales across all your books, maintains perfect consistency, and grows more intelligent as you write.

---

## Getting Started Checklist

- [ ] Create `character-mcp-server` directory
- [ ] Copy all files (server.py, characters.json, etc.)
- [ ] Install Python + MCP package
- [ ] Configure Cursor with MCP server
- [ ] Test all 6 tools
- [ ] Customize characters.json with your characters
- [ ] Write Chapter 1 using the MCP
- [ ] Evaluate: Did this genuinely help?
- [ ] Decide: Expand system or simplify?

**Start building today. This is possible. This is exciting. This is novel.**

---

*Document created: 2026-01-08*
*Version: 1.0*
*Status: Ready for implementation*
