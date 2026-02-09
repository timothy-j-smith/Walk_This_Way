# WORKSPACE REORGANIZATION OUTLINE
**Created:** February 9, 2026, ~11:15 PM PST (Pacific Standard Time, Portland, Oregon)  
**Status:** APPROVED -- Execution in progress

---

## TERMINOLOGY GUIDE (Use These Terms Correctly)

**Folder** = A directory on your computer's filesystem (e.g., `Walk This Way/`, `Draft_1/`). This is the basic building block. Everything lives in folders.

**Workspace** = When you open a Folder in Cursor, it becomes a "Workspace." A Workspace is just Cursor's view of a Folder. One Folder = One Workspace. When people say "open a workspace," they mean "open a folder in Cursor."

**Multi-Root Workspace** = A special Cursor feature where you open MULTIPLE Folders in a single Cursor window. Defined by a `.code-workspace` file. Instead of seeing one folder in the sidebar, you see two or more. This is how we share the MCP Library across novels.

**`.code-workspace` file** = A JSON file that tells Cursor which Folders to combine into a Multi-Root Workspace. You double-click this file to open Cursor with all the listed folders visible.

**Git Repository (repo)** = A folder tracked by Git for version control. Each repo has its own `.git/` folder, its own commit history, and its own GitHub remote. One Folder = One Repo (typically).

**MCP (Model Context Protocol) Server** = A tool that runs in the background and gives AI capabilities (search, memory, thinking, etc.). Configured in either user-level or project-level config.

**User-Level MCP Config** (`~/.cursor/mcp.json`) = MCP settings shared across ALL workspaces on your machine. Put your core MCPs here once, and they work everywhere.

**Project-Level MCP Config** (`.cursor/config/mcp.json`) = MCP settings for ONE specific workspace only. Put novel-specific MCPs here (like the Walk This Way filesystem MCP).

**Root Level** = The top level of a folder, what you see first when you open it. "Root-level files" means files sitting at the top, not inside any subfolder.

**Can you put a folder inside a folder?** YES. That is normal and expected. `Draft_1/Act_I/` is a folder inside a folder. Nest as deep as you need.

**Can you put a workspace inside a workspace?** NO, but you do not need to. Multi-Root Workspaces solve this by showing multiple folders side-by-side in one Cursor window.

---

## GIT TERMINOLOGY FOR FICTION WRITERS

**Git Repository (Repo)** = A folder that Git is tracking. It remembers every change you have ever made, like a time machine for your files.

**Commit** = A snapshot of your files at a specific moment. Like taking a photo of your manuscript. Each commit has a unique ID (e.g., `b7969c0`), a message describing what changed, and a timestamp.

**Push** = Send your commits to GitHub (the cloud backup). Your work is now safe online.

**Pull** = Download the latest commits from GitHub to your machine. Do this when switching from Mac Studio to MacBook Air.

**Branch** = A parallel version of your repo. Think of it like a fork in the road.

**Main Branch** = Your primary, "official" branch. This is where your real work lives.

**Why NOT to use branches for novel drafts:** Branches were designed for code where two developers work on the same file and then MERGE their changes together. Novel drafts do not work this way -- Draft 2 does not merge into Draft 1, it replaces it. With branches, you can only see ONE draft at a time. With folders (`Draft_1/`, `Active_Draft_2/`), you see ALL drafts side by side, can compare chapters, and never get confused about "which branch am I on?" **Use folders for drafts, not branches.**

**What branches ARE useful for:** If you wanted to experiment with a radical rewrite of Chapter 10 without risking your current version, you could create a branch, try the rewrite, and either keep it (merge) or throw it away (delete the branch). But for most fiction writing, Git's commit history already lets you go back to any previous version.

---

## USER-LEVEL vs PROJECT-LEVEL MCP -- WITH EXAMPLES

**User-Level MCP Config** (`~/.cursor/mcp.json`)
- Location: Your home folder, hidden file
- Scope: Available in EVERY workspace you open on this machine
- What goes here: MCPs you want everywhere

