# CURSOR PROJECT MANAGEMENT GUIDE

**Created**: January 17, 2026, 09:30 PST  
**Purpose**: How to create and manage To Do lists, notes, and project organization in Cursor  
**For**: Clear, organized project management

---

## 🎯 OVERVIEW

Cursor offers several ways to stay organized and share information with Claude outside of chat. This guide covers practical methods that work with your workflow (printing, tactile review, `((comments))` system).

---

## 📝 METHOD 1: TODO TOOL (BUILT-IN)

### What It Is
Cursor has a built-in TODO system that Claude can read and update. I've been using it in our sessions.

### How to Use It

**Claude Creates TODOs**:
- I can create TODO lists during our sessions
- They persist across sessions
- You can see them in Cursor's interface

**You Can Create TODOs**:
- Create a file: `TODO.md` or `TODO_LIST.md` in your project root
- Format it like this:

```markdown
# TODO LIST - Walk This Way Draft 2

## ACTIVE (Current Focus)
- [ ] Review DRAFT_2_MASTER_BLUEPRINT_V2.md with ((notes))
- [ ] Expand chapter descriptions in blueprint
- [ ] Fix Style Guide corrections

## NEXT UP
- [ ] Start Chapter 00 rewrite
- [ ] Review Act I structure

## LATER
- [ ] Update Story Bible
- [ ] Character Hierarchy updates
```

**Claude Can Read This**:
- I can read your TODO.md file
- I can update it based on our work
- You can print it, mark it up, I'll incorporate changes

---

## 📄 METHOD 2: MARKDOWN NOTES FILES

### Create Project Notes File

**File**: `PROJECT_NOTES.md` or `WORKING_NOTES.md`

**Format**:
```markdown
# PROJECT NOTES - Walk This Way Draft 2

**Last Updated**: January 17, 2026, 09:30 PST

## CURRENT FOCUS
[What you're working on now]

## QUESTIONS FOR CLAUDE
- [Your questions here]
- [Use ((comments)) for notes]

## DECISIONS MADE
- [Decision 1]
- [Decision 2]

## IDEAS TO EXPLORE
- [Idea 1]
- [Idea 2]
```

**Benefits**:
- ✅ You can print it
- ✅ Mark it up with handwritten notes
- ✅ I can read it and respond
- ✅ Persists across sessions
- ✅ You control the format

---

## 📋 METHOD 3: SESSION PREP FILE

### Create Before Each Session

**File**: `SESSION_PREP.md` (update before each session)

**Format**:
```markdown
# SESSION PREP - [Date]

**Date**: January 17, 2026  
**Time**: [Your session time]  
**Focus**: [What you want to work on]

## WHAT I WANT TO ACCOMPLISH
1. [Goal 1]
2. [Goal 2]

## QUESTIONS I HAVE
- [Question 1]
- [Question 2]

## FILES I'VE REVIEWED
- [File 1] - Notes: [Your notes]
- [File 2] - Notes: [Your notes]

## FILES I NEED CLAUDE TO REVIEW
- [File 1] - What I need: [Specific request]
- [File 2] - What I need: [Specific request]
```

**Benefits**:
- ✅ Sets clear agenda
- ✅ I know what you need
- ✅ You stay focused and organized
- ✅ Can reference past sessions

---

## 🗂️ METHOD 4: FOLDER-BASED ORGANIZATION

### Create Status Folders

**Structure**:
```
Walk This Way/
├── Active_Draft_2/          (Current work)
├── In_Review/               (Files you're reviewing)
│   ├── DRAFT_2_MASTER_BLUEPRINT_V2.md (with your ((notes)))
│   └── DRAFT_2_STYLE_GUIDE.md (with your ((notes)))
├── Completed/               (Finished work)
└── Questions/               (Questions for Claude)
    └── 2026-01-17_Questions.md
```

**Workflow**:
1. Move file to `In_Review/` when you start reviewing
2. Add your `((notes))` 
3. Move to `Active_Draft_2/` when done
4. Move to `Completed/` when work is finished

---

## 💬 METHOD 5: COMMENTS IN CODE/DOCUMENTS

### Use `((comments))` System (You Already Do This!)

**Format**: `((your comment here))`

**Examples**:
```markdown
## Chapter 04: Belt Buckles

((Need to add more detail about cafeteria setting))

The belt buckles caught the light.

((This feels too short - expand?))
```

**Benefits**:
- ✅ I can read them
- ✅ You can print and mark up
- ✅ Clear distinction from document text
- ✅ Easy to search for `((` in document

---

## 📊 METHOD 6: STATUS TRACKING FILE

### Create Progress Tracker

**File**: `DRAFT_2_PROGRESS.md`

