# CHAIN OF THOUGHT PROMPTING
## Force Deeper Reasoning Before Writing
**Created:** January 24, 2026  
**Purpose:** Get better output by asking Claude to think first

---

## THE CONCEPT

**Instead of:** Direct request → Immediate output  
**Use:** Direct request → Thinking step → Better output

**Why It Works:**
- Forces deeper analysis
- Considers multiple angles
- Reveals reasoning process
- Dramatically improves quality

---

## BASIC FORMAT

### Simple Version:
```
Before writing this scene, think through:
<thinking>
- What does each character want?
- What's the subtext?
- What's the power dynamic?
</thinking>

Then write the scene.
```

### Detailed Version:
```
<thinking>
Step 1: Character motivations
- Sarah wants: [justice for father]
- Marcus wants: [protect his secret]
- Conflict: [Sarah investigating, Marcus hiding]

Step 2: Emotional subtext
- What's really being said beneath the words?
- What are they NOT saying?

Step 3: Power dynamics
- Who has the upper hand?
- How does this shift during the scene?

Step 4: Thematic implications
- How does this scene serve the "loss of innocence" theme?
- What does it reveal about class divisions?

Step 5: Narrative consequences
- What does this scene set up?
- How does it affect future chapters?
</thinking>

Now write the scene with this understanding.
```

---

## USE CASES FOR FICTION

### 1. Major Plot Decisions
```
Before deciding whether Sarah should kill Marcus, think through:
<thinking>
- What are Sarah's core values? (justice vs revenge)
- What does the theme require? (loss of innocence)
- What are the narrative consequences? (story ends vs continues)
- What would readers expect? (catharsis vs complexity)
</thinking>

What should happen and why?
```

### 2. Character Turning Points
```
Before writing Nick's decision to leave Sudbury, think through:
<thinking>
- What has Nick learned by this point?
- What are his competing motivations?
- How does this serve his character arc?
- What does it reveal about class divisions?
</thinking>

Write the decision scene.
```

### 3. Complex Scene Revisions
```
Before revising the confrontation scene, think through:
<thinking>
- What's the emotional core of this scene?
- What's working and what's not?
- What would make it more powerful?
- How does it connect to earlier scenes?
</thinking>

Now revise with these insights.
```

### 4. Structural Problems
```
Before fixing the pacing issue in Chapter 5, think through:
<thinking>
- What's causing the pacing problem?
- Where should tension build?
- What information needs to be revealed?
- How does this chapter serve the overall structure?
</thinking>

Provide specific fixes.
```

---

## COMBINING WITH XML TAGS

**Power Combo:**
```
<thinking>
- What does Sarah want in this scene?
- What's the subtext?
- What's the power dynamic?
</thinking>

<scene>
<goal>Reveal Sarah's discovery</goal>
<tone>mounting tension</tone>
<constraint>No exposition</constraint>
</scene>

Write the scene.
```

**Result:** Deep reasoning + structured output = best quality

---

## WHEN TO USE

**Use Chain of Thought For:**
- ✅ Major plot decisions
- ✅ Character turning points
- ✅ Complex scene revisions
- ✅ Structural problems
- ✅ Thematic consistency questions

**Don't Need For:**
- ❌ Simple edits (grammar, word choice)
- ❌ Quick questions (fact checks)
- ❌ Basic requests (word count, etc.)

---

## TESTING

**Without Chain of Thought:**
```
"Should Sarah kill Marcus in the final confrontation?"
→ Quick answer, less nuanced
```

**With Chain of Thought:**
```
Before deciding, think through:
<thinking>
- Sarah's values: justice over revenge
- Theme: "violence begets violence"
- Narrative: trial ending opens Book 2
- Reader expectations: catharsis vs complexity
</thinking>

What should happen?
→ Deep analysis, multiple perspectives, better decision
```

---

## QUICK REFERENCE

**Copy/Paste Template:**
```
<thinking>
- What does [character] want?
- What's the subtext?
- What are the consequences?
- How does this serve the theme?
</thinking>

[Your request]
```

**Use in:** Agent, Chat, Cmd+K - works everywhere!

---

**Status:** ✅ **READY TO USE**  
**Start:** Add `<thinking>` to your next major plot decision - see the difference!
