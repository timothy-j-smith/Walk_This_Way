# XML TAGS FOR STRUCTURED PROMPTING
## Quick Reference Guide
**Created:** January 24, 2026  
**Purpose:** Use structured XML tags to dramatically improve AI prompt clarity

---

## THE BASICS

**XML is just angle brackets - no learning curve needed!**

**Format:**
```
<tag>content</tag>
```

**That's it. Use angle brackets like HTML.**

---

## CORE TAGS FOR FICTION WRITING

### Essential Tags (Use These 5 Most Often):

**1. `<goal>` - What you want to achieve**
```
<goal>reveal Emma's secret without David realizing</goal>
<goal>increase dialogue between Sarah and Marcus</goal>
<goal>raise the stakes in this confrontation</goal>
```

**2. `<tone>` - Emotional quality**
```
<tone>mounting tension</tone>
<tone>desperate hope beneath surface calm</tone>
<tone>melancholic with sardonic edge</tone>
```

**3. `<constraint>` - What NOT to do**
```
<constraint>no exposition, only dialogue</constraint>
<constraint>no flashbacks, stay in present moment</constraint>
<constraint>maintain Maxanne's radio DJ voice</constraint>
```

**4. `<technique>` - How to do it**
```
<technique>imply through body language, not thoughts</technique>
<technique>short sentences building to one long release</technique>
<technique>show emotion through action, not declaration</technique>
```

**5. `<character>` - Who's involved**
```
<characters>Sarah, Marcus</characters>
<characters>Nick, Jackie, Patty</characters>
```

---

## COMPLETE EXAMPLES

### Example 1: Scene Rewrite
```
<scene>
<characters>Sarah, Marcus</characters>
<goal>Reveal Sarah's secret without Marcus realizing</goal>
<tone>Mounting tension, subtext-heavy</tone>
<constraint>No exposition, show through dialogue</constraint>
<technique>Use body language to show Sarah's nervousness</technique>
</scene>

Rewrite this scene:
[your scene text here]
```

### Example 2: Character Decision
```
<character_decision>
<character>Sarah</character>
<goal>Decide whether to confront Marcus</goal>
<thinking>
- What does Sarah want?
- What's the subtext?
- What's the power dynamic?
- What are the consequences?
</thinking>
</character_decision>

Write Sarah's decision scene.
```

### Example 3: Style Emulation
```
<style_emulation>
<target_author>Dennis Lehane</target_author>
<goal>Match Lehane's Boston grit and visceral descriptions</goal>
<technique>Short declarative sentences, concrete details, working-class authenticity</technique>
<constraint>Maintain your story's emotional truth</constraint>
</style_emulation>

Rewrite this passage:
[your text]
```

---

## ADVANCED PATTERNS

### Nested Tags (Multiple Levels):
```
<scene>
<goal>Reveal betrayal</goal>
<dialogue>
<tone>rising tension</tone>
<subtext>Emma suspects betrayal</subtext>
</dialogue>
<description>
<technique>concrete details, not abstract</technique>
<sensory>focus on smell and sound</sensory>
</description>
</scene>
```

### Multiple Goals:
```
<goals>
<primary>Reveal Marcus's involvement</primary>
<secondary>Show Sarah's growing suspicion</secondary>
<tertiary>Foreshadow the confrontation</tertiary>
</goals>
```

---

## WHEN TO USE XML TAGS

**Use XML Tags For:**
- ✅ Complex scene rewrites
- ✅ Character decision scenes
- ✅ Style emulation requests
- ✅ Multi-file editing tasks
- ✅ When you need precise control

**Don't Need XML Tags For:**
- ❌ Simple questions ("What's Sarah's age?")
- ❌ Quick edits (single sentence fixes)
- ❌ Basic requests (word count, etc.)

---

## TESTING

**Before XML:**
```
"Write a tense scene where Sarah confronts Marcus about the pendant."
```

**With XML:**
```
<scene>
<characters>Sarah, Marcus</characters>
<goal>Confrontation about the pendant</goal>
<tone>mounting tension</tone>
<constraint>No exposition, show through dialogue and action</constraint>
</scene>

Write the scene.
```

**Result:** Noticeably better output - clearer structure, better focus, more precise execution.

---

## QUICK REFERENCE

**Copy/Paste These Tags:**
```
<goal></goal>
<tone></tone>
<constraint></constraint>
<technique></technique>
<characters></characters>
<thinking></thinking>
<scene></scene>
<style_emulation></style_emulation>
```

**Use in:** Cmd+K, Agent, Chat - works everywhere!

---

**Status:** ✅ **READY TO USE**  
**Start:** Use `<goal>` and `<tone>` in your next prompt - immediate improvement!
