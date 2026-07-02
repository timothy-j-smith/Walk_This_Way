# MCP SERVER SETUP INSTRUCTIONS
**Date:** January 10, 2026

---

## CURRENTLY CONFIGURED

### ✅ **Walk This Way Files**
- **Status:** Active
- **Purpose:** Filesystem access to project
- **No setup needed** - Works immediately

### ✅ **DuckDuckGo Search**
- **Status:** Active
- **Purpose:** Web search for research and fact-checking
- **No setup needed** - Works immediately

### ✅ **Sequential Thinking**
- **Status:** Active
- **Purpose:** Structured problem-solving for plot issues
- **No setup needed** - Works immediately

### ⚠️ **GitHub MCP**
- **Status:** Configured, needs token
- **Purpose:** Repository access, issue tracking
- **Setup Required:** 
  ```bash
  # Set GitHub token in environment
  export GITHUB_TOKEN="your_github_token_here"
  
  # Or add to ~/.zshrc for persistence:
  echo 'export GITHUB_TOKEN="your_github_token_here"' >> ~/.zshrc
  source ~/.zshrc
  ```
- **Get Token:** GitHub → Settings → Developer settings → Personal access tokens → Generate token (repo scope)

---

## NOT YET CONFIGURED

### ❌ **Google Drive MCP**
- **Status:** Deferred (complex OAuth setup)
- **Reason:** Requires OAuth authentication, more complex setup
- **Alternative:** Can access files via filesystem MCP if synced locally

### ❌ **Notion MCP**
- **Status:** Deferred
- **Setup:** Requires Notion API key
- **Can add later** if needed for documentation

---

## TESTING MCP SERVERS

After configuring, test by asking AI:
- "Search DuckDuckGo for [topic]"
- "Use sequential thinking to solve [problem]"
- "Show me GitHub repository info"

---

## NOTES

- **Most servers use npx** - Automatically downloads on first use
- **GitHub requires token** - Set environment variable
- **Google Drive/Notion** - More complex, can add later if needed
- **Restart Cursor** after adding new MCP servers

---

**Current Status:** 3 servers active (Files, DuckDuckGo, Sequential Thinking), GitHub configured (needs token)
