# MCP ADDITIONS REQUIRED
## Two Critical MCPs Missing from Configuration

**Date:** January 24, 2026  
**Time:** Current  
**Status:** Identified 2 critical MCPs that need to be added

---

## ✅ MCPs ADDED TO CONFIGURATION

Both MCPs have been added to `.cursor/config/mcp.json`:

1. ✅ **zen-orchestrator** - Added (needs repository clone + API keys)
2. ✅ **dennis-lehane-style** - Added (needs server.py creation)

---

## ⚠️ SETUP REQUIRED

### 1. Zen MCP Setup

**Status:** Added to mcp.json, needs installation

**Steps:**
1. **Clone Repository:**
   ```bash
   mkdir -p ~/mcp-servers
   cd ~/mcp-servers
   git clone https://github.com/BeehiveInnovations/zen-mcp-server.git
   cd zen-mcp-server
   npm install
   ```

2. **Get API Keys:**
   - **OpenAI:** <https://platform.openai.com/> → API Keys → Create new key
   - **Google:** <https://ai.google.dev/> → Get API key
   - **Anthropic:** Already have (verify it's in environment)

3. **Add to Environment:**
   ```bash
   export OPENAI_API_KEY="your_openai_key"
   export GOOGLE_API_KEY="your_google_key"
   export ANTHROPIC_API_KEY="your_anthropic_key"
   ```
   Add to `~/.zshrc` and run `source ~/.zshrc`

4. **Verify Path:**
   - Current path in mcp.json: `/Users/timothy/mcp-servers/zen-mcp-server/index.js`
   - Adjust if repository is cloned to different location

---

### 2. Dennis Lehane MCP Setup

**Status:** Added to mcp.json, needs server.py creation

**Current State:**
- ✅ Data exists: `zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/data/lehane_analysis.json`
- ⚠️ Server missing: `server.py` needs to be created

**Steps:**
1. **Create server.py** (based on COMPASS Writing Guides MCP structure)
2. **Location:** `zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/server.py`
3. **Purpose:** Provide MCP interface to `lehane_analysis.json` data

**Note:** I can create the server.py file for you if you'd like, using the COMPASS Writing Guides MCP as a template.

---

## 📊 FINAL STATUS

**Total MCPs in Configuration:** 27 (25 existing + 2 new)

**Ready to Use:** 23 MCPs  
**Needs Setup:** 4 MCPs
- Zen MCP (needs repository clone + API keys)
- Dennis Lehane MCP (needs server.py creation)
- Firecrawl (needs API key)
- Vectara (needs API keys)

---

**Next Steps:**
1. Clone Zen MCP repository
2. Get API keys for Zen MCP
3. Create Dennis Lehane MCP server.py (or ask me to create it)
4. Get Firecrawl and Vectara API keys
5. Restart Cursor
