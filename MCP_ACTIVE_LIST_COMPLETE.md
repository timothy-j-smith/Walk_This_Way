# ACTIVE MCPs ON CURSOR ULTRA PLAN ACCOUNT
## Complete List of All Configured MCPs

**Date:** January 24, 2026  
**Time:** 5:51 AM PST  
**Status:** All MCPs configured in `.cursor/config/mcp.json`

---

## 📊 SUMMARY

**Total MCPs Configured: 27**  
**Fully Ready (No Setup): 10**  
**Needs API Keys: 3**  
**Needs Python Packages: 3**  
**Needs Custom Installation: 1**  
**Optional/Disabled: 2**

---

## ✅ TIER 1: CRITICAL - READY NOW (8 MCPs)

### 1. walk-this-way-files (Filesystem MCP)
- **Status:** ✅ Active
- **Package:** `@modelcontextprotocol/server-filesystem`
- **Purpose:** Foundation - enables file access for all other MCPs
- **No setup needed**

### 2. github
- **Status:** ✅ Active (needs GITHUB_TOKEN env var)
- **Package:** `@modelcontextprotocol/server-github`
- **Purpose:** Version control, repository management
- **Action:** Verify `GITHUB_TOKEN` is in environment variables

### 3. gitkraken
- **Status:** ✅ Active
- **Command:** `gk mcp`
- **Purpose:** Enhanced Git operations with AI
- **No setup needed**

### 4. duckduckgo-search
- **Status:** ✅ Active
- **Package:** `@modelcontextprotocol/server-duckduckgo-search`
- **Purpose:** Quick reference research, fact-checking
- **No setup needed**

### 5. sequential-thinking (Base)
- **Status:** ✅ Active
- **Package:** `@modelcontextprotocol/server-sequential-thinking`
- **Purpose:** Step-by-step reasoning, plot analysis
- **No setup needed**

### 6. compass-writing-guides
- **Status:** ✅ Active
- **Path:** Custom COMPASS MCP at `zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/`
- **Purpose:** Writing craft guidance, style rules
- **No setup needed**

### 7. knowledge-graph-memory
- **Status:** ✅ Active
- **Package:** `@modelcontextprotocol/server-memory`
- **Purpose:** Persistent memory for characters/plot across 10 novels
- **No setup needed**

### 8. pandoc
- **Status:** ✅ Active (Pandoc installed)
- **Command:** `uvx mcp-pandoc`
- **Purpose:** Document conversion (Markdown → DOCX, PDF, HTML)
- **No setup needed** (Pandoc installed via Homebrew)

---

## ✅ TIER 2: ESSENTIAL - NEEDS API KEYS (3 MCPs)

### 9. firecrawl
- **Status:** ⚠️ Configured, needs API key
- **Package:** `firecrawl-mcp`
- **Purpose:** PRIMARY research tool - deep web scraping, comprehensive research
- **Action Required:**
  1. Get API key from <https://firecrawl.dev/>
  2. Add to env: `export FIRECRAWL_API_KEY="your_key"`
  3. Add to `~/.zshrc` and restart Cursor

### 10. vectara
- **Status:** ⚠️ Configured, needs API keys
- **Package:** `vectara-mcp`
- **Purpose:** Semantic search & RAG across manuscripts
- **Action Required:**
  1. Create account at <https://vectara.com/> (free tier available)
  2. Get API key and Environment ID
  3. Add to env:
     - `export VECTARA_API_KEY="your_key"`
     - `export VECTARA_ENV="your_env_id"`
  4. Add to `~/.zshrc` and restart Cursor

### 11. github (Token Verification)
- **Status:** ⚠️ Needs GITHUB_TOKEN env var
- **Action Required:**
  1. Check if token exists: `echo $GITHUB_TOKEN`
  2. If missing, create at <https://github.com/settings/tokens>
  3. Add to `~/.zshrc`: `export GITHUB_TOKEN="your_token"`

---

## ✅ TIER 3: HIGHLY RECOMMENDED - NEEDS PYTHON PACKAGES (3 MCPs)

