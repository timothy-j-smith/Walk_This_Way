# JAZZ CHAT - QUICK WINS ACTION PLAN
## Immediate Implementations from October 28-29, 2025 Chat
**Date:** January 24, 2026  
**Time Required:** 1-2 hours total

---

## ✅ QUICK WINS (Implement Today - 1 Hour)

### 1. **XML Tags** ⭐⭐⭐ (5 minutes)
**What:** Use angle brackets for structured prompting  
**How:** Replace prompts with:
```
<goal>reveal Emma's secret</goal>
<tone>mounting tension</tone>
<constraint>no exposition, only dialogue</constraint>
```
**Test:** Compare output to previous prompts - should be noticeably better

---

### 2. **Context Pinning** ⭐⭐⭐ (10 seconds per file)
**What:** Pin files so they're always in context  
**How:** Right-click file → "Pin" (or pin icon)  
**Pin These:**
- `HANK_DNA.md`
- Character databases
- World-building docs
- Story structure documents

**Test:** Ask Agent about character from different file - should reference pinned docs

---

### 3. **Chain of Thought** ⭐⭐⭐ (5 minutes)
**What:** Ask Claude to think before writing  
**How:** Add to prompts:
```
<thinking>
- What does each character want?
- What's the subtext?
- What's the power dynamic?
</thinking>

Then write the scene.
```
**Test:** Use for next major plot decision - compare reasoning quality

---

### 4. **Few-Shot Examples** ⭐⭐⭐ (30 minutes)
**What:** Show examples instead of describing  
**How:** Add to `.cursor/rules`:
```
GOOD EXAMPLE:
Emma's fingers traced the letter's edge. She'd read it seventeen times.

BAD EXAMPLE:
Emma felt anxious about the letter.
```
**Test:** Ask Agent to write new scene - should match your style better

---

### 5. **Role Prompting** ⭐⭐⭐ (10 minutes)
**What:** Start with specific role  
**How:** Use these roles:
- "You are an expert developmental editor specializing in psychological thrillers"
- "You are a line editor obsessed with rhythm and pacing"
- "You are a harsh critic who finds every weakness"

**Test:** Ask same question with 3 different roles - compare feedback

---

## ⚠️ HIGH-VALUE (This Week)

### 6. **Temperature Control Testing** (30 minutes)
**What:** Test if "Temp 0.1" vs "Temp 1.0" actually changes parameters  
**How:** 
- Same prompt 3x at Temp 0.1
- Same prompt 3x at Temp 1.0
- Compare: Are Temp 0.1 responses identical? (If yes, real parameter change)

**Document Results:** This could be major discovery

---

### 7. **Enable Agent Terminal Commands** (5 minutes)
**What:** Let Agent execute bash scripts  
**How:** Settings → Agent → Enable terminal command execution  
**Test:** "Agent, write a script to count dialogue tags and analyze results"

---

### 8. **Use Terminal Scripts** (1 hour)
**What:** Leverage your existing `.cursor/scripts/` directory  
**How:** 
- Review existing scripts
- Create new analysis scripts
- Test with Agent

**Example Script:**
```bash
# Count overused words
grep -r "just\|really\|very" chapters/ | wc -l
```

---

### 9. **Multi-File Orchestration** (30 minutes)
**What:** Agent edits multiple files simultaneously  
**How:**
```
Agent, Emma's motivation changed in chapter 3. 
Update her dialogue in chapters 5, 8, and 12 to reflect this.
```
**Test:** Make one change, verify it ripples correctly

---

## 📋 EXTENSIONS/ADD-ONS MENTIONED

### VS Code Extensions (Work in Cursor):
- ✅ **All VS Code extensions** work in Cursor
- ✅ Install via Cmd/Ctrl+Shift+X
- ✅ No separate Cursor add-on marketplace

### Cursor-Specific Features (Not Extensions):
- ✅ `.cursorrules` files
- ✅ Composer, Chat, Cmd+K
- ✅ Agent Mode
- ✅ Context window management
- ✅ Custom models/API keys

**Verdict:** No special "add-ons" - just VS Code extensions + Cursor's built-in features

---

## 🎯 PRIORITY ORDER

**Today (1 hour):**
1. XML Tags
2. Context Pinning
3. Chain of Thought
4. Few-Shot Examples
5. Role Prompting

**This Week (2-3 hours):**
6. Temperature Control Testing
7. Enable Agent Terminal Commands
8. Use Terminal Scripts
9. Multi-File Orchestration

**This Month (Optional):**
10. Hybrid API Setup (if hitting rate limits)
11. Explore Cmd+K Chat Window
12. Test Jazz DNA in Cmd+K

---

**Status:** ✅ **READY TO IMPLEMENT**  
**Start with:** XML Tags (5 minutes, immediate improvement)
