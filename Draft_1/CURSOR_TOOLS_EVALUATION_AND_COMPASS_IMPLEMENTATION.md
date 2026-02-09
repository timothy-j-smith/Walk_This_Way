# Cursor Tools Evaluation & COMPASS Implementation

**Applied to:** Draft_1 (Walk This Way Rewrite)  
**Purpose:** Evaluate 8 proposed Cursor tools/methods for the COMPASS Creative Writing System; identify worthy vs. superfluous; recommend implementation for the Walk This Way rewrite.  
**Last Updated:** 2026

---

## Summary: The 8 Tools at a Glance

| # | Tool / Method | Verdict | Implement in COMPASS? |
|---|----------------|---------|------------------------|
| 1 | Reference-Document Stack (CREATIVE_COLLABORATOR.md, STORY_BIBLE, etc.) | **Worthy** | Yes—formalize as "Session Load Stack" |
| 2 | XML Chapter Brief (`<chapter>`, `<goal>`, `<Refactoring>`, etc.) | **Worthy** | Yes—use as chapter brief template |
| 3 | Project DNA / System Message (First Draft "Make It Good" mode) | **Worthy** | Yes—already partly in place; unify |
| 4 | Few-Shot Pattern Learning (GOOD vs. BAD prose examples) | **Worthy** | Yes—add to PROSE_DNA / author-style-library |
| 5 | Chain of Thought (`<thinking>`) for Complex Decisions | **Worthy** | Yes—use in prompts before big rewrites |
| 6 | Post-Completion "AFTER" Prompt (next chapters strategy) | **Worthy** | Yes—standardize as session handoff |
| 7 | AI Self-Direction (Strategy for full rewrite) | **Partially superseded** | Use STRATEGIC_WRITING_COORDINATOR + existing docs |
| 8 | Terminal Word Report + Novel Plan + Autonomous Story Bible | **Partially superseded** | Use existing scripts + Story_Bible; enhance script |

---

## The 8 Tools: Four-Sentence Analysis Each

### 1. Reference-Document Stack (CREATIVE_COLLABORATOR.md, Agent.md, STORY_BIBLE.md, PROSE_DNA, SCALPEL_HOSE_*, OPTIMAL_WRITING_SETUP, QUICK_START_GUIDE, Chapter_Analysis, Session Logs)

**What it aims to achieve:** Load a consistent set of project documents at session start so the AI has role, vision, character details, voice, methodology, and recent context in one place.

**Would it achieve its goal?** Yes. Explicitly listing these files (or using @mentions) gives Cursor a stable "project DNA" and reduces ambiguity about voice, constraints, and where to save work.

**Is there an existing better tool?** Cursor’s @-mentions and rules (e.g. `.cursor/rules/walk-this-way-writing-directives.md`) already provide project context; what’s missing is a single, agreed "Session Load Stack" so you don’t have to remember the list each time.

**Implementation in COMPASS / Walk This Way:** Create a `Draft_1/SESSION_LOAD_STACK.md` (or add to QUICK_START_GUIDE) that lists, in order: Creative_Collaborator.md (or the agent you’re using), Agent.md, Story_Bible/character-bible.md, PROSE_DNA.md, SCALPEL_HOSE_APPLIED_TO_WALK_THIS_WAY, OPTIMAL_WRITING_SETUP (if present), and the latest Chapter_Analysis or Session log. Start each major session with: "Load the Session Load Stack for Walk This Way, then we're working on [chapter/task]."

---

### 2. XML Chapter Brief (`<chapter>`, `<goal>`, `<specific>`, `<constrain>`, `<technique>`, `<character>`, `<Refactoring>`, `<Debugging>`, `<Testing>`, `<GIT branches>`, `<Functions>`, `<Linting>`, `<Compiling>`)

**What it aims to achieve:** Give the model a structured, machine-parseable brief for a single chapter that encodes creative intent (goal, specifics, constraints, technique, characters), software metaphors (refactoring, debugging, testing, functions, linting, compiling), and process (Git, assembly).