Example MCPs for User-Level:
- Sequential Thinking (all 5 Brothers) -- you want thinking tools everywhere
- Knowledge Graph Memory -- you want memory everywhere
- DuckDuckGo Search -- you want web search everywhere
- Firecrawl -- you want web scraping everywhere
- GitKraken -- you want Git tools everywhere
- GitHub -- you want GitHub access everywhere

**Project-Level MCP Config** (`.cursor/config/mcp.json`)
- Location: Inside a specific folder's `.cursor/config/` directory
- Scope: ONLY available when that folder is open
- What goes here: MCPs specific to ONE novel or project

Example MCPs for Project-Level:
- `walk-this-way-files` -- a Filesystem MCP that ONLY reads Walk This Way folders
- `phantom-cowboy-files` -- a Filesystem MCP that ONLY reads Phantom Cowboy folders
- A custom Walk This Way character database MCP (if you build one someday)

**The rule:** If you would want it in every novel workspace, put it in User-Level. If it only makes sense for one novel, put it in Project-Level.

---

## CURRENT STATE: Walk This Way Folder (THE PROBLEM)

141 items at the root level. Hard to find anything.

```
Walk This Way/                        (THIS IS ONE FOLDER / ONE GIT REPO)
├── 128 .md files at root level       ← THE CLUTTER (89 are MCP/COMPASS docs)
├── Draft_1/                          ← Novel content (good, organized)
├── Active_Draft_2/                   ← Novel content (good, organized)
├── First_Drafts/                     ← Novel content (good)
├── Story_Bible/                      ← Novel content (good)
├── Completed/                        ← Novel content (good)
├── In_Review/                        ← Novel content (good)
├── Agent_Work/                       ← 40 files of agent output
├── Session_Summaries/                ← 8 session logs
├── SmartWrite/                       ← Writing request system
├── Questions/                        ← 1 question file
├── zz_COMPASS/                       ← 102 COMPASS system files
├── yy_Archive/                       ← 600+ archived files
├── tmp/                              ← 60+ session summary JSONs
├── .cursor/                          ← Cursor config (rules, commands, docs)
├── .vscode/                          ← VS Code settings
└── .git/                             ← Git repository
```

---

## PROPOSED STATE: After Reorganization

### FOLDER 1: Walk This Way (Git Repo -- YOUR NOVEL)

Clean, focused on the novel. Only novel content at the root.

```
Walk This Way/
│
├── Draft_1/                          ← STAYS (36 chapters across 3 Acts)
│   ├── Act_I/
│   ├── Act_II/
│   └── Act_III/
│
├── Active_Draft_2/                   ← STAYS (Draft 2 in progress)
├── Scene_Workshop/                    ← RENAMED from "First_Drafts/" (AI-generated scene drafts before refinement)
├── Story_Bible/                      ← STAYS (characters, timeline, music)
├── Completed/                        ← STAYS (finished chapters)
├── In_Review/                        ← STAYS (chapters under review)
│
├── Novel_Docs/                       ← NEW SUBFOLDER (novel-specific documents)
│   ├── DRAFT_2_MASTER_BLUEPRINT_V2.md
│   ├── DRAFT_2_PROGRESS.md
│   ├── DRAFT_2_FILE_STATUS.md
│   ├── PROJECT_NOTES.md
│   ├── STRUCTURAL_ANALYSIS_FOUR_QUADRANTS.md
│   ├── CURRENT_DOCUMENTS_OUTLINE.md
│   ├── CHAPTER_CRITIQUE_GUIDE.md
│   ├── CHAPTER_CRITIQUE_RESULTS.md
│   ├── CHARACTER_CONSISTENCY_CHECKING_GUIDE.md
│   ├── STORY_BIBLE_SYNC_README.md
│   └── sync_story_bible.py
│
├── Agent_Work/                       ← STAYS but REORGANIZE (see Agent Work section below)
├── Session_Summaries/                ← STAYS (manual session history -- 7 entries)
├── Questions/                        ← STAYS
│
├── DNA/                              ← NEW SUBFOLDER (creative partnership DNA)
│   ├── HANK_DNA.md
│   └── TIMOTHY_WORKING_STYLE_DNA.md
│
├── yy_Archive/                       ← STAYS (Sub-Agent will catalog -- see below)
├── Chat_Summaries/                   ← RENAMED from "tmp/" (automated JSON summaries)
│
├── .cursor/                          ← STAYS (Cursor config, rules, commands)
├── .vscode/                          ← STAYS
├── .git/                             ← STAYS (Git repo)
│
├── README.md                         ← STAYS
├── TODO.md                           ← STAYS
├── DASHBOARD.md                      ← STAYS
│
└── Walk_This_Way.code-workspace      ← NEW (Multi-Root Workspace file)
```

