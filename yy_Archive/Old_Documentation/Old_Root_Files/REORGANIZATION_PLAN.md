# FOLDER REORGANIZATION PLAN
## Created: October 8, 2025

## Current State Analysis

### What We Have:
- **Complete manuscript**: `Desktop Walk This Way : needs a lot of work copy TXT.txt` (~1100 lines, all 25 chapters)
- **Revised chapters (Ch 1-6)**: Extracted into individual folders with multiple versions
- **Empty chapter folders (Ch 7-25)**: Placeholder structure
- **Support documents**: 
  - `.cursorrules` (novel-specific)
  - `Universal-Fiction-Templates.md`
  - Various Cursor guides and encyclopedia files
  - `.pages` files (may be outdated)

### Current Issues:
1. No consistent naming convention (some "Ch_01", some "Chapter 4")
2. Multiple versions without clear "working" vs "archive" designation
3. Mixed content types in root (novel content + general Cursor documentation)
4. No dedicated folders for story bible, outlines, research

## Proposed New Structure

```
/Walk_This_Way_Novel/                    # Renamed for clarity
│
├── .git/                                # (Will be created in Phase 2)
├── .gitignore                           # (Will be created in Phase 2)
├── .cursorrules                         # Novel-specific rules (KEEP)
│
├── /Chapters/                           # Clean chapter organization
│   ├── /Ch_01/
│   │   ├── Ch_01_Working.txt           # Active working version
│   │   └── /Archive/                   # Older versions moved here
│   │       ├── Ch_01_Prose_Vault.txt
│   │       ├── Ch_01_alternate.txt
│   │       └── Ch_01_V4.txt
│   ├── /Ch_02/
│   │   ├── Ch_02_Working.txt
│   │   └── /Archive/
│   └── ... (through Ch_25)
│
├── /Story_Bible/                        # Story-specific knowledge base
│   ├── character-bible.md              # All character details
│   ├── timeline-1973-1979.md           # Past events timeline
│   ├── timeline-2024.md                # Present-day Maxanne broadcast
│   ├── music-references.md             # Songs, when they appear, why
│   ├── boston-research.md              # WBCN, venues, historical details
│   ├── sudbury-geography.md            # Hop Brook, neighborhoods
│   └── themes-tracker.md               # Thematic threads through novel
│
├── /Outlines/                           # Planning documents
│   ├── chapter-by-chapter-outline.md   # High-level plan (TO CREATE)
│   ├── scene-list.md                   # Scene-by-scene breakdown
│   ├── act-structure.md                # Three-act breakdown
│   └── synopsis.md                     # Novel summary
│
├── /Writing_Notes/                      # Working notes
│   ├── daily-log.md                    # Track what you work on
│   ├── questions-to-resolve.md         # Things to research/decide
│   ├── revision-notes.md               # What needs fixing per chapter
│   └── continuity-tracker.md           # Ensuring consistency
│
├── /Research/                           # Reference materials
│   ├── 1970s-boston-music-scene.md
│   ├── WBCN-history.md
│   └── construction-industry-1977.md   # For Dan Johnson's accident
│
├── /Drafts/                            # Full manuscript versions
│   ├── Complete_Draft_v1.txt          # Original complete draft
│   └── (future complete drafts)
│
├── /Documentation/                      # How to use this system
│   ├── WORKFLOW.md                     # (Will create in Phase 10)
│   ├── GIT_GUIDE.md                    # (Will create in Phase 10)
│   └── README.md                       # Novel overview
│
└── /Archive_Pre_Reorg/                 # Safety: everything that doesn't fit above
    ├── Cursor guides and documentation
    ├── .pages files
    └── miscellaneous

```

## Reorganization Actions Required

### 1. Create New Folder Structure
- Create all new directories listed above
- Preserve existing chapter folders during transition

### 2. Rename and Consolidate Chapters
**For Chapters 1-6 (have content):**
- Identify the "best" or "most recent" version as `Ch_XX_Working.txt`
- Move alternate versions to `/Archive/` subfolder
- Standardize naming: `Ch_01_Working.txt` (not "Walk This Way TXT.txt")

**For Chapters 7-25 (empty folders):**
- Keep folders as placeholder
- Will populate from complete manuscript later

### 3. Move Complete Draft
- Move `Desktop Walk This Way : needs a lot of work copy TXT.txt` → `/Drafts/Complete_Draft_v1.txt`
- This becomes reference for extracting chapters 7-25

### 4. Create Story Bible Files
- Create template files in `/Story_Bible/`
- Populate with known information from `.cursorrules`

### 5. Archive Miscellaneous Files
**Move to `/Archive_Pre_Reorg/`:**
- All Cursor guide files (these are general, not novel-specific)
- `.pages` files (may be outdated)
- ARTIFACT files (migration guides - not needed in active workspace)

**Keep in root or move appropriately:**
- `.cursorrules` → KEEP in root (Git needs to see it)
- `Universal-Fiction-Templates.md` → This should move UP one directory level (it's for ALL novels, not just this one)

### 6. Create Initial Documentation
- README.md with novel overview
- Empty template files for later population

## Safety Measures

1. **No files will be deleted** - everything goes somewhere
2. **Archives preserve history** - all versions kept in `/Archive/` folders
3. **Complete draft preserved** - original manuscript moved, not modified
4. **Git initialization happens AFTER reorganization** - clean history from start

## Next Steps After Reorganization

1. Initialize Git (Phase 2)
2. Create initial commit with clean structure
3. Set up GitHub backup (Phase 3)
4. Begin systematic revision work

## Questions to Confirm Before Proceeding

1. ✓ For Chapters 1-6: Which version is the "working" version?
   - Default assumption: The non-"Prose Vault" version is working
   
2. ✓ Universal-Fiction-Templates.md: Keep in this novel, or move up for all novels?
   - Recommendation: Move up one directory (it's for all novels)

3. ✓ `.pages` files: Archive or keep?
   - Recommendation: Archive (work in .txt/.md files for Git compatibility)

---

**Status**: Plan complete, ready to implement
**Estimated time**: 20 minutes
**Risk level**: Low (nothing deleted, everything archived)



