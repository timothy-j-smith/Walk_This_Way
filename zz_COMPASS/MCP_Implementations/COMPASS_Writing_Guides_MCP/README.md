# COMPASS_WRITING_GUIDES_MCP

**Comprehensive Fiction Writing Reference Database**

A Model Context Protocol (MCP) server providing instant access to writing advice, author insights, techniques, and principles from master writers. This is the **first-of-its-kind Writing Guides MCP** for fiction writers.

---

## 🎯 What This MCP Provides

### **Author Writing Advice**
- **Stephen King** - "On Writing" principles and quotes
- **Anne Lamott** - "Bird by Bird" insights
- **Brandon Sanderson** - Craft-focused advice
- More authors can be added easily

### **Writing Topics & Principles**
- Dialogue
- Pacing
- Character Development
- Prose Style
- Atmosphere & Mood
- Point of View
- Show Don't Tell
- Revision

### **Author Style Guides**
Complete style breakdowns for:
- Stephen King
- Richard Russo
- Dennis Lehane
- Donna Tartt
- J.D. Salinger
- Annie Proulx
- Cormac McCarthy
- Colson Whitehead

### **Writing Techniques**
Organized techniques for:
- Pacing techniques
- Dialogue techniques
- Character techniques
- Prose techniques
- Atmosphere techniques

### **Genre Guidance**
Specific advice for:
- Literary Fiction
- Crime/Mystery
- Horror/Supernatural
- Coming of Age

### **Writing Quotes**
Inspirational quotes from master writers, searchable by author or keyword.

---

## 🚀 Quick Start

### 1. Setup

```bash
cd zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP
./setup.sh
```

This will:
- Create a Python virtual environment
- Install MCP dependencies
- Make server.py executable

### 2. Configure Cursor

Add to `~/.cursor/mcp.json` (or `.cursor/config/mcp.json`):

```json
{
  "mcpServers": {
    "compass-writing-guides": {
      "command": "/full/path/to/COMPASS_Writing_Guides_MCP/venv/bin/python",
      "args": [
        "/full/path/to/COMPASS_Writing_Guides_MCP/server.py"
      ]
    }
  }
}
```

**Note:** Replace `/full/path/to/` with the actual absolute path to your project directory.

### 3. Restart Cursor

**Important:** Completely quit Cursor (Cmd+Q) and restart for MCP changes to take effect.

### 4. Test It

Try these queries:

```
Use compass-writing-guides MCP to get Stephen King's advice on adverbs
```

```
Use compass-writing-guides MCP to get guidance on dialogue
```

```
Use compass-writing-guides MCP to get Richard Russo's style guide
```

---

## 📚 Available Tools

### **Get Author Advice**
```
Get writing advice and principles from a specific author
```
**Parameters:**
- `author` (required): Author name (e.g., "Stephen King", "Anne Lamott")
- `topic` (optional): Filter by topic (e.g., "adverbs", "dialogue")

**Example:**
```
Use compass-writing-guides MCP to get Stephen King's advice on dialogue
```

### **Get Topic Guidance**
```
Get comprehensive guidance on a writing topic
```
**Parameters:**
- `topic` (required): Topic name (e.g., "dialogue", "pacing", "character_development", "prose_style", "atmosphere", "point_of_view", "show_dont_tell", "revision")

**Example:**
```
Use compass-writing-guides MCP to get guidance on pacing
```

### **Get Author Style**
```
Get detailed author style guide (prose style, narrative technique, themes, signature moves, use cases)
```
**Parameters:**
- `author` (required): Author name

**Available Authors:**
- Stephen King
- Richard Russo
- Dennis Lehane
- Donna Tartt
- J.D. Salinger
- Annie Proulx
- Cormac McCarthy
- Colson Whitehead

**Example:**
```
Use compass-writing-guides MCP to get Donna Tartt's style guide
```

### **Get Quote**
```
Get inspirational writing quotes
```
**Parameters:**
- `author` (optional): Filter by author name
- `keyword` (optional): Search for quotes containing keyword

**Example:**
```
Use compass-writing-guides MCP to get quotes about revision
```

### **Get Technique**
```
Get techniques for a specific aspect of writing
```
**Parameters:**
- `technique_type` (required): Type of technique (e.g., "pacing_techniques", "dialogue_techniques", "character_techniques", "prose_techniques", "atmosphere_techniques")

