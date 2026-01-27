# QUICK WINS - MASTER REFERENCE
## 5 Workflow Optimizations That Multiply Your MCP System
**Created:** January 24, 2026  
**Purpose:** One-page reference for all 5 Quick Wins

---

## ⚡ THE 5 QUICK WINS

### 1. XML TAGS (5 min setup)
**What:** Use `<goal>`, `<tone>`, `<constraint>` tags for structured prompts  
**Why:** Dramatically clearer prompts = better output  
**How:** Wrap your requests in XML tags  
**Example:**
```
<goal>Reveal Sarah's secret</goal>
<tone>Mounting tension</tone>
<constraint>No exposition</constraint>
Write the scene.
```
**Full Guide:** `.cursor/rules/xml-tags-guide.md`

---

### 2. CONTEXT PINNING (10 sec setup)
**What:** Pin files to keep them in context automatically  
**Why:** No repeated @mentions = massive time savings  
**How:** Right-click file → "Pin to Context"  
**Always Pin:**
- Story Bible
- Writing Directives  
- Current Chapter
**Full Guide:** `.cursor/rules/context-pinning-guide.md`

---

### 3. CHAIN OF THOUGHT (5 min setup)
**What:** Ask Claude to think before writing  
**Why:** Deeper reasoning = better output  
**How:** Add `<thinking>` step before request  
**Example:**
```
<thinking>
- What does Sarah want?
- What's the subtext?
- What are the consequences?
</thinking>
Write the scene.
```
**Full Guide:** `.cursor/rules/chain-of-thought-guide.md`

---

### 4. FEW-SHOT EXAMPLES (30 min setup)
**What:** Show examples instead of describing style  
**Why:** Examples lock in exact style = consistency  
**How:** Provide Good/Bad example pairs  
**Example:**
```
GOOD - Nick's Voice:
"I didn't need his help. I could handle it."

BAD - Too Polished:
"I did not require his assistance."

Now write Nick's dialogue.
```
**Full Guide:** `.cursor/rules/few-shot-examples-guide.md`

---

### 5. ROLE PROMPTING (10 min setup)
**What:** Activate specialized AI personas  
**Why:** Different roles = different feedback angles  
**How:** Start with "You are a [role]..."  
**Example:**
```
You are a developmental editor specializing in psychological thrillers.
Analyze this chapter's pacing.
```
**Full Guide:** `.cursor/rules/role-prompting-library.md`

---

## 🚀 QUICK START (1 Hour Total)

### Step 1: XML Tags (5 min)
1. Read: `xml-tags-guide.md`
2. Try: Use `<goal>` and `<tone>` in next prompt
3. Result: Immediate improvement

### Step 2: Context Pinning (10 sec)
1. Right-click: Story Bible → Pin
2. Right-click: Writing Directives → Pin
3. Right-click: Current Chapter → Pin
4. Result: Instant context access

### Step 3: Chain of Thought (5 min)
1. Read: `chain-of-thought-guide.md`
2. Try: Add `<thinking>` to next major decision
3. Result: Deeper analysis

### Step 4: Few-Shot Examples (30 min)
1. Read: `few-shot-examples-guide.md`
2. Create: One Good/Bad example pair for your best character voice
3. Try: Use in next dialogue request
4. Result: Style consistency locked in

### Step 5: Role Prompting (10 min)
1. Read: `role-prompting-library.md`
2. Try: Use 3 different roles on same question
3. Result: Multiple feedback angles

---

## 💡 COMBINING TECHNIQUES

### Power Combo 1: All 5 Together
```
You are a developmental editor specializing in psychological thrillers.

<thinking>
- What does Sarah want?
- What's the subtext?
- What are the consequences?
</thinking>

<scene>
<goal>Reveal Sarah's secret</goal>
<tone>Mounting tension</tone>
<constraint>No exposition</constraint>
</scene>

GOOD EXAMPLE:
[Your best writing]

BAD EXAMPLE:
[Writing that doesn't work]

Now rewrite this scene.
```

### Power Combo 2: XML + Chain of Thought
```
<thinking>
- Character motivations?
- Emotional subtext?
- Power dynamics?
</thinking>

<scene>
<goal>Fix pacing</goal>
<tone>Rising tension</tone>
</scene>

Analyze and provide fixes.
```

### Power Combo 3: Role + Few-Shot
```
You are a line editor specializing in working-class authenticity.

GOOD - Authentic:
"I didn't need his help."

BAD - Inauthentic:
"I did not require his assistance."

Now improve this passage.
```

---

## 📊 EXPECTED IMPROVEMENTS

**Before Quick Wins:**
- Generic feedback
- Inconsistent style
- Repeated @mentions
- Surface-level analysis

**After Quick Wins:**
- Precise, structured feedback
- Consistent style matching
- Instant context access
- Deep, thoughtful analysis

**Time Savings:**
- XML Tags: Better output (fewer revisions)
- Context Pinning: 10+ sec per request × 20 = 3+ min/session
- Chain of Thought: Better decisions (fewer rewrites)
- Few-Shot: Style consistency (less editing)
- Role Prompting: Targeted feedback (faster iteration)

**Total:** 10-15 minutes saved per session + better quality output

---

## 🎯 WHEN TO USE WHICH

**For Scene Rewrites:**
→ XML Tags + Chain of Thought + Few-Shot

**For Character Consistency:**
→ Context Pinning (Story Bible) + Few-Shot Examples

**For Structural Analysis:**
→ Role Prompting (Developmental Editor) + Chain of Thought

**For Style Emulation:**
→ Role Prompting (Line Editor) + Few-Shot Examples + XML Tags

**For Quick Edits:**
→ Context Pinning (Current Chapter) + XML Tags

**For Major Decisions:**
→ Chain of Thought + Role Prompting (Multiple roles)

---

## 📁 FILE LOCATIONS

All guides in: `.cursor/rules/`

1. `xml-tags-guide.md` - XML tag reference
2. `context-pinning-guide.md` - Pinning workflow
3. `chain-of-thought-guide.md` - Thinking prompts
4. `few-shot-examples-guide.md` - Example library
5. `role-prompting-library.md` - Role templates
6. `QUICK_WINS_MASTER_REFERENCE.md` - This file

---

## ✅ IMPLEMENTATION CHECKLIST

- [ ] Read all 5 guides (1 hour)
- [ ] Pin Story Bible + Directives + Current Chapter (10 sec)
- [ ] Try XML tags in next prompt (5 min)
- [ ] Add Chain of Thought to next major decision (5 min)
- [ ] Create one Few-Shot example pair (30 min)
- [ ] Try 3 different roles on same question (10 min)

**Total Time:** ~2 hours for complete setup  
**Ongoing:** Use techniques as needed

---

## 🎉 RESULT

**These aren't replacements for your MCP system - they're force multipliers.**

Your MCP system provides:
- Instant file access
- Specialized tools
- Memory systems
- Agent coordination

Quick Wins provide:
- Better prompt clarity
- Persistent context
- Deeper reasoning
- Style consistency
- Specialized feedback

**Together = Most powerful creative writing system possible**

---

**Status:** ✅ **ALL 5 QUICK WINS READY**  
**Next:** Start with Context Pinning (10 sec) + XML Tags (5 min) = immediate improvement!
