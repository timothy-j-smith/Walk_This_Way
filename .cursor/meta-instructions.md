# META INSTRUCTIONS — WALK THIS WAY WORKSPACE

**Purpose:** Tell every agent (especially Creative Collaborator) how to interpret Timothy’s prompts, how to use memory assets, and how to balance COMPASS values during prose or planning work.

---

## 1. Core Directives

- **Emotional Truth First:** Prioritize lived feeling, physical detail, and subtext before plot mechanics.
- **Character Consistency:** Voices defined in `.cursor/docs/character-voices.md` are canonical. Flag any drift.
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

**Last Updated:** November 9, 2025  
**Stewards:** Timothy Johnson & Hank (Creative Collaborator)

