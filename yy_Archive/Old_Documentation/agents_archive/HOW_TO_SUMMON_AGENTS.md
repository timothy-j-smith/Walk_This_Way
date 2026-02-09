# HOW TO SUMMON AGENTS - COMPLETE GUIDE

**Understanding Custom Agents vs Code Agents vs @ Mentions**

---

## 🎯 THREE WAYS TO USE AGENTS IN CURSOR

### **1. CUSTOM AGENTS (Settings-Based)**
**What They Are:**
- Agents configured in Cursor Settings → Custom Agents
- These are YOUR custom agents (HANK, Creative Collaborator, etc.)
- Defined by JSON files in `.cursor/agents/`
- Auto-load when selected from dropdown

**How to Summon:**
1. Open Cursor Settings (`Cmd+,`)
2. Go to "Custom Agents" section
3. Select agent from dropdown (e.g., "Creative Collaborator")
4. Start new chat - agent loads automatically with its definition

**Current Custom Agents:**
- ✅ HANK (COMPASS Super Agent)
- ✅ Creative Collaborator (Hands-on rewriting)
- ✅ Strategic Writing Coordinator
- ✅ Structural Perfection Specialist
- ✅ Character Depth Coach
- ✅ Prose Polish Expert
- ✅ CAROLINA (Technical Systems)

**Important:** 
- Custom Agent descriptions in Settings dropdown may be outdated
- The actual agent definition comes from `.cursor/agents/[AGENT_NAME].json`
- JSON file is the source of truth, not the Settings description

---

### **2. @ MENTIONS (File-Based)**
**What They Are:**
- Direct file references using `@` symbol
- References `.md` or `.json` files directly
- Works in any chat, any time
- No Settings configuration needed

**How to Summon:**
```
@.cursor/agents/CREATIVE_COLLABORATOR.json
```

**Or:**
```
@CREATIVE_COLLABORATOR.md
```

**Examples:**
- `@.cursor/agents/Agent.json` - Master orchestration
- `@.cursor/agents/STRATEGIC_WRITING_COORDINATOR.json` - Strategic coordinator
- `@Story_Bible/character-bible.md` - Character reference

**When to Use:**
- Quick access without Settings
- Referencing specific files
- Combining multiple agents in one chat
- Testing agent definitions

---

### **3. CODE AGENTS (Built-In)**
**What They Are:**
- Cursor's built-in agents for code development
- Examples: "Refactor Agent", "Test Agent", "Documentation Agent"
- Designed for software development workflows
- NOT for fiction writing (different purpose)

**How They Work:**
- Automatically suggested by Cursor based on code context
- Appear in Composer or Agent mode
- Use code-specific tools (Git, terminal, file operations)
- Focus on technical tasks, not creative writing

**For Fiction Writing:**
- ❌ Code agents are NOT suitable for novel writing
- ✅ Use Custom Agents (your writing agents) instead
- ✅ Use @ mentions for file-based references

---

## 🔧 CUSTOM AGENT SETTINGS EXPLAINED

### **Where Settings Come From:**
1. **Settings UI** (`Cmd+,` → Custom Agents):
   - Dropdown list of available agents
   - Description field (may be outdated)
   - MCP checkbox
   - Temperature/Intelligence settings

2. **JSON Definition Files** (`.cursor/agents/[AGENT].json`):
   - **THIS IS THE SOURCE OF TRUTH**
   - Contains complete agent definition
   - System prompt, context files, capabilities
   - Auto-loaded when agent is selected

### **Can Settings Point to JSON Files?**
**YES!** The Custom Agent system automatically:
1. Scans `.cursor/agents/` for JSON files
2. Loads agent definitions from JSON
3. Uses JSON as the authoritative definition
4. Settings UI is just a selector - JSON is the actual definition

**Important:** 
- JSON file = Agent definition (what agent knows, how it behaves)
- Settings UI = Agent selector (which agent to use)
- The JSON file is what actually loads, not the Settings description

---

## 📋 TOOLS LIST IN CUSTOM AGENT SETTINGS

### **What Is "Tools"?**
The "Tools" list in Custom Agent Settings shows:
- **Capabilities** - What the agent can do
- **Context Files** - Files the agent references
- **MCP Access** - External data sources

### **Where Tools Come From:**
1. **From JSON Definition:**
   ```json
   "capabilities": [
     "hands-on-prose-rewriting",
     "scene-creation",
     "creative-brainstorming"
   ],
   "contextFiles": [
     ".cursor/agents/Agent.json",
     "Test_Draft_Copy/",
     "Story_Bible/"
   ]
   ```

2. **From MCP Configuration:**
   - If MCP is enabled, agent can access MCP server resources
   - MCP provides file system access, external APIs, etc.

3. **Built-In Cursor Tools:**
   - File reading/writing
   - Code editing
   - Terminal access
   - Git operations

**The Tools list is informational** - it shows what the agent CAN do, but the actual capabilities come from the JSON definition.

---

## 🚀 RECOMMENDED WORKFLOW

### **For Daily Writing:**
1. **Use Custom Agent dropdown:**
   - Select agent from Settings
   - Start new chat
   - Agent auto-loads with full definition

2. **Or use @ mention:**
   ```
   @.cursor/agents/CREATIVE_COLLABORATOR.json
   ```

### **For Quick References:**
```
@.cursor/agents/Agent.json
@Story_Bible/character-bible.md
```

### **For Multiple Agents:**
```
@.cursor/agents/STRATEGIC_WRITING_COORDINATOR.json
@.cursor/agents/CHARACTER_DEPTH_COACH.json
Analyze Chapter 5 from both strategic and character perspectives
```

---

## ⚠️ COMMON ISSUES

### **Issue: Agent doesn't know its role**
**Fix:** Check that JSON file exists in `.cursor/agents/` and is valid

### **Issue: Agent references wrong files**
**Fix:** Update `contextFiles` in JSON definition (we fixed Working_Chapters → Test_Draft_Copy)

### **Issue: Settings description is outdated**
**Fix:** Settings description is just metadata - JSON file is the source of truth

### **Issue: Agent can't find files**
**Fix:** 
- Check MCP is enabled in Settings
- Verify file paths in `contextFiles` are correct
- Use absolute paths if needed

---

## 📝 SUMMARY

**Custom Agents:**
- ✅ Your writing agents (HANK, Creative Collaborator, etc.)
- ✅ Defined in `.cursor/agents/*.json`
- ✅ Selected from Settings dropdown
- ✅ Auto-load with full definition

**@ Mentions:**
- ✅ Direct file references
- ✅ Works anywhere, anytime
- ✅ No Settings needed

**Code Agents:**
- ❌ Built-in for code development
- ❌ NOT for fiction writing
- ✅ Use Custom Agents instead

**JSON Files:**
- ✅ Source of truth for agent definitions
- ✅ Auto-loaded by Custom Agent system
- ✅ Settings UI is just a selector

---

**Last Updated:** November 1, 2025
**Status:** All agents unified, folder references fixed, ready to use!

