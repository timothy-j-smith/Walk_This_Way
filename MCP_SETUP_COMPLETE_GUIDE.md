# MCP SETUP COMPLETE GUIDE
## Complete Setup Instructions for All Active Arsenal MCPs

**Date:** January 24, 2026  
**Time:** 5:51 AM PST  
**Purpose:** Step-by-step guide to activate all MCPs in your active arsenal

---

## ✅ ALREADY CONFIGURED & READY (8 MCPs)

These MCPs are already in your configuration and ready to use:

1. ✅ **walk-this-way-files** (Filesystem MCP) - Active
2. ✅ **github** - Active (needs GITHUB_TOKEN env var)
3. ✅ **gitkraken** - Active
4. ✅ **duckduckgo-search** - Active
5. ✅ **sequential-thinking** (Base) - Active
6. ✅ **compass-writing-guides** - Active
7. ✅ **knowledge-graph-memory** - Active
8. ✅ **pandoc** - Active (but Pandoc not installed yet - see below)

---

## ⚠️ NEEDS API KEYS / SETUP (11 MCPs)

### 1. Firecrawl MCP ⭐⭐⭐⭐⭐ (ESSENTIAL)

**Status:** Configured but needs API key  
**Priority:** CRITICAL - PRIMARY research tool

**Setup Steps:**
1. Go to <https://firecrawl.dev/>
2. Sign up for account (free tier available)
3. Navigate to API Keys section
4. Copy your API key
5. Add to environment variables:
   ```bash
   export FIRECRAWL_API_KEY="your_key_here"
   ```
6. Add to your shell profile (`~/.zshrc`):
   ```bash
   echo 'export FIRECRAWL_API_KEY="your_key_here"' >> ~/.zshrc
   source ~/.zshrc
   ```
7. Restart Cursor

**Cost:** Free tier available, paid plans start at $20/month

---

### 2. Vectara MCP ⭐⭐⭐⭐⭐ (ESSENTIAL)

**Status:** Configured but needs API keys  
**Priority:** CRITICAL - Semantic search & RAG

**Setup Steps:**
1. Go to <https://vectara.com/>
2. Sign up for account (free tier available)
3. Create an environment (note the Environment ID)
4. Navigate to API Keys section
5. Create API key
6. Add to environment variables:
   ```bash
   export VECTARA_API_KEY="your_key_here"
   export VECTARA_ENV="your_environment_id"
   ```
7. Add to your shell profile (`~/.zshrc`):
   ```bash
   echo 'export VECTARA_API_KEY="your_key_here"' >> ~/.zshrc
   echo 'export VECTARA_ENV="your_environment_id"' >> ~/.zshrc
   source ~/.zshrc
   ```
8. Restart Cursor

**Cost:** Free tier available, paid plans available

---

### 3. Pandoc MCP ⭐⭐⭐⭐ (ESSENTIAL)

**Status:** Configured but Pandoc not installed  
**Priority:** ESSENTIAL - Document conversion

**Setup Steps:**
1. Install Pandoc via Homebrew:
   ```bash
   brew install pandoc
   ```
2. Verify installation:
   ```bash
   which pandoc
   pandoc --version
   ```
3. Restart Cursor

**Cost:** Free (open source)

---

### 4. GitHub MCP (Needs Token)

**Status:** Configured but needs GITHUB_TOKEN  
**Priority:** CRITICAL - Already have token, just needs env var

