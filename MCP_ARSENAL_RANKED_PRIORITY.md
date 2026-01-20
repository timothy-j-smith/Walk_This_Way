# MCP ARSENAL - RANKED PRIORITY
## Forward Plan Only - Active Arsenal

**Date:** January 19, 2026  
**Time:** 2:12 PM  
**Purpose:** Lean, actionable list of MCPs in active arsenal, ranked from most critical to least critical, with setup status and activation instructions.

---

## TIER 1: CRITICAL - DO THIS NOW (Foundation)

### 1. Filesystem MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Foundation for all other MCPs  
**Setup:** Already active in `.cursor/config/mcp.json` as `walk-this-way-files`  
**Why Critical:** Enables all other MCPs to access your novel files. Without this, nothing works.

---

### 2. Knowledge Graph Memory MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Persistent memory for characters/plot  
**Setup:** Already active in `.cursor/config/mcp.json` as `knowledge-graph-memory`  
**Why Critical:** Stores all character details, relationships, plot threads. Essential for consistency across 10 independent novels.

---

### 3. Sequential Thinking MCP (Base) ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Step-by-step reasoning  
**Setup:** Already active in `.cursor/config/mcp.json` as `sequential-thinking`  
**Why Critical:** Makes implicit logic explicit. Essential for plot analysis and character consistency checks.

---

### 4. COMPASS Writing Guides MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Your writing system foundation  
**Setup:** Already active in `.cursor/config/mcp.json` as `compass-writing-guides`  
**Why Critical:** The heart of your writing system. Provides craft guidance, style rules, character development frameworks.

---

### 5. GitHub MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Version control  
**Setup:** Already active in `.cursor/config/mcp.json` as `github`  
**Why Critical:** Repository management, issue tracking, pull requests. Essential for professional workflow.

---

### 6. GitKraken MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** CRITICAL - Enhanced Git operations  
**Setup:** Already active in `.cursor/config/mcp.json` as `gitkraken`  
**Why Critical:** AI-powered commit messages, workspace management, multi-repo orchestration.

---

## TIER 2: ESSENTIAL - SET UP SOON (Core Functionality)

### 7. DuckDuckGo Search MCP ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Already configured  
**Priority:** ESSENTIAL - Quick reference research  
**Setup:** Already active in `.cursor/config/mcp.json` as `duckduckgo-search`  
**Why Essential:** Quick fact-checking during writing. Complements Firecrawl for rapid lookups.

---

### 8. Firecrawl MCP ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS API KEY**  
**Priority:** ESSENTIAL - PRIMARY research tool  
**Setup Instructions:**
1. Get API key from <https://firecrawl.dev/>
2. Add to `.cursor/config/mcp.json`:
```json
"firecrawl": {
  "command": "npx",
  "args": ["-y", "firecrawl-mcp"],
  "env": {
    "FIRECRAWL_API_KEY": "env:FIRECRAWL_API_KEY"
  },
  "disabled": false
}
```
3. Add `FIRECRAWL_API_KEY` to your environment variables
**Why Essential:** PRIMARY research tool for deep, comprehensive research dossiers. Firecrawl extracts full articles, scrapes entire websites, compiles multi-page research.

---

### 9. Vectara MCP ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS API KEY**  
**Priority:** ESSENTIAL - Semantic search & RAG  
**Setup Instructions:**
1. Create account at <https://vectara.com/> (free tier available)
2. Get API key and environment ID
3. Add to `.cursor/config/mcp.json`:
```json
"vectara": {
  "command": "npx",
  "args": ["-y", "vectara-mcp"],
  "env": {
    "VECTARA_API_KEY": "env:VECTARA_API_KEY",
    "VECTARA_ENV": "env:VECTARA_ENV"
  },
  "disabled": false
}
```
4. Add both environment variables
**Why Essential:** Semantic search across manuscripts. Finds content by meaning, not keywords. Essential for thematic analysis.

---

### 10. Pandoc MCP ⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS PANDOC INSTALLATION**  
**Priority:** ESSENTIAL - Document conversion  
**Setup Instructions:**
1. Install Pandoc: `brew install pandoc`
2. Verify: `which pandoc` (should show path)
3. Already configured in `.cursor/config/mcp.json` as `pandoc` - just needs Pandoc installed
**Why Essential:** Converts Markdown to DOCX, PDF, HTML. Essential for submission-ready manuscripts.

---

### 11. Dennis Lehane MCP (Custom) ⭐⭐⭐⭐⭐
**Status:** ✅ **READY TO GO** - Foundation complete  
**Priority:** ESSENTIAL - Style analysis for "Walk This Way"  
**Setup:** Already complete at `zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/`  
**Why Essential:** Private, confidential style guide specifically for "Walk This Way." Provides Boston grit, visceral descriptions, thematic depth.

---

## TIER 3: HIGHLY RECOMMENDED - ADD WHEN READY (Advanced Capabilities)

