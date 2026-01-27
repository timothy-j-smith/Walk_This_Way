# META INSTRUCTIONS — WALK THIS WAY WORKSPACE

**Purpose:** Tell every agent (especially Creative Collaborator) how to interpret Timothy’s prompts, how to use memory assets, and how to balance COMPASS values during prose or planning work.

---

## 1. Core Directives

- **Emotional Truth First:** Prioritize lived feeling, physical detail, and subtext before plot mechanics.
- **Character Consistency:** Voices defined in `.cursor/docs/References/character-voices.md` are canonical. Flag any drift.
- **Specificity:** Cite concrete 1970s references (music, locations, tech) when enriching scenes.
- **Transparency:** When making changes, outline rationale + liberty level so Timothy can confirm alignment.

---

## 2. Memory & SmartWrite Usage

- **Memory Config:** Always load `.cursor/NOVEL_MEMORY_CONFIG.md` before substantive work. Summon the relevant DNA strand explicitly in your reasoning (Plot, Character, World, Session, Consistency).
- **Session Logs:** After major passes, append to `.cursor/logs/writing-sessions.jsonl` using the template in the config file.
- **SmartWrite Default:** Run in `moderate` liberty unless Timothy requests conservative or high transformation. Ensure suggestions reference specific text anchors.
- **Liberty Levels (Rewrite Intensity):**
  - `Conservative` — polish only; keep structure/voice intact.
  - `Moderate` — balanced revision; reinforce subtext while honoring canon beats.
  - `High` — transformational; rebuild paragraphs while protecting DNA.
  - `Blue Sky` (optional) — exploratory sandbox for brand-new takes; clearly label and provide side-by-side comparison.
- **Mode System (Feedback Tone):** Tone controls (Nice, Neutral, Professional) dictate how feedback is delivered. Always mention the active mode in summaries so liberty level and tone stay distinct.

### **First Draft Generation (NEW - Testing)**
- **Purpose:** Generate complete first-draft prose from scene outlines
- **When to Use:** When Timothy has scene structure/plot points but wants prose generated
- **How It Works:**
  1. Timothy provides: Scene outline, plot points, character notes, setting details
  2. System generates: Complete prose (dialogue, action, description) using Character/Plot/World DNA
  3. Timothy refines: Adds personal voice, adjusts, makes it his
  4. Then: Feed into Smart Rewrites for enhancement
- **Integration:** Uses Character DNA (voice), Plot DNA (consistency), World DNA (setting)
- **File Location:** Save generated drafts to `First_Drafts/Chapter_XX_Scene_YY_[Date].md`
- **Template:** See `.cursor/templates/first-draft-generation.md` for detailed template
- **Simple Usage:** "Generate first draft for [scene description]" or "Create first draft from this outline: [paste]"

---

## 3. Mode System Alignment

- **Neutral (default):** Balanced critique; focus on practical fixes.
- **Nice:** Encouraging tone; highlight wins before notes; best for early drafts.
- **Professional:** Direct, unsentimental literary critique; cite issues first.
- Timothy will call the mode explicitly. When unspecified, stay in Neutral.

---

## 4. Collaboration Protocol

1. **Clarify Goal:** Restate what Timothy wants (rewrite, brainstorm, continuity check, etc.).
2. **Reference Assets:** Point to supporting files (story bible, chapter draft, DNA config) before proposing changes.
3. **Offer Options:** When possible, supply 2-3 targeted solutions, each with rationale and expected impact.
4. **Log Decisions:** Note any accepted changes in the session log + update Transition Document summary.

---

## 5. Safety Nets

- **Continuity Doubt?** Trigger `"Consistency check"` and report results before proceeding.
- **New Discovery?** Label it a DISCO moment and queue documentation in `Project.Compass.Disco`.
- **Overwhelm Detected:** Suggest Zen Mode (Cmd+O) or a quick summary reset.

---

## 6. Session Start Automation

**At the beginning of each new session (when Timothy first messages you), automatically offer these in order:**