**Result:** Root level goes from 141 items down to about 18. Clean and scannable.

---

### FOLDER 2: MCP Library and COMPASS (Git Repo -- SHARED TOOLS)

A new Folder containing all your MCP research, COMPASS system, Cursor guides, 
and Git guides. This is your "study binder" library -- organized by topic, 
perfect for printing.

This Folder gets added to any novel's Multi-Root Workspace so it is always 
visible in the sidebar alongside your novel.

```
MCP_Library_COMPASS/
│
├── MCP_Encyclopedia/                 ← THE master reference
│   └── MCP_ENCYCLOPEDIA.md
│
├── MCP_Research/                     ← Study binder: MCP deep dives
│   ├── MCP_ARSENAL_RANKED_PRIORITY.md
│   ├── MCP_COMPREHENSIVE_EVALUATION.md
│   ├── MCP_FINAL_RESEARCH_REPORT.md
│   ├── MCP_POWERHOUSE_INTEGRATION_ANALYSIS.md
│   ├── MCP_ADVANCED_CREATIVE_ANALYSIS.md
│   ├── ANTHROPIC_MCP_COMPLETE.md
│   ├── ANTHROPIC_MCP_VERIFICATION_COMPLETE.md
│   ├── LANGUAGE_SPECIFIC_MCPS_RESEARCH.md
│   ├── MCP_ORCHESTRATION_STRATEGY.md
│   ├── MCP_PROFILE_TEMPLATES.md
│   ├── MCP_FOR_MCPS.md
│   ├── MCPs_ADDITIONAL_CONSIDERATION_CATEGORIZED.md
│   ├── MCPs_TO_CONSIDER_REFERENCE.md
│   └── ... (all MCP research files)
│
├── MCP_Setup/                        ← Study binder: setup and API guides
│   ├── MCP_SETUP_COMPLETE_GUIDE.md
│   ├── MCP_SETUP_INSTRUCTIONS.md
│   ├── MCP_FILESYSTEM_SETUP_GUIDE.md
│   ├── MCP_ENABLEMENT_COMPLETE.md
│   ├── API_ACQUISITION_GUIDE.md
│   ├── API_SETUP_PROGRESS.md
│   ├── MCP_API_KEYS_AND_SETUP_REFERENCE.md
│   ├── MCP_EVALUATION_GUIDE.md
│   └── setup_mcp.sh
│
├── Sequential_Thinking/              ← Study binder: the Brothers
│   ├── SEQUENTIAL_THINKING_MCP_REFERENCE.md
│   ├── SEQUENTIAL_THINKING_MCP_APPLICATIONS.md
│   ├── SEQUENTIAL_THINKING_CURSOR_MASTERY.md
│   ├── SEQUENTIAL_THINKING_COMPASS_AUTOMATION_ANALYSIS.md
│   ├── SEQUENTIAL_THINKING_COMPASS_PREMIUM_COMPLETE.md
│   ├── SEQUENTIAL_THINKING_EXECUTION_EVALUATION.md
│   ├── SEQUENTIAL_THINKING_QUICK_WINS_AUTOMATION.md
│   ├── SEQUENTIAL_THINKING_REVERSE_ENGINEERING_MCP.md
│   ├── SEQUENTIAL_THINKING_STYLE_EMULATION_ANALYSIS.md
│   ├── SEQUENTIAL_THINKING_SUBSCRIPTION_OPTIMIZATION.md
│   ├── SEQUENTIAL_THINKING_TECHNICAL_MANUAL_CHAT_ANALYSIS.md
│   └── SEQUENTIAL_THINKING_TOOLBOX_ORCHESTRATOR.md
│
├── COMPASS/                          ← Full COMPASS writing system
│   ├── Agents/                       (moved from zz_COMPASS/)
│   │   ├── Core_5/
│   │   ├── Master/
│   │   └── Special/
│   ├── Commands/
│   ├── Core/
│   ├── MCP_Implementations/
│   ├── Prompts/
│   └── Archive/
│
├── Cursor_Guides/                    ← Study binder: Cursor mastery
│   ├── CURSOR_DEEP_DIVE_GUIDES.md
│   ├── CURSOR_EXTENSIONS_GUIDE.md
│   ├── CURSOR_MASTERY_SEQUENTIAL_THINKING.md
│   ├── CURSOR_PRO_VS_ULTRA_ANALYSIS.md
│   ├── CURSOR_PROJECT_MANAGEMENT_GUIDE.md
│   ├── CURSOR_BUILT_IN_TOOLS_SEQUENTIAL_THINKING.md
│   ├── CURSOR_SETTINGS_VERIFICATION.md
│   ├── CURSOR_SOURCE_CONTROL_GUI_GUIDE.md
│   ├── CURSOR_SUPER_AGENT_ACTION_PLAN.md
│   └── CURSOR_SETUP_COMPLETE.md
│
├── Git_Guides/                       ← Study binder: Git/GitHub/GitKraken
│   ├── GITHUB_AND_GIT_HIDDEN_FEATURES.md
│   ├── GITKRAKEN_QUICK_START.md
│   ├── GITKRAKEN_DESKTOP_GUI_GUIDE.md
│   ├── GITKRAKEN_HIDDEN_FEATURES.md
│   ├── GITKRAKEN_CLI_SETUP.md
│   ├── GIT_GITKRAKEN_GITHUB_WORKFLOW.md
│   ├── GitKraken_MCP_Setup_Summary.md
│   └── SPELL_CHECKER_GUIDE.md
│
├── Automation/                       ← Study binder: Quick Wins and workflows
│   ├── AUTOMATION_SYSTEM_COMPLETE.md
│   ├── AUTOMATION_SYSTEM_DESIGN.md
│   ├── QUICK_WINS_AUTOMATION_COMPLETE.md
│   ├── QUICK_WINS_AUTOMATION_UPGRADE.md
│   ├── QUICK_WINS_IMPLEMENTATION_COMPLETE.md
│   ├── QUICK_WINS_OPTIMIZATION_COMPLETE.md
│   ├── QUICK_WINS_EXAMPLE_TEMPLATE.md
│   ├── QUICK_WINS_TEMPLATE_SCENE_EXAMPLE.md
│   ├── QUICK_WINS_TEMPLATE_VS_DIRECT_COMPARISON.md
│   ├── QUICK_WINS_TEST_EXECUTION.md
│   ├── QUICK_WINS_TEST_GUIDE.md
│   ├── FIRST_DRAFT_GENERATION_WORKFLOW_ANALYSIS.md
│   ├── TOOLBOX_ORCHESTRATOR_FINAL_STATUS.md
│   ├── TOOLBOX_ORCHESTRATOR_IMPLEMENTATION.md
│   ├── TOOLBOX_ORCHESTRATOR_INSTALLATION_COMPLETE.md
│   ├── TOOLBOX_ORCHESTRATOR_SETUP_COMPLETE.md
│   └── CURSOR_API_EXTENSIONS_WORKFLOW_ORCHESTRATOR.md
│
├── Style_MCPs/                       ← Study binder: style emulation
│   ├── DENNIS_LEHANE_MCP_PLAN.md
│   ├── STYLE_EMULATION_DENNIS_LEHANE_INTEGRATION_ANALYSIS.md
│   ├── STYLE_EMULATION_MCP_INSTALLATION_COMPLETE.md
│   ├── STYLE_EMULATION_MCP_SETUP_COMPLETE.md
│   ├── FICTION_REVERSE_ENGINEERING_MCP_COMPLETE.md
│   ├── FICTION_REVERSE_ENGINEERING_MCP_SETUP_COMPLETE.md
│   ├── PROFESSIONAL_EDITOR_MCP_SETUP_COMPLETE.md
│   └── PRE_COMMIT_CONSISTENCY_CHECKING_MCP.md
│
├── Session_Analysis/                 ← Study binder: past session analysis
│   ├── CAROLINA_SESSION_ANALYSIS.md
│   ├── CHAT_TRANSCRIPT_MCP_ANALYSIS.md
│   ├── JAZZ_CHAT_ANALYSIS.md
│   ├── JAZZ_CHAT_QUICK_WINS.md
│   └── COMPASS_SYSTEMS_VS_MCP_ANALYSIS.md
│
├── COMPASS_Docs/                     ← COMPASS planning and roadmap files
│   ├── COMPASS_AUTOMATION_RECOMMENDATION.md
│   ├── COMPASS_MCP_MANIFEST.md
│   ├── COMPASS_PREMIUM_ROADMAP.md
│   ├── COMPASS_PREMIUM_SUMMARY.md
│   └── 01_10_26_CURSOR_COMPASS_ENCYCLOPEDIA.md
│
├── Misc/                             ← Other reference files
│   ├── CHECK_HOMEBREW.md
│   ├── TERMINAL_FIX_ALTERNATIVE.md
│   ├── TERMINAL_STATUS_CHECK.md
│   ├── SUBSCRIPTION_OPTIMIZATION_PLAN.md
│   ├── SESSION_PREP.md
│   ├── build_story_structure_mcp.py
│   └── FOAM NOTE (EST).md
│
├── REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md
│
├── .cursor/                          ← Shared Cursor config for this Folder
│   └── rules/                        (shared rules that apply to all novels)
│
├── .git/                             ← Git repo (separate from Walk This Way)
└── README.md
```