**Example:**
```
Use compass-writing-guides MCP to get dialogue techniques
```

### **Get Genre Guidance**
```
Get genre-specific writing guidance
```
**Parameters:**
- `genre` (required): Genre name (e.g., "literary_fiction", "crime_mystery", "horror_supernatural", "coming_of_age")

**Example:**
```
Use compass-writing-guides MCP to get guidance for crime mystery
```

### **Search Guides**
```
Search across all writing guides by keyword
```
**Parameters:**
- `query` (required): Search keyword or phrase

**Example:**
```
Use compass-writing-guides MCP to search for advice on character motivation
```

### **List Authors**
```
List all available authors with writing advice
```

### **List Topics**
```
List all available writing topics
```

### **Get Writing Tip**
```
Get a quick writing tip on a specific topic or from a specific author
```
**Parameters:**
- `topic` (optional): Topic name
- `author` (optional): Author name

**Example:**
```
Use compass-writing-guides MCP to get a writing tip on dialogue from Stephen King
```

### **Get Methodology**
```
Get writing methodology/philosophy guidance
```
**Parameters:**
- `methodology` (required): Methodology name (e.g., "scalpel_hose", "compass_advanced_tools", "json_prompts")
- `section` (optional): Specific section (e.g., "process", "character_depth_hierarchy", "core_systems")

**Available Methodologies:**
- **scalpel_hose** - The Blood Brothers System for Novel Writing (dual methodology: cut with precision, add depth)
- **compass_advanced_tools** - COMPASS Advanced Cursor Novel Writing Tools system
- **json_prompts** - JSON Prompts System for quick command library

**Example:**
```
Use compass-writing-guides MCP to get the Scalpel & Hose methodology
```

```
Use compass-writing-guides MCP to get the Scalpel & Hose process section
```

### **List Methodologies**
```
List all available writing methodologies and philosophies
```

---

## 💡 Usage Examples

### During Chapter Writing

**Before writing dialogue:**
```
Use compass-writing-guides MCP to get guidance on dialogue, then help me write authentic dialogue for this scene between Nick and Jackie.
```

**Stuck on pacing:**
```
Use compass-writing-guides MCP to get pacing techniques, then help me improve the pacing of this action scene.
```

**Character development:**
```
Use compass-writing-guides MCP to get guidance on character development, then help me deepen Maxanne's emotional journey in this chapter.
```

### Style Reference

**Adopting an author's voice:**
```
Use compass-writing-guides MCP to get Richard Russo's style guide, then help me rewrite this scene with Russo's working-class empathy and community focus.
```

**Multiple style references:**
```
Use compass-writing-guides MCP to get Dennis Lehane's style guide and Stephen King's style guide. I want to combine Lehane's Boston grit with King's accessible prose for this scene.
```

### Revision & Editing

**Prose improvement:**
```
Use compass-writing-guides MCP to get Stephen King's advice on adverbs, then help me identify and fix adverb overuse in this passage.
```

**Show don't tell:**
```
Use compass-writing-guides MCP to get guidance on show_dont_tell, then help me rewrite these paragraphs to show emotions instead of telling them.
```

### Inspiration & Learning

**Quick tips:**
```
Use compass-writing-guides MCP to get a writing tip on character development
```

**Quotes for motivation:**
```
Use compass-writing-guides MCP to get quotes from Stephen King about writing practice
```

**Genre guidance:**
```
Use compass-writing-guides MCP to get guidance for literary_fiction, then help me understand if this chapter fits the genre conventions.
```

**Using methodologies:**
```
Use compass-writing-guides MCP to get the Scalpel & Hose methodology, then help me apply it to edit this chapter.
```

```
Use compass-writing-guides MCP to get the Scalpel & Hose character_depth_hierarchy, then help me identify which tier each character is in this scene.
```

```
Use compass-writing-guides MCP to get the COMPASS advanced tools system, then help me understand which agents would be best for this revision pass.
```

---

## 🔧 Data Structure

The MCP uses a JSON database (`data/writing_guides.json`) organized into:

