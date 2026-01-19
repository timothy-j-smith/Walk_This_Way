# Filesystem MCP Setup Guide: Project-Specific Configuration
**Date:** January 17, 2026  
**Time:** 21:38 PST  
**Project:** Walk This Way + COMPASS Advanced System  
**Purpose:** Understanding Filesystem MCP configuration for current and future novels

---

## 🎯 YOUR QUESTION ANSWERED

**Q: "Is Filesystem MCP specific to Walk This Way folder, and for the next novel I'd set it up similarly and make sure we don't forget since it's embedded in Walk This Way?"**

**A: YES - Exactly right!** Here's how it works:

---

## 📁 HOW FILESYSTEM MCP WORKS

### **Current Setup (Walk This Way):**

**Location:** `.cursor/config/mcp.json` (project-specific config)

**Configuration:**
```json
{
  "mcpServers": {
    "walk-this-way-files": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
      ],
      "disabled": false
    }
  }
}
```

**What This Means:**
- ✅ **Project-specific:** Config is in `.cursor/config/mcp.json` (inside the project)
- ✅ **Scoped to Walk This Way:** Path points specifically to "Walk This Way" folder
- ✅ **Isolated:** Only accesses files in that folder (doesn't see other novels)

---

## 🔄 FOR FUTURE NOVELS (Novel #2, #3, etc.)

### **What You'll Need to Do:**

**When Starting Novel #2:**
1. Create new novel folder (e.g., `04_Novels/Phantom Cowboy/`)
2. Set up project structure (`.cursor/config/` folder)
3. Create `.cursor/config/mcp.json` with Filesystem MCP
4. Update the path to point to the new novel folder

**Example for Novel #2:**
```json
{
  "mcpServers": {
    "novel-2-files": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/04_Novels/Phantom Cowboy"
      ],
      "disabled": false
    }
  }
}
```

**Key Differences:**
- ✅ **Different MCP name:** `novel-2-files` (instead of `walk-this-way-files`)
- ✅ **Different path:** Points to new novel folder
- ✅ **Same structure:** Same MCP package, same setup process

---

## 🎯 WHY PROJECT-SPECIFIC CONFIG IS BETTER

### **Advantages:**
1. ✅ **Isolation:** Each novel has its own MCP scope (no cross-contamination)
2. ✅ **Portability:** Easy to move/backup/share novel folders
3. ✅ **Version Control:** MCP config stays with the project (in Git)
4. ✅ **Flexibility:** Different novels can have different MCP setups

### **Alternative (Global Config):**
You *could* use `~/.cursor/mcp.json` (global), but:
- ❌ **Less Isolation:** All novels share the same config
- ❌ **Harder to Manage:** One config for all projects
- ❌ **Less Portable:** Config not with the project

**Recommendation:** ✅ **Stick with project-specific** (`.cursor/config/mcp.json`)

---

## 📋 COMPASS TEMPLATE: MCP SETUP CHECKLIST

### **To Prevent Forgetting, Include in COMPASS Template:**

**File:** `zz_COMPASS/Core/Universal-Fiction-Templates.md` or `zz_COMPASS/Helpful_Hints.md`

**Add Section:**
```markdown
## MCP CONFIGURATION CHECKLIST (Novel Setup)

When starting a new novel, remember to set up MCPs:

### **Step 1: Create MCP Config Folder**
- Create `.cursor/config/` folder in novel root
- Create `.cursor/config/mcp.json` file

### **Step 2: Configure Filesystem MCP**
- Add Filesystem MCP with novel-specific path
- Name MCP appropriately (e.g., `novel-name-files`)
- Point to novel folder path

### **Step 3: Configure Core MCPs**
- Filesystem MCP (novel-specific path) ✅
- Sequential Thinking MCP ✅
- COMPASS Writing Guides MCP ✅
- Knowledge Graph Memory MCP ✅
- (Add other MCPs as needed)

### **Step 4: Test MCPs**
- Restart Cursor completely (Cmd+Q)
- Test: "Show me the README from this project" (tests Filesystem)
- Test: "Use sequential-thinking MCP to analyze this problem" (tests Sequential Thinking)

**Template MCP Config:**
```json
{
  "mcpServers": {
    "[novel-name]-files": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/PATH/TO/NOVEL/FOLDER"
      ],
      "disabled": false
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "disabled": false
    },
    "compass-writing-guides": {
      "command": "/PATH/TO/COMPASS/Writing_Guides_MCP/venv/bin/python",
      "args": ["/PATH/TO/COMPASS/Writing_Guides_MCP/server.py"],
      "disabled": false
    }
  }
}
```
```

---

## 🔧 HOW TO REMEMBER (COMPASS Integration)

### **Option 1: COMPASS Template File**
- ✅ Add MCP setup checklist to `zz_COMPASS/Core/Universal-Fiction-Templates.md`
- ✅ Include example config
- ✅ Reference in novel setup process

### **Option 2: COMPASS Helpful Hints**
- ✅ Add MCP reminder to `zz_COMPASS/Helpful_Hints.md`
- ✅ Include in "Project Setup" section

### **Option 3: COMPASS Novel Kickoff Protocol**
- ✅ Add MCP setup as Step 1 in novel kickoff checklist
- ✅ Make it part of standard novel setup process

---

## ✅ SUMMARY: YOUR UNDERSTANDING IS CORRECT

**What You Said:**
> "Filesystem MCP is specific to Walk This Way folder, and for the next novel I'd set it up similarly and make sure we don't forget since it's embedded in Walk This Way?"

**Answer:**
✅ **YES - Exactly!**

**Details:**
1. ✅ **Current:** Filesystem MCP is project-specific (embedded in "Walk This Way")
2. ✅ **Future:** Each novel needs its own `.cursor/config/mcp.json` with its own path
3. ✅ **Prevent Forgetting:** Add MCP setup to COMPASS template/checklist
4. ✅ **Isolation:** Each novel has its own MCP scope (good!)

**Recommendation:**
- ✅ Keep project-specific config (better isolation)
- ✅ Add MCP setup to COMPASS template
- ✅ Include in novel kickoff checklist
- ✅ Reference example config from "Walk This Way"

---

## 🚀 NEXT STEPS

1. ✅ **Confirm Understanding:** You've got it right!
2. ✅ **Add to COMPASS Template:** Include MCP setup checklist
3. ✅ **Document Template Config:** Create example `.cursor/config/mcp.json` template
4. ✅ **Novel #2:** Use template when starting next novel

**Bottom Line:** Project-specific config is the right approach. Add MCP setup to COMPASS template so you don't forget for Novel #2! 🎯

---

*Last Updated: January 17, 2026 21:38 PST*