**Would it achieve its goal?** Yes. A well-filled XML brief reduces vague "make it better" and aligns the model with your editorial and structural goals for that chapter.

**Is there an existing better tool?** Cursor doesn’t have a built-in "chapter brief" format; your `.cursor/rules` and templates are the closest. The XML format is not superseded—it’s a clear, reusable pattern.

**Implementation in COMPASS / Walk This Way:** Add a template `Draft_1/CHAPTER_BRIEF_TEMPLATE.xml` (or .md with XML block) and a rule or note: "For major chapter rewrites, fill the chapter brief and pass it with the chapter file." When rewriting e.g. Chapter 26, paste the filled brief into chat so Scalpel & Hose, voice, and Act III transition are explicit. Store completed briefs in `Agent_Work/Creative_Collaborator/Chapter_XX_Brief_[Date].md` for traceability.

---

### 3. Project DNA / System Message ("Make It Good" Mode — Goal, System Message, Parameters)

**What it aims to achieve:** Fix the model’s "persona" and constraints in one place: literary quality (e.g. 8/10→9/10), voice (e.g. Russo/King/DeHane, working-class detail), and parameters (temperature, top_p, frequency_penalty, presence_penalty, agent mode, target quality).

**Would it achieve its goal?** Yes. A single "Project DNA" or system block at the start of a conversation consistently steers tone, style, and quality bar.

**Is there an existing better tool?** You already have PROSE_DNA, DRAFT_MODES.json, walk-this-way-writing-directives, and Creative_Collaborator. The "better" approach is to unify, not add another parallel system.

**Implementation in COMPASS / Walk This Way:** In `Agent_Work/Creative_Collaborator/` or `.cursor/rules/`, add or update one "MAKE_IT_GOOD_DNA.md" that is the single source for: (1) the exact system message you pasted (First Draft "Make It Good" mode), (2) a pointer to DRAFT_MODES.json for parameters, and (3) a one-line reminder: "When doing Draft 2 passes, load MAKE_IT_GOOD_DNA + PROSE_DNA." Use this for Act III rewrites and then Act I/II so the same "Make It Good" bar applies everywhere.

---

### 4. Few-Shot Pattern Learning (GOOD vs. BAD Prose Examples)

**What it aims to achieve:** Teach the model your taste by contrast: one paragraph you consider GOOD (concrete, specific, no purple prose) and one BAD (overwritten, rhyme-driven, vague), so it learns the boundary.

**Would it achieve its goal?** Yes. Few-shot examples are one of the most effective ways to align an LLM with subjective style in a given project.

**Is there an existing better tool?** You have PROSE_DNA and author-style-library; they may already include do/don’t examples. If not, this pattern is not superseded—it’s a best practice.

**Implementation in COMPASS / Walk This Way:** In `Story_Bible/author-style-library.md` or a new `PROSE_EXAMPLES_WALK_THIS_WAY.md`, add a short "GOOD vs. BAD" section. Use your exact GOOD (Johnson house, concrete detail) and BAD (Sudbury tribes, "Rampers/Rats" rhyme) examples and 2–3 more as you find them. Reference this file in the Session Load Stack and in chapter briefs: "Match the GOOD style in PROSE_EXAMPLES_WALK_THIS_WAY; avoid the BAD."

---

### 5. Chain of Thought for Complex Decisions (`<thinking>` Before Rewriting)

**What it aims to achieve:** Force the model to reason before acting: e.g. what gives the chapter energy, what it represents, what creates tension, how it sets up Act III, how to show (not tell) loss of innocence, class, prejudice, and transitions.

**Would it achieve its goal?** Yes. Explicit "think first" steps improve coherence and thematic consistency, especially for pivotal chapters like 26.

**Is there an existing better tool?** Cursor’s Composer and chat don’t enforce `<thinking>`; you already have `.cursor/rules/chain-of-thought-guide.md`. So the method is supported; the missing piece is consistently applying it to chapter-scale rewrites.

