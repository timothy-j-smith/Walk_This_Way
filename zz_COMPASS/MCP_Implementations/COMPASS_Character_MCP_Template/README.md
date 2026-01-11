# COMPASS Writing System - Character Database MCP Template

## Overview

This is a **universal template** for creating character database MCP servers for any fiction novel. Part of the COMPASS Writing System, this template provides a standardized way to manage character data across all your writing projects.

## What This Template Provides

- **Universal Character Structure**: Works for any genre (literary fiction, thriller, romance, sci-fi, fantasy, etc.)
- **Placeholder System**: Replace `WRITE_X_HERE` placeholders with your novel's specific information
- **Extensible Design**: Add custom fields beyond the template as your story requires
- **Relationship Tracking**: Built-in support for complex character relationships and evolution
- **Arc Management**: Track character development from beginning to end
- **Voice Consistency**: Store and query speech patterns for authentic dialogue

## Quick Start for New Novel

### 1. Copy Template Directory

```bash
# From your novel's project directory
cp -r "/path/to/COMPASS_Character_MCP_Template" "./MyNovel_Character_MCP"
cd "./MyNovel_Character_MCP"
```

### 2. Copy and Rename Template File

```bash
cd data
cp characters_template.json characters.json
```

### 3. Fill In Your Characters

Open `data/characters.json` and replace all `WRITE_X_HERE` placeholders with your novel's specific information.

**Example transformation:**

```json
// BEFORE (template)
"CHARACTER_NAME_1": {
  "basic_info": {
    "age": "WRITE_AGE_HERE",
    "occupation": "WRITE_OCCUPATION_HERE"
  }
}

// AFTER (your novel)
"Sarah Chen": {
  "basic_info": {
    "age": 28,
    "occupation": "Cryptography PhD student"
  }
}
```

### 4. Install and Configure

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install mcp

# Make executable
chmod +x server.py
```

### 5. Configure Cursor

Add to `~/.cursor/mcp_settings.json`:

```json
{
  "mcpServers": {
    "mynovel-characters": {
      "command": "/full/path/to/MyNovel_Character_MCP/venv/bin/python",
      "args": [
        "/full/path/to/MyNovel_Character_MCP/server.py"
      ]
    }
  }
}
```

### 6. Restart Cursor and Test

```
Use mynovel-characters MCP to list all characters
```

## Template Structure

### Required Fields (Minimum Viable Character)

```json
{
  "CHARACTER_NAME": {
    "basic_info": {
      "age": "...",
      "occupation": "..."
    },
    "personality": {
      "traits": ["...", "..."]
    },
    "arc": {
      "starting_state": "...",
      "ending_state": "..."
    }
  }
}
```

### Recommended Fields (Full Character Profile)

- `basic_info`: Physical and demographic details
- `personality`: Traits, voice, quirks
- `preferences`: Likes and dislikes
- `background`: History, family, education
- `relationships`: Connections to other characters
- `arc`: Development with key moments
- `first_appearance`: Where character appears

### Optional Custom Fields You Can Add

```json
{
  "CHARACTER_NAME": {
    // ... standard fields ...
    "skills": ["skill1", "skill2"],
    "goals": ["short-term goal", "long-term goal"],
    "fears": ["fear1", "fear2"],
    "secrets": "hidden information",
    "symbolic_items": ["item that represents character"],
    "theme": "what character represents in story"
  }
}
```

## Available Tools

All tools work with your custom character data:

1. **`list_characters`** - Get all character names
2. **`get_character`** - Complete profile
3. **`get_character_attribute`** - Specific attribute (nested paths supported)
4. **`check_character_fact`** - Consistency validation
5. **`get_relationship`** - Relationship between two characters
6. **`search_characters`** - Find by trait/attribute
7. **`get_character_arc`** - Complete character development
8. **`get_character_voice`** - Voice patterns for dialogue
9. **`get_all_relationships`** - All relationships for a character
10. **`compare_characters`** - Compare two characters

## Placeholder Naming Convention

All placeholders follow this pattern:

- `WRITE_X_HERE` for single values (e.g., `WRITE_AGE_HERE`)
- `CHARACTER_NAME_X` for character references (e.g., `CHARACTER_NAME_2`)
- `CATEGORY_NAME` for custom categories (e.g., `CATEGORY_OF_PREFERENCE`)

## Usage Examples

### During Chapter Writing

**Query character before scene:**
```
I'm writing a scene with Sarah Chen at a coffee shop.
Get her preferences and personality traits from the MCP.
```

**Check dialogue consistency:**
```
Get Sarah Chen's voice patterns. Does this line sound like her:
"Yo dude, that's totally rad!"
```

**Verify relationship status:**
```
What's the current relationship between Sarah Chen and Dr. Martinez
at Chapter 7? (use MCP)
```

### Updating Your Database

As you write and discover new character details:

1. Open `data/characters.json`
2. Add the new information
3. Save the file
4. Continue writing (no restart needed)

**Example update:**

```json
"Sarah Chen": {
  "personality": {
    "quirks": [
      "Taps fingers when thinking",
      "Quotes movies when nervous",
      "Always orders black coffee, never adds sugar"  // NEW
    ]
  }
}
```

## Multi-Novel Workflow

### Option A: One MCP Per Novel

Create separate MCP server for each novel:

```
MyNovels/
  Novel_1/
    Novel1_Character_MCP/
  Novel_2/
    Novel2_Character_MCP/
