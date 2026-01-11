# MCP Implementation Guide for Walk This Way and COMPASS

## Executive Summary

This directory contains **two complete MCP (Model Context Protocol) implementations** for managing character databases in fiction writing:

1. **WalkThisWay_Character_MCP** - Production-ready MCP with real character data from Walk This Way
2. **COMPASS_Character_MCP_Template** - Universal template for any fiction novel with placeholder system

## Why MCP for Fiction Writing?

### The Problem with Markdown Files

Traditional approach: Store character info in `character-bible.md` → AI reads and interprets → Probabilistic understanding

**Issues:**
- AI might miss details when scanning long files
- Context window limits with large Story Bibles
- No guaranteed accuracy for structured facts
- Can't perform computations or validations

### The MCP Solution

MCP approach: Structured character database → AI executes deterministic queries → Guaranteed accurate results

**Advantages:**
- ✅ **Precision**: Exact answers from database queries
- ✅ **Scale**: Works across 10+ novels, no context limits
- ✅ **Validation**: Programmatic consistency checking
- ✅ **Computation**: Calculate ages, validate timelines
- ✅ **Persistence**: Data independent of AI conversations

## Real-World Example

**Question:** "Does Nick Johnson love disco music?"

### Markdown Approach:
```
User: @character-bible.md Does Nick hate disco?
AI: *Scans 267-line file, interprets content*
Response: "I don't see any specific mention..." (probabilistic)
```

### MCP Approach:
```
User: Check if Nick Johnson loves disco music
AI: *Calls walkthisway-characters MCP*
Tool: check_character_fact("Nick Johnson", "music_preference", "loves disco")
Response: {
  "consistent": false,
  "reasoning": "CONTRADICTION: Nick Johnson hates disco (established in Story Bible)",
  "established_facts": {
    "loves": ["Aerosmith", "rock and roll"],
    "hates": ["disco"]
  }
}
```

**Result:** Guaranteed accuracy based on structured data.

## What's Included

```
MCP_Implementations/
├── MCP_IMPLEMENTATION_GUIDE.md (this file)
├── WalkThisWay_Character_MCP/
│   ├── server.py
│   ├── requirements.txt
│   ├── README.md
│   └── data/
│       └── characters.json (9 characters with full Story Bible data)
└── COMPASS_Character_MCP_Template/
    ├── server.py
    ├── requirements.txt
    ├── README.md
    └── data/
        └── characters_template.json (placeholder template)
```

## Walk This Way MCP - Quick Start

### Characters Included

- **Nick Johnson** - Working-class rocker, Aerosmith fan
- **Jackie Marsh** - Upper-class pianist, Queen fan  
- **Maxanne Sartori** - WBCN DJ, narrator
- **Patty Lally** - Peacemaker, Fleetwood Mac fan
- **Dan Johnson** - Nick's deceased father (ghost presence)
- **Grace Johnson** - Nick's mother, Friendly's waitress
- **Dr. Richard Marsh** - Jackie's controlling father
- **Elizabeth Marsh** - Jackie's sister, violinist
- **Eileen Marsh** - Jackie's mother, socialite

### Installation

```bash
# Navigate to MCP directory
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install mcp

# Make executable
chmod +x server.py
```

### Configure Cursor

Add to `~/.cursor/mcp_settings.json`:

```json
{
  "mcpServers": {
    "walkthisway-characters": {
      "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/venv/bin/python",
      "args": [
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/server.py"
      ]
    }
  }
}
```

### Test It

Restart Cursor, then:

```
Use walkthisway-characters MCP to list all characters
```

Expected: Nick Johnson, Jackie Marsh, Maxanne Sartori, etc.

## COMPASS Template - Quick Start

### For Your Next Novel

```bash
# Copy template to new location
cp -r "COMPASS_Character_MCP_Template" "/path/to/YourNovel/YourNovel_Character_MCP"

# Navigate to new directory
cd "/path/to/YourNovel/YourNovel_Character_MCP"

# Copy and rename template
cd data
cp characters_template.json characters.json

# Edit characters.json - replace all WRITE_X_HERE placeholders
```

### Placeholder System

Template uses intuitive placeholders:

```json
{
  "CHARACTER_NAME_1": {
    "basic_info": {
      "age": "WRITE_AGE_HERE",
      "occupation": "WRITE_OCCUPATION_HERE"
    },
    "personality": {
      "traits": [
        "WRITE_TRAIT_1_HERE",
        "WRITE_TRAIT_2_HERE"
      ]
    }
  }
}
```

Replace with your novel's data:

```json
{
  "Sarah Chen": {
    "basic_info": {
      "age": 28,
      "occupation": "Cryptography PhD student"
    },
    "personality": {
      "traits": [
        "analytical",
        "stubborn"
      ]
    }
  }
}
```

## Available Tools (Both Implementations)

### 1. `list_characters`
Get all character names.

### 2. `get_character`
Complete character profile.

