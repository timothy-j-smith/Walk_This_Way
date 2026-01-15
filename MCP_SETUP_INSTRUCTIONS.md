# MCP Server Setup & Management Guide
**Date:** January 12, 2026  
**Purpose:** Complete guide to setting up and managing MCP servers for Walk This Way

---

## 🎯 Quick Reference: Enable/Disable MCP Servers

**To disable an MCP server:** Add `"disabled": true` to its config  
**To enable an MCP server:** Set `"disabled": false` or remove the disabled field  
**Config location:** `.cursor/config/mcp.json` (project) or `~/.cursor/mcp.json` (global)

---

## 📋 Current MCP Servers

### ✅ ACTIVE (disabled: false)
1. **walk-this-way-files** - Filesystem access to your novel files

### 🔴 CONFIGURED BUT DISABLED (disabled: true)
2. **github** - GitHub repository access
3. **gitkraken** - GitKraken git operations
4. **duckduckgo-search** - Web search for research
5. **sequential-thinking** - Structured problem-solving
6. **compass-writing-guides** - Custom COMPASS writing guides

---

## 🛠️ Setup Instructions

### 1. Install GitKraken CLI

**Option A: Direct Install (Recommended)**
```bash
curl -o- https://cli.gitkraken.com/install.sh | sh
```

**Option B: Homebrew**
```bash
brew install gitkraken-cli
```

**Verify Installation:**
```bash
which gk
# Should show: /Users/timothy/.local/bin/gk (or similar)
```

**Authenticate:**
```bash
gk auth login
```

---

### 2. Set Up GitHub Token

**Create GitHub Personal Access Token:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `read:user`, `read:org`
4. Copy the token (starts with `ghp_`)

**Set Environment Variable:**

Add to your `~/.zshrc` (or `~/.bash_profile` if using bash):
```bash
export GITHUB_TOKEN="ghp_YOUR_TOKEN_HERE"
```

**Apply Changes:**
```bash
source ~/.zshrc
```

**Verify:**
```bash
echo $GITHUB_TOKEN
# Should show your token
```

---

### 3. Update MCP Configuration

The configuration is already set up in:
- **Project:** `.cursor/config/mcp.json`
- **Global:** `~/.cursor/mcp.json` (optional backup)

**All servers are disabled by default except `walk-this-way-files`.**

---

## 🎮 How to Enable/Disable MCP Servers

### Method 1: Edit Config File Directly

**To enable GitHub MCP:**
```json
"github": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-github",
    "--token",
    "env:GITHUB_TOKEN"
  ],
  "disabled": false  // ← Change this
}
```

**To disable GitKraken MCP:**
```json
"gitkraken": {
  "command": "gk",
  "args": ["mcp"],
  "disabled": true  // ← Change this
}
```

### Method 2: Comment Out (Alternative)

You can also comment out entire server blocks:
```json
{
  "mcpServers": {
    "walk-this-way-files": {
      "command": "npx",
      "args": ["..."]
    }
    // "github": {
    //   "command": "npx",
    //   "args": ["..."]
    // }
  }
}
```

---

## 🧪 Testing MCP Servers

### Test GitKraken MCP
1. Enable GitKraken in config (`"disabled": false`)
2. Restart Cursor
3. Ask AI: "Show me recent git commits"

### Test GitHub MCP
1. Enable GitHub in config (`"disabled": false`)
2. Restart Cursor
3. Ask AI: "Show me the README from timothy-j-smith/Walk_This_Way"

### Test DuckDuckGo Search
1. Enable duckduckgo-search in config
2. Restart Cursor
3. Ask AI: "Search for disco music in 1979"

---

## 📊 Recommended MCP Profiles

### Profile 1: Writing Mode (Default)
**Enabled:**
- walk-this-way-files
- compass-writing-guides

**Disabled:**
- All others

**Use for:** Daily writing, drafting, COMPASS work

---

### Profile 2: Research Mode
**Enabled:**
- walk-this-way-files
- duckduckgo-search
- sequential-thinking

**Disabled:**
- github, gitkraken, compass-writing-guides

**Use for:** Historical research, fact-checking

---

### Profile 3: Development Mode
**Enabled:**
- walk-this-way-files
- github
- gitkraken

**Disabled:**
- duckduckgo-search, sequential-thinking, compass-writing-guides

**Use for:** COMPASS development, git operations, MCP debugging

---

### Profile 4: Everything Mode
**Enabled:**
- All servers

**Disabled:**
- None

**Use for:** Testing, complex multi-tool tasks

⚠️ **Warning:** Running all MCP servers simultaneously may slow down Cursor startup

---

## 🔧 Troubleshooting

### GitKraken MCP Not Working
```bash
# Check if gk is installed
which gk

# Check if authenticated
gk auth status

# Re-authenticate if needed
gk auth login
```

### GitHub MCP Not Working
```bash
# Check if token is set
echo $GITHUB_TOKEN

# Test token with GitHub API
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

### MCP Server Not Loading
1. Check for JSON syntax errors in `.cursor/config/mcp.json`
2. Restart Cursor completely
3. Check Cursor logs: Help → Toggle Developer Tools → Console

---

## 📁 File Locations

**Project MCP Config:**
```
.cursor/config/mcp.json
```

**Global MCP Config (backup):**
```
~/.cursor/mcp.json
```

**GitKraken CLI:**
```
~/.local/bin/gk
```

**GitHub Token (in shell config):**
```
~/.zshrc or ~/.bash_profile
```

---

## 🎯 Next Steps

1. ✅ Install GitKraken CLI
2. ✅ Set up GitHub token environment variable
3. ✅ Test each MCP server individually
4. ✅ Create your preferred MCP profiles
5. ✅ Document which profile you use for different tasks

---

**Status:** Configuration ready, pending GitKraken CLI install and GitHub token setup  
**Last Updated:** January 12, 2026
