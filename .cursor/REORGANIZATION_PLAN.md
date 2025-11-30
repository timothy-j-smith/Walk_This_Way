# COMPASS FOLDER REORGANIZATION PLAN
**Logical Waterfall Hierarchy for Easy Navigation & Replication**

**Created:** Saturday, November 29, 2025  
**Goal:** Create clean, logical structure that's easy to navigate, reference, and replicate for Novel #2

---

## CURRENT PROBLEM

**Scattered Configuration Files:**
- `.cursorignore` at root (potentially deprecated)
- `.cursor/` configs split between root and `Original Writing/.cursor/`
- No clear hierarchy
- Hard to find files
- Difficult to replicate for Novel #2

---

## PROPOSED STRUCTURE: LOGICAL WATERFALL HIERARCHY

```
Walk This Way/
│
├── .cursor/                          ← ALL CURSOR CONFIG IN ONE PLACE
│   │
│   ├── settings.json                 ← Editor settings
│   │
│   ├── rules/                        ← Writing rules (replaces .cursorrules)
│   │   └── walk-this-way-writing-directives.md
│   │
│   ├── agents/                       ← All agent definitions
│   │   ├── Core_5/
│   │   │   ├── STRATEGIC_WRITING_COORDINATOR.json
│   │   │   ├── STRATEGIC_WRITING_COORDINATOR.md
│   │   │   ├── STRUCTURAL_PERFECTION_SPECIALIST.json
│   │   │   ├── STRUCTURAL_PERFECTION_SPECIALIST.md
│   │   │   ├── CHARACTER_DEPTH_COACH.json
│   │   │   ├── CHARACTER_DEPTH_COACH.md
│   │   │   ├── PROSE_POLISH_EXPERT.json
│   │   │   ├── PROSE_POLISH_EXPERT.md
│   │   │   ├── CREATIVE_COLLABORATOR.json
│   │   │   └── CREATIVE_COLLABORATOR.md
│   │   │
│   │   ├── Special/
│   │   │   ├── CAROLINA.json
│   │   │   ├── JAZZ.json
│   │   │   └── HANK.json
│   │   │
│   │   ├── Master/
│   │   │   └── Agent.json
│   │   │
│   │   └── Documentation/
│   │       ├── AGENT_ACCESS_QUICK_REFERENCE.md
│   │       ├── AGENT_TESTING_GUIDE.md
│   │       └── HOW_TO_SUMMON_AGENTS.md
│   │
│   ├── commands/                     ← All 25 custom commands
│   │   ├── Writing/
│   │   │   ├── prose.md
│   │   │   ├── dialogue.md
│   │   │   ├── voice.md
│   │   │   ├── detail.md
│   │   │   ├── pacing.md
│   │   │   ├── tension.md
│   │   │   └── poetic.md
│   │   │
│   │   ├── Atmosphere/
│   │   │   ├── atmosphere.md
│   │   │   ├── dark.md
│   │   │   ├── romantic.md
│   │   │   └── tense.md
│   │   │
│   │   ├── Psychological/
│   │   │   ├── emotion.md
│   │   │   ├── intuition.md
│   │   │   └── thoughts.md
│   │   │
│   │   ├── Action/
│   │   │   ├── action.md
│   │   │   └── argument.md
│   │   │
│   │   ├── Style/
│   │   │   ├── russo.md              ← CREATE (priority #1)
│   │   │   ├── lehane.md             ← CREATE (priority #2)
│   │   │   ├── king.md
│   │   │   ├── chbosky.md
│   │   │   ├── goldman.md
│   │   │   ├── harris.md
│   │   │   └── ondaatje.md
│   │   │   └── REMOVE: dickey.md, robinson.md
│   │   │
│   │   └── Analysis/
│   │       ├── coach.md
│   │       ├── pov.md
│   │       └── love.md
│   │
│   ├── prompts.json                  ← All 11 JSON prompts
│   │
│   ├── configs/                      ← Configuration files
│   │   ├── DRAFT_MODES.json
│   │   ├── NOVEL_MEMORY_CONFIG.md
│   │   ├── meta-instructions.md
│   │   └── writing_modes.json
│   │
│   ├── docs/                         ← Documentation & guides
│   │   ├── character-voices.md
│   │   ├── COMPASS_ENCYCLOPEDIA_ANALYSIS.md
│   │   └── REORGANIZATION_PLAN.md (this file)
│   │
│   ├── logs/                         ← Session logging
│   │   └── writing-sessions.jsonl
│   │
│   ├── ignore/                       ← File ignore patterns (if deprecated from root)
│   │   └── .cursorignore
│   │
│   └── workflows/                    ← Workflow templates
│       └── EXAMPLE_WORKFLOW_TEMPLATE.md
│
├── .gitignore                        ← Git ignore patterns
├── .git/                             ← Git repository (if initialized)
│
└── [Rest of project structure...]
```

