# CLEANUP PLAN - Orphans, Placeholders, Problems
**Date:** January 10, 2026  
**Purpose:** Systematic cleanup after reorganization

---

## CURRENT STATUS

### **Orphans: ~237 files**
- Files not linked/referenced by other files
- Many are expected (archive files, drafts)
- Not urgent - they're just unlinked, not broken

### **Placeholders: ~84 links**
- Broken links/references to non-existent files
- Need fixing - these are broken references
- Many from reorganization (old paths)

---

## CLEANUP STRATEGY

### **Phase 1: Fix Placeholders (Broken Links) - Priority**

**What to Fix:**
1. References to old "Original Writing/" paths
2. References to old ".cursor/" locations that moved
3. Broken cross-references in documentation
4. Outdated file paths in config files

**How:**
- Use Cursor's "All Links" feature to identify broken links
- Update references to new file locations
- Remove links to files that no longer exist

**Files to Check:**
- `.cursor/docs/` - Documentation cross-references
- `README.md` - Project references
- Configuration files - Path references

---

### **Phase 2: Review Orphans (Unlinked Files) - Lower Priority**

**What to Review:**
1. Archive files in `yy_Archive/` (expected to be unlinked)
2. Old documentation files
3. Draft files not in main structure
4. Historical files

**Strategy:**
- Many orphans are expected (archive material)
- Focus on identifying which orphans should be linked
- Don't worry about archive files being unlinked

---

## SPECIFIC ITEMS TO ADDRESS

### **1. Update File Path References**

**Old paths to find and update:**
- `Original Writing/` → Remove or update
- `Documentation/` → `.cursor/docs/` (if referencing)
- Old `.cursor/` locations → New `.cursor/config/` structure

**Files likely to have old paths:**
- README.md
- Documentation files in `.cursor/docs/`
- Configuration files

### **2. Fix Broken Links**

**Common broken links:**
- References to deleted files
- References to moved files
- Cross-references between documentation files

### **3. Clean Up Documentation**

**Items to address:**
- Outdated references in guides
- Links to files that no longer exist
- References to old folder structures

---

## EXECUTION PLAN

### **Step 1: Identify All Placeholders**
```bash
# Use Cursor's "All Links" feature
# Or search for common broken patterns
```

### **Step 2: Update References Systematically**
- Start with README.md
- Then .cursor/docs/ files
- Then configuration files

### **Step 3: Review Orphans**
- Identify which are expected (archive)
- Identify which should be linked
- Leave archive files as-is (they're intentionally unlinked)

---

## NOTES

- **Orphans are not urgent** - Many are expected (archive files)
- **Placeholders need fixing** - Broken links cause confusion
- **After cleanup** - Both numbers should decrease significantly
- **Focus on placeholders first** - They're more problematic than orphans

---

## PROGRESS TRACKING

- [ ] Step 1: Identify all placeholders
- [ ] Step 2: Fix file path references
- [ ] Step 3: Fix broken links in documentation
- [ ] Step 4: Review orphan files
- [ ] Step 5: Verify cleanup results

---

**Next Session:** Start with Step 1 - Identify placeholders systematically
