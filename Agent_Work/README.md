# AGENT_WORK
**Purpose:** Central location for all agent feedback and analysis

---

## 📁 STRUCTURE

**Each agent folder contains:**
- `[Agent_Name].json` - **CRITICAL** Agent definition (enforced by Cursor/COMPASS)
- `[Agent_Name].md` - Job description (human-readable reference)
- `README.md` - Folder guide and usage instructions
- Feedback files organized by date

---

## 🎯 AGENT ORGANIZATION

### **Core 5 Agents:**
- `Creative_Collaborator/` - Hands-on rewriting partner
- `STRATEGIC_WRITING_COORDINATOR/` - Strategic oversight
- `STRUCTURAL_PERFECTION_SPECIALIST/` - Pacing and structure
- `CHARACTER_DEPTH_COACH/` - Character development
- `PROSE_POLISH_EXPERT/` - Sentence-level refinement

### **Special Agents:**
- `JAZZ/` - Creative thought partner (hidden superpowers)
- `CAROLINA/` - Systems architect (technical foundation)
- `HANK/` - Super Agent (strategic partner)

---

## 📝 DOCUMENTATION STANDARDS

### **JSON Files (CRITICAL):**
- **Purpose:** Agent definition that Cursor/COMPASS enforces
- **Why JSON:** More powerful/forceful than MD files
- **Location:** `Agent_Work/[Agent_Name]/[Agent_Name].json`
- **Status:** REQUIRED for all agents

### **MD Files (Reference):**
- **Purpose:** Human-readable job description
- **Why MD:** Easy to read and understand
- **Location:** `Agent_Work/[Agent_Name]/[Agent_Name].md`
- **Status:** Required for all agents

### **Feedback Files:**
- **Format:** `Chapter_XX_[Type]_[YYYY-MM-DD].md` or `[Descriptive_Name]_[YYYY-MM-DD].md`
- **Location:** `Agent_Work/[Agent_Name]/`
- **Purpose:** Agent analysis and feedback

---

## 🔄 WORKFLOW

1. Agent receives request via `@mention`
2. Agent reads their `.json` definition (enforced)
3. Agent reads their `.md` job description (reference)
4. Agent provides feedback/analysis
5. Agent saves to `Agent_Work/[Agent_Name]/` with date

---

## 📊 HANK_Work vs Agent_Work/HANK

**HANK_Work/** - Session summaries (different purpose)
- `HANK_Work/Session_Summaries/` - Daily session recaps
- Separate from agent feedback

**Agent_Work/HANK/** - HANK agent feedback
- `HANK.json` - Agent definition
- `HANK.md` - Job description
- Feedback files from HANK agent requests

---

## ⚠️ CRITICAL NOTES

1. **JSON files are REQUIRED** - Agents follow JSON definitions more reliably than MD
2. **Both JSON and MD needed** - JSON for enforcement, MD for human reference
3. **Consistent structure** - All agents follow same pattern
4. **No exceptions** - Even special agents (HANK, JAZZ, CAROLINA) follow same structure

---

**Last Updated:** Saturday, November 29, 2025
