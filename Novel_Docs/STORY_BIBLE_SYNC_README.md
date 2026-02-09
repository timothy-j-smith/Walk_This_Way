# Walk This Way - Story Bible Auto-Sync Tools

## Overview

Automated tools to sync Story Bible markdown files → MCP JSON databases

**Purpose:** Eliminate manual JSON editing. Update markdown, run script, MCP syncs automatically.

---

## Scripts Available

### 1. `sync_story_bible.py` (Main Tool)

**Syncs:**
- `Story_Bible/character-bible.md` → `WalkThisWay_Character_MCP/data/characters.json`
- `Story_Bible/timeline.md` → `WalkThisWay_Timeline_MCP/data/timeline.json` (future)
- `Story_Bible/music-references.md` → `WalkThisWay_Music_MCP/data/music.json` (future)

**Usage:**
```bash
python sync_story_bible.py
```

**What it does:**
1. Reads your Story Bible markdown files
2. Uses Claude API to intelligently convert to MCP JSON format
3. Creates backup of existing MCP files
4. Writes updated MCP JSON
5. Shows summary of changes

**Requirements:**
- Anthropic API key (get from https://console.anthropic.com/settings/keys)
- Python 3.8+
- `anthropic` package

### 2. `build_story_structure_mcp.py`

**Syncs:**
- `Story_Bible/synopsis.md` → `WalkThisWay_Story_MCP/data/story_structure.json`
- `Story_Bible/outline.md` → Same MCP

**Usage:**
```bash
python build_story_structure_mcp.py
```

---

## Setup (One Time)

### Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Anthropic SDK
pip install anthropic
```

### Set API Key

**Option A: Environment Variable (Recommended)**
```bash
# Add to your ~/.zshrc or ~/.bash_profile
export ANTHROPIC_API_KEY="sk-ant-..."

# Reload shell
source ~/.zshrc
```

**Option B: Script Will Prompt**
```bash
# Just run script, it will ask for key
python sync_story_bible.py
```

---

## Workflow

### Weekly Sync Workflow

```bash
# 1. Write 2-3 chapters
# Discover new character details while writing

# 2. Update Story Bible (Friday afternoon)
open Story_Bible/character-bible.md
# Add new discoveries
# Save

# 3. Run sync script
python sync_story_bible.py

# 4. Review changes
# Script shows what was updated

# 5. Restart Cursor (if needed)
# MCP servers reload automatically

# 6. Continue writing
# MCPs now have latest data
```

### After Major Story Bible Updates

```bash
# Update all markdown files
open Story_Bible/character-bible.md
open Story_Bible/synopsis.md  
open Story_Bible/outline.md

# Make changes, save all

# Run both sync scripts
python sync_story_bible.py
python build_story_structure_mcp.py

# Restart Cursor
# All MCPs updated
```

---

## What Gets Synced

### Character Bible → Character MCP

**Markdown format (natural language):**
```markdown
### Nick Johnson
**Voice/Personality:** Nick speaks with economical, direct sentences. 
Working-class Boston roots show in his word choices and defensive edge.
When emotional, he gets quieter, not louder.
```

**Converts to MCP JSON (structured):**
```json
{
  "Nick Johnson": {
    "personality": {
      "voice": "Economical, direct sentences. Working-class Boston dialect. Gets quieter when emotional, not louder. Defensive edge.",
      "traits": ["economical speech", "working-class roots", "defensive", "quiet when emotional"]
    }
  }
}
```

**You write naturally in markdown → Script structures for MCP**

### Synopsis/Outline → Story Structure MCP

**Markdown:**
```markdown
# Walk This Way - Synopsis

Two teenage musicians in 1979 Boston—one working-class, one privileged—
see their friendship destroyed by class divisions...

# Outline

## Act I: Friendship
Chapter 1: Maxanne's final broadcast begins
Chapter 4: Nick and Jackie meet (belt buckles)
...
```

**Converts to:**
```json
{
  "synopsis": {
    "logline": "...",
    "premise": "..."
  },
  "acts": {
    "act_1": {
      "chapters": "1-12",
      "key_beats": [...]
    }
  }
}
```

---

## Features

### Intelligent Conversion

✅ **Natural language understanding** - Write Story Bible in your voice  
✅ **Preserves all details** - Nothing lost in conversion  
✅ **Handles formatting variations** - Markdown formatting doesn't matter  
✅ **Creates consistent structure** - MCP format standardized  

### Safety Features

✅ **Automatic backups** - Creates `.backup` before overwriting  
✅ **Validation** - Checks JSON is valid before writing  
✅ **Error handling** - Clear error messages if something fails  
✅ **Dry run option** - Can preview changes without writing  

### Cost

💰 **~$0.05 per sync** using Claude API  
💰 **Weekly syncs: ~$0.20/month**  
💰 **Negligible cost for automated accuracy**

---

## Troubleshooting

### "API key not found"

```bash
# Set environment variable
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Or let script prompt you
```

### "File not found"

```bash
# Check paths
ls Story_Bible/
# Should see: character-bible.md, timeline.md, etc.

# If missing, create them
touch Story_Bible/synopsis.md
touch Story_Bible/outline.md
```

### "Invalid JSON in response"

This means Claude's response wasn't valid JSON. Usually fixed by:
1. Running script again
2. Checking Story Bible markdown isn't corrupted
3. Updating anthropic package: `pip install --upgrade anthropic`

### "MCP not updating in Cursor"

```bash
# Cursor needs restart to reload MCP data
# Cmd+Q (full quit)
# Reopen Cursor
```

---

## Advanced Usage

### Sync Only Characters

```python
# In sync_story_bible.py, comment out other syncs
def main():
    results = {
        "characters": sync_characters(),
        # "timeline": sync_timeline(),  # Skip
        # "music": sync_music()          # Skip
    }
```

### Preview Without Writing

Add to scripts:

```python
# Add --dry-run flag
import sys
DRY_RUN = '--dry-run' in sys.argv

if not DRY_RUN:
    write_json_safe(CHARACTER_MCP, mcp_data)
else:
    print("DRY RUN: Would write:", mcp_data)
```

### Custom MCP Format

Edit the prompt in `convert_character_bible_to_mcp()` to change MCP structure.

---

## File Locations

```
Walk This Way/
├── sync_story_bible.py               ← Main sync tool
├── build_story_structure_mcp.py      ← Story structure tool
├── Story_Bible/
│   ├── character-bible.md            ← Update this (human)
│   ├── timeline.md                   ← Update this (human)
│   ├── music-references.md           ← Update this (human)
│   ├── synopsis.md                   ← Update this (human)
│   └── outline.md                    ← Update this (human)
└── zz_COMPASS/MCP_Implementations/
    ├── WalkThisWay_Character_MCP/
    │   └── data/
    │       ├── characters.json       ← Auto-generated
    │       └── characters.json.backup
    └── WalkThisWay_Story_MCP/
        └── data/
            └── story_structure.json  ← Auto-generated
```

**Rule:** Only edit `.md` files. Scripts generate `.json` files.

---

## Integration with Writing Workflow

### Before Writing Session

```bash
# Quick sync to ensure MCPs current
python sync_story_bible.py
```

### During Writing Session

- Update Story Bible as you discover details
- Don't sync yet (interrupts flow)

### After Writing Session

```bash
# Weekly sync
python sync_story_bible.py

# Commit to Git
git add Story_Bible/ zz_COMPASS/MCP_Implementations/
git commit -m "Updated Story Bible and synced MCPs - Ch 15-17 discoveries"
```

---

## Next Steps

1. **Update Story Bible markdown files** with natural, readable prose
2. **Run sync scripts** to generate MCP JSON
3. **Test in Cursor** - MCPs should have latest data
4. **Iterate** - Refine Story Bible, re-sync as needed

---

**Created:** January 10, 2026  
**Part of:** COMPASS Writing System  
**Status:** Production ready

**Questions? Test the sync and report results to Hank!**
