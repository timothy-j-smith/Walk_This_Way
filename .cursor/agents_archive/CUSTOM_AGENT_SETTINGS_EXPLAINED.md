# CUSTOM AGENT SETTINGS EXPLAINED

**Understanding the Settings UI vs JSON Files**

---

## 🎯 THE KEY QUESTION

**Does the "Job Description" field in Custom Agent Settings actually get used, or does Cursor read from JSON files?**

---

## ✅ THE ANSWER

### **How Cursor Actually Works:**

1. **JSON Files Are Source of Truth:**
   - Cursor scans `.cursor/agents/` for JSON files
   - JSON files contain the complete agent definition
   - `systemPrompt` in JSON = what agent actually uses

2. **Settings UI is Just a Selector:**
   - The "Job Description" field in Settings is **metadata only**
   - It's for YOUR reference, not what the agent reads
   - The dropdown menu IS used to select which agent to load

3. **What Actually Loads:**
   - When you select agent from dropdown → Cursor loads the JSON file
   - JSON file's `systemPrompt` = what agent actually gets
   - Settings description = just a label for you

---

## 📋 RECOMMENDED SETUP

### **For Custom Agent Settings UI:**

**Job Description Field:**
- Keep it SIMPLE and SHORT
- Just a quick reference for you
- Example: "Hands-on rewriting partner & Advanced Tools Expert"

**Better Yet - Point to JSON:**
- You could put: "See .cursor/agents/CREATIVE_COLLABORATOR.json"
- But this is just for YOUR reference
- The agent doesn't read this field

### **What Actually Matters:**
- ✅ JSON file in `.cursor/agents/`
- ✅ JSON file's `systemPrompt` field
- ✅ JSON file's `contextFiles` array
- ✅ JSON file's `capabilities` array

---

## 🔧 CURRENT SETUP ANALYSIS

### **What You Have:**
- ✅ JSON files in `.cursor/agents/` (source of truth)
- ✅ Settings UI with dropdown (selector)
- ⚠️ Settings description may be outdated (doesn't matter - JSON is authoritative)

### **What You Should Do:**

**Option 1: Simple Description (Recommended)**
```
Job Description: "Hands-on rewriting partner & Advanced Tools Expert"
```

**Option 2: Point to JSON**
```
Job Description: "See .cursor/agents/CREATIVE_COLLABORATOR.json for full definition"
```

**Option 3: Brief Summary**
```
Job Description: "Creative Collaborator - Works WITH you on prose rewriting using Smart Rewrites, JSON Prompts, and DNA Memory integration"
```

---

## 🎯 THE DROPDOWN MENU

### **Is It Actually Used?**

**YES!** The dropdown menu IS used by Cursor:

1. **You select agent from dropdown**
2. **Cursor loads the corresponding JSON file**
3. **JSON file's `systemPrompt` becomes the agent's instructions**
4. **Agent starts with that definition**

**The dropdown is the SELECTOR - it tells Cursor which JSON file to load.**

---

## ✅ CENTRAL "AGENT" SETUP

### **Agent.json Status:**

**Current Setup:**
- ✅ `Agent.json` exists in `.cursor/agents/`
- ✅ Contains master orchestration (themes, characters, vision)
- ✅ Referenced by all other agents in `contextFiles`
- ✅ Has both JSON and MD backup

**Is It Set Up Correctly?**

**YES!** Agent.json is:
- ✅ In correct location (`.cursor/agents/`)
- ✅ Valid JSON format
- ✅ Referenced by other agents
- ✅ Contains complete project vision

**How It Works:**
- Other agents reference it in `contextFiles`
- When agent loads, it reads Agent.json
- Agent now knows master theme, characters, vision
- Agent can reference it during conversations

---

## 📝 RECOMMENDATIONS

### **For Custom Agent Settings:**

1. **Job Description:**
   - Keep it SHORT (1-2 sentences)
   - Just for YOUR quick reference
   - Don't duplicate JSON content here

2. **Example Good Descriptions:**
   - "Hands-on rewriting partner & Advanced Tools Expert"
   - "Strategic coordinator & workflow manager"
   - "Character development & voice consistency expert"

3. **Enable MCP:**
   - ✅ Check the MCP checkbox (if you want file access)
   - This enables Model Context Protocol

4. **Tools:**
   - Check "All tools" or select individual tools
   - This controls what the agent CAN do

---

## 🔍 VERIFICATION

### **To Verify Setup:**

1. **Check JSON File Exists:**
   - `.cursor/agents/[AGENT].json` exists
   - JSON is valid

2. **Check Settings:**
   - Agent appears in dropdown
   - Description is simple (for your reference)

3. **Test Agent:**
   - Select from dropdown
   - Start chat
   - Agent should know its role (from JSON, not Settings description)

---

## 💡 KEY INSIGHTS

1. **JSON Files = Source of Truth**
   - Complete agent definition
   - What agent actually reads

2. **Settings UI = Selector + Metadata**
   - Dropdown selects which JSON to load
   - Description is just for your reference

3. **Agent.json = Master Reference**
   - Central orchestration document
   - Other agents reference it
   - Contains project vision

4. **The Connection:**
   - Settings dropdown → Selects JSON file
   - JSON file → Defines agent behavior
   - Agent.json → Provides project context

---

**Last Updated:** November 1, 2025
**Key Insight:** Settings description is metadata. JSON files are authoritative.

