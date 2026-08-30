# Session Summaries

One folder for this novel. Write a file here only when Timothy says the sitting is over (going to bed, leaving for work, “create a session summary”). Not after every chat turn.

**Naming:** `YYYY-MM-DD_HHMM_PDT_Short_Title.md` (use `PST` in winter)

**Examples:**

- `2026-01-13_2130_PST_Draft_2_Planning_Marathon.md`
- `2026-01-15_0930_PST_File_Organization_Cleanup.md`

Retired after-each-turn JSON crumbs (formerly `Chat_Summaries/` and `tmp/summary-*.json`) live in one archive: `2026-02-08_Turn_Recaps_Combined.md`. Do not add to that file. Do not recreate `Chat_Summaries/`.

---

## 📋 NAMING CONVENTION

**Format**: `YYYY-MM-DD_HHMM_PST_Session_Title.md` or `YYYY-MM-DD_HHMM_PDT_Session_Title.md`

**Examples**:

- `2026-01-13_2130_PST_Draft_2_Planning_Marathon.md`
- `2026-01-15_0930_PST_File_Organization_Cleanup.md`
- `2026-01-17_1430_PST_Chapter_00_Rewrite.md`

**Components**:
- **Date**: `YYYY-MM-DD` (sorts chronologically)
- **Time**: `HHMM` (24-hour format, e.g., 2130 = 9:30 PM)
- **Timezone**: `PST` (Pacific Standard Time, Nov-Mar) or `PDT` (Pacific Daylight Time, Mar-Nov)
- **Title**: Brief descriptive title (use underscores, no spaces)

**Why Pacific Time?**
- Timothy works in Pacific Time zone
- Multiple sessions in same day need precise timestamps
- Hyperfocus marathon sessions can span late hours
- Actual time helps distinguish between sessions

---

## 📁 STRUCTURE

```
Session_Summaries/
├── README.md (this file)
├── 2026-01-13_Evening_Draft_2_Planning_Marathon.md
├── 2026-01-15_Morning_File_Organization_Cleanup.md
└── ...
```

---

## 🎯 PURPOSE

**Session Summaries Document**:
- What we achieved
- Key decisions made
- Files created/modified
- Next steps
- Questions to address
- Context for future sessions

**Different from Other Folders**:
- `Active_Draft_2/` = Current work files (blueprints, style guide)
- `Agent_Work/` = Agent feedback on your writing
- `Session_Summaries/` = Daily session documentation

---

## 📝 SESSION SUMMARY FORMAT

**Header** (Required):
```markdown
# YYYY-MM-DD | Time | Session Title

**Date**: [Full date]
**Time**: [Time of day]
**Participants**: Timothy (Author) + Claude (Cursor AI)
**Duration**: [How long]
**Status**: [Current status]
```

**Sections** (Standard):
- Purpose of Document
- Project Overview
- Key Achievements/Breakthroughs
- Files Created/Modified
- Key Decisions Locked In
- Workflow Established
- Next Steps
- Timothy's Working Style & Preferences
- Technical Notes
- Questions to Address
- Notes for Future Sessions

---

## 🚀 USAGE

**At the end of a sitting, when Timothy asks:**

1. Create one session summary with the naming above
2. Save it in this folder
3. Reference it next day for continuity

**Benefits**:
- Continuity across sessions
- Track progress over time
- Reference past decisions
- Clear handoff between sessions
- Context preservation (critical for Timothy's workflow)

---

## 🗂️ FILE LIFECYCLE

**Active Summaries** (this folder):
- Keep all session summaries here
- Never delete (historical record)
- Use for reference when context is lost

**Organization**:
- Chronological order (date in filename ensures sorting)
- One summary per session
- Update README if folder structure changes

---

**This system ensures our work is documented and easily referenced!**

**Last Updated**: 26 August 2026