**This Folder is its own Git Repo, pushed to its own GitHub repository.**
**It appears in every novel's sidebar via Multi-Root Workspace.**

---

### FOLDER 3: Tim Cursor Experiment (Git Repo -- SANDBOX)

Pull out useful content, keep as an empty sandbox for future experimentation.

**Pull INTO MCP_Library_COMPASS (if useful):**
- Any MCP research or setup docs
- Any COMPASS-related content
- Any Cursor guides or tips

**Leave behind (keep the Folder as your sandbox):**
- The Git Repo stays active
- The .cursor/ config stays (for testing new MCPs, rules, etc.)
- README.md explaining this is your test/experiment space

```
Tim Cursor Experiment/                ← KEEP AS SANDBOX
├── .cursor/                          ← For testing new MCPs and rules
├── .git/                             ← Stays as its own Git Repo
└── README.md                         ← "This is Timothy's experiment sandbox"
```

---

### FOLDER 4 (Future): The Phantom Cowboy (Git Repo -- NOVEL 2)

When ready, this novel gets its own Folder and Git Repo.

```
The Phantom Cowboy/
├── Draft_1/
├── Story_Bible/
├── Novel_Docs/
├── Agent_Work/
├── .cursor/
│   └── config/
│       └── mcp.json                  ← Phantom Cowboy-specific MCPs only
├── .git/                             ← Its own Git Repo
└── Phantom_Cowboy.code-workspace     ← Opens with MCP_Library_COMPASS
```

