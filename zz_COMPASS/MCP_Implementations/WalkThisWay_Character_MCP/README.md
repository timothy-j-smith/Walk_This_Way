# Walk This Way - Character Database MCP Server

## Overview

This MCP server provides structured, queryable access to all character information from the novel **Walk This Way**. Instead of relying on markdown files and AI interpretation, this server delivers deterministic, accurate data directly from your Story Bible.

## Features

- **Character Profiles**: Complete structured data for Nick Johnson, Jackie Marsh, Maxanne Sartori, and all supporting characters
- **Relationship Tracking**: Full evolution timelines for character relationships (Nick & Jackie's friendship-to-rivalry arc, etc.)
- **Timeline Validation**: Check consistency of events with character ages and established chronology
- **Voice/Dialogue Support**: Get detailed voice patterns for authentic dialogue writing
- **Music Preferences**: Query character music tastes for scene accuracy
- **Consistency Checking**: Validate proposed facts against established Story Bible canon

## Available Tools

### 1. `list_characters`
Get all character names in the database.

**Example:**
```
List all characters in Walk This Way using the MCP
```

### 2. `get_character`
Get complete profile for any character.

**Example:**
```
Get Nick Johnson's complete character profile using the MCP
```

### 3. `get_character_attribute`
Query specific attributes (nested paths supported).

**Examples:**
```
What music does Nick Johnson love? (uses MCP)
What is Jackie Marsh's voice pattern for dialogue? (uses MCP)
Get Nick's relationship with his father Dan (uses MCP)
```

### 4. `check_character_fact`
Validate proposed facts against Story Bible.

**Examples:**
```
Check consistency: "Nick Johnson loves disco music"
Check consistency: "Jackie Marsh speaks in casual slang"
```

### 5. `get_relationship`
Get full relationship details with evolution timeline.

**Examples:**
```
Get the relationship between Nick Johnson and Jackie Marsh
Get Maxanne's relationship with Nick Johnson
```

### 6. `search_characters`
Find characters by any attribute.

**Examples:**
```
Find all characters who love Aerosmith
Search for characters connected to WBCN
Find working-class characters
```

### 7. `get_character_timeline`
Get complete arc with all key moments.

**Example:**
```
Get Nick Johnson's complete character arc timeline
```

### 8. `get_character_voice`
Get voice patterns for dialogue writing.

**Example:**
```
Get Jackie Marsh's voice patterns for this dialogue scene
```

### 9. `get_characters_by_year`
Get all character ages and status for a specific year.

**Examples:**
```
Get all character ages in 1975
Who was alive in 1979?
```

### 10. `check_timeline_consistency`
Verify proposed events against character timeline.

**Example:**
```
Check if this is consistent: Nick Johnson plays guitar at age 8 in 1975
```

## Installation

### 1. Create Directory Structure
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP"
```

### 2. Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install MCP
pip install mcp
```

### 3. Make Server Executable
```bash
chmod +x server.py
```

### 4. Configure Cursor

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

### 5. Restart Cursor

Completely quit and reopen Cursor for MCP server to initialize.

### 6. Test Installation

```
Use walkthisway-characters MCP to list all characters
```

Expected result: Nick Johnson, Jackie Marsh, Maxanne Sartori, etc.

## Usage Workflow

### Writing Chapter Drafts

**Before writing a scene:**
```
I'm writing the 1979 Battle of the Bands scene with Nick and Jackie.
Get their relationship status from the MCP and their musical styles.
```

**During dialogue:**
```
Get Nick Johnson's voice patterns. I need to write dialogue where
he's defensive about his working-class background.
```

### Consistency Checking

**After drafting:**
```
I just wrote: "Nick smiled, remembering the disco nights at The Rat"
Check if this contradicts established facts using the MCP.
```

### Timeline Validation

**When adding events:**
```
Check timeline: Nick performs at WBCN in 1977 (age 15)
Is this consistent with his arc?
```

## Data Structure

The character database (`data/characters.json`) contains:

- **basic_info**: Ages, occupation, location, physical traits
- **personality**: Traits, voice patterns, quirks
- **preferences**: Music (loves/hates), food, etc.
- **background**: Family, education, history, key places
- **relationships**: Full evolution with key moments
- **musical_identity**: Instruments, style, bands, philosophy
- **arc**: Starting state, key moments, ending state

## Advantages Over Markdown Files

| Feature | Markdown | MCP Server |
|---------|----------|------------|
| **Accuracy** | AI interprets | Deterministic queries |
| **Scalability** | Context window limited | No limits |
| **Validation** | Manual | Programmatic |
| **Speed** | Scan entire file | Direct lookup |
| **Consistency** | Probabilistic | Guaranteed |

## Maintenance

### Updating Character Data

As you write, update `data/characters.json`:

1. Draft chapter
2. Discover new character trait/fact
3. Add to `characters.json`
4. Future queries automatically include new information

### Example Update Workflow

```json
// After writing Chapter 15, you discover Nick has a new habit
"quirks": [
  "Plays $25 pawn shop guitar held together with duct tape",
  "Known as 'that guitar guy' around town",
  "Taps his guitar pick against his thumb when nervous"  // NEW
]
```

No Cursor restart required—changes are live immediately.

## Integration with COMPASS Agents

Your COMPASS writing agents can use this MCP:

**Creative Collaborator** can query character voice before suggesting prose.
**Character Depth Coach** can validate emotional arcs against timeline.
**Structural Perfection Specialist** can check relationship evolution.

## Future Enhancements

Potential additions:

- **Timeline MCP**: Chronological event tracking with location data
- **Music References MCP**: Song usage tracking and rights management
- **Sudbury Geography MCP**: Location consistency (Hop Brook, Dutton Road, etc.)
- **Dialogue Voice Analysis**: Statistical pattern matching for character speech

## Story Bible Source Files

This MCP synthesizes data from:
- `Story_Bible/character-bible.md`
- `Story_Bible/timeline.md`
- `Story_Bible/music-references.md`

Keep those files as human-readable references; use MCP for AI queries.

---

**Created:** January 10, 2026  
**Novel:** Walk This Way by Timothy J. Smith  
**Status:** Ready for production use