- **`authors`**: Writing advice and principles from specific authors
- **`topics`**: Comprehensive guidance on writing topics
- **`author_styles`**: Detailed author style guides
- **`techniques`**: Organized writing techniques
- **`genre_guidance`**: Genre-specific advice
- **`quotes`**: Inspirational writing quotes
- **`methodologies`**: Writing methodologies and philosophies (Scalpel & Hose, COMPASS tools, JSON prompts)

---

## 📝 Adding New Content

The data file (`data/writing_guides.json`) is human-readable JSON. You can:

1. **Add new authors**: Add entries to `authors` and/or `author_styles`
2. **Add new topics**: Add entries to `topics`
3. **Add new quotes**: Add to `quotes.general_writing` or create author-specific quote sections
4. **Add techniques**: Add to `techniques`
5. **Add genres**: Add to `genre_guidance`
6. **Add methodologies**: Add entries to `methodologies`

**No code changes needed** - just edit the JSON file and the MCP will use the new content immediately (after a Cursor restart if the server is running).

---

## 🔗 Integration with COMPASS

This MCP integrates seamlessly with the COMPASS Writing System:

- **Works with COMPASS Agents**: Agents can query this MCP for writing guidance
- **Complements Character MCP**: Character MCP handles character data; Writing Guides MCP handles writing craft
- **References Author Style Library**: Uses content from `Story_Bible/author-style-library.md`
- **Uses Commands Content**: Incorporates principles from `zz_COMPASS/Commands/`

---

## 🎨 Example Workflows

### Workflow 1: Writing a Dialogue Scene

1. Query: `Get guidance on dialogue`
2. Query: `Get Stephen King's advice on dialogue`
3. Write the scene using the guidance
4. Query: `Get techniques for dialogue`
5. Refine the scene using specific techniques

### Workflow 2: Adopting an Author's Style

1. Query: `Get Richard Russo's style guide`
2. Review prose style, narrative technique, themes
3. Query: `Get Russo's signature moves`
4. Apply the style to your scene
5. Query: `Get guidance on show_dont_tell` (to ensure authentic application)

### Workflow 3: Genre-Specific Writing

1. Query: `Get guidance for literary_fiction`
2. Review focus, pacing, key elements
3. Query: `Get representative authors` (to see examples)
4. Query: `Get [author]'s style guide` for reference
5. Write with genre conventions in mind

---

## 🚨 Troubleshooting

### "MCP server not found"
- Verify the path in `mcp.json` is absolute (not relative)
- Ensure you've restarted Cursor completely (Cmd+Q, then reopen)
- Check that `server.py` is executable: `chmod +x server.py`

### "Author not found"
- Check available authors: `Use compass-writing-guides MCP to list authors`
- Author names are case-sensitive (e.g., "Stephen King" not "stephen king")

### "Topic not found"
- Check available topics: `Use compass-writing-guides MCP to list topics`
- Topic names use underscores (e.g., "character_development" not "character development")

### Server errors
- Check that virtual environment is activated
- Verify MCP package is installed: `pip list | grep mcp`
- Check server.py is executable and has correct shebang: `#!/usr/bin/env python3`

---

## 📚 Sources & Credits

This MCP integrates content from:

- **Story_Bible/author-style-library.md** - Author style guides
- **zz_COMPASS/Commands/** - Writing techniques and commands
- **Stephen King: On Writing** - Writing principles and quotes
- **Anne Lamott: Bird by Bird** - Writing philosophy
- **Brandon Sanderson** - Craft-focused advice
- **Various master authors** - Style guides and techniques

---

## 🎉 DISCO DANCING IN HEAVEN!

This is a **pioneering MCP for fiction writing** - likely the first comprehensive Writing Guides MCP that integrates author advice, techniques, style guides, and genre guidance into a queryable database.

**What makes this special:**
- ✅ Queryable author advice and principles
- ✅ Comprehensive topic guidance
- ✅ Detailed author style guides
- ✅ Organized writing techniques
- ✅ Genre-specific guidance
- ✅ Searchable quotes
- ✅ Integrates with existing COMPASS system
- ✅ Easy to extend with new content

**This is a game-changer for your 10-novel contract!** 🚀

---

**COMPASS Writing System**  
**Created:** January 10, 2026  
**Version:** 1.0.0  
**Status:** Production Ready
