# DOCS REVIEW EXECUTION PLAN
**Date:** January 10, 2026  
**Based on:** User decisions in HANK_SUGGESTIONS_FOR_REVIEW.md

---

## ✅ USER DECISIONS FROM REVIEW

### **Files to Keep (User Changes):**
- COMPLETE_ANSWERS.md (changed from Archive to Keep - has "To Do" items)
- CURSOR_ADVANCED_FEATURES_ANALYSIS.md (changed from Archive to Keep - to address "cursorrc")
- VSCODE_SETTINGS_EXPLANATION.md (changed from Archive to Keep - wants spell check enabled)
- COMPREHENSIVE_CLEANUP_PLAN.md (changed from Delete to Keep - was double listed)

### **Files to Archive:**
- DOCUMENTATION_REVIEW_SYSTEM.md (changed from Keep to Archive)

### **Files Already Archived:**
Many files from the ARCHIVE list don't exist in `.cursor/docs/` - they've likely already been archived or deleted.

---

## 📋 ACTION ITEMS FROM USER NOTES

### **1. Enable Spell Check**
- User wants to enable spell check in settings
- Location: `.vscode/settings.json`
- Change `"spell.enabled": false` to `"spell.enabled": true`
- User asks: "What region of Cursor will utilize the spell check is it in the Text Editor?"

### **2. Organize .cursor/docs/ Folder**
- User is considering subfolders: SMARTWRITE, GIT, etc.
- Concern: Don't want it to become a "dumping ground"
- Important files to reference often: STORY_BIBLE_INVENTORY.md, character-voices.md
- User says: "perhaps we make all of our initial changes and circle back on this point unless you have a great idea on how best to organize the .docs folder"

### **3. Add 5 New Author Commands**
- Need to add to COMPLETE_COMMAND_INVENTORY.md
- Authors: Richard Russo, Dennis Lehane, Donna Tartt, Colson Whitehead, Nick Hornby
- Reference: Story_Bible/author-style-library.md

### **4. Address "To Do" Items:**
- FILE_EXPLORER_CHEAT_SHEET.md - has "To Do" items
- MCP_CONFIGURATION.md - has "To Do" items related to MCP
- COMPLETE_ANSWERS.md - has "To Do" items for "cursorrc", "MCP", ".cursor/architecture"

### **5. ASK_TIMOTHY_QUESTIONNAIRE.md**
- User asks: "Do we need to specifically address this list or are we addressing all of these questions in chunks now?"

---

## 🎯 EXECUTION PRIORITY

1. **Enable Spell Check** (Quick win)
2. **Archive DOCUMENTATION_REVIEW_SYSTEM.md** (If it exists)
3. **Organize .cursor/docs/ structure** (User decision needed)
4. **Address "To Do" items** (Can be done systematically)
5. **Add 5 new author commands** (After reviewing author-style-library.md)

---

## 💡 RECOMMENDATION FOR .cursor/docs/ ORGANIZATION

**Option A: Keep Flat Structure (Current)**
- Pros: Simple, easy to search
- Cons: Could get cluttered as it grows

**Option B: Create Subfolders**
- `SmartWrite/` - All SMARTWRITE_*.md files
- `Git/` - All GIT_*.md files  
- `References/` - STORY_BIBLE_INVENTORY.md, character-voices.md, CHAPTER_*.md
- `System/` - SYSTEM_*.md, MCP_CONFIGURATION.md, etc.
- `Guides/` - All *_GUIDE.md files
- `Historical/` - Move archived files here before moving to yy_Archive

**Option C: Minimal Organization**
- Keep most files flat
- Only create `References/` subfolder for frequently accessed files (STORY_BIBLE_INVENTORY.md, character-voices.md)

**My Recommendation:** Option C - Create just a `References/` subfolder for the most important files you reference often, keep everything else flat for now. We can reorganize later if needed.

---

**Ready to execute! Which approach do you prefer?**