```

Configure Cursor with all servers:

```json
{
  "mcpServers": {
    "novel1-characters": { "command": "...", "args": ["..."] },
    "novel2-characters": { "command": "...", "args": ["..."] }
  }
}
```

### Option B: Shared Universe (Multiple Novels, Same Characters)

Use single MCP server with all characters:

```
MyUniverse/
  Shared_Character_MCP/
    data/
      characters.json  // All characters from all novels
```

## Integration with COMPASS Agents

Your COMPASS writing agents can query the character MCP:

**Example agent instruction:**
```
Before suggesting any dialogue, use the character MCP to get
the character's voice patterns and ensure consistency.
```

**Example agent workflow:**
1. Receive writing request
2. Query character MCP for relevant details
3. Generate prose consistent with character database
4. Validate output against character facts

## Field Type Reference

### String Fields
```json
"name": "VALUE"
```

### Array Fields
```json
"traits": ["value1", "value2"]
```

### Object Fields
```json
"physical": {
  "height": "...",
  "eyes": "..."
}
```

### Nested Relationships with Evolution
```json
"CHARACTER_X": {
  "type": "friend",
  "status": "complicated",
  "evolution": "Description of how relationship changes",
  "key_moments": [
    {
      "chapter": 5,
      "event": "What happens",
      "change": "How relationship changes"
    }
  ]
}
```

## Tips for Filling Template

### Start Simple
Don't fill every field immediately. Start with:
- Basic info (age, occupation)
- 3-5 personality traits
- Key relationships
- Starting and ending states

### Add As You Write
Discover details through writing, then update database.

### Be Specific
Instead of: `"voice": "WRITE_VOICE_HERE"`
Write: `"voice": "Southern drawl, uses 'honey' and 'darlin', never swears"`

### Use Concrete Examples
Instead of: `"quirk": "WRITE_QUIRK_HERE"`
Write: `"quirk": "Adjusts glasses when lying"`

### Track Evolution
For relationships and arcs, include specific chapters and events:

```json
"key_moments": [
  {
    "chapter": 12,
    "event": "Sarah discovers John's betrayal",
    "change": "Trust turns to suspicion",
    "emotional_state": "Devastated, questioning everything"
  }
]
```

## Advanced: Custom Server Name

Edit `server.py` line 13:

```python
# Default
app = Server("compass-characters")

# Custom for your novel
app = Server("mynovel-characters")
```

## Advanced: Additional Tools

You can add custom tools to `server.py`:

```python
Tool(
    name="get_character_skills",
    description="Get all skills for a character",
    inputSchema={
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        },
        "required": ["name"]
    }
)
```

Then implement the tool in `call_tool()` function.

## Troubleshooting

### "Character not found"
- Check exact spelling (case-sensitive)
- Verify character exists in `characters.json`
- Remove `_TEMPLATE_NOTES` section after filling template

### "Attribute not found"
- Use dot notation: `preferences.music.loves`
- Check that attribute exists in character profile
- Use `get_character` to see full structure

### MCP Server Not Loading
- Verify Cursor config file path is correct
- Check that `server.py` is executable (`chmod +x server.py`)
- Ensure virtual environment python path is absolute
- Restart Cursor completely

## File Checklist

When creating new novel MCP:

- [ ] Copy template directory
- [ ] Rename to `YourNovel_Character_MCP`
- [ ] Copy `characters_template.json` to `characters.json`
- [ ] Fill in character placeholders
- [ ] Delete `_TEMPLATE_NOTES` section
- [ ] Create virtual environment
- [ ] Install `mcp` package
- [ ] Make `server.py` executable
- [ ] Configure Cursor `mcp_settings.json`
- [ ] Restart Cursor
- [ ] Test with `list_characters`

## Future Expansion

Consider creating additional COMPASS MCP templates:

- **Timeline MCP**: Chronological event tracking
- **Location MCP**: Setting and geography database
- **Plot MCP**: Thread tracking and structure
- **Worldbuilding MCP**: Rules, magic systems, technology

All following this same template philosophy.

---

**COMPASS Writing System**  
**Created:** January 10, 2026  
**Template Version:** 1.0  
**Compatible With:** Any fiction novel, any genre
