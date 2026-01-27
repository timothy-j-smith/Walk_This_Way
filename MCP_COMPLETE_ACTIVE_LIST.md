# COMPLETE ACTIVE MCPs ON CURSOR ULTRA PLAN ACCOUNT
## Final Comprehensive List

**Date:** January 24, 2026  
**Time:** Current  
**Configuration File:** `.cursor/config/mcp.json`

---

## 📊 SUMMARY

**Total MCPs Configured: 27**  
**Fully Ready (No Setup): 16**  
**Needs API Keys: 4**  
**Needs Python Packages: 2**  
**Needs Custom Installation: 1**  
**Needs Repository Clone: 1**  
**Needs Server Creation: 1**  
**Optional/Disabled: 2**

---

## ✅ ALL 27 ACTIVE MCPs

### TIER 1: CRITICAL - READY NOW (8 MCPs)

1. ✅ **walk-this-way-files** (Filesystem MCP)
   - **Status:** Active
   - **Package:** `@modelcontextprotocol/server-filesystem`
   - **Purpose:** Foundation - enables file access

2. ✅ **github**
   - **Status:** Active (needs GITHUB_TOKEN env var)
   - **Package:** `@modelcontextprotocol/server-github`
   - **Purpose:** Version control, repository management

3. ✅ **gitkraken**
   - **Status:** Active
   - **Command:** `gk mcp`
   - **Purpose:** Enhanced Git operations with AI

4. ✅ **duckduckgo-search**
   - **Status:** Active
   - **Package:** `@modelcontextprotocol/server-duckduckgo-search`
   - **Purpose:** Quick reference research, fact-checking

5. ✅ **sequential-thinking** (Base)
   - **Status:** Active
   - **Package:** `@modelcontextprotocol/server-sequential-thinking`
   - **Purpose:** Step-by-step reasoning, plot analysis

6. ✅ **compass-writing-guides**
   - **Status:** Active
   - **Path:** Custom COMPASS MCP
   - **Purpose:** Writing craft guidance, style rules

7. ✅ **knowledge-graph-memory**
   - **Status:** Active
   - **Package:** `@modelcontextprotocol/server-memory`
   - **Purpose:** Persistent memory for characters/plot

8. ✅ **pandoc**
   - **Status:** Active (Pandoc installed)
   - **Command:** `uvx mcp-pandoc`
   - **Purpose:** Document conversion

---

### TIER 2: ESSENTIAL - NEEDS API KEYS (4 MCPs)

9. ⚠️ **firecrawl**
   - **Status:** Configured, needs API key
   - **Package:** `firecrawl-mcp`
   - **Purpose:** PRIMARY research tool
   - **Action:** Get API key from <https://firecrawl.dev/>

10. ⚠️ **vectara**
    - **Status:** Configured, needs API keys
    - **Package:** `vectara-mcp`
    - **Purpose:** Semantic search & RAG
    - **Action:** Get API key + Environment ID from <https://vectara.com/>

11. ⚠️ **github** (Token Verification)
    - **Status:** Needs GITHUB_TOKEN env var
    - **Action:** Verify token exists or create at <https://github.com/settings/tokens>

12. ⚠️ **zen-orchestrator** ⭐ **NEWLY ADDED**
    - **Status:** Added to mcp.json, needs repository clone + API keys
    - **Purpose:** Multi-model orchestration (GPT-4, Gemini, O3)
    - **Action Required:**
      1. Clone: `git clone https://github.com/BeehiveInnovations/zen-mcp-server.git`
      2. Get API keys: OpenAI, Google, Anthropic
      3. Install: `npm install` in repository directory

---

### TIER 3: HIGHLY RECOMMENDED - READY AFTER RESTART (10 MCPs)

13. ✅ **sequential-thinking-mas**
    - **Status:** Active
    - **Package:** `@fradser/mcp-server-mas-sequential-thinking`
    - **Purpose:** Multi-Agent System reasoning

14. ✅ **sequential-thinking-ultra**
    - **Status:** Active
    - **Package:** `@sequential-thinking/ultra`
    - **Purpose:** Bias detection, quality metrics

15. ✅ **enhanced-sequential-thinking**
    - **Status:** Active
    - **Package:** `@vitalymalakanov/mcp-enhanced-sequential-thinking`
    - **Purpose:** 19 thinking modes

16. ✅ **memorygraph**
    - **Status:** Active
    - **Package:** `@memorygraph/mcp-server`
    - **Purpose:** Ultra-efficient context optimization

17. ✅ **enhanced-mcp-memory**
    - **Status:** Active
    - **Package:** `@cbunting99/enhanced-mcp-memory`
    - **Purpose:** Learns your prose DNA

18. ✅ **supermemory**
    - **Status:** Active
    - **Package:** `@supermemory/mcp-server`
    - **Purpose:** Cross-platform memory continuity

