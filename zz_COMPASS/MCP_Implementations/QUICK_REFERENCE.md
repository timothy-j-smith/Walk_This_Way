# MCP Quick Reference - Walk This Way

## Installation (One-Time Setup)

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP"

./setup.sh
```

Follow the prompts, then add configuration to Cursor and restart.

## Common Queries

### Character Lookups

```
List all Walk This Way characters (use MCP)

Get Nick Johnson's complete profile

Get Jackie Marsh's voice patterns for dialogue
```

### Consistency Checks

```
Check if this is consistent with Walk This Way: 
"Nick Johnson loves disco music"

Verify: Jackie Marsh speaks in casual slang
```

### Relationships

```
Get the relationship between Nick Johnson and Jackie Marsh

Show me Maxanne's relationship with Nick Johnson

What is Dr. Richard Marsh's relationship with Jackie?
```

### Timeline & Ages

```
Get all character ages in 1979

How old was Nick when his father died?

Check timeline: Nick plays guitar at age 8 in 1970
```

### Music & Preferences

```
What music does Nick Johnson love?

Get Jackie Marsh's favorite bands

Find all characters who hate disco
```

### Voice & Dialogue

```
I'm writing dialogue for Nick Johnson. Get his voice patterns.

Does this line sound like Jackie: "Yo dude, that's rad!"

Get Maxanne's speaking style for narration
```

### Character Arcs

```
Get Nick Johnson's complete character arc

Show me Jackie's key moments from 1975-1979

What is Patty Lally's role in the story?
```

### Searching

```
Find all characters connected to Aerosmith

Search for working-class characters

Find characters who appear in 1976
```

## Tools Reference

| Tool | What It Does | Example Use |
|------|-------------|-------------|
| `list_characters` | Get all names | "List all characters" |
| `get_character` | Full profile | "Get Nick Johnson's profile" |
| `get_character_attribute` | Specific detail | "Get Nick's music preferences" |
| `check_character_fact` | Verify consistency | "Does Nick love disco?" |
| `get_relationship` | Relationship details | "Nick and Jackie relationship" |
| `search_characters` | Find by attribute | "Find Aerosmith fans" |
| `get_character_timeline` | Character arc | "Nick's character arc" |
| `get_character_voice` | Dialogue patterns | "Nick's speaking style" |
| `get_characters_by_year` | Ages in year | "Ages in 1979" |
| `check_timeline_consistency` | Validate events | "Nick age 8 in 1970?" |

## Attribute Paths (Dot Notation)

Access nested data:

```
preferences.music.loves
personality.traits
personality.voice
relationships.Jackie Marsh
arc.key_moments
background.family
basic_info.age_1979
```

Example:
```
Get Nick Johnson's attribute: preferences.music.loves
```

## Quick Troubleshooting

**MCP not showing in Cursor:**
- Check `~/.cursor/mcp_settings.json` exists
- Verify paths are absolute (not relative)
- Completely quit and restart Cursor

**Character not found:**
- Check exact spelling (case-sensitive)
- Try: "List all characters" to see available names

**Unexpected results:**
- Use "Get CHARACTER's complete profile" to see structure
- Check attribute path syntax (use dots: `preferences.music`)

## Update Character Data

```bash
# Edit character file
open "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/data/characters.json"

# No restart needed - changes are live immediately
```

## Characters Available

- Nick Johnson (protagonist)
- Jackie Marsh (protagonist)
- Maxanne Sartori (narrator)
- Patty Lally (peacemaker)
- Dan Johnson (Nick's father, deceased)
- Grace Johnson (Nick's mother)
- Dr. Richard Marsh (Jackie's father)
- Elizabeth Marsh (Jackie's sister)
- Eileen Marsh (Jackie's mother)

---

**Full Documentation:** See `MCP_IMPLEMENTATION_GUIDE.md`