The `.code-workspace` file would contain:
```json
{
  "folders": [
    { "path": "." },
    { "path": "../MCP_Library_COMPASS" }
  ]
}
```

---

### FOLDER 5 (Future): Archive (Git Repo)

Eventually, yy_Archive moves here from Walk This Way.

```
Archive/
├── Walk_This_Way/
│   ├── Old_Chapters/
│   ├── Old_Documentation/
│   ├── Original_Writing/
│   ├── Reference_Materials/
│   └── Screenplay/
├── .git/
└── README.md
```

---

## HOW IT ALL CONNECTS (Multi-Root Workspace)

```
                    USER-LEVEL MCP CONFIG
                    (~/.cursor/mcp.json)
                    Contains: Sequential Thinking x5,
                    Knowledge Graph, DuckDuckGo,
                    Firecrawl, GitKraken, etc.
                            |
                    Available in ALL Folders
                            |
            ┌───────────────┼───────────────┐
            |               |               |
    ┌───────▼───────┐ ┌────▼────────┐ ┌────▼──────────────┐
    | Walk This Way | | Phantom     | | Tim Cursor        |
    | (Novel 1)     | | Cowboy      | | Experiment        |
    | Git Repo      | | (Novel 2)   | | (Sandbox)         |
    |               | | Git Repo    | | Git Repo          |
    └───────┬───────┘ └─────┬───────┘ └───────────────────┘
            |               |
            |    Multi-Root |    Multi-Root
            |    Workspace  |    Workspace
            |               |
    ┌───────▼───────────────▼───────┐
    |   MCP Library and COMPASS    |
    |   (Shared Folder)            |
    |   Git Repo                   |
    |                              |
    |   Visible in sidebar of      |
    |   any novel you are working  |
    |   on via .code-workspace     |
    └──────────────────────────────┘
```