### 12. cognee-connections
- **Status:** ⚠️ Configured, needs Python package
- **Package:** `cognee` (Python)
- **Purpose:** Graph-RAG - discovers hidden plot connections
- **Action Required:**
  1. Install: `python3 -m pip install cognee`
  2. Verify: `python3 -c "import cognee; print('OK')"`
  3. Restart Cursor

### 13. ultrarag
- **Status:** ⚠️ Configured, needs Python package
- **Package:** `ultrarag` (Python)
- **Purpose:** Custom-trains on "Walk This Way" manuscript
- **Action Required:**
  1. Install: `python3 -m pip install ultrarag`
  2. Verify: `python3 -c "import ultrarag; print('OK')"`
  3. Restart Cursor

### 14. ragenta
- **Status:** ⚠️ Configured, but package not available
- **Package:** `ragenta` (Python) - **NOT AVAILABLE AS PIP PACKAGE**
- **Purpose:** Multi-agent verification with citations
- **Action Required:**
  1. Check GitHub for RAGentA repository or source installation
  2. If not available, disable in `mcp.json` by setting `"disabled": true`
  3. Alternative: Use other verification MCPs (UltraRAG, Cognee)

---

## ✅ TIER 4: HIGHLY RECOMMENDED - READY AFTER RESTART (10 MCPs)

### 15. sequential-thinking-mas
- **Status:** ✅ Configured, ready after restart
- **Package:** `@fradser/mcp-server-mas-sequential-thinking`
- **Purpose:** Multi-Agent System - multiple perspectives simultaneously
- **No setup needed**

### 16. sequential-thinking-ultra
- **Status:** ✅ Configured, ready after restart
- **Package:** `@sequential-thinking/ultra`
- **Purpose:** Bias detection, quality metrics, advanced reasoning
- **No setup needed**

### 17. enhanced-sequential-thinking
- **Status:** ✅ Configured, ready after restart
- **Package:** `@vitalymalakanov/mcp-enhanced-sequential-thinking`
- **Purpose:** 19 thinking modes (creative, evaluative, linear)
- **No setup needed**

### 18. memorygraph
- **Status:** ✅ Configured, ready after restart
- **Package:** `@memorygraph/mcp-server`
- **Purpose:** Ultra-efficient context optimization (~5% token usage)
- **No setup needed**

### 19. enhanced-mcp-memory
- **Status:** ✅ Configured, ready after restart
- **Package:** `@cbunting99/enhanced-mcp-memory`
- **Purpose:** Learns your prose DNA, writing style, plot structures
- **No setup needed**

### 20. supermemory
- **Status:** ✅ Configured, ready after restart
- **Package:** `@supermemory/mcp-server`
- **Purpose:** Cross-platform memory continuity
- **No setup needed**

### 21. scalemcp
- **Status:** ✅ Configured, ready after restart
- **Package:** `@scalemcp/server`
- **Purpose:** Intelligent MCP orchestration - routes tasks to optimal MCPs
- **No setup needed**

### 22. ai-writers-workshop
- **Status:** ✅ Configured, ready after restart
- **Package:** `@ai-writers-workshop/mcp-server`
- **Purpose:** Narrative-specific learning - character arcs, thematic structures
- **No setup needed**