---

## MIGRATION STEPS

### PHASE 1: Consolidate .cursor/ Structure

1. **Move all Original Writing/.cursor/ files to root .cursor/**
   - `agents/` → `.cursor/agents/` (organize into subfolders)
   - `commands/` → `.cursor/commands/` (organize into subfolders)
   - `prompts.json` → `.cursor/prompts.json`
   - `workspace.json` → `.cursor/configs/workspace.json`
   - `tools.json` → `.cursor/configs/tools.json`
   - `writing_modes.json` → `.cursor/configs/writing_modes.json`
   - `system_messages.md` → `.cursor/configs/system_messages.md`

2. **Create logical subfolders**
   - Organize agents into Core_5/, Special/, Master/, Documentation/
   - Organize commands into Writing/, Atmosphere/, Psychological/, Action/, Style/, Analysis/
   - Move configs to configs/ subfolder
   - Move docs to docs/ subfolder

3. **Handle .cursorignore**
   - Check if deprecated
   - If yes: Move to `.cursor/ignore/.cursorignore`
   - If no: Keep at root but verify structure

### PHASE 2: Update All File References

1. **Update .cursor/settings.json**
   - Fix all paths to point to new locations

2. **Update agent files**
   - Update contextFiles arrays with new paths

3. **Update COMPASS rules file**
   - Update all references to new structure

4. **Update documentation**
   - Fix all path references

### PHASE 3: Archive Reference Material

1. **Create Archive/Reference_Materials/**
   - Move Encyclopedia volumes
   - Move old documentation
   - Keep accessible but organized

2. **Create Archive index**
   - Document what's in Archive and why

### PHASE 4: Clean Up

1. **Remove duplicate files**
   - Delete old `.cursorrules` (after migration verified)
   - Remove duplicate .gitignore if needed

2. **Verify nothing broken**
   - Test agent access
   - Test command access
   - Test prompts access

---

## BENEFITS OF THIS STRUCTURE

1. **Easy Navigation:** Everything in logical folders
2. **Easy Replication:** Copy entire `.cursor/` folder for Novel #2
3. **Clear Hierarchy:** Commands organized by purpose
4. **Scalable:** Easy to add new commands/agents
5. **Maintainable:** All configs in one place

---

## CRITICAL FILES TO KEEP VISIBLE

These should NOT be archived:
- `.cursor/rules/walk-this-way-writing-directives.md`
- `.cursor/agents/` (all agent files)
- `.cursor/commands/` (all command files)
- `.cursor/prompts.json`
- `.cursor/configs/` (all configs)
- `.cursor/docs/character-voices.md`

---

## ARCHIVE CANDIDATES

Move to `Archive/Reference_Materials/`:
- Encyclopedia Volumes (already in Archive_Pre_Reorg/)
- Old documentation versions
- Historical notes and planning docs
- Old system documentation that's been superseded

---

**Ready to execute reorganization when approved**