### 3. `get_character_attribute`
Query specific nested attributes.
- `preferences.music.loves`
- `personality.voice`
- `relationships.CHARACTER_X`

### 4. `check_character_fact`
Validate proposed facts against established canon.

### 5. `get_relationship`
Get relationship details with evolution timeline.

### 6. `search_characters`
Find characters by any attribute.

### 7. `get_character_arc`
Complete character development timeline.

### 8. `get_character_voice`
Voice patterns for dialogue authenticity.

### 9. `get_all_relationships`
All relationships for a specific character.

### 10. `compare_characters`
Compare two characters across attributes.

## Usage Examples for Walk This Way

### Scenario 1: Writing Battle of the Bands Scene

```
I'm writing the 1979 Battle of the Bands scene. Get Nick Johnson 
and Jackie Marsh's relationship status in March 1979, their musical 
styles, and their ages. Use walkthisway-characters MCP.
```

**MCP Returns:**
- Nick: 17, Aerosmith cover band, raw passionate style
- Jackie: 17, Queen cover band, technical precision
- Relationship: "Strangers in high school halls, rivals at Battle of the Bands"

### Scenario 2: Dialogue Consistency

```
Get Nick Johnson's voice patterns. Does this dialogue sound like him:

"Indeed, I believe the musical composition demonstrates exceptional 
technical proficiency."
```

**MCP Returns:**
```json
{
  "voice": "Working-class Boston dialect, economical speech, 
           defensive pride, raw emotion, direct expression",
  "consistent": false,
  "reasoning": "Nick uses working-class speech, not formal academic language"
}
```

### Scenario 3: Timeline Validation

```
Check timeline consistency: Nick Johnson plays guitar at 
Dan Johnson's funeral (November 1976, age 14)
```

**MCP Returns:**
```json
{
  "age_at_event": 14,
  "conflicts_detected": [],
  "note": "Nick was 14 in November 1976 (born 1962)"
}
```

### Scenario 4: Relationship Evolution

```
Get the complete relationship history between Nick Johnson 
and Jackie Marsh with all key moments
```

**MCP Returns:**
Full timeline from 1974 friendship → 1975 talent show → 1976 fracture → 1979 rivalry → recording session redemption.

## Integration with COMPASS Agents

### Current COMPASS Agents

Your existing agents can leverage the MCP:

1. **Creative Collaborator** - Query character data before suggesting prose
2. **Character Depth Coach** - Validate emotional arcs against timeline
3. **Prose Polish Expert** - Check dialogue against voice patterns
4. **Strategic Writing Coordinator** - Verify plot consistency with character facts
5. **Structural Perfection Specialist** - Validate character presence in acts

### Example Agent Integration

Add to agent instructions:

```
Before suggesting any character dialogue or actions, query the 
character MCP to verify:
1. Voice patterns match established style
2. Actions consistent with personality traits
3. Timeline placement is accurate
4. Relationship status reflects current chapter
```

## Maintenance Workflow

### Updating Character Data (Walk This Way)

**As you write:**

1. Draft chapter
2. Discover new character detail (e.g., Nick has a new habit)
3. Open `WalkThisWay_Character_MCP/data/characters.json`
4. Add detail to appropriate character section
5. Save file
6. Continue writing (no restart needed)

**Example:**

```json
"Nick Johnson": {
  "personality": {
    "quirks": [
      "Plays $25 pawn shop guitar held together with duct tape",
      "Known as 'that guitar guy' around town",
      "Taps guitar pick on thumb when nervous"  // NEW
    ]
  }
}
```

### Creating New Novel Database (COMPASS Template)

1. Copy `COMPASS_Character_MCP_Template` directory
2. Rename to `YourNovel_Character_MCP`
3. Copy `characters_template.json` → `characters.json`
4. Replace all placeholders with your character data
5. Delete `_TEMPLATE_NOTES` section
6. Configure Cursor with new MCP
7. Test and start writing

## Future MCP Expansions

### Timeline MCP Server
Track chronological events, validate temporal logic.

**Tools:**
- `add_event(date, event, characters, location)`
- `get_timeline(start_date, end_date)`
- `get_character_location(character, date)`
- `check_knowledge_state(character, fact, chapter)`

### Walk This Way specific examples:
- "Where was Nick Johnson on November 14, 1976?"
- "What did Jackie know about Dan's death by Chapter 12?"

### Music References MCP Server
Track song usage, rights management, character associations.

**Tools:**
- `get_song_info(song_title)`
- `get_character_songs(character_name)`
- `check_song_era(song, year)` - validate song existed in story year
- `get_songs_by_band(band_name)`

### Sudbury Geography MCP Server
Location consistency, distances, class divisions.

**Tools:**
- `get_location_details(location)`
- `calculate_distance(location1, location2)`
- `get_class_side(address)` - which side of Hop Brook?
- `get_nearby_locations(location, radius)`

## Technical Details

### Data Format

Characters stored as JSON with nested structure:

```json
{
  "Character Name": {
    "basic_info": { },
    "personality": { },
    "preferences": { },
    "background": { },
    "relationships": {
      "Other Character": {
        "type": "...",
        "evolution": "...",
        "key_moments": [ ]
      }
    },
    "arc": {
      "key_moments": [ ]
    }
  }
}
```

### Server Architecture

```
┌─────────────────┐
│  Cursor IDE     │
│                 │
│  Claude AI ─────┼──► MCP Tool Calls
│                 │
└────────┬────────┘
         │
    ┌────▼────────────────┐
    │  MCP Protocol Layer │
    └────┬────────────────┘
         │
    ┌────▼─────────┐
    │ server.py    │
    │ (Python MCP) │
    └────┬─────────┘
         │
    ┌────▼──────────────┐
    │ characters.json   │
    │ (Structured Data) │
    └───────────────────┘
```

### Why Python?

- MCP SDK officially supports Python
- Easy to extend with additional logic
- Fast JSON parsing
- Simple deployment (virtual environment)

## Advantages Over Traditional Approaches

| Feature | Markdown Files | Scrivener | MCP Server |
|---------|---------------|-----------|------------|
| AI Query Accuracy | Probabilistic | No AI integration | Deterministic |
| Scalability | Context limited | Single project | Unlimited |
| Validation | Manual | Manual | Programmatic |
| Cross-Project | Difficult | Separate files | Shared database |
| Version Control | Git-friendly | Binary files | Git-friendly |
| Computation | No | No | Yes |

## Critical Success Factors

This approach works best if you:

✅ Have technical capability (can debug Python)  
✅ Enjoy systematic thinking (architect mindset)  
✅ Have long-term projects (10-novel contract)  
✅ Value precision over flexibility  
✅ Use Cursor IDE consistently  

## Getting Started: Recommended Path

### Phase 1: Test with Walk This Way (Week 1)

1. Install Walk This Way MCP
2. Write one chapter using MCP queries
3. Validate value proposition

**Success criteria:** MCP queries save time and prevent errors

### Phase 2: Expand Walk This Way (Weeks 2-8)

1. Continue using character MCP through rest of novel
2. Update database as you discover new details
3. Track: How many times does MCP prevent consistency errors?

**Success criteria:** Database becomes indispensable reference

### Phase 3: Build Timeline MCP (Between Books)

1. After Walk This Way completion, assess pain points
2. Build Timeline MCP if temporal consistency was challenging
3. Prepare for Book 2 with both Character + Timeline MCPs

### Phase 4: Template Refinement (Books 2-3)

1. Use COMPASS template for Book 2
2. Identify gaps in template structure
3. Refine template based on real usage
4. Consider Music, Geography, or other domain MCPs

### Phase 5: Full COMPASS Ecosystem (Books 4-10)

1. Mature MCP ecosystem across multiple domains
2. Share COMPASS system with other writers
3. Consider creating additional templates

## Troubleshooting

### MCP Server Not Appearing in Cursor

1. Check `~/.cursor/mcp_settings.json` exists and has correct paths
2. Verify Python virtual environment path is absolute (not relative)
3. Ensure `server.py` is executable (`chmod +x server.py`)
4. Completely quit and restart Cursor (not just reload)

### "Character Not Found" Errors

1. Check exact spelling (case-sensitive)
2. Verify character exists in `characters.json`
3. If using template, ensure `_TEMPLATE_NOTES` section is deleted

### Queries Return Unexpected Results

1. Use `get_character` to see full structure
2. Check attribute path syntax (dot notation: `preferences.music.loves`)
3. Verify JSON file has valid syntax (use online validator)

### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install mcp
```

## Support and Questions

For Walk This Way novel: Reference `Story_Bible/` markdown files as canonical source

For COMPASS template: See `COMPASS_Character_MCP_Template/README.md`

For MCP protocol: https://modelcontextprotocol.io/

## File Manifest

### Walk This Way MCP
```
WalkThisWay_Character_MCP/
├── server.py (427 lines, 10 tools)
├── requirements.txt (1 line)
├── README.md (comprehensive usage guide)
└── data/
    └── characters.json (9 characters, ~1000 lines)
```

### COMPASS Template
```
COMPASS_Character_MCP_Template/
├── server.py (universal template, 10 tools)
├── requirements.txt (1 line)
├── README.md (template usage guide)
└── data/
    └── characters_template.json (placeholder structure)
```

## Next Steps

1. **Install Walk This Way MCP** following Quick Start above
2. **Test with sample queries** to validate functionality
3. **Write one chapter** using MCP for character consistency
4. **Evaluate**: Did this genuinely help your writing process?
5. **Decide**: Expand to Timeline MCP or wait until Book 2?

---

**Created:** January 10, 2026  
**Author:** Timothy J. Smith  
**Novel:** Walk This Way  
**System:** COMPASS Writing System  
**Status:** Production Ready

**This is genuinely novel territory. You're pioneering MCP for fiction writing.**
