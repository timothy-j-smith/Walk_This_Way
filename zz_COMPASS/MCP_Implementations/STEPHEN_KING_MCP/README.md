# Stephen King MCP — "The Writer's Toolbox"

**PRIVATE & CONFIDENTIAL — For Timothy and Claude's Use Only**

A craft philosophy educational engine built on Stephen King's *On Writing: A Memoir of the Craft*, designed as a companion to Timothy's A.B.S.H. writing system.

## 3-3-3 Architecture

### 3 Tools

| Tool | Function | A.B.S.H. Phase |
|------|----------|----------------|
| `king_imagine` | Situations, stakes, fear, planning | Architecture |
| `king_craft` | Voice, pacing, telepathy, building | Brick |
| `king_revise` | Cutting and adding | Scalpel & Hose |

### 3 Modes

| Mode | What It Does | Default Level |
|------|-------------|---------------|
| `create` | Idea → story | Nice |
| `transform` | Draft → better draft | Neutral |
| `edit` | Chapters → mastery | Professional |

### 3 Liberty Levels

| Level | When to Use |
|-------|------------|
| `nice` | Early ideas, first drafts, fragile moments |
| `neutral` | Middle drafts, working sessions |
| `professional` | Final drafts, pre-submission |

## Setup

```bash
cd zz_COMPASS/MCP_Implementations/STEPHEN_KING_MCP
bash setup.sh
```

Or manually:

```bash
python3 -m venv venv
venv/bin/pip install mcp
```

## Cursor MCP Configuration

Add to your Cursor MCP settings:

```json
{
  "mcpServers": {
    "stephen-king-toolbox": {
      "command": "/path/to/STEPHEN_KING_MCP/venv/bin/python",
      "args": ["/path/to/STEPHEN_KING_MCP/server.py"]
    }
  }
}
```

## Usage Examples

- "King Create" — nurture an early idea (nice by default)
- "King Transform" — quick polish a paragraph (neutral by default)
- "King Edit Professional" — full rigorous chapter review
- "King Create Professional" — rigorous planning, no hand-holding
- "King Edit Nice" — deep review with encouragement first

## Files

```
STEPHEN_KING_MCP/
├── STEPHEN_KING_MCP_DESIGN.md    ← Design document
├── server.py                      ← MCP server (3 tools)
├── data/
│   └── king_analysis.json         ← King craft knowledge base
├── requirements.txt               ← Dependencies
├── setup.sh                       ← Automated setup
└── README.md                      ← This file
```