When you open `Walk_This_Way.code-workspace`:
- You see TWO root Folders in the sidebar: "Walk This Way" and "MCP Library COMPASS"
- All 20 MCPs are running (from User-Level Config)
- Walk This Way has its own Knowledge Graph memory file
- COMPASS guides and MCP Encyclopedia are right there for reference
- You can switch to `Phantom_Cowboy.code-workspace` and get the same shared library

---

## PHASE EXECUTION ORDER

| Phase | What | When | Status |
|-------|------|------|--------|
| 0 | Push everything to GitHub (safety net) | NOW | Ready |
| 1a | Create MCP_Library_COMPASS Folder | NOW | Ready |
| 1b | Move shared rules there | HOLD (keep in Walk This Way during transition) | Waiting |
| 1c | Create Walk_This_Way.code-workspace file | NOW | Ready |
| 1d | Clean up Walk This Way root (move 89+ files to MCP Library) | AFTER APPROVAL OF THIS OUTLINE | Waiting |
| 1e | Pull useful content from Tim Cursor Experiment | AFTER 1d | Ready |
| 1f | Rename confusing folders (First_Drafts, tmp) | WITH 1d | Ready |
| 1g | Reorganize Agent_Work/ structure | WITH 1d | Ready |
| 1h | Move SmartWrite/ into COMPASS/ | WITH 1d | Ready |
| 2 | Mac Studio reboot (backup to external drive first) | TOMORROW | Waiting |
| 3 | Storage: Local on both machines + GitHub sync | DECIDED | Option B confirmed |
| 4 | Create The Phantom Cowboy Folder | AFTER cleanup is done | Ready |
| 5 | Launch Sub-Agent: COMPASS Auditor | AFTER COMPASS moves to MCP Library | Planned |
| 6 | Launch Sub-Agent: Archive Archaeologist | CAN RUN IN PARALLEL | Planned |
| 7 | Launch Sub-Agent: .cursor/ Config Organizer | AFTER Phase 4 | Planned |
| 8 | COMPASS + MCP Integration Audit | AFTER Sub-Agent 1 completes | Planned |

---

## IMPORTANT TOOL PRESERVATION

Custom tools like `sync_story_bible.py`, `setup_mcp.sh`, and `build_story_structure_mcp.py` 
must be retained and reorganized into the right locations. Many of these were built before 
MCPs existed. Once organized, we should audit all COMPASS tools against current MCP 
capabilities to eliminate redundancy and identify where MCPs make COMPASS stronger.