**Setup Steps:**
1. If you already have a GitHub token, add to environment:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```
2. If you need a new token:
   - Go to <https://github.com/settings/tokens>
   - Click "Generate new token (classic)"
   - Select scopes: `repo`, `read:org`, `read:user`
   - Copy token
   - Add to environment:
     ```bash
     export GITHUB_TOKEN="your_token_here"
     echo 'export GITHUB_TOKEN="your_token_here"' >> ~/.zshrc
     source ~/.zshrc
     ```
3. Restart Cursor

**Cost:** Free

---

## ⚠️ NEEDS PYTHON PACKAGES (3 MCPs)

### 5. Cognee MCP ⭐⭐⭐⭐⭐ (HIGHLY RECOMMENDED)

**Status:** Configured but needs Python package  
**Priority:** HIGHLY RECOMMENDED - Discovers hidden connections

**Setup Steps:**
1. Install Cognee:
   ```bash
   pip install cognee
   ```
2. Verify installation:
   ```bash
   python -c "import cognee; print('Cognee installed')"
   ```
3. Create data directory (already configured in mcp.json):
   ```bash
   mkdir -p "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cognee-data"
   ```
4. Restart Cursor

**Cost:** Free (open source)

---

### 6. UltraRAG ⭐⭐⭐⭐⭐ (HIGHLY RECOMMENDED)

**Status:** Configured but needs Python package  
**Priority:** HIGHLY RECOMMENDED - Custom-trains on your writing

**Setup Steps:**
1. Install UltraRAG:
   ```bash
   pip install ultrarag
   ```
2. Verify installation:
   ```bash
   python -c "import ultrarag; print('UltraRAG installed')"
   ```
3. Restart Cursor

**Cost:** Free (open source)

---

### 7. RAGentA ⭐⭐⭐⭐ (RECOMMENDED)

**Status:** ⚠️ **PACKAGE NOT AVAILABLE** - May need custom installation  
**Priority:** RECOMMENDED - Multi-agent verification

**Note:** RAGentA may not be available as a standard pip package. This MCP may need to be:
- Installed from source/GitHub repository
- Or disabled if package is not available

**Setup Steps:**
1. Check if RAGentA is available:
   ```bash
   pip search ragenta  # or check GitHub for RAGentA repository
   ```
2. If available, install from source or follow repository instructions
3. If not available, this MCP can be disabled in `mcp.json` by setting `"disabled": true`
4. Restart Cursor

**Cost:** Free (if available as open source)

---

## ⚠️ NEEDS CUSTOM INSTALLATION (1 MCP)

### 8. Style Emulation MCP ⭐⭐⭐⭐⭐ (HIGHLY RECOMMENDED)

**Status:** Code complete, needs installation  
**Priority:** HIGHLY RECOMMENDED - Style analysis & emulation

**Setup Steps:**
1. Create directory:
   ```bash
   mkdir -p ~/mcp-servers/style-emulation-mcp
   cd ~/mcp-servers/style-emulation-mcp
   ```

2. **Extract code from `REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md` PART III:**
   - The complete code is in the document starting at line 1639
   - You need to create these files:
     - `pyproject.toml`
     - `README.md`
     - `.env.example`
     - `install.sh`
     - `src/style_emulation/__init__.py`
     - `src/style_emulation/server.py`
     - `src/style_emulation/analyzer.py`
     - `src/style_emulation/transformer.py`
     - `src/style_emulation/database.py`

3. **Run installation:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

4. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

5. **Verify installation:**
   ```bash
   source venv/bin/activate
   python -m style_emulation.server --help
   ```

6. **Update MCP config path** (already done in mcp.json):
   - Path is set to: `/Users/timothy/mcp-servers/style-emulation-mcp/src`
   - Make sure this matches your installation

7. Restart Cursor

**Cost:** Free (requires ANTHROPIC_API_KEY)

---

## ✅ READY TO USE (No Setup Needed - 10 MCPs)

These MCPs are configured and will work immediately after restarting Cursor:

1. ✅ **sequential-thinking-mas** - Multi-Agent System Sequential Thinking
2. ✅ **sequential-thinking-ultra** - Bias detection & quality metrics
3. ✅ **enhanced-sequential-thinking** - 19 thinking modes
4. ✅ **memorygraph** - Ultra-efficient context optimization
5. ✅ **enhanced-mcp-memory** - Learns your prose DNA
6. ✅ **supermemory** - Cross-platform memory continuity
7. ✅ **scalemcp** - Intelligent MCP orchestration
8. ✅ **ai-writers-workshop** - Narrative-specific learning
9. ✅ **anki-flashcards** - Spaced repetition (needs Anki app installed separately)

---

## ⚠️ OPTIONAL - DISABLED BY DEFAULT (2 MCPs)

### 9. Google Workspace MCP ⭐⭐⭐ (OPTIONAL)

**Status:** Configured but disabled  
**Priority:** OPTIONAL - Cloud collaboration

**To Enable:**
1. Create Google Cloud project at <https://console.cloud.google.com/>
2. Enable Google Workspace API
3. Create OAuth 2.0 credentials
4. Add to environment:
   ```bash
   export GOOGLE_OAUTH_CLIENT_ID="your_client_id"
   export GOOGLE_OAUTH_CLIENT_SECRET="your_client_secret"
   ```
5. In `mcp.json`, change `"disabled": true` to `"disabled": false`
6. Restart Cursor

**Cost:** Free (requires Google account)

---

### 10. n8n MCP ⭐⭐⭐ (OPTIONAL)

**Status:** Configured but disabled  
**Priority:** OPTIONAL - Workflow automation

**To Enable:**
1. Install n8n (self-hosted): <https://n8n.io/>
2. Get API key from n8n instance
3. Add to environment:
   ```bash
   export N8N_API_KEY="your_api_key"
   ```
4. In `mcp.json`, change `"disabled": true` to `"disabled": false`
5. Restart Cursor

**Cost:** Free (self-hosted)

---

## 🚀 QUICK SETUP CHECKLIST

### Immediate Actions (Do Now):

- [ ] **Install Pandoc:** `brew install pandoc`
- [ ] **Get Firecrawl API key:** <https://firecrawl.dev/> → Add to env vars
- [ ] **Get Vectara API key:** <https://vectara.com/> → Add to env vars
- [ ] **Verify GitHub token:** Check if `GITHUB_TOKEN` is in env vars
- [ ] **Install Python packages:**
  - [ ] `pip install cognee`
  - [ ] `pip install ultrarag`
  - [ ] `pip install ragenta`
- [ ] **Set up Style Emulation MCP:** Extract code from document and install
- [ ] **Restart Cursor** after all setup

### After Setup:

- [ ] Test each MCP by asking Cursor to use them
- [ ] Verify environment variables are loaded
- [ ] Check Cursor MCP status panel

---

## 📋 ENVIRONMENT VARIABLES SUMMARY

Add these to your `~/.zshrc`:

```bash
# Firecrawl
export FIRECRAWL_API_KEY="your_key_here"