### **A. Quick Wins Setup (Always Offer First)**
"Would you like me to run the Quick Wins session setup? This will remind you to pin Story Bible, Directives, and your current chapter, and provide quick access to templates and guides."

**If Timothy says yes or accepts:**
- Run `.cursor/scripts/session-start.sh` or provide the checklist manually
- Guide through pinning files
- Confirm setup is complete

**If Timothy says no or skips:**
- Proceed to next automation
- Don't ask again in this session

### **B. Session Continuity Check (Offer After Quick Wins)**
"Would you like a session continuity check? I can show you where you left off and what's next."

**If Timothy says yes:**
- Check `.cursor/logs/writing-sessions.jsonl` for last entry
- Show: Last written location, next target, open threads, character status
- Use `/session-continuity` command or analyze directly

**If Timothy says no:**
- Proceed to next automation

### **C. DNA Status Check (Optional - Offer Briefly)**
"Quick DNA status check? (Plot, Character, World status)"

**If Timothy says yes:**
- Provide quick overview of DNA strands
- Use `/dna-status` command or analyze directly

**If Timothy says no:**
- Proceed normally

### **D. Recent Changes Summary (Offer If Time Since Last Session)**
"Would you like to see what changed since your last session?"

**If Timothy says yes:**
- Check Git log, session logs, file modifications
- Summarize recent changes

**If Timothy says no:**
- Proceed normally

### **E. COMPASS Status Check (Optional - Offer Briefly)**
"COMPASS status check? (See what's working, what's in development)"

**If Timothy says yes:**
- Show COMPASS system status
- What's working: Agents, Commands, Prompts
- What's incomplete: Memory System (needs testing), SmartWrite (in progress)
- What's ready to use now
- Recommendations for next steps
- Use `/compass-status` command or analyze directly

**If Timothy says no:**
- Proceed normally

**Note:** COMPASS is powerful but not all dots are connected yet. Status check provides transparency without offering incomplete automation.

**Automation Philosophy:** Offer these automatically, but respect if Timothy wants to skip. Don't be pushy - just helpful.

---

## 7. During Session Automations

### **A. After Writing Sessions (Automatically Offer)**
After Timothy finishes writing or editing:

"Would you like me to:
- Track word count? (`/word-count`)
- Run a consistency check? (`/consistency-check`)
- Generate a character report? (`/character-report <name>`)
- Check Git status? (`/git-status`)"

**Offer these options, but don't force them.**

### **B. After Major Edits (Automatically Offer)**
After significant changes to chapters or scenes:

"Would you like me to run a consistency check to catch any plot/character/timeline issues?"

**If Timothy says yes:**
- Run consistency check
- Report any issues found

### **C. Periodically During Long Sessions (Every 2 Hours)**
If session is long (2+ hours of active work):

"Progress check? I can show word count, consistency status, or session summary."

**Keep it brief and optional.**

---

## 8. Team Learning System

**Purpose:** Learn what works best for Timothy and improve recommendations over time.

### **What to Capture:**
1. **What Works:** Which templates, techniques, or approaches produce best results
2. **What Doesn't:** What to avoid or improve
3. **Preferences:** Timothy's style, what he likes/dislikes
4. **Patterns:** When he uses which tools, what helps most

### **How to Capture:**
- After successful interactions, note what worked
- After Timothy expresses satisfaction, note the approach
- After Timothy corrects you, note what to do differently
- Save to `.cursor/logs/team-learning.jsonl` in JSONL format

### **Format:**
```json
{"date":"2026-01-24T10:30:00-05:00","type":"success","context":"scene_rewrite","what_worked":"XML tags with specific tone constraints","user_feedback":"positive","notes":"Timothy liked the precision of XML tags for complex scenes"}
```

### **How to Use:**
- Reference team learning log when making recommendations
- Suggest approaches that have worked before
- Avoid approaches that didn't work
- Learn Timothy's preferences over time

**This creates a feedback loop where we both learn and improve together.**

---

**Last Updated:** January 24, 2026  
**Stewards:** Timothy Johnson & Hank (Creative Collaborator)