Tools will move to:
- `sync_story_bible.py` --> Walk This Way/Novel_Docs/ (novel-specific tool)
- `setup_mcp.sh` --> MCP_Library_COMPASS/MCP_Setup/ (shared MCP tool)
- `build_story_structure_mcp.py` --> MCP_Library_COMPASS/MCP_Setup/ (shared MCP tool)
- SmartWrite/ --> Moves INTO COMPASS/ (it is part of the COMPASS system)

---

## RENAMED ITEMS (confusing names fixed)

| Old Name | New Name | Why |
|----------|----------|-----|
| `First_Drafts/` | `Scene_Workshop/` | Confused with `Draft_1/`. Scene_Workshop clarifies this is a staging area for AI-generated scene drafts before they move to chapter files. |
| `tmp/` | `Chat_Summaries/` | "tmp" means nothing. These are automated JSON summaries from the after_each_chat rule. |
| `zz_COMPASS/` | Moves to `MCP_Library_COMPASS/COMPASS/` | No longer needs the "zz_" prefix to sort to the bottom. Gets its own proper home. |

---

## AGENT WORK FOLDER -- PROPOSED REORGANIZATION

Currently 40 files across agent subfolders. Proposed cleaner structure:

```
Agent_Work/
├── By_Agent/                         ← Agent-specific feedback
│   ├── CAROLINA/                     (3 files -- creative feedback)
│   ├── HANK/                         (2 files -- technical guidance)
│   ├── JAZZ/                         (3 files -- discovery/exploration)
│   ├── PROSE_POLISH_EXPERT/          (3 files -- prose refinement)
│   ├── CHARACTER_DEPTH_COACH/        (3 files -- character development)
│   ├── CREATIVE_COLLABORATOR/        (13 files -- creative output)
│   ├── STRATEGIC_WRITING_COORDINATOR/ (4 files -- strategy)
│   └── STRUCTURAL_PERFECTION_SPECIALIST/ (3 files -- structure)
│
├── Cross_Agent/                      ← Work product that spans agents
│   ├── PROSE_DNA.md
│   ├── SCALPEL_HOSE_PHILOSOPHY.md
│   └── SCALPEL_HOSE_APPLIED_TO_WALK_THIS_WAY.md
│
└── README.md                         ← Index of what each agent produced
```

---

## SESSION SUMMARIES -- STATUS CHECK

Two separate systems exist (not connected to each other):

