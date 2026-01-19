# MCP Profile Templates: Quick Reference Guide
**Date:** January 17, 2026  
**Time:** 20:48 PST  
**Project:** Walk This Way + COMPASS Advanced System  
**Purpose:** Quick reference for task-specific MCP profiles

---

## 🎯 RECOMMENDED DEFAULT CONFIGURATION

### **Smart Default (Most Tasks):**

```json
{
  "mcpServers": {
    "walk-this-way-files": { "disabled": false },      // ✅ Always on
    "compass-writing-guides": { "disabled": false },   // ✅ Always on
    "github": { "disabled": true },                     // ⏸️ Enable for commits/planning
    "gitkraken": { "disabled": true },                  // ⏸️ Enable for commits/planning
    "sequential-thinking": { "disabled": true },        // ⏸️ Enable for complex problems
    "duckduckgo-search": { "disabled": true }           // ⏸️ Enable for research
  }
}
```

**Why:** Filesystem + COMPASS = Essential for most writing. Others = Enable when needed.

---

## 📋 TASK-SPECIFIC PROFILES

### **Profile 1: Writing Mode (Default)**

**Use For:** Daily writing sessions, chapter editing, prose refinement

```json
{
  "walk-this-way-files": { "disabled": false },      // ✅ Read files
  "compass-writing-guides": { "disabled": false },   // ✅ Writing rules
  "github": { "disabled": true },                     // ❌ Not needed
  "gitkraken": { "disabled": true },                  // ❌ Not needed
  "sequential-thinking": { "disabled": true },        // ❌ Not needed
  "duckduckgo-search": { "disabled": true }           // ❌ Not needed
}
```

**Efficiency:** Fast, focused, minimal overhead

---

### **Profile 2: Pre-Commit Consistency Check**

**Use For:** Before committing, consistency validation, quality checks

```json
{
  "walk-this-way-files": { "disabled": false },      // ✅ Read files
  "compass-writing-guides": { "disabled": false },   // ✅ Writing rules
  "github": { "disabled": false },                    // ✅ Repository metadata
  "gitkraken": { "disabled": false },                 // ✅ Git context
  "sequential-thinking": { "disabled": false },       // ✅ Deep analysis
  "duckduckgo-search": { "disabled": true }           // ❌ Not needed
}
```

**Efficiency:** Comprehensive, thorough, all context available

---

### **Profile 3: Strategic Planning**

**Use For:** 2026 novel planning, goal setting, workflow optimization

```json
{
  "walk-this-way-files": { "disabled": false },      // ✅ Read blueprints
  "sequential-thinking": { "disabled": false },       // ✅ Strategic analysis
  "github": { "disabled": false },                    // ✅ Milestone tracking
  "gitkraken": { "disabled": false },                 // ✅ Progress tracking
  "compass-writing-guides": { "disabled": true },     // ❌ Not needed
  "duckduckgo-search": { "disabled": true }           // ❌ Not needed
}
```

**Efficiency:** Strategic focus, no writing rules overhead

---

### **Profile 4: Research Mode**

**Use For:** Historical research, fact-checking, timeline verification

```json
{
  "walk-this-way-files": { "disabled": false },      // ✅ Read research docs
  "duckduckgo-search": { "disabled": false },         // ✅ Web search
  "sequential-thinking": { "disabled": false },       // ✅ Research planning
  "github": { "disabled": true },                     // ❌ Not needed
  "gitkraken": { "disabled": true },                  // ❌ Not needed
  "compass-writing-guides": { "disabled": true }      // ❌ Not needed
}
```

**Efficiency:** Research focus, no git overhead

---

### **Profile 5: Git Operations**

**Use For:** Committing changes, pushing to GitHub, branch management

```json
{
  "github": { "disabled": false },                    // ✅ Repository access
  "gitkraken": { "disabled": false },                 // ✅ Git operations
  "walk-this-way-files": { "disabled": true },        // ❌ Not needed
  "compass-writing-guides": { "disabled": true },     // ❌ Not needed
  "sequential-thinking": { "disabled": true },        // ❌ Not needed
  "duckduckgo-search": { "disabled": true }           // ❌ Not needed
}
```

**Efficiency:** Fast git operations, minimal overhead

---

### **Profile 6: Complex Problem-Solving**

**Use For:** Act II pacing, ending structure, character arc completion

```json
{
  "walk-this-way-files": { "disabled": false },      // ✅ Read blueprint
  "sequential-thinking": { "disabled": false },       // ✅ Deep analysis
  "compass-writing-guides": { "disabled": false },   // ✅ Writing rules
  "github": { "disabled": true },                     // ❌ Not needed
  "gitkraken": { "disabled": true },                  // ❌ Not needed
  "duckduckgo-search": { "disabled": true }           // ❌ Not needed
}
```

**Efficiency:** Deep analysis focus, no git overhead

---

## 🎨 QUICK SWITCH GUIDE

### **How to Switch Profiles:**

1. **Edit `.cursor/config/mcp.json`**
2. **Change `"disabled": true/false`** for each MCP
3. **Restart Cursor** (MCPs load on startup)

**Or use profile files:**
- Copy profile JSON to `mcp.json`
- Restart Cursor

---

**Bottom Line:** Filesystem MCP is essential - keep it enabled. Toggle other MCPs based on task for maximum efficiency!

---

*Last Updated: January 17, 2026 20:48 PST*