**Implementation in COMPASS / Walk This Way:** In the chapter brief or in your prompt template, add a required step: "Before rewriting, output a short <thinking> block that answers: (1) What gives this chapter energy and excitement? (2) What does this chapter represent in the arc? (3) How does it set up Act III? (4) How will we show loss of innocence, class, and prejudice here?" Then do the rewrite. Save the thinking block in the same Agent_Work file as the chapter feedback so you have a record of intent.

---

### 6. Post-Completion "AFTER" Prompt (Strategy for Next Chapters)

**What it aims to achieve:** After finishing a chapter (e.g. 26), ask the model to produce a concise strategy for the next units (e.g. Chapters 27–34): approach, priorities, and how to maintain strength and fluidity.

**Would it achieve its goal?** Yes. It turns a one-off completion into a handoff document and keeps the next session aligned.

**Is there an existing better tool?** No built-in "session handoff" exists; this is a prompt pattern, not a tool. It complements the Strategic Writing Coordinator’s role.

**Implementation in COMPASS / Walk This Way:** Add to your session checklist: "When I complete a major chapter rewrite, ask: 'Provide a 1–2 page strategy for rewriting Chapters [X–Y] to maintain voice, theme, and pacing.'" Save the answer as `Agent_Work/STRATEGIC_WRITING_COORDINATOR/Chapters_XX-YY_Rewrite_Strategy_[Date].md` and load it at the start of the next session so COMPASS and the next agent (or you) follow a single plan.

---

### 7. AI Self-Direction (Full-Rewrite Strategy from Prologue)

**What it aims to achieve:** Have the AI generate a high-level, professional-grade strategy for a full novel rewrite (Prologue through end), keeping storyline and main characters, focusing on showing theme (loss of innocence, class, prejudice, Greek tragedy) and producing publishable-level fiction.

**Would it achieve its goal?** Partially. The AI can produce a plausible strategy document, but "self-direction" can be generic; the best strategies come from your vision plus AI-assisted breakdown.

**Is there an existing better tool?** Yes. You already have STRATEGIC_WRITING_COORDINATOR, Agent.md, DRAFT_2_MASTER_BLUEPRINT_V2, and COMPASS orchestration. A one-shot "create full strategy" prompt is useful once; ongoing direction should stay in the Coordinator + blueprints.

**Implementation in COMPASS / Walk This Way:** Use this as a one-time or rare "strategy refresh" prompt: "As STRATEGIC_WRITING_COORDINATOR, produce a professional-level strategy for the full rewrite of Walk This Way from Prologue onward, preserving storyline and main characters, emphasizing show-don’t-tell for loss of innocence, class, prejudice, and Greek tragedy." Save the output in Agent_Work/STRATEGIC_WRITING_COORDINATOR/Full_Rewrite_Strategy_[Date].md and treat it as input to (not replacement for) your existing blueprints and COMPASS workflow.

---

### 8. Terminal Word Report + Novel Plan + Autonomous Story Bible

**What it aims to achieve:** (A) A script that reports word count by chapter and by Act; (B) a novel plan to reach ~80,000 words with a professional balance across Acts; (C) autonomous creation of a Character Bible for Tier 1 and Tier 2 characters.

**Would it achieve its goal?** (A) and (B) yes; (C) only partly—"autonomous" Story Bible creation is better as a guided, human-reviewed process.

**Is there an existing better tool?** Yes for (A) and (B): you have `.cursor/scripts/word_count.sh`, `.cursor/notepads/terminal-automation-cheatsheet.md` (word by chapter/Act), and DRAFT_2_MASTER_BLUEPRINT_V2 with word targets. For (C), Story_Bible/character-bible.md and COMPASS already define Tier 1/2 characters; an AI can draft or extend entries, but you should approve them.