**Format**:
```markdown
# DRAFT 2 PROGRESS TRACKER

**Last Updated**: January 17, 2026, 09:30 PST

## PHASE 1: BLUEPRINT FINALIZATION
- [x] Master Blueprint V2 created
- [ ] Timothy review with ((notes))
- [ ] Incorporate feedback
- [ ] Expand chapter descriptions

## PHASE 2: STYLE GUIDE
- [x] Style Guide created
- [ ] Timothy corrections applied
- [ ] Final review

## PHASE 3: CHAPTER REWRITES
- [ ] Act I (Chapters 00-12)
- [ ] Act II (Chapters 13-28)
- [ ] Act III (Chapters 29-38)

## BLOCKERS
- [None currently]

## NEXT SESSION FOCUS
- Review blueprint with Timothy's notes
```

**Benefits**:
- ✅ Visual progress tracking
- ✅ Clear next steps
- ✅ I can update it
- ✅ You can print it

---

## 🔄 RECOMMENDED WORKFLOW

### Daily/Per Session

1. **Before Session**:
   - Update `SESSION_PREP.md` with your goals
   - Move files to `In_Review/` if you've marked them up
   - Check `TODO.md` for current priorities

2. **During Session**:
   - I read your prep file
   - We work on your priorities
   - I update TODO list as we go
   - I read your `((comments))` in files

3. **After Session**:
   - I create session summary (with Pacific Time!)
   - Update `DRAFT_2_PROGRESS.md`
   - Move completed files to appropriate folders
   - Update `SESSION_PREP.md` for next session

---

## 🎯 BEST PRACTICES FOR YOUR WORKFLOW

### 1. Print-Friendly Format
- Use markdown (`.md` files)
- Clear headings
- Bullet points
- Easy to print and mark up

### 2. Date/Time Stamps
- Always include date and time (Pacific Time)
- Format: `January 17, 2026, 09:30 PST`
- Helps track when things happened

### 3. Clear Status Indicators
- `[ ]` = Not started
- `[~]` = In progress
- `[x]` = Complete
- `[!]` = Blocked/Issue

### 4. Use Your `((comments))` System
- Keep using it - it works!
- I can search for `((` to find all your notes
- Easy to distinguish from document text

### 5. One Source of Truth
- Don't duplicate information
- Update one file, not multiple
- Reference other files when needed

---

## 📁 SUGGESTED FILE STRUCTURE

```
Walk This Way/
├── Active_Draft_2/              (Current work)
├── In_Review/                    (Files you're reviewing)
├── Completed/                    (Finished work)
├── Questions/                    (Questions for Claude)
├── TODO.md                       (Master TODO list)
├── PROJECT_NOTES.md              (Your working notes)
├── SESSION_PREP.md               (Session agenda)
├── DRAFT_2_PROGRESS.md           (Progress tracker)
└── Session_Summaries/            (Historical records)
```

---

## 💡 QUICK START

**Right Now, Create These Files**:

1. **TODO.md** (in root):
```markdown
# TODO - Walk This Way Draft 2

## ACTIVE
- [ ] Review Active_Draft_2 files
- [ ] Add ((notes)) to blueprint
- [ ] Review Style Guide corrections

## NEXT
- [ ] Start Chapter 00 rewrite
```

2. **SESSION_PREP.md** (in root):
```markdown
# SESSION PREP

**Date**: [Today's date]  
**Time**: [Your time]  
**Focus**: [What you want to work on]
```

3. **PROJECT_NOTES.md** (in root):
```markdown
# PROJECT NOTES

**Last Updated**: [Date and time]

## CURRENT FOCUS
[What you're working on]

## QUESTIONS
- [Your questions]
```

---

## 🤝 HOW CLAUDE USES THESE

**I Can**:
- ✅ Read any `.md` file you create
- ✅ Update TODO lists
- ✅ Respond to your questions in files
- ✅ Incorporate your `((comments))`
- ✅ Update progress trackers
- ✅ Reference session prep files

**I Will**:
- Check `SESSION_PREP.md` at start of session
- Read your `((comments))` in files
- Update `TODO.md` as we work
- Create session summaries with Pacific Time
- Reference your notes when making decisions

---

## 🎨 CUSTOMIZATION

**Make It Yours**:
- Use whatever file names work for you
- Create folders that match your thinking
- Use your `((comments))` system everywhere
- Print what you need
- Mark it up however you want

**The Key**: Consistency helps maintain organization. Once you find a system that works, stick with it.

---

## 📞 QUESTIONS?

**If you have questions about**:
- How to set up a specific file
- Whether I can read a certain format
- How to organize something specific
- Best practices for your workflow

**Just ask!** I can help you customize this system to work perfectly for your brain.

---

**This system gives you control, clarity, and continuity. Print what you need, mark it up, and I'll work with whatever you create.**

**DISCO! 🎸**

---

*Created: January 17, 2026, 09:30 PST*  
*Last Updated: January 17, 2026, 09:30 PST*