### 12. Sequential Thinking MAS (Multi-Agent System) ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Multi-perspective reasoning  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"sequential-thinking-mas": {
  "command": "npx",
  "args": ["-y", "@fradser/mcp-server-mas-sequential-thinking"],
  "disabled": false
}
```
**Why Recommended:** Multiple specialized agents (Factual, Emotional, Critical, Optimistic, Creative, Synthesis) analyze from different perspectives simultaneously.

---

### 13. Sequential Thinking Ultra ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Bias detection & quality metrics  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"sequential-thinking-ultra": {
  "command": "npx",
  "args": ["-y", "@sequential-thinking/ultra"],
  "disabled": false
}
```
**Why Recommended:** Detects cognitive biases, provides confidence scores, dynamic branching for complex plot analysis.

---

### 14. Enhanced Sequential Thinking (VitalyMalakanov) ⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** RECOMMENDED - 19 thinking modes  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"enhanced-sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@vitalymalakanov/mcp-enhanced-sequential-thinking"],
  "disabled": false
}
```
**Why Recommended:** Provides granular control over reasoning style (creative, evaluative, linear modes).

---

### 15. MemoryGraph MCP ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Ultra-efficient context optimization  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"memorygraph": {
  "command": "npx",
  "args": ["-y", "@memorygraph/mcp-server"],
  "disabled": false
}
```
**Why Recommended:** Uses only ~5% of token window for memory context. Solves the "context window problem" for long-form fiction.

---

### 16. enhanced-mcp-memory (cbunting99) ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Learns your prose DNA  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"enhanced-mcp-memory": {
  "command": "npx",
  "args": ["-y", "@cbunting99/enhanced-mcp-memory"],
  "disabled": false
}
```
**Why Recommended:** Learns your writing style, plot structures, workflow patterns. Maintains consistency automatically.

---

### 17. Supermemory MCP ⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** RECOMMENDED - Cross-platform memory continuity  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"supermemory": {
  "command": "npx",
  "args": ["-y", "@supermemory/mcp-server"],
  "disabled": false
}
```
**Why Recommended:** If you work across multiple AI tools (Cursor, Claude Desktop), this provides unified memory layer.

---

### 18. Zen MCP (Multi-Model Orchestration) ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP + API KEYS**  
**Priority:** HIGHLY RECOMMENDED - Routes tasks to optimal AI models  
**Setup Instructions:**
1. Get API keys: OpenAI (GPT-4), Google (Gemini), Anthropic (Claude)
2. Add to `.cursor/config/mcp.json`:
```json
"zen-orchestrator": {
  "command": "node",
  "args": ["/path/to/zen-mcp-server/index.js"],
  "env": {
    "OPENAI_API_KEY": "env:OPENAI_API_KEY",
    "GOOGLE_API_KEY": "env:GOOGLE_API_KEY",
    "ANTHROPIC_API_KEY": "env:ANTHROPIC_API_KEY"
  },
  "disabled": false
}
```
**Why Recommended:** Routes dialogue to GPT-4, analysis to Gemini, logic to O3. Each AI does what it does best.

---

### 19. Cognee MCP ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Discovers hidden connections  
**Setup Instructions:**
1. Install: `pip install cognee`
2. Add to `.cursor/config/mcp.json`:
```json
"cognee-connections": {
  "command": "python",
  "args": ["-m", "cognee_mcp"],
  "env": {
    "COGNEE_DATA_PATH": "/path/to/cognee-data"
  },
  "disabled": false
}
```
**Why Recommended:** Automatically discovers hidden plot connections you didn't consciously write. Revolutionary for thematic depth.

---

### 20. UltraRAG ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Custom-trains on your writing  
**Setup Instructions:**
1. Install: `pip install ultrarag`
2. Add to `.cursor/config/mcp.json`:
```json
"ultrarag": {
  "command": "python",
  "args": ["-m", "ultrarag"],
  "disabled": false
}
```
**Why Recommended:** Trains on "Walk This Way" manuscript, learns your writing patterns, optimizes retrieval specifically for your novel.

---

### 21. RAGentA ⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** RECOMMENDED - Multi-agent verification with citations  
**Setup Instructions:**
1. Install: `pip install ragenta`
2. Add to `.cursor/config/mcp.json`:
```json
"ragenta": {
  "command": "python",
  "args": ["-m", "ragenta"],
  "disabled": false
}
```
**Why Recommended:** Multiple agents verify answers with citations. Ensures thematic connections are traceable.

---

