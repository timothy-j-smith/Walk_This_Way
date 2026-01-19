# MCP INTEGRATION IN COMPASS
**Date:** January 17, 2026  
**Last Updated:** January 17, 2026 21:40 PST  
**Purpose:** Model Context Protocol for COMPASS and Walk This Way

---

## 🎯 MCP FOR COMPASS

**Model Context Protocol (MCP)** extends COMPASS capabilities by connecting to external tools and data sources.

---

## 📋 MCP SERVERS FOR COMPASS

### **Research & Fact-Checking:**
- **DuckDuckGo Web Search** - Historical research, fact-checking
- **Firecrawl MCP** - Web scraping and deep research (recommended over DuckDuckGo)
- **Google Drive** - Access research documents
- **Notion** - Documentation, planning

### **System Management:**
- **GitHub MCP** - Version control, issue tracking
- **GitKraken MCP** - Enhanced Git operations with AI
- **Sequential Thinking** - Structured problem-solving

### **Writing Support:**
- **Filesystem MCP** - Access to novel files, drafts, Story Bible
- **Knowledge Graph Memory MCP** - Persistent memory for character consistency
- **Vectara MCP** - Semantic search across documents
- **COMPASS Writing Guides MCP** - Writing craft and author guidance

### **Export & Conversion:**
- **Pandoc MCP** - Document conversion (Markdown → DOCX, etc.)

---

## 📁 MCP CONFIGURATION

**Location:** `.cursor/config/mcp.json` (project-specific)

**Important:** Each novel needs its own MCP configuration with novel-specific paths!

**Included in COMPASS:**
- ✅ MCP configuration template
- ✅ Documentation for setup
- ✅ Integration with COMPASS agents
- ✅ Novel setup checklist (see below)

---

## 🚀 MCP SETUP CHECKLIST (NOVEL SETUP PROTOCOL)

### **When Starting a New Novel, Remember to Set Up MCPs:**

---

### **Step 1: Create MCP Config Folder**
- ✅ Create `.cursor/config/` folder in novel root
- ✅ Create `.cursor/config/mcp.json` file

---

### **Step 2: Configure Filesystem MCP** (CRITICAL - Don't Forget!)
- ✅ Add Filesystem MCP with novel-specific path
- ✅ Name MCP appropriately (e.g., `[novel-name]-files`)
- ✅ Point to novel folder path (must be absolute path)

**Example Template:**
```json
{
  "mcpServers": {
    "[novel-name]-files": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/FULL/ABSOLUTE/PATH/TO/NOVEL/FOLDER"
      ],
      "disabled": false
    }
  }
}
```

**Real Example (Walk This Way):**
```json
"walk-this-way-files": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
  ],
  "disabled": false
}
```

**Why Project-Specific:**
- ✅ **Isolation:** Each novel has its own MCP scope (no cross-contamination)
- ✅ **Portability:** Easy to move/backup/share novel folders
- ✅ **Version Control:** MCP config stays with the project (in Git)
- ✅ **Flexibility:** Different novels can have different MCP setups

---

### **Step 3: Configure Core MCPs**

**Essential MCPs (Always Enable):**
1. ✅ **Filesystem MCP** (novel-specific path) - CRITICAL!
2. ✅ **Sequential Thinking MCP** - Structured problem-solving
3. ✅ **COMPASS Writing Guides MCP** - Writing craft guidance
4. ✅ **Knowledge Graph Memory MCP** - Character consistency
5. ✅ **Vectara MCP** - Semantic search

**Task-Specific MCPs (Enable as Needed):**
- 🔄 **Firecrawl MCP** - Research mode
- 🔄 **Pandoc MCP** - Export mode
- 🔄 **Google Workspace MCP** - Collaboration mode
- 🔄 **GitHub MCP** - Git operations
- 🔄 **GitKraken MCP** - Git operations

---

### **Step 4: Complete MCP Config Template**

**Full Template for New Novel:**
```json
{
  "mcpServers": {
    "[novel-name]-files": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/FULL/ABSOLUTE/PATH/TO/NOVEL/FOLDER"
      ],
      "disabled": false
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "disabled": false
    },
    "compass-writing-guides": {
      "command": "/FULL/PATH/TO/COMPASS/Writing_Guides_MCP/venv/bin/python",
      "args": [
        "/FULL/PATH/TO/COMPASS/Writing_Guides_MCP/server.py"
      ],
      "disabled": false
    },
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github",
        "--token",
        "env:GITHUB_TOKEN"
      ],
      "disabled": false
    },
    "gitkraken": {
      "command": "gk",
      "args": ["mcp"],
      "disabled": false
    }
  }
}
```

**Important Notes:**
- ⚠️ **All paths must be absolute** (not relative)
- ⚠️ **Filesystem MCP path must point to novel folder** (not COMPASS folder)
- ⚠️ **COMPASS Writing Guides MCP path** points to shared COMPASS folder (same for all novels)

---

### **Step 5: Test MCPs**

**After Setup, Test Each MCP:**

1. ✅ **Restart Cursor completely** (Cmd+Q, don't just reload window)
2. ✅ **Test Filesystem MCP:** "Show me the README from this project"
3. ✅ **Test Sequential Thinking:** "Use sequential-thinking MCP to analyze this problem"
4. ✅ **Test COMPASS Guides:** "Use compass-writing-guides MCP to get Stephen King's advice on adverbs"
5. ✅ **Test GitHub (if enabled):** "Show me recent git commits from my GitHub repo"
6. ✅ **Test GitKraken (if enabled):** "Show me GitKraken workspace status"

**Troubleshooting:**
- ❌ **MCP not found:** Check paths are absolute, restart Cursor completely
- ❌ **Filesystem MCP can't access files:** Verify path points to novel folder
- ❌ **COMPASS MCP not found:** Verify COMPASS path is correct

---

## ✅ BENEFITS FOR COMPASS

1. ✅ **Enhanced Research** - Real-time fact-checking (Firecrawl)
2. ✅ **External Data** - Connect to story bible databases (Filesystem)
3. ✅ **Character Consistency** - Persistent memory across sessions (Knowledge Graph Memory)
4. ✅ **Tool Integration** - Connect to writing tools (Git, GitKraken)
5. ✅ **System Extension** - Expand COMPASS capabilities (all MCPs)
6. ✅ **Semantic Search** - Find similar scenes/themes (Vectara)
7. ✅ **Writing Guidance** - Access to master writer advice (COMPASS Writing Guides)

---

## 📚 REFERENCE

**See Also:**
- `MCP_COMPREHENSIVE_EVALUATION.md` - Complete MCP evaluation and recommendations
- `MCP_FILESYSTEM_SETUP_GUIDE.md` - Detailed Filesystem MCP setup guide
- `MCP_ORCHESTRATION_STRATEGY.md` - Task-specific MCP configuration strategies

---

**MCP is integrated into COMPASS structure and documentation. Remember: Each novel needs its own MCP configuration!**




