# Compass Intelligence Pipeline
## The Brain of Your Writing Ecosystem

**Command:** `/compass-intel` or `/intel` or `/pipeline`

**Action:** Shows the Compass Intelligence Pipeline status and available tools.

**Usage:** Type `/compass-intel` in Cursor Chat.

---

## Available Pipeline Commands

### Visualization
| Command | What It Does |
|---------|-------------|
| `/kg-viz` | Generate Mermaid diagram from Knowledge Graph |
| `/kg-viz characters` | Visualize only characters |
| `/kg-viz events` | Visualize only events |
| `/kg-viz themes` | Visualize only themes |

### Extraction
| Command | What It Does |
|---------|-------------|
| `/chapter-to-kg <file>` | Extract intelligence from chapter -> write to KG -> visualize |
| `/chapter-to-kg --dry-run <file>` | Preview extraction without writing |

### Prompt Engineering
| Command | What It Does |
|---------|-------------|
| `/intel patterns` | List all stored prompt engineering patterns |
| `/intel pattern xml_tags character_extraction` | Get a specific pattern |
| `/intel save-pattern` | Save a new prompt pattern |

### Pipeline Status
| Command | What It Does |
|---------|-------------|
| `/intel status` | Show pipeline status (chapters processed, patterns stored) |
| `/intel help` | Show full pipeline documentation |

---

## The 6-Step Pipeline

```
Chapter Text
    |
    v
[1] READ chapter file
    |
    v
[2] GENERATE extraction prompt (Compass Intelligence MCP)
    - XML tags for structured categories
    - Chain of Thought for reasoning
    - Few-shot examples for quality
    |
    v
[3] EXTRACT intelligence (Claude AI)
    - Characters, Locations, Events
    - Themes, Plot Threads, Craft Notes
    |
    v
[4] VALIDATE extraction (Compass Intelligence MCP)
    - Check entity format
    - Flag conflicts with existing KG
    |
    v
[5] WRITE to Knowledge Graph (Knowledge Graph Memory MCP)
    - create_entities for new items
    - add_observations for updates
    - create_relations for connections
    |
    v
[6] VISUALIZE (Compass Intelligence + Mermaid MCP)
    - Transform KG to Mermaid syntax
    - Generate color-coded diagram
    - Characters=red, Locations=teal
    - Events=blue, Themes=orange
```

---

## MCPs Used

| MCP | Role in Pipeline |
|-----|-----------------|
| **compass-intelligence** | Extraction prompts, KG->Mermaid transform, pattern library |
| **knowledge-graph-memory** | Persistent entity/relation storage |
| **mcp-mermaid** | Diagram generation |
| **sequential-thinking** | Complex reasoning when needed |
| **walkthisway-characters** | Character DNA cross-reference |

---

## Prompt Engineering Library

The Compass Intelligence MCP stores your prompt engineering patterns:

| Category | What It Stores |
|----------|---------------|
| **xml_tags** | Extraction tags like `<character_extraction>`, `<theme_extraction>` |
| **chain_of_thought** | Step-by-step reasoning templates |
| **context_pinning** | What to pin as reference context |
| **few_shot_examples** | Example extractions for quality |

Add new patterns anytime with `save_prompt_pattern`.

---

**Status:** Ready to Use
**MCPs Required:** compass-intelligence + knowledge-graph-memory + mcp-mermaid (all installed)