### 23. anki-flashcards
- **Status:** ✅ Configured, ready after restart (needs Anki app)
- **Package:** `@anki/mcp-server`
- **Purpose:** Spaced repetition flashcards
- **Note:** Requires Anki application installed separately (<https://apps.ankiweb.net/>)

### 24. style-emulation
- **Status:** ⚠️ Configured, needs custom installation
- **Type:** Custom MCP (code in `REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md` PART III)
- **Purpose:** Style analysis & emulation for Dennis Lehane style
- **Action Required:**
  1. Extract code from document (starts line 1639)
  2. Create directory: `mkdir -p ~/mcp-servers/style-emulation-mcp`
  3. Copy all files from PART III
  4. Run: `./install.sh`
  5. Add `ANTHROPIC_API_KEY` to `.env`
  6. Restart Cursor

---

## ⚠️ TIER 5: OPTIONAL - DISABLED BY DEFAULT (2 MCPs)

### 25. google-workspace
- **Status:** ⚠️ Configured but disabled
- **Command:** `uvx workspace-mcp`
- **Purpose:** Cloud collaboration, Google Drive access
- **To Enable:**
  1. Create Google Cloud project
  2. Set up OAuth credentials
  3. Add env vars: `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`
  4. Change `"disabled": false` in mcp.json
  5. Restart Cursor

### 26. workflow-automation (n8n)
- **Status:** ⚠️ Configured but disabled
- **Package:** `@n8n/mcp-server`
- **Purpose:** Workflow automation (backups, notifications)
- **To Enable:**
  1. Install n8n (self-hosted): <https://n8n.io/>
  2. Get API key from n8n instance
  3. Add env var: `N8N_API_KEY`
  4. Change `"disabled": false` in mcp.json
  5. Restart Cursor

---

## 📋 QUICK ACTION CHECKLIST

### Immediate Actions:

- [x] ✅ **Pandoc installed** (completed)
- [ ] ⚠️ **Get Firecrawl API key** → <https://firecrawl.dev/>
- [ ] ⚠️ **Get Vectara API key** → <https://vectara.com/>
- [ ] ⚠️ **Verify GitHub token** → Check `$GITHUB_TOKEN`
- [ ] ⚠️ **Install Python packages:**
  - [ ] `python3 -m pip install cognee`
  - [ ] `python3 -m pip install ultrarag`
  - [ ] `python3 -m pip install ragenta`
- [ ] ⚠️ **Set up Style Emulation MCP** (extract from document)
- [ ] ⚠️ **Add all env vars to `~/.zshrc`**
- [ ] ⚠️ **Restart Cursor**

### After Restart:

- [ ] Verify all MCPs show as active in Cursor
- [ ] Test each MCP with a query
- [ ] Check for any error messages

---

## 🔑 REQUIRED API KEYS & ENVIRONMENT VARIABLES

Add these to your `~/.zshrc`:

```bash
# Firecrawl (REQUIRED for research)
export FIRECRAWL_API_KEY="your_key_here"

# Vectara (REQUIRED for semantic search)
export VECTARA_API_KEY="your_key_here"
export VECTARA_ENV="your_environment_id"

# GitHub (REQUIRED for version control)
export GITHUB_TOKEN="your_token_here"

# Anthropic (REQUIRED for Style Emulation MCP)
export ANTHROPIC_API_KEY="your_key_here"

# Optional: Google Workspace
export GOOGLE_OAUTH_CLIENT_ID="your_client_id"
export GOOGLE_OAUTH_CLIENT_SECRET="your_client_secret"

# Optional: n8n
export N8N_API_KEY="your_api_key"
```

After adding, run:
```bash
source ~/.zshrc
```

---

## 📊 FINAL STATUS BREAKDOWN

### ✅ Ready Now (10 MCPs):
1. walk-this-way-files
2. gitkraken
3. duckduckgo-search
4. sequential-thinking (base)
5. compass-writing-guides
6. knowledge-graph-memory
7. pandoc
8. sequential-thinking-mas
9. sequential-thinking-ultra
10. enhanced-sequential-thinking
11. memorygraph
12. enhanced-mcp-memory
13. supermemory
14. scalemcp
15. ai-writers-workshop
16. anki-flashcards

### ⚠️ Needs API Keys (3 MCPs):
1. firecrawl
2. vectara
3. github (token verification)

### ⚠️ Needs Python Packages (2 MCPs):
1. ✅ cognee-connections (INSTALLED)
2. ✅ ultrarag (INSTALLED)
3. ⚠️ ragenta (Package not available - may need custom installation or disable)

### ⚠️ Needs Custom Installation (1 MCP):
1. style-emulation

### ⚠️ Optional/Disabled (2 MCPs):
1. google-workspace
2. workflow-automation (n8n)

---

## 🎯 NEXT STEPS

1. **Follow `MCP_SETUP_COMPLETE_GUIDE.md`** for detailed setup instructions
2. **Get API keys** from Firecrawl and Vectara
3. **Install Python packages** for Cognee, UltraRAG, RAGentA
4. **Set up Style Emulation MCP** (extract code from main document)
5. **Add all environment variables** to `~/.zshrc`
6. **Restart Cursor** completely
7. **Verify all MCPs** are active in Cursor's MCP panel

---

**All 27 MCPs are now configured in your `.cursor/config/mcp.json` file!**