# Vectara
export VECTARA_API_KEY="your_key_here"
export VECTARA_ENV="your_environment_id"

# GitHub (if not already set)
export GITHUB_TOKEN="your_token_here"

# Anthropic (for Style Emulation MCP)
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

## ✅ VERIFICATION

After setup, verify MCPs are working:

1. **Restart Cursor completely**
2. **Open Cursor MCP panel** (usually in settings or status bar)
3. **Check each MCP status:**
   - Green = Active
   - Yellow = Needs setup
   - Red = Error (check logs)

4. **Test with a query:**
   - "Use Firecrawl to research 1970s Boston music scene"
   - "Use Vectara to search for scenes about Nick's grief"
   - "Use Sequential Thinking Ultra to analyze plot consistency"

---

## 📊 FINAL STATUS

**Total MCPs in Active Arsenal: 27**

- ✅ **Ready Now (8):** Filesystem, GitHub, GitKraken, DuckDuckGo, Sequential Thinking (Base), COMPASS, Knowledge Graph Memory, Pandoc (after install)
- ⚠️ **Needs API Keys (3):** Firecrawl, Vectara, GitHub Token
- ⚠️ **Needs Python Packages (3):** Cognee, UltraRAG, RAGentA
- ⚠️ **Needs Custom Install (1):** Style Emulation MCP
- ✅ **Ready After Restart (10):** All Sequential Thinking variants, Memory MCPs, ScaleMCP, AI Writers Workshop, Anki
- ⚠️ **Optional/Disabled (2):** Google Workspace, n8n

---

**Next Step:** Follow the checklist above, then restart Cursor and verify all MCPs are active!