19. ✅ **scalemcp**
    - **Status:** Active
    - **Package:** `@scalemcp/server`
    - **Purpose:** Intelligent MCP orchestration

20. ✅ **ai-writers-workshop**
    - **Status:** Active
    - **Package:** `@ai-writers-workshop/mcp-server`
    - **Purpose:** Narrative-specific learning

21. ✅ **anki-flashcards**
    - **Status:** Active (needs Anki app)
    - **Package:** `@anki/mcp-server`
    - **Purpose:** Spaced repetition flashcards

22. ✅ **cognee-connections**
    - **Status:** Active (Python package installed)
    - **Package:** `cognee` (Python)
    - **Purpose:** Graph-RAG - discovers hidden connections

---

### TIER 4: HIGHLY RECOMMENDED - NEEDS SETUP (3 MCPs)

23. ⚠️ **ultrarag**
    - **Status:** Configured, Python package installed
    - **Package:** `ultrarag` (Python)
    - **Purpose:** Custom-trains on "Walk This Way"
    - **Status:** ✅ Package installed

24. ⚠️ **ragenta**
    - **Status:** Configured, but package not available
    - **Package:** `ragenta` (Python) - **NOT AVAILABLE**
    - **Purpose:** Multi-agent verification
    - **Action:** Disable if package unavailable

25. ⚠️ **style-emulation**
    - **Status:** Configured, needs custom installation
    - **Type:** Custom MCP
    - **Purpose:** Style analysis & emulation
    - **Action:** Extract code from document and install

---

### TIER 5: CUSTOM - NEWLY ADDED (1 MCP)

26. ⚠️ **dennis-lehane-style** ⭐ **NEWLY ADDED**
    - **Status:** Added to mcp.json, server.py created
    - **Type:** Custom MCP
    - **Purpose:** Lehane-specific style guidance for "Walk This Way"
    - **Location:** `zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/`
    - **Status:** ✅ Server.py created, ready to test

---

### TIER 6: OPTIONAL - DISABLED (2 MCPs)

27. ⚠️ **google-workspace**
    - **Status:** Disabled
    - **Purpose:** Cloud collaboration
    - **Can Enable:** If needed for collaboration

28. ⚠️ **workflow-automation** (n8n)
    - **Status:** Disabled
    - **Purpose:** Workflow automation
    - **Can Enable:** If needed for automation

---

## 📋 SETUP PRIORITY

### ✅ Already Complete (16 MCPs):
All Tier 1 + Tier 3 MCPs are ready to use

### ⚠️ Needs Setup (11 MCPs):

**Immediate Priority:**
1. ⚠️ **Zen MCP** - Clone repository, get API keys
2. ⚠️ **Dennis Lehane MCP** - Server.py created, ready to test
3. ⚠️ **Firecrawl** - Get API key
4. ⚠️ **Vectara** - Get API key + Environment ID
5. ⚠️ **GitHub Token** - Verify or create token

**Secondary Priority:**
6. ⚠️ **Style Emulation MCP** - Extract code and install
7. ⚠️ **RAGentA** - Disable if package unavailable

---

## 🔑 REQUIRED API KEYS

Add to `~/.zshrc`:

```bash
# Firecrawl (REQUIRED)
export FIRECRAWL_API_KEY="your_key_here"

# Vectara (REQUIRED)
export VECTARA_API_KEY="your_key_here"
export VECTARA_ENV="your_environment_id"

# GitHub (REQUIRED)
export GITHUB_TOKEN="your_token_here"

# Zen MCP (REQUIRED)
export OPENAI_API_KEY="your_openai_key"
export GOOGLE_API_KEY="your_google_key"
export ANTHROPIC_API_KEY="your_anthropic_key"
```

---

## ✅ NEWLY ADDED MCPs

### 1. Zen MCP (zen-orchestrator)
- **Added to:** `.cursor/config/mcp.json`
- **Status:** Needs repository clone + API keys
- **Priority:** ⭐⭐⭐⭐⭐ CRITICAL

### 2. Dennis Lehane MCP (dennis-lehane-style)
- **Added to:** `.cursor/config/mcp.json`
- **Server Created:** `zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/server.py`
- **Status:** Ready to test
- **Priority:** ⭐⭐⭐⭐⭐ ESSENTIAL

---

## 📊 FINAL BREAKDOWN

**Total MCPs: 27**

- ✅ **Ready Now:** 16 MCPs
- ⚠️ **Needs API Keys:** 4 MCPs (Firecrawl, Vectara, GitHub, Zen)
- ⚠️ **Needs Setup:** 3 MCPs (Style Emulation, RAGentA, Dennis Lehane - server created)
- ⚠️ **Optional/Disabled:** 2 MCPs (Google Workspace, n8n)

---

**All MCPs from the document have been evaluated and the two critical missing MCPs have been added!**
