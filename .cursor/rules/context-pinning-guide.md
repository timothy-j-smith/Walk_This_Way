# CONTEXT PINNING - INSTANT FILE ACCESS
## Pin Files for Persistent Context
**Created:** January 24, 2026  
**Purpose:** Keep important files always available without @mentions

---

## THE CONCEPT

**Pin files to keep them in context automatically.**

**How It Works:**
- Pin a file → It stays in context for the entire session
- No need to @mention repeatedly
- Massive time savings
- Works with MCP for instant access

---

## HOW TO PIN FILES

### Method 1: Right-Click Menu
1. Right-click file in sidebar
2. Select "Pin to Context"
3. File stays pinned (shows pin icon)

### Method 2: Command Palette
1. `Cmd+Shift+P` (Command Palette)
2. Type "Pin"
3. Select "Pin to Context"
4. Choose file

### Method 3: Chat Command
```
@filename.md pin this
```

---

## WHAT TO PIN

### Always Pin (Session Start):
1. **Story Bible** (`Story_Bible/character-bible.md`)
   - Character voices, arcs, details
   - Always needed for consistency

2. **Writing Directives** (`.cursor/rules/walk-this-way-writing-directives.md`)
   - Core writing rules, style guide
   - Ensures all feedback follows guidelines

3. **Current Chapter** (e.g., `Active_Draft_2/Ch_05.md`)
   - What you're working on
   - Keeps focus on current work

### Pin When Needed:
4. **Timeline** (`Story_Bible/timeline.md`)
   - When checking dates, chronology
   - Pin during timeline-sensitive editing

5. **Author Style Library** (`Story_Bible/author-style-library.md`)
   - When emulating specific authors
   - Pin during style emulation work

6. **Music References** (`Story_Bible/music-references.md`)
   - When checking song details, period accuracy
   - Pin during music-heavy scenes

7. **Previous Chapter** (e.g., `Active_Draft_2/Ch_04.md`)
   - When checking continuity
   - Pin during continuity checks

---

## WORKFLOW PATTERNS

### Pattern 1: Daily Writing Session
```
1. Pin: Story Bible
2. Pin: Writing Directives
3. Pin: Current Chapter
4. Start writing/editing
→ All context available automatically
```

### Pattern 2: Continuity Check
```
1. Pin: Story Bible
2. Pin: Current Chapter
3. Pin: Previous Chapter
4. Ask: "Check consistency between chapters"
→ All relevant files in context
```

### Pattern 3: Style Emulation
```
1. Pin: Author Style Library
2. Pin: Writing Directives
3. Pin: Current Chapter
4. Ask: "Rewrite in Dennis Lehane style"
→ Style guide + current work available
```

### Pattern 4: Character Development
```
1. Pin: Character Bible
2. Pin: Current Chapter
3. Pin: Previous Character Scenes
4. Ask: "Is Nick's voice consistent?"
→ All character context available
```

---

## COMBINING WITH MCP

**MCP + Pinning = Power Combo:**

**Without MCP:**
- Pin files manually
- Still need to @mention sometimes
- Works but slower

**With MCP:**
- MCP provides instant file access
- Pinning keeps key files always loaded
- Fastest possible workflow

**Best Practice:**
- Pin 3-5 key files (Story Bible, Directives, Current Chapter)
- Use MCP for everything else (instant access when needed)
- Unpin when switching to different work

---

## WHEN TO PIN VS. @MENTION

**Pin When:**
- ✅ File needed throughout entire session
- ✅ Core reference (Story Bible, Directives)
- ✅ Current work file
- ✅ Multiple references expected

**@Mention When:**
- ✅ One-time reference
- ✅ Quick check
- ✅ Not needed for rest of session

**Best Practice:**
- Pin 3-5 core files at session start
- @Mention everything else as needed
- Unpin when switching focus

---

## UNPINNING FILES

### Method 1: Right-Click
1. Right-click pinned file
2. Select "Unpin from Context"

### Method 2: Command Palette
1. `Cmd+Shift+P`
2. Type "Unpin"
3. Select file to unpin

### Method 3: Sidebar
- Click pin icon to unpin

---

## TESTING

**Before Pinning:**
```
You: "Check if Nick's age is consistent"
Agent: "Please @mention Story Bible and Chapter 5"
You: @Story_Bible @Ch_05
Agent: [Checks consistency]
→ Multiple steps, slower
```

**After Pinning:**
```
You: [Story Bible and Ch_05 already pinned]
You: "Check if Nick's age is consistent"
Agent: [Instantly checks, no @mentions needed]
→ One step, instant
```

**Time Savings:** 10+ seconds per request × 20 requests = 3+ minutes saved per session

---

## QUICK REFERENCE

**Session Start Checklist:**
- [ ] Pin Story Bible
- [ ] Pin Writing Directives
- [ ] Pin Current Chapter
- [ ] Start working

**Session End:**
- [ ] Unpin files (optional, auto-unpins on close)

**Files to Always Pin:**
1. Story Bible
2. Writing Directives
3. Current Chapter

---

**Status:** ✅ **READY TO USE**  
**Start:** Pin Story Bible + Writing Directives + Current Chapter right now - instant improvement!