### 22. ScaleMCP ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** HIGHLY RECOMMENDED - Intelligent MCP orchestration  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"scalemcp": {
  "command": "npx",
  "args": ["-y", "@scalemcp/server"],
  "disabled": false
}
```
**Why Recommended:** Automatically routes tasks to optimal MCPs. Learns which MCPs to use when. Like having an AI that manages your AI tools.

---

### 23. Style Emulation MCP (Custom) ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS INSTALLATION** - Code complete, ready to install  
**Priority:** HIGHLY RECOMMENDED - Style analysis & emulation  
**Setup Instructions:**
1. **Location:** Complete implementation in `REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md` PART III (starts around line 1639)
2. **Files included:** `server.py`, `analyzer.py`, `transformer.py`, `database.py`, `pyproject.toml`, `install.sh`, `.env.example`, `README.md`
3. **Installation:**
   - Create directory: `mkdir -p ~/mcp-servers/style-emulation-mcp`
   - Copy all files from PART III
   - Run: `./install.sh`
   - Add ANTHROPIC_API_KEY to `.env`
   - Add to `.cursor/config/mcp.json`:
```json
"style-emulation": {
  "command": "python",
  "args": ["-m", "style_emulation.server"],
  "env": {
    "PYTHONPATH": "/path/to/style-emulation-mcp/src",
    "ANTHROPIC_API_KEY": "env:ANTHROPIC_API_KEY"
  },
  "disabled": false
}
```
**Why Recommended:** Comprehensive style analysis and emulation. Essential for maintaining Dennis Lehane-style consistency.

---

### 24. AI Writers Workshop MCP ⭐⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** RECOMMENDED - Narrative-specific learning  
**Setup Instructions:**
1. Add to `.cursor/config/mcp.json`:
```json
"ai-writers-workshop": {
  "command": "npx",
  "args": ["-y", "@ai-writers-workshop/mcp-server"],
  "disabled": false
}
```
**Why Recommended:** Learns your narrative patterns, character arcs, thematic structures. Narrative-specific analysis.

---

## TIER 4: OPTIONAL - ADD LATER (Nice to Have)

### 25. Google Workspace MCP ⭐⭐⭐
**Status:** ⚠️ **NEEDS OAUTH SETUP**  
**Priority:** OPTIONAL - Cloud collaboration  
**Setup Instructions:**
1. Create Google Cloud project
2. Set up OAuth credentials
3. Add to `.cursor/config/mcp.json`:
```json
"google_workspace": {
  "command": "uvx",
  "args": ["workspace-mcp"],
  "env": {
    "GOOGLE_OAUTH_CLIENT_ID": "env:GOOGLE_OAUTH_CLIENT_ID",
    "GOOGLE_OAUTH_CLIENT_SECRET": "env:GOOGLE_OAUTH_CLIENT_SECRET"
  },
  "disabled": false
}
```
**Why Optional:** Useful for cloud backups and collaboration, but not essential for solo writing.

---

### 26. Anki MCP ⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** OPTIONAL - Spaced repetition flashcards  
**Setup Instructions:**
1. Install Anki application: <https://apps.ankiweb.net/>
2. Install AnkiConnect addon
3. Add to `.cursor/config/mcp.json`:
```json
"anki-flashcards": {
  "command": "npx",
  "args": ["-y", "@anki/mcp-server"],
  "disabled": false
}
```
**Why Optional:** Useful for character memory reinforcement, but not essential if you have good memory systems.

---

### 27. n8n MCP ⭐⭐⭐
**Status:** ⚠️ **NEEDS SETUP**  
**Priority:** OPTIONAL - Workflow automation  
**Setup Instructions:**
1. Install n8n (self-hosted is free): <https://n8n.io/>
2. Add to `.cursor/config/mcp.json`:
```json
"workflow-automation": {
  "command": "npx",
  "args": ["-y", "@n8n/mcp-server"],
  "env": {
    "N8N_API_KEY": "env:N8N_API_KEY"
  },
  "disabled": false
}
```
**Why Optional:** Automates workflows (backups, notifications), but not essential for core writing.

---

## SUMMARY: SETUP PRIORITY

### ✅ Already Ready (6 MCPs):
1. Filesystem MCP
2. Knowledge Graph Memory MCP
3. Sequential Thinking MCP (Base)
4. COMPASS Writing Guides MCP
5. GitHub MCP
6. GitKraken MCP
7. DuckDuckGo Search MCP
8. Dennis Lehane MCP

### ⚠️ Needs Setup - Do Soon (5 MCPs):
1. Firecrawl MCP (needs API key)
2. Vectara MCP (needs API key)
3. Pandoc MCP (needs `brew install pandoc`)
4. Style Emulation MCP (code ready, needs installation)
5. Sequential Thinking Ultra (needs config)

### ⚠️ Needs Setup - Add When Ready (15 MCPs):
- Sequential Thinking MAS
- Enhanced Sequential Thinking
- MemoryGraph MCP
- enhanced-mcp-memory
- Supermemory MCP
- Zen MCP (needs API keys)
- Cognee MCP
- UltraRAG
- RAGentA
- ScaleMCP
- AI Writers Workshop MCP

### ⚠️ Optional - Add Later (3 MCPs):
- Google Workspace MCP
- Anki MCP
- n8n MCP

---

## NON-ESSENTIAL MCPs (Covered by Others)

These MCPs are marked as non-essential because their functionality is covered by other MCPs in the arsenal:

- **RAGVUE** - Diagnostic tool, not essential for daily writing (moved to archive)
- **PiloTY** - Infrastructure automation, not essential for core writing (moved to archive)
- **Spotify MCP** - Music control, not essential for writing (moved to archive)
- **Airtable MCP** - Project management, not essential (moved to archive)

---

**Total Active Arsenal MCPs: 27**  
**Ready to Use: 8**  
**Needs Setup: 19**

---

*This document focuses on forward plan only. For complete documentation including archive shelf, see `REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md`.*