1. **Session_Summaries/** (MANUAL) -- 7 detailed summaries written by you and Claude 
   after major working sessions (Nov 2025 - Jan 2026). These are valuable historical 
   records. NOT automated. Stopped being created when session habits changed.

2. **Chat_Summaries/ (renamed from tmp/)** (AUTOMATED) -- 60+ JSON files created 
   automatically by the `after_each_chat.mdc` rule after every chat turn. These are 
   brief snapshots, useful for session continuity.

Both systems serve different purposes and both should be kept.

---

## SUB-AGENT PROPOSALS

### Sub-Agent 1: COMPASS Auditor

**Purpose:** Dive deep into the 102 files in zz_COMPASS/, organize them, test the 
COMPASS system, identify gaps and broken links, eliminate duplication, and create a 
"COMPASS Working Encyclopedia" that consolidates the critical data.

**Tasks:**
1. Read every file in zz_COMPASS/
2. Map all agents, commands, prompts, and workflows
3. Identify what still works, what is broken, what is redundant
4. Identify where MCPs now do what COMPASS tools used to do manually
5. Create a COMPASS Encyclopedia (like the MCP Encyclopedia)
6. Propose "upgrade" suggestions where MCPs can enhance COMPASS
7. Reorganize the 102 files into clean, intuitive subfolders

**Suggested Agent DNA:** HANK-style (methodical, technical, detail-oriented, 
understands both COMPASS and MCP systems deeply)

**When:** After Phase 1d cleanup is complete and COMPASS has moved to 
MCP_Library_COMPASS/COMPASS/

---

### Sub-Agent 2: Archive Archaeologist

**Purpose:** Read all 600+ files in yy_Archive/, catalog everything, create an 
"Archive Encyclopedia" pulling out critical data, and organize files into intuitive 
subfolders that are easy to search and reference.

**Tasks:**
1. Read every file in yy_Archive/ (600+ files across 9 subfolders)
2. Catalog each file: what it contains, when it was created, why it matters
3. Identify any files that should NOT be in the archive (still needed)
4. Create an Archive Encyclopedia with key findings organized by topic
5. Reorganize into clean subfolders (by date? by topic? by type?)
6. Flag any duplicate content that exists elsewhere in the workspace

**Suggested Agent DNA:** JAZZ-style (thorough explorer, curious, detail-oriented, 
good at finding hidden gems) or CAROLINA-style (analytical, systematic)

**When:** Can run in parallel with other work. Timothy approves the Sub-Agent, 
then it works independently while Timothy and the main agent focus on other tasks.

---

### Sub-Agent 3: .cursor/ Config Organizer

**Purpose:** Review the .cursor/ folder (rules, commands, docs, scripts, configs), 
create a clean template that can be reused for future novels, and identify what is 
novel-specific vs. what is shared.

**Tasks:**
1. Audit all 12 rules, 24 commands, 13 scripts, 131+ docs
2. Separate novel-specific from shared content
3. Create a "Novel Starter Kit" template (.cursor/ config for any new novel)
4. Identify broken references or outdated configs
5. Document what each rule, command, and script does

**Suggested Agent DNA:** HANK-style (technical, systematic, config-focused)

**When:** After Phase 1d cleanup, as part of preparing for The Phantom Cowboy workspace.

---

## WHAT DOES NOT MOVE (stays in Walk This Way)

These are novel-specific and belong with your novel:
- All Draft_1/ chapters
- All Active_Draft_2/ content
- All First_Drafts/ content
- Story_Bible/
- Agent_Work/ (agent output specific to Walk This Way)
- .cursor/docs/ files about Walk This Way chapters, characters, cleanup
- .cursor/rules/walk-this-way-writing-directives.md
- .cursor/docs/Chat_History/ (52 conversation transcripts)

---

## WHAT MOVES (from Walk This Way root to MCP Library)

89 files, organized into "study binder" subfolders:
- 30+ MCP research docs --> MCP_Research/
- 10+ MCP setup/status docs --> MCP_Setup/
- 12 Sequential Thinking docs --> Sequential_Thinking/
- 10 Cursor guide docs --> Cursor_Guides/
- 7 Git/GitKraken docs --> Git_Guides/
- 17 Automation/Quick Wins docs --> Automation/
- 8 Style/Editor MCP docs --> Style_MCPs/
- 5 Session analysis docs --> Session_Analysis/
- 5 COMPASS planning docs --> COMPASS_Docs/
- zz_COMPASS/ folder (102 files) --> COMPASS/

**Nothing is deleted. Everything is moved and organized.**

---

## REVIEW CHECKLIST

Timothy, please review and confirm:

- [ ] Walk This Way root structure looks good?
- [ ] Rename "First_Drafts/" to "Scene_Workshop/" -- agree?
- [ ] Rename "tmp/" to "Chat_Summaries/" -- agree?
- [ ] Agent_Work/ reorganization (By_Agent + Cross_Agent) looks good?
- [ ] SmartWrite/ moving into COMPASS/ makes sense?
- [ ] MCP_Library_COMPASS subfolder organization makes sense?
- [ ] Tim Cursor Experiment plan (empty sandbox) is correct?
- [ ] The Phantom Cowboy template looks right for Novel 2?
- [ ] Sub-Agent 1 (COMPASS Auditor) -- approve concept?
- [ ] Sub-Agent 2 (Archive Archaeologist) -- approve concept?
- [ ] Sub-Agent 3 (.cursor/ Config Organizer) -- approve concept?
- [ ] Any files you want in a different location?
- [ ] Any subfolder names you want changed?
- [ ] Ready to proceed with Phase 0 (push to GitHub)?

---

*This outline was created for review. No files have been moved yet.*
*Once approved, execution will proceed phase by phase.*
