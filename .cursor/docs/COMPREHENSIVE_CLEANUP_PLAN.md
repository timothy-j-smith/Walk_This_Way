# COMPREHENSIVE CLEANUP PLAN
**Date:** Saturday, November 29, 2025

---

## 🔍 ISSUES IDENTIFIED

### **1. System Files at Root**
- ✅ `.cursorconfig` - May be outdated (we use `.cursor/config/` now)
- ✅ `.cursorconfig_example` - Example file, can archive
- ✅ `.cursorignore` - Should stay (system file)
- ✅ `.gitignore` - Should stay (system file)
- ✅ `.cspell.json` - Should stay (spell check config)

### **2. Multiple README Files**
- Root `README.md` - Keep (main project readme)
- `.cursor/config/README.md` - Keep (explains config folder)
- `zz_COMPASS/README.md` - Keep (explains COMPASS)
- `HANK_Work/README.md` - Keep (explains HANK system)
- `Original Writing/README.md` - Remove (folder being deleted)

### **3. Story_Bible Duplication**
- `Documentation/STORY_BIBLE.md` - Old consolidated version
- `Story_Bible/` folder - Current canonical location
- **Action:** Archive `Documentation/STORY_BIBLE.md`

### **4. Story_Bible Old .txt Files**
- `10:20:25 Notes from Walk this Way chat TXT 3.txt`
- `1979 BATTLE OF THE BANDS TXT.txt`
- **Action:** Archive to `Archive/Reference_Materials/Story_Bible_Notes/`

### **5. Original Writing Folder**
- **User Request:** Remove entirely
- **References Found:**
  - `.cursor/config/settings.json` - Memory sources (3 references)
  - `.cursor/agents_archive/` - Old historical references
  - `.cursor/docs/` - Historical documentation references
- **Action:** Update all references, then remove folder

### **6. Agent Organization**
- **Issue:** `Agent_Work/` only has 2 agents (Creative_Collaborator, Strategic_Coordinator)
- **Missing:** CHARACTER_DEPTH_COACH, PROSE_POLISH_EXPERT, STRUCTURAL_PERFECTION_SPECIALIST
- **Action:** Create folders for all 5 core agents

### **7. .cursor/agents_archive**
- **What it is:** Old agent files from `Original Writing/.cursor/` that we backed up
- **Issue:** Should be in `Archive/` not `.cursor/`
- **Action:** Move to `Archive/Old_Documentation/agents_archive/`

### **8. Creative_Collaborator Files**
- **Issue:** 12 files, many can be archived
- **Action:** User will review, but we can identify obvious candidates

---

## ✅ CLEANUP ACTIONS

### **Phase 1: System Files**
1. Check if `.cursorconfig` is still needed (compare with `.cursor/config/`)
2. Archive `.cursorconfig_example` if not needed
3. Keep `.cursorignore`, `.gitignore`, `.cspell.json` at root

### **Phase 2: Story_Bible**
1. Archive `Documentation/STORY_BIBLE.md` (old consolidated version)
2. Archive old `.txt` files from `Story_Bible/` folder
3. Keep `Story_Bible/` folder as canonical location

### **Phase 3: Original Writing Removal**
1. Update `.cursor/config/settings.json` - Remove "Original Writing" references
2. Move `.cursor/agents_archive/` to `Archive/Old_Documentation/`
3. Remove `Original Writing/` folder
4. Update any remaining references in docs (historical is OK)

### **Phase 4: Agent Organization**
1. Create folders for all 5 core agents in `Agent_Work/`
2. Move `.cursor/agents_archive/` to Archive
3. Document agent organization structure

### **Phase 5: Creative_Collaborator Review**
1. Identify files that are clearly archive candidates
2. Create archive structure for user review

---

**Ready to execute? Let me know and I'll proceed step by step.**

