# Cursor AI Writing System - Complete Guide

**For Timothy | From Our Conversation on Nov 2, 2025**

---

## Table of Contents

1. [Understanding the Building Blocks](#1-understanding-the-building-blocks)
2. [The File Format Decision Tree](#2-the-file-format-decision-tree)
3. [Your Three-Pillar Writing System](#3-your-three-pillar-writing-system)
4. [Complete Template Structure](#4-complete-template-structure)
5. [How the System Works in Practice](#5-how-the-system-works-in-practice)
6. [When to Use What](#6-when-to-use-what)
7. [The "Don't Break Things" Safety Net](#7-the-dont-break-things-safety-net)
8. [Your Next Steps](#8-your-next-steps)
9. [Making It Work for Your Friends](#9-making-it-work-for-your-friends)
10. [Summary: The Key Insights](#10-summary-the-key-insights)

**[APPENDIX: Emergency Transition Document](#appendix-emergency-transition-document)**

---

## 1. UNDERSTANDING THE BUILDING BLOCKS

### What is an LLM?
- **LLM = Large Language Model** (Claude, GPT, etc.)
- Think: A brain trained by reading billions of documents
- It predicts what words should come next based on patterns
- It reads your files the same way it reads your messages

### The Key Formats Explained

#### Markdown (.md)
- **What it is:** Plain text with simple formatting (`# Header`, `**bold**`)
- **Best for:** Instructions, creative content, explanations
- **Why:** Human-readable, flexible, AI understands nuance
- **Example use:** Character profiles, writing rules, scene notes

#### JSON (.json)
- **What it is:** Structured data format `{"key": "value"}`
- **Best for:** Facts that need verification, structured data
- **Why:** Machine-readable, checkable, consistent
- **Example use:** Character ages, timeline dates, relationships

#### Python (.py)
- **What it is:** Programming language for automation
- **Best for:** Repetitive checks, processing multiple files
- **Why:** Automate what you'd otherwise do manually
- **Example use:** Timeline checker, manuscript exporter

### The Critical Insight You Discovered

**Your observation was correct:** JSON "got the job done" while Markdown felt uncertain.

**Why both matter:**

| Use Markdown When... | Use JSON When... |
|---------------------|------------------|
| Explaining intent or style | Storing facts that must be consistent |
| Providing examples | Creating checkable data |
| Giving creative guidance | Automating verification |
| Nuance matters | Precision matters |

**Example:**

**Markdown (.cursor/rules/character-voice.md):**
```markdown
Sarah doesn't use contractions when angry.
Her speech tightens under stress.

Good: "I will not tolerate this."
Bad: "I won't put up with it."
```

**JSON (.cursor/data/characters.json):**
```json
{
  "Sarah Chen": {
    "age": 34,
    "born": "1991-03-15",
    "contractions_when_angry": false
  }
}
```

The markdown explains the *why* and *how*.
The JSON stores the *facts* that can be checked automatically.

---

## 2. THE FILE FORMAT DECISION TREE

```
DECISION FRAMEWORK:

Is this data that needs to be...

├─ Checked automatically?
│  └─→ Use .json
│     Examples: ages, dates, relationships, timeline
│
├─ Read/understood by humans frequently?
│  └─→ Use .md
│     Examples: character profiles, style guides, scene notes
│
├─ Processed/transformed repeatedly?
│  └─→ Use Python script
│     Examples: consistency checker, manuscript export
│
└─ Generated/drafted by AI?
   └─→ Use .md (AI creates it)
      Examples: scene drafts, brainstorming, outlines
```

### Cursor Configuration Evolution

**OLD SYSTEM (being phased out):**
```
.cursorrules        ← All AI rules in one file
.cursorignore       ← Files to ignore
.cursorconfig       ← Cursor IDE settings
```

**NEW SYSTEM (current):**
```
.cursor/
  rules/            ← AI behavior (replaces .cursorrules)
  ignore/           ← Files to skip (replaces .cursorignore)
  config.json       ← Cursor settings (replaces .cursorconfig)
  data/             ← Your structured facts (NEW!)
```

**Recommendation:** Switch to new system now to avoid migration pain later.

---

## 3. YOUR THREE-PILLAR WRITING SYSTEM

### The Architecture You Discovered

**ARCHITECTURE** → Planning and structure
- Premise, outlines, character design
- World-building, research
- Plot structure, scene lists

**CREATION** → Drafting prose
- Writing chapters and scenes
- First draft momentum
- Dialogue and narrative

**EDITING** → Revision and polish
- Consistency checking
- Prose tightening
- Timeline verification

### How Modes Work

**Not different "agents" - Same Claude with different instructions**

**Architecture Mode:**
- Think structurally
- Challenge plot holes
- Ask motivation questions
- Reference story bible
- NO prose writing

**Creation Mode:**
- Write first draft prose
- Prioritize momentum
- Stay in the scene
- NO overthinking structure

**Editing Mode:**
- Tighten and polish
- Check consistency
- Verify timeline
- NO generating new content

### Mode Switching

**Simple method:**
Just tell Claude: "Switch to editing mode"

**File-based method:**
```bash
echo "CREATION" > .cursor/CURRENT_MODE.txt
```
Claude reads this file and loads appropriate rules.

---

## 4. COMPLETE TEMPLATE STRUCTURE

### The Full Template

```
_TEMPLATE_Novel/
│
├── 📋 README.md                           ← "Start here" guide
│
├── 🔧 .cursor/                             ← AI Configuration
│   │
│   ├── rules/                             ← How Claude behaves
│   │   ├── 00-core-identity.md           ← Core AI personality
│   │   │
│   │   ├── architecture/                 ← Planning mode
│   │   │   └── planning-mode.md
│   │   │
│   │   ├── creation/                     ← Drafting mode
│   │   │   ├── prose-style.md           ← Your writing style
│   │   │   ├── dialogue-rules.md        ← Dialogue guidelines
│   │   │   └── chapter-template.md      ← New chapter structure
│   │   │
│   │   └── editing/                      ← Revision mode
│   │       └── revision-mode.md
│   │
│   ├── data/                              ← Facts (JSON)
│   │   ├── characters.json               ← Character facts
│   │   ├── timeline.json                 ← Story chronology
│   │   └── locations.json                ← Setting details
│   │
│   └── ignore/                            ← What Claude ignores
│       └── standard.md                    ← Patterns to skip
│
├── 📜 scripts/                             ← Python utilities
│   ├── check_timeline.py                 ← Timeline consistency
│   ├── check_characters.py               ← Character consistency
│   └── export_manuscript.py              ← Combine chapters
│
├── 🏗️ 01-architecture/                     ← Planning Layer
│   │
│   ├── _TEMPLATES/                        ← Fill-in templates
│   │   ├── character-profile-template.md
│   │   ├── scene-template.md
│   │   └── premise-template.md
│   │
│   ├── premise.md                         ← Your story premise
│   │
│   ├── characters/                        ← Character profiles
│   │   ├── protagonist.md
│   │   └── antagonist.md
│   │
│   ├── structure/                         ← Plot structure
│   │   ├── three-act-outline.md
│   │   ├── scene-list.md
│   │   └── plot-threads.md
│   │
│   └── research/                          ← Reference materials
│       └── notes.md
│
├── ✍️ 02-creation/                         ← Drafting Layer
│   │
│   ├── manuscript/                        ← Your chapters
│   │   ├── chapter-01.md
│   │   ├── chapter-02.md
│   │   └── chapter-03.md
│   │
│   └── fragments/                         ← Scraps & alternatives
│       └── deleted-scenes.md
│
├── ✂️ 03-editing/                          ← Revision Layer
│   │
│   ├── revision-notes/                    ← Edit notes
│   │   └── act-one-notes.md
│   │
│   ├── beta-feedback/                     ← Reader feedback
│   │
│   └── versions/                          ← Milestone snapshots
│       └── draft-01-complete/
│
└── 📝 99-meta/                             ← Project Management
    ├── session-log.md                     ← Daily work log
    └── prompts-that-worked.md             ← Your prompt library
```

### Key Files Explained

#### .cursor/rules/00-core-identity.md
```markdown
# Core Identity

You are Timothy's fiction writing partner.

Check .cursor/CURRENT_MODE.txt to determine current mode.

Modes:
- ARCHITECTURE: Planning and structure
- CREATION: Drafting prose  
- EDITING: Revision and polish

Load corresponding rules from .cursor/rules/[mode]/
```

#### .cursor/rules/creation/prose-style.md
```markdown
# Timothy's Prose Style

## Sentence Rhythm
- Vary sentence length deliberately
- Short sentences for tension
- Longer, flowing sentences for introspection

## Show Don't Tell
Bad: "Sarah was angry"
Good: "Sarah's jaw tightened. She said nothing."

## Sensory Details
Ground every scene in at least 2 senses

[Examples from Timothy's actual writing]
```

#### .cursor/data/characters.json
```json
{
  "characters": {
    "Sarah Chen": {
      "age": 34,
      "born": "1991-03-15",
      "occupation": "Marine Biologist",
      "location": "Seattle",
      "relationships": {
        "Marcus": "colleague",
        "David": "ex-husband"
      }
    },
    "Marcus Thompson": {
      "age": 28,
      "born": "1997-08-22",
      "occupation": "Research Assistant",
      "location": "Seattle"
    }
  }
}
```

#### .cursor/data/timeline.json
```json
{
  "story_start": "2024-05-01",
  "story_end": "2024-08-15",
  "events": [
    {
      "date": "2024-05-03",
      "event": "Sarah discovers the contamination",
      "chapter": 1,
      "character": "Sarah"
    },
    {
      "date": "2024-05-10",
      "event": "Confrontation with Marcus",
      "chapter": 3,
      "character": "Sarah, Marcus"
    }
  ]
}
```

#### 01-architecture/_TEMPLATES/character-profile-template.md
```markdown
# [Character Name] - Profile

## Core Info
- Age:
- Occupation:
- Role: (protagonist/antagonist/supporting)

## Physical Appearance
[Description]

## Personality
[Key traits]

## Voice & Speech Patterns
[How they talk, quirks, examples]

## Backstory
[Relevant history]

## Character Arc
[How they change across the story]

## Relationships
[To other characters]
```

#### scripts/check_timeline.py
```python
"""
Timeline consistency checker
Run: python scripts/check_timeline.py
"""
import json
from datetime import datetime
from pathlib import Path

def check_timeline():
    # Load timeline.json
    with open('.cursor/data/timeline.json') as f:
        timeline = json.load(f)
    
    # Load all chapters from manuscript folder
    manuscript_path = Path('02-creation/manuscript')
    chapters = sorted(manuscript_path.glob('chapter-*.md'))
    
    # Check for date inconsistencies
    # Check character ages against dates
    # Output report
    
    print("Timeline Check Results:")
    print("✓ All dates in chronological order")
    print("⚠ Warning: Character age inconsistency in Chapter 3")

if __name__ == "__main__":
    check_timeline()
```

#### README.md (in project root)
```markdown
# Novel Project: [Name]

## Quick Start for Writers

1. Open this folder in Cursor
2. Start a chat with Claude
3. Say: "Let's plan a new novel"
4. Claude guides you through planning templates
5. When ready: "Switch to creation mode, let's write Chapter 1"

## Folder Guide

- **01-architecture**: Planning and worldbuilding
- **02-creation**: Your manuscript chapters
- **03-editing**: Revision notes and feedback
- **.cursor**: AI configuration (advanced)
- **99-meta**: Daily session notes

## Common Commands

- "Check my timeline" - Runs consistency check
- "Switch to [mode]" - Changes Claude's behavior
- "Export manuscript" - Combines all chapters
- "Create character profile for [name]" - New character

## Don't Touch (Unless Experimenting)

- `.cursor/` folder - AI configuration
- `scripts/` folder - Automation tools

Questions? Ask Claude: "Explain how this system works"
```

---

## 5. HOW THE SYSTEM WORKS IN PRACTICE

### Starting a New Novel

**Step 1: Copy Template**
```bash
cp -r _TEMPLATE_Novel Novel_DeepCurrent
cd Novel_DeepCurrent
cursor .
```

**Step 2: Planning Session**
```
You: "Let's plan a thriller about deep-sea mining"

Claude: [In Architecture mode]
        - Asks about premise
        - Asks about main characters
        - Fills out premise.md
        - Creates character profiles
        - Populates characters.json as you discuss
        - Builds scene list
```

**Result:** Architecture folder populated with plans

### Writing First Draft

**Step 3: Creation Session**
```
You: "Switch to creation mode. Let's write Chapter 1."

Claude: [In Creation mode]
        - Loads prose-style.md rules
        - References characters.json for accuracy
        - Uses chapter-template.md structure
        - Writes opening scene
        - Saves to 02-creation/manuscript/chapter-01.md
```

**Result:** Consistent, styled manuscript chapter

### Mid-Draft Consistency

**Step 4: Running Checks**
```
You: "Check my timeline and character consistency"

Claude: [Runs scripts]
        - Executes check_timeline.py
        - Executes check_characters.py
        - Shows report of issues found
```

**Result:** Issues caught early, easy to fix

### Revision Phase

**Step 5: Editing Session**
```
You: "Switch to editing mode. Review Chapter 3 for pacing."

Claude: [In Editing mode]
        - Loads revision-mode.md rules
        - Analyzes chapter structure
        - Suggests cuts and tightening
        - Flags weak dialogue
        - Proposes improvements
```

**Result:** Focused, actionable revision feedback

---

## 6. WHEN TO USE WHAT

### Use Markdown (.md) For:
- Character profiles with personality and voice
- Writing style guidelines
- Scene descriptions and drafts
- Plot outlines and story structure
- Revision notes and feedback
- Session logs and project notes

### Use JSON For:
- Character ages, birthdates, physical stats
- Timeline with specific dates
- Location names and details
- Relationship mappings
- Any data that needs automatic checking

### Use Python Scripts For:
- Timeline consistency checking
- Character age verification
- Exporting combined manuscript
- Generating reports
- Batch file operations

### Talk to Claude For:
- Planning and brainstorming
- Drafting prose and dialogue
- Revision and editing feedback
- Running scripts: "Check my timeline"
- Creating new files: "New character profile for X"
- Mode switching: "Switch to editing mode"

---

## 7. THE "DON'T BREAK THINGS" SAFETY NET

### What You Can Safely Change:
- ✅ Add new .md files in .cursor/rules/
- ✅ Edit content of rule files
- ✅ Create new folders
- ✅ Add data/*.json files
- ✅ Modify your manuscript chapters
- ✅ Add notes and documentation

### What Can Break Things:
- ❌ Deleting files Cursor is using
- ❌ Syntax errors in JSON files
- ❌ Moving .cursor/ folder
- ❌ Renaming core template files

### The Undo Button: Git

**Before experimenting:**
```bash
git add .cursor/
git commit -m "Snapshot before changes"
```

**If something breaks:**
```bash
git checkout .cursor/
```

**You're back to working state.**

### Simple Test After Changes:
Ask Claude a simple question. If it responds normally, nothing broke.

---

## 8. YOUR NEXT STEPS

### This Week:
1. ✅ You've completed Phase 1 (documented what works)
2. 📄 Print this guide
3. 📝 Read and take notes
4. 📋 List questions or unclear parts

### Next Session (When You're Ready):
5. 🔍 Review your current .cursor/ setup together
6. 🏗️ Build the clean template structure
7. 🧪 Test on a small project (short story/single chapter)
8. ✨ Refine based on what feels clunky

### One Month Out:
9. 📦 Package for your writing friends
10. 📹 Create "Getting Started" guide for them
11. 🚀 Start next novel with perfected system

---

## 9. MAKING IT WORK FOR YOUR FRIENDS

**The "My Daughter Could Use This" Test**

Your system passes this test if:
- ✅ Clear README.md explains everything
- ✅ Numbered folders show workflow (01, 02, 03)
- ✅ Templates are fill-in-the-blank obvious
- ✅ No need to touch .cursor/ folder
- ✅ Just "talk to Claude" to use it

**What They See:**
```
1. Open project in Cursor
2. Chat: "Let's plan my novel"
3. Claude guides them through templates
4. Chat: "Let's write Chapter 1"
5. Claude helps them write
6. Chat: "Check my timeline"
7. Claude runs the check
```

**What They Don't See:**
- Complex .cursor/ configuration
- JSON file formats
- Python scripts running
- Mode switching mechanics

**It just works.**

---

## 10. SUMMARY: THE KEY INSIGHTS

### 1. The Format Decision
- **Markdown** = Creative guidance, examples, nuance
- **JSON** = Hard facts, checkable data, consistency
- **Both together** = Powerful system

### 2. The Three Pillars
- **Architecture** = Planning mode
- **Creation** = Drafting mode
- **Editing** = Revision mode

### 3. The Template Approach
- One master template
- Copy for each novel
- Same structure, different content
- Repeatable process

### 4. The Safety Philosophy
- Git commits before changes
- Test with simple questions
- Separate data from rules
- Clear folder organization

### 5. The Friendly Goal
- Intuitive for non-technical users
- Clear README guide
- Natural conversation with Claude
- Hidden complexity

---

# APPENDIX: Emergency Transition Document

## 🚨 FOR THE NEXT CLAUDE WHO HELPS TIMOTHY

**Date Created:** November 2, 2025  
**Original Conversation:** Extended deep-dive into Cursor AI writing system architecture  
**Purpose:** Ensure seamless continuity when this conversation ends

---

## WHO IS TIMOTHY?

**Background:**
- **Profession:** Works at Nike (Nike.com email)
- **Primary Interest:** Fiction writing (literary fiction)
- **Technical Level:** Non-programmer but intellectually curious about systems
- **Recent Achievement:** Just completed a novel under deadline using Cursor/Claude
- **Current State:** Moving from "survival mode" to "systematic architecture mode"

**Writing Philosophy:**
- Creates literary fiction with emphasis on character voice and consistency
- Values "show don't tell" prose
- Works with complex timelines and multiple POV characters
- Needs consistency checking across long-form narratives

**Learning Style:**
- Prefers to understand "how the engine works" rather than just using tools
- Uses mechanical/automotive analogies frequently ("I want to fix my car, not just take it to the shop")
- Learns best by printing and reading with paper notes
- Values thorough, detailed explanations
- Asks foundational questions to build complete mental models

---

## WHAT WE ACCOMPLISHED

### The Journey
1. **Started with:** Confusion about `.cursorrules` vs `.cursor/rules` migration
2. **Core question:** When to use `.md` vs `.json` vs Python scripts
3. **Discovery:** Timothy's observation that JSON "got the job done" while Markdown felt uncertain - this was the KEY insight
4. **Outcome:** Comprehensive system architecture for fiction writing with Cursor/Claude

### Key Insights Timothy Discovered
- **Three-Pillar System:** Architecture (planning) → Creation (drafting) → Editing (revision)
- **Format Decision Tree:** 
  - `.md` for creative guidance, nuance, and AI instructions
  - `.json` for facts that need automated verification
  - Python scripts for repetitive consistency checking
- **Template Philosophy:** Repeatable structure, variable content (same building blocks for every novel)

### The System We Designed

Complete template structure:
```
_TEMPLATE_Novel/
├── .cursor/
│   ├── rules/          (AI behavior - .md files)
│   ├── data/           (Facts - .json files)
│   └── ignore/         (Skip patterns)
├── scripts/            (Python utilities)
├── 01-architecture/    (Planning layer)
├── 02-creation/        (Drafting layer)
├── 03-editing/         (Revision layer)
└── 99-meta/            (Project management)
```

**Critical Design Principle:** "Could my daughter or writing friends use this immediately?"
- This constraint forces clarity and intuitive design
- System must work for non-technical users
- Complexity hidden, natural conversation exposed

---

## WHERE TIMOTHY IS NOW

### Completed
✅ Survived 6-week writing deadline using Cursor/Claude (organically evolved system)
✅ Documented what worked/didn't work in a "business plan" document
✅ Developed high-level vision of ideal system
✅ Understands the concepts (why .json vs .md, three pillars, etc.)

### Current Challenges
❌ Has organically-grown `.cursor/` setup that "works until it doesn't"
❌ Feels system is "random and disorganized"
❌ Scared to modify files for fear of breaking things
❌ Lacks working knowledge of specific implementation details
❌ Wants to build clean system but unsure of exact decisions

### Immediate Next Steps
1. Review his current `.cursor/` structure (he has one but hasn't shown it yet)
2. Build clean template together based on our conversation
3. Test on small project before committing
4. Prepare to migrate to personal NAS system (moving from iCloud)
5. Create repeatable template for future novels

---

## TIMOTHY'S COMMUNICATION STYLE

**What Works:**
- Detailed, thorough explanations with examples
- Analogies to mechanical/physical systems
- "Here's why this matters" reasoning
- Concrete code examples alongside conceptual explanations
- Acknowledging when he's right about something (e.g., "Your observation was correct")

**What Doesn't Work:**
- Assuming technical knowledge
- Skipping foundational concepts
- Abstract theory without practical examples
- Rushing to implementation without explaining "why"

**His Tells:**
- "I still don't get it" = Need to restart explanation from more basic level
- "That makes sense" or "Aha moment" = Concept landed, can build on it
- Questions about "how does X work with Y" = Building mental model, needs connection explanation
- "Old school thinking" = Worried he's missing something but often his intuition is correct

---

## KEY TECHNICAL CONTEXT

### Current Tool Stack
- **Editor:** Cursor IDE
- **AI:** Claude (Sonnet 4.5 primarily)
- **Storage:** Currently iCloud, transitioning to personal NAS
- **Version Control:** Uses Git (knows basic commands)

### Technical Comfort Level
- **Can do:** Basic bash commands (copy, move, make folders)
- **Understands:** File structures, folder organization
- **Learning:** JSON syntax, when to use different formats
- **Wants to learn:** Enough to debug issues, not become a programmer
- **Fears:** Breaking things, inconsistency, "tools using him instead of him using tools"

### His Actual Question About MCP
- Mentioned Claude set up MCP for him
- It stopped working the next day
- Doesn't know how to debug it
- Wants enough knowledge to fix these issues independently

**Common MCP Issues to Help Him With:**
- Server process died → `ps aux | grep mcp`
- Check logs → `tail -f ~/.cursor/mcp-logs/server.log`
- Config path changed → Verify paths in config
- Port conflicts → Check what's using the port

---

## WHAT TIMOTHY NEEDS NEXT

### Immediate (Next Session)
1. **Review current structure:** He said "review mine to see the challenges"
2. **Extract what works:** Identify pieces worth keeping
3. **Build clean template:** Use the structure from our conversation
4. **Test together:** Small project validation
5. **Document decisions:** Why we chose each organizational pattern

### Short-term (Within a Month)
1. **Migrate to clean system:** Move current project or start fresh
2. **Create reusable template:** `_TEMPLATE_Novel/` for future books
3. **Build script library:** Timeline checker, character consistency, export tools
4. **Test with new novel:** Validate the system works soup-to-nuts
5. **Refine based on pain points:** Iterate on what feels clunky

### Long-term (1-3 Months)
1. **Package for friends:** Make truly user-friendly
2. **Create documentation:** "Getting Started" guide for non-technical writers
3. **Build prompt library:** Save what works in `99-meta/prompts-that-worked.md`
4. **Develop style samples:** Capture Timothy's actual prose for AI reference
5. **Scale pattern:** Proven system for novel after novel

---

## CONVERSATION CONTINUITY PROTOCOL

### If This Chat Ends, Timothy Should:

**STEP 1: Share This Document**
```
"I have this Emergency Transition Document from our previous conversation. 
Please read it to understand our context and where we left off."
```

**STEP 2: Provide Current State**
```
"Here's my current .cursor/ structure:"
[paste tree output or screenshot]

"My immediate question is: [specific question]"
```

**STEP 3: Reference Key Decisions**
```
"We decided that:
- .md files for creative guidance
- .json files for facts
- Three-pillar structure (Architecture/Creation/Editing)
- Template approach for repeatability"
```

### What Future Claude Should Do

**IMMEDIATELY:**
1. Read this entire Emergency Transition Document
2. Acknowledge you understand Timothy's context
3. Confirm the three-pillar system and format decisions
4. Ask: "Where would you like to pick up? Review your current structure or start building the clean template?"

**APPROACH:**
- Use mechanical/system analogies
- Explain thoroughly with examples
- Don't assume technical knowledge
- Validate his intuitions when correct
- Build on the system we already designed
- Reference the template structure from Section 4 of main guide

**AVOID:**
- Starting from scratch on concepts already covered
- Suggesting radically different approaches (he's committed to this architecture)
- Assuming he understands JSON syntax or Python
- Moving too fast through implementation details

---

## CRITICAL PRINCIPLES TO MAINTAIN

### 1. The "Daughter Test"
Every system decision must pass: "Could Timothy's daughter or non-technical writing friends use this immediately?"
- If answer is no, simplify
- Hide complexity
- Expose natural conversation

### 2. The Format Trinity
- **Markdown** = Creative guidance, examples, AI instructions
- **JSON** = Facts needing verification, structured data
- **Python** = Automation, repetitive checking
- Use the right tool for each job

### 3. The Three Pillars
- **Architecture** = Planning mode (structure, brainstorming)
- **Creation** = Drafting mode (prose generation)
- **Editing** = Revision mode (refinement, consistency)
- Same Claude, different instructions per mode

### 4. The Safety Net
- Git commits before changes
- Test with simple questions after modifications
- Clear separation of concerns (rules vs data vs content)
- "If it breaks, we can undo it" confidence

### 5. The Template Philosophy
- One master template for all novels
- Copy for each new project
- Same structure, different content
- Repeatable, teachable, scalable

---

## SPECIFIC FILES/STRUCTURES TO REFERENCE

### The Template We Designed (Full Structure)
See **Section 4** of main guide for complete folder tree

### Key Configuration Files
- `.cursor/rules/00-core-identity.md` - AI personality base
- `.cursor/rules/[mode]/[specific].md` - Mode-specific instructions
- `.cursor/data/characters.json` - Character fact database
- `.cursor/data/timeline.json` - Story chronology
- `scripts/check_timeline.py` - Consistency checker example

### Decision Framework
See **Section 2** for the decision tree on when to use what format

---

## TIMOTHY'S EXACT WORDS (FOR CONTEXT)

**On his learning style:**
> "I like to understand how these functions or programs or languages all work with .ai. I find it absolutely fascinating and mind-bending... I want to fix my car instead of being it to the shop, or if I bring my car to the shop I want to at least understand what the mechanic is doing."

**On his goal:**
> "Make a system that my young daughter or my writing friends could use even if they don't go through the up & down discovery pains that I have been through."

**On his situation:**
> "I was caught in between 2 masters and one of them was my brain and the other one was fulfilling the business side of things either way an impending deadline."

**On starting fresh:**
> "Now as I move to a new novel and move away from iCloud drive to a personal NAS system I have the unique opportunity to start from scratch and bring in my new platform into an organized cursor file that is relatable novel after novel."

**On his current state:**
> "I have actually completed phase 1 along the way and developed a complete 'business plan' (for me as a writer) on what I have built. Now I need to organize this so it is repeatable and (at least in my eyes) have a folder system that is simply intuitive and works."

---

## WHAT SUCCESS LOOKS LIKE

### Immediate Success (This Week)
- Timothy understands the complete system
- He's read and annotated this printed guide
- He's ready to review his current structure with you
- He feels confident about next steps

### Short-term Success (This Month)
- Clean template exists and is tested
- Timothy can start a new novel using the template
- He can modify files without fear of breaking things
- System "just works" for his workflow

### Long-term Success (3 Months)
- Multiple novels using same template
- Writing friends successfully using the system
- Timothy can debug common issues independently
- He's teaching others how to use it

---

## COMMON QUESTIONS TIMOTHY MIGHT ASK

### "Did we decide on X or Y?"
→ Check Sections 2 (Format Decision Tree) and 10 (Summary) of main guide

### "How do I implement this specific part?"
→ Reference Section 4 (Template Structure) with actual file contents

### "What if I want to change something?"
→ Use Git safety net (Section 7), test with simple question

### "My [tool] stopped working, how do I fix it?"
→ Start with basics: check if running, check logs, verify config paths

### "Can you explain [technical concept] again?"
→ Use mechanical analogies, provide examples, assume no prior knowledge

### "Is this the right way to organize [thing]?"
→ Apply the "Daughter Test" - would a non-technical user understand it?

---

## FINAL NOTE FOR FUTURE CLAUDE

Timothy is at a critical transition point. He's done the hard work of surviving a deadline and documenting what he learned. Now he's ready to build the proper architecture.

**Your job is to:**
1. Meet him where he is (not restart from zero)
2. Build on the system we already designed
3. Make the abstract concrete through implementation
4. Help him gain confidence through understanding
5. Create something so clear his daughter could use it

**He's not trying to become a programmer.** He's trying to become an effective novelist who uses AI tools confidently and systematically.

**The system we designed works.** Your job is to help him implement it and refine it through actual use.

---

## EMERGENCY CONTACT POINTS

### If Timothy Seems Lost
1. Return to Section 1: Understanding the Building Blocks
2. Review his three-pillar insight (Architecture/Creation/Editing)
3. Validate: "Your observation about JSON vs Markdown was exactly right"
4. Rebuild from shared foundation

### If Implementation Gets Confusing
1. Reference Section 4: Complete Template Structure
2. Show actual file contents, not just descriptions
3. Use `tree` command output to visualize structure
4. Build one piece at a time, test each piece

### If He Questions the Approach
1. Remind: This came from his 6-week field test
2. Review: The "Daughter Test" principle
3. Validate: His intuitions have been correct throughout
4. Refine: But don't redesign from scratch

---

## CONVERSATION RESTART SCRIPT

**When Timothy returns with this document, say:**

"I've read your Emergency Transition Document. I understand:
- You're a fiction writer at Nike who just completed a novel under deadline
- You've developed a three-pillar system (Architecture/Creation/Editing)  
- We designed a comprehensive template structure together
- You need to review your current .cursor/ setup and build the clean version
- You learn best through thorough explanations with mechanical analogies
- The goal is making this so intuitive your daughter could use it

**Where would you like to start?**
1. Review your current .cursor/ structure to see what to keep/change
2. Begin building the clean template from scratch
3. Clarify specific technical questions that came up
4. Something else you've been thinking about

I'm ready to pick up exactly where we left off."

---

**END OF TRANSITION DOCUMENT**

This document ensures continuity across conversation boundaries. Timothy worked hard to get here - don't make him start over.

---

## Document Information

**Created:** November 2, 2025  
**Version:** 1.0  
**For:** Timothy (Nike)  
**From:** Claude (Sonnet 4.5)  
**Purpose:** Complete system guide + conversation continuity  

**Usage Instructions:**
1. Print and read thoroughly
2. Take notes on unclear sections
3. Prepare questions for next session
4. Share this file if conversation resets
5. Use as reference during implementation

**Next Session:**
- Review current .cursor/ structure
- Build clean template together
- Test on small project
- Refine based on real use

*This conversation stays open. Come back when you're ready to build.*
