# UNIFIED AGENT STRUCTURE
**All Agents at Same Hierarchy Level**

---

## 📁 STRUCTURE:

```
Original Writing/
├── .cursor/
│   └── agents/
│       ├── Agent.json          ← Master orchestration (Walk This Way)
│       ├── Agent.md            ← Backup/reference
│       ├── HANK.json           ← COMPASS Super Agent
│       ├── HANK.md             ← Backup/reference (if exists)
│       ├── CREATIVE_COLLABORATOR.json
│       ├── CREATIVE_COLLABORATOR.md
│       ├── CAROLINA.json       ← Technical Systems Agent
│       ├── CAROLINA.md         ← Backup/reference (if exists)
│       ├── STRATEGIC_WRITING_COORDINATOR.json (to be created)
│       ├── STRATEGIC_WRITING_COORDINATOR.md (to be created)
│       ├── STRUCTURAL_PERFECTION_SPECIALIST.json (to be created)
│       ├── STRUCTURAL_PERFECTION_SPECIALIST.md (to be created)
│       ├── CHARACTER_DEPTH_COACH.json (to be created)
│       ├── CHARACTER_DEPTH_COACH.md (to be created)
│       ├── PROSE_POLISH_EXPERT.json (to be created)
│       └── PROSE_POLISH_EXPERT.md (to be created)
```

---

## ✅ CURRENT STATUS:

### **Completed:**
- ✅ `Agent.json` + `Agent.md` (Master orchestration)
- ✅ `HANK.json` (moved from `.cursor/HANK_Super_Agent_Definition.json`)
- ✅ `CREATIVE_COLLABORATOR.json` + `CREATIVE_COLLABORATOR.md`
- ✅ `CAROLINA Super Agent` (needs to be renamed to `CAROLINA.json`)

### **To Do:**
- ⚠️ Rename `CAROLINA Super Agent` → `CAROLINA.json`
- ⚠️ Create `CAROLINA.md` backup
- ⚠️ Convert remaining 4 agents to JSON + MD
- ⚠️ Remove old `HANK_Super_Agent_Definition.json` from `.cursor/` root

---

## 🔗 REFERENCE PATTERNS:

### **All Agents Should:**
1. **Reference Agent.json** (if working on Walk This Way):
   ```json
   "contextFiles": [
     ".cursor/agents/Agent.json",
     "Agent.md",
     ...
   ]
   ```

2. **Use Same Structure:**
   - `.json` file = Auto-loading definition
   - `.md` file = Backup/reference/human-readable

3. **Be in Same Folder:**
   - All in `.cursor/agents/`
   - No agents in root `.cursor/`
   - No agents in project root

---

## 🔧 MCP CONFIGURATION:

**Current MCP Path:**
```json
{
  "mcpServers": {
    "walk-this-way": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing"
      ]
    }
  }
}
```

**✅ MCP is CORRECT** - Points to `Original Writing` root, so it can access:
- `.cursor/agents/` (all agent definitions)
- `Agent.md` (backup in root)
- `Story_Bible/`
- `Working_Chapters/`
- Everything else

**No MCP changes needed!**

---

## 📋 AGENT HIERARCHY:

### **Level 1: Master Agents**
- `Agent.json` - Walk This Way orchestration
- `HANK.json` - COMPASS system architect
- `CAROLINA.json` - Technical systems expert

### **Level 2: Specialized Writing Agents**
- `CREATIVE_COLLABORATOR.json` - Hands-on rewriting
- `STRATEGIC_WRITING_COORDINATOR.json` - Strategic oversight
- `STRUCTURAL_PERFECTION_SPECIALIST.json` - Structure & pacing
- `CHARACTER_DEPTH_COACH.json` - Character development
- `PROSE_POLISH_EXPERT.json` - Sentence-level polish

---

## 🎯 BENEFITS OF UNIFIED STRUCTURE:

1. **Consistency** - All agents in same location
2. **Auto-loading** - JSON files load automatically
3. **Backup** - MD files for reference/backup
4. **MCP Access** - All agents accessible via MCP
5. **Maintainability** - Easy to find and update
6. **Scalability** - Add new agents easily

---

## 🚀 NEXT STEPS:

1. ✅ Rename CAROLINA file
2. ✅ Create CAROLINA.md backup
3. ⚠️ Remove old HANK file from `.cursor/` root
4. ⚠️ Convert remaining 4 agents
5. ⚠️ Test all agents load correctly

---

**Last Updated:** November 1, 2025
**Status:** Structure unified, remaining agents to convert