**Implementation in COMPASS / Walk This Way:** (A) Use the existing cheatsheet commands from the project root (e.g. `find Draft_1 -name "*.txt" -exec sh -c 'echo "$(basename "$1"): $(wc -w < "$1") words"' _ {} \;` for per-chapter, and by-Act loop). Optionally, add a `Draft_1/WORD_REPORT.md` that you or the AI regenerate after major milestones. (B) Keep the Novel Plan in DRAFT_2_MASTER_BLUEPRINT_V2 or a dedicated NOVEL_PLAN_WALK_THIS_WAY.md (target 80k, balance across Acts). (C) Use prompts like "Using Story_Bible/character-bible.md, draft [or expand] Tier 2 character entries for [names]; keep format consistent and I’ll review" rather than full autonomy—then implement approved changes in the Story Bible.

---

## HOOKS and SKILLS: Relevance to COMPASS and Walk This Way

**HOOKS (in Cursor/git/workflows):** Hooks are automated triggers (e.g. pre-commit, post-save) that run scripts or checks. For COMPASS, hooks could run a quick word count, run a linter on changed `.txt`/`.md` files, or remind you to update the Session Log. They would support consistency and reduce manual steps but are not required for creative quality—they’re efficiency and discipline tools. For Walk This Way, a light use is best: e.g. a post-save hook that appends to a "last edited" log or runs word count only when files under `Draft_1/` change, so you don’t add friction during drafting.

**SKILLS (reusable prompt/instruction sets):** "Skills" here mean named, reusable instruction bundles (e.g. "Scalpel & Hose pass," "Voice consistency check," "Chapter brief fill"). In COMPASS, skills can be implemented as Cursor rules, saved prompts in a doc, or MCP tools that encapsulate a procedure. For Walk This Way, defining 3–5 skills—e.g. "Open with Session Load Stack," "Apply Chapter Brief + Chain of Thought," "Run GOOD/BAD prose check," "End with AFTER strategy for next chapters"—would make sessions repeatable and easier to hand off between you and agents. They don’t replace your existing agents; they standardize how those agents are invoked and in what order.

---

## Recommended Next Steps for Draft_1 and COMPASS

1. **Create** `Draft_1/SESSION_LOAD_STACK.md` (or add a section to QUICK_START_GUIDE) listing the exact files to load at session start.
2. **Add** `Draft_1/CHAPTER_BRIEF_TEMPLATE.md` using your XML chapter-brief structure (goal, specific, constrain, technique, character, Refactoring, Debugging, Testing, Functions, Linting, Compiling, GIT).
3. **Unify** "Make It Good" in one place: e.g. `MAKE_IT_GOOD_DNA.md` linked from PROSE_DNA and DRAFT_MODES.json.
4. **Add** a GOOD vs. BAD prose section to `Story_Bible/author-style-library.md` or `PROSE_EXAMPLES_WALK_THIS_WAY.md` and reference it in the Session Load Stack and chapter briefs.
5. **Require** a short `<thinking>` block before major chapter rewrites (in the chapter brief or prompt) and save it with the chapter feedback.
6. **Standardize** the "AFTER" handoff: after completing a chapter, request a rewrite strategy for the next chunk and save it under STRATEGIC_WRITING_COORDINATOR.
7. **Use** AI self-direction sparingly for full-rewrite strategy refreshes; keep day-to-day direction in STRATEGIC_WRITING_COORDINATOR and blueprints.
8. **Use** existing word-count scripts and cheatsheet for WORD REPORT; keep Novel Plan in blueprint or NOVEL_PLAN doc; use AI to draft/expand Story Bible entries with your review.
9. **Consider** one or two light hooks (e.g. word count or "last edited" log when `Draft_1/` changes) and define 3–5 named "skills" (Session Load Stack → Chapter Brief + Thinking → Rewrite → GOOD/BAD check → AFTER strategy) for COMPASS.

---

## Document Source

This evaluation applies the "Important Cursor created document / tool" (the 8 numbered examples) to the folder **Draft_1** and to the COMPASS Creative Writing System for the novel **Walk This Way**. It distinguishes tools that are worthy and should be implemented from those that are partly or fully superseded by existing Cursor features, MCPs, scripts, and COMPASS assets.
