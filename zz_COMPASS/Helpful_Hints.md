# HELPFUL HINTS - COMPLETE GUIDE
**Date:** Saturday, November 29, 2025  
**Purpose:** Comprehensive reference for COMPASS and Walk This Way

---

## 📋 TABLE OF CONTENTS

1. [Git & GitHub Guide](#git--github-guide)
2. [Multi-Root Workspaces](#multi-root-workspaces)
3. [COMPASS Core vs Premium](#compass-core-vs-premium)
4. [File Types Guide](#file-types-guide)
5. [Critical Clarifications](#critical-clarifications)
6. [Quick Reference](#quick-reference)

---

## 🔐 GIT & GITHUB GUIDE

### **Creating a Git Repository**

**Initial Setup:**
```bash
cd "/path/to/Walk This Way"
git init
git add .
git commit -m "Initial commit - Walk This Way novel"
```

**Connect to GitHub:**
```bash
git remote add origin https://github.com/yourusername/walk-this-way.git
git branch -M main
git push -u origin main
```

---

### **Daily Git Workflow**

**Check Status:**
```bash
git status
```

**Stage Changes:**
```bash
git add .
# or specific files:
git add Draft_1/Chapter_01.txt
```

**Commit Changes:**
```bash
git commit -m "Updated Chapter 1 - Draft 1"
```

**Push to GitHub:**
```bash
git push
```

**Pull from GitHub:**
```bash
git pull
```

---

### **Best Practices**

- ✅ **Commit often** - After each writing session
- ✅ **Descriptive commit messages** - "Updated Chapter 5 - Draft 1"
- ✅ **Push regularly** - Backup your work
- ✅ **Use branches** - For major rewrites (Draft_2, Draft_3)

---

### **Submitting to GitHub**

**First Time:**
1. Create repository on GitHub
2. Connect local repo: `git remote add origin [URL]`
3. Push: `git push -u origin main`

**Regular Submissions:**
```bash
git add .
git commit -m "Your commit message"
git push
```

---

## 🔗 MULTI-ROOT WORKSPACES

### **What is Multi-Root Workspace?**

Allows you to open multiple project folders in one Cursor window.

**Example:**
- COMPASS folder (system)
- Walk This Way folder (novel)
- Novel #2 folder (future)

All accessible in same Cursor window!

---

### **Setting Up Multi-Root Workspace**

**Method 1: Via Cursor UI**
1. File → Add Folder to Workspace
2. Select folders to add
3. Save workspace: File → Save Workspace As...

**Method 2: Via Workspace File**
Create `Walk_This_Way.code-workspace`:
```json
{
  "folders": [
    {
      "path": "Walk This Way"
    },
    {
      "path": "COMPASS"
    },
    {
      "path": "../Novel_2"
    }
  ]
}
```

---

### **Benefits for COMPASS**

- ✅ **Share COMPASS** across multiple novels
- ✅ **Access both** COMPASS and Walk This Way together
- ✅ **Easy navigation** between projects
- ✅ **Unified workspace** for all writing projects

---

### **Future Use (When COMPASS Extracted)**

When COMPASS becomes its own folder:
1. Create multi-root workspace
2. Include: COMPASS folder + Novel folders
3. COMPASS accessible to all novels

---

## 📊 COMPASS CORE VS PREMIUM

### **COMPASS Core**

**What's Included:**
- ✅ Agent System (Core 5 agents)
- ✅ Writing Directives (.cursor/rules/)
- ✅ Custom Commands (26 commands)
- ✅ JSON Prompts (11 prompts)
- ✅ Basic Configuration

**Status:** ✅ Implemented and in use

**Purpose:** Essential writing system, foundational tools

---

### **COMPASS Premium**

**What's Included (Phase 2):**
- ⏳ Writing DNA Memory System (automatic tracking)
- ⏳ Smart Rewrites System (Liberty Levels)
- ⏳ Agent Choreography (parallel processing)
- ⏳ Novel Kickoff Protocol (guided discovery)
- ⏳ Advanced Error Tracking

**Status:** ⏳ Designed, not yet built

**Purpose:** Advanced features for professional production

---

### **Current Strategy**

**For v1.0:** Unified Premium package (simpler, more value)

**Future:** May separate Core/Premium if needed

**Reference:** See `COMPASS_CORE_VS_PREMIUM_ARCHITECTURE.md` for details

---

## 📄 FILE TYPES GUIDE

### **When to Use Each File Type**

#### **.txt Files**
**Purpose:** Plain text, chapter files, drafts  
**When to use:**
- ✅ Chapter files (Draft_1/Chapter_01.txt)
- ✅ Draft manuscripts
- ✅ Plain text notes
- ✅ Simple documentation

**Example:** `Draft_1/Act_I/Chapter_01_The_Belt_Buckle.txt`

---

#### **.md Files (Markdown)**
**Purpose:** Documentation, rules, instructions, rich formatting  
**When to use:**
- ✅ Documentation (README.md, guides)
- ✅ Rules (.cursor/rules/walk-this-way-writing-directives.md)
- ✅ Agent definitions (STRATEGIC_WRITING_COORDINATOR.md)
- ✅ Story Bible (character-bible.md)
- ✅ Any file needing formatting, links, headers

**Example:** `Story_Bible/character-bible.md`, `.cursor/rules/walk-this-way-writing-directives.md`

---

#### **.json Files**
**Purpose:** Configuration, data, structured information  
**When to use:**
- ✅ Configuration files (settings.json, DRAFT_MODES.json)
- ✅ Agent definitions (CREATIVE_COLLABORATOR.json)
- ✅ Prompts (prompts.json)
- ✅ Data structures
- ✅ Machine-readable config

**Example:** `.cursor/config/DRAFT_MODES.json`, `.cursor/config/prompts.json`

---

#### **.py Files (Python)**
**Purpose:** Scripts, automation, tools  
**When to use:**
- ✅ Automation scripts
- ✅ Custom tools
- ✅ Data processing
- ✅ MCP servers (if needed)

**Status:** Phase 2 (future)

**Example:** `scripts/process_chapters.py` (future)

---

### **Quick Decision Guide**

**Need formatting?** → Use `.md`  
**Need config/data?** → Use `.json`  
**Plain text?** → Use `.txt`  
**Automation?** → Use `.py` (Phase 2)

---

## 🎯 CRITICAL CLARIFICATIONS

### **Prompts vs Commands vs Rules**

#### **Prompts (JSON)**
- **Location:** `.cursor/config/prompts.json` or `.cursor/Prompts/`
- **Usage:** `@prompt_name` in chat
- **Purpose:** Specific writing transformations
- **Example:** `@scene_creation`, `@pov_conversion`

**Total:** 11 JSON prompts

---

#### **Commands (Custom)**
- **Location:** `.cursor/commands/` or `zz_COMPASS/Commands/`
- **Usage:** Type `/` in chat, select from dropdown
- **Purpose:** Reusable prompts for specific tasks
- **Example:** `/fix_grammar`, `/improve_prose`

**Total:** 26 custom commands

---

#### **Rules (.cursor/rules/)**
- **Location:** `.cursor/rules/walk-this-way-writing-directives.md`
- **Usage:** Automatically applied when referenced
- **Purpose:** Project-wide writing directives, guidelines
- **Example:** COMPASS writing system rules, character voices

**Status:** Standard Cursor directory (can be at multiple levels)

---

### **Agent Organization**

#### **Core 5 Agents:**
- STRATEGIC_WRITING_COORDINATOR
- STRUCTURAL_PERFECTION_SPECIALIST
- CHARACTER_DEPTH_COACH
- PROSE_POLISH_EXPERT
- CREATIVE_COLLABORATOR

**Location:** `zz_COMPASS/Agents/Core_5/`

---

#### **Special Agents:**
- HANK (Super Agent)
- CAROLINA
- JAZZ

**Location:** `zz_COMPASS/Agents/Special/`

---

#### **Master Agent:**
- AGENT.json (master agent definition)

**Location:** `zz_COMPASS/Agents/Master/`

---

### **Story_Bible vs Documentation/STORY_BIBLE.md**

#### **Story_Bible/ Folder**
- **Purpose:** Core reference files (canonical)
- **Files:**
  - `character-bible.md`
  - `timeline.md`
  - `music-references.md`
  - `author-style-library.md`
- **Location:** Root level `Story_Bible/`

**Use for:** Quick character/timeline/music reference

---

#### **Documentation/STORY_BIBLE.md**
- **Purpose:** Comprehensive project documentation (709 lines)
- **Content:** Full story bible, project details, true story behind novel
- **Location:** `Documentation/STORY_BIBLE.md`

**Use for:** Complete project reference, comprehensive documentation

**Note:** Different purposes - Story_Bible/ = quick reference, Documentation/STORY_BIBLE.md = full documentation

---

### **System File Locations**

#### **.cursor/ Structure:**
```
.cursor/
├── rules/          ← Standard (COMPASS rules)
├── config/         ← Custom (JSON configs)
├── docs/           ← Custom (documentation)
├── logs/           ← Custom (session logs)
└── settings.json   ← Custom (Cursor settings)
```

**Note:** Only `.cursor/rules/` is standard Cursor. Everything else is custom COMPASS organization.

---

#### **Hidden System Files:**
- `.git/` - Git repository (version control)
- `.gitignore` - Git ignore file (root level)
- `.cursorignore` - Cursor ignore file (root level)
- `.vscode/` - VS Code/Cursor workspace settings

**Will carry over:** ✅ Yes, these are part of your project

---

### **Draft Management**

#### **Current Draft:**
- `Draft_1/` - Your current complete draft (34 chapters)

#### **Starting Draft 2:**
```bash
cp -r Draft_1 Draft_2
```
Then edit `Draft_2/` - this becomes your edited version

#### **When Draft 2 Complete:**
Move `Draft_1/` → `Archive/Completed_Drafts/Draft_1/`

**Rule:** Only 2 drafts visible at once (current + previous for reference)

---

### **Liberty Levels vs Mode System**

#### **Liberty Levels (Rewrite Intensity)**
- **Conservative:** Minimal changes, preserve voice
- **Moderate:** Balanced enhancement
- **High:** Dramatic transformation
- **Blue Sky:** Complete rewrite (optional)

**Use for:** Smart Rewrites, prose transformation

---

#### **Mode System (Feedback Tone)**
- **Nice:** Supportive, encouraging (early drafts)
- **Neutral:** Balanced professional assessment (default)
- **Professional:** Honest critique, literary agent level

**Use for:** Agent feedback, critique tone

**Note:** Different purposes - Liberty = rewrite intensity, Mode = feedback tone

---

### **Temperature & Parameters**

#### **Draft Phases:**
- **Get It Down (Draft 1):** Temp 0.9 (creative)
- **Make It Good (Draft 2):** Temp 0.6 (balanced)
- **Make It Shine (Draft 3):** Temp 0.3 (precise)

**Location:** `.cursor/config/DRAFT_MODES.json`

**Flexible:** Can adjust temperature as needed (not fixed)

---

## 📚 QUICK REFERENCE

### **File Locations**

**Current Draft:** `Draft_1/`  
**Story Reference:** `Story_Bible/`  
**Project Docs:** `Documentation/`  
**Agent Feedback:** `Agent_Work/`  
**COMPASS System:** `zz_COMPASS/`  
**Config Files:** `.cursor/config/`  
**Old Files:** `Archive/`

---

### **Common Commands**

**Copy Draft:**
```bash
cp -r Draft_1 Draft_2
```

**Git Status:**
```bash
git status
```

**Git Commit:**
```bash
git add .
git commit -m "Your message"
git push
```

---

### **Agent Usage**

**Call Agent:**
```
@STRATEGIC_WRITING_COORDINATOR.md
```

**With Mode:**
```
@CREATIVE_COLLABORATOR.md Nice
```

**With Prompt:**
```
@scene_creation [outline or beats]
```

---

### **File Explorer Items**

- **Orphans:** Unlinked files (237) - Many will be archived
- **Placeholders:** Broken links (84) - Will be fixed during reorganization
- **Timeline:** Git history view
- **All Links:** Shows markdown links in project

---

## 🚀 TROUBLESHOOTING

### **Can't Find File?**
- Use Cmd+P (Quick Open) to search
- Check if file is in `.cursorignore`
- Verify file path is correct

### **Agent Not Working?**
- Verify agent file exists in `zz_COMPASS/Agents/`
- Check file path in @mention
- Ensure agent .md file is accessible

### **Git Issues?**
- Check `.gitignore` settings
- Verify repository is initialized
- Check remote URL: `git remote -v`

---

## 📝 NOTES

- **Story_Bible errors:** Dr. Marsh profession needs correction (Economist/Psychiatrist/Surgeon)
- **MCP:** May already exist but needs verification/configuration
- **.cursorignore:** Current standard (not `.cursor/ignore/`)
- **Multi-root workspaces:** Will be useful when COMPASS extracted

---

**Last Updated:** Saturday, November 29, 2025  
**Status:** Comprehensive guide complete




