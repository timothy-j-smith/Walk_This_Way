# Cursor Creative Writing: Secret Sauce & Mind-Bending Master Guide

**Purpose:** Systematic, numbered answers to advanced Cursor/Claude prompting, MCPs, and creative-writing techniques.  
**Created:** 2026  
**Use:** Reference for COMPASS, Walk This Way, and fiction writing in Cursor.

---

## PART I: CHAIN OF THOUGHT PROMPTING

### 1. What is Chain of Thought (CoT)?

1. **Definition:** A prompting technique that asks the model to produce explicit reasoning steps before answering.
2. **Mechanism:** Instead of "answer → output," you use "think step-by-step → then answer."
3. **Root:** Comes from research showing that models perform better on complex tasks when they "show their work" (Wei et al., 2022).
4. **Effect:** Forces the model to consider multiple angles, surface assumptions, and reduce logical leaps.

### 2. What does it do?

1. **Slows the model down** so it doesn't jump to a premature conclusion.
2. **Increases traceability** — you see *why* the model chose a path.
3. **Reduces confabulation** — stepwise reasoning catches contradictions.
4. **Improves consistency** — when the model states assumptions, it's more likely to honor them in the output.

### 3. How to implement it

1. **Simple:** Add `<thinking>` before your request:  
   `Before answering, think through: <thinking>...[steps]...</thinking> Then [your task].`
2. **Structured:** Use numbered steps (Step 1: Character motivations, Step 2: Subtext, etc.).
3. **Rule-based:** Add to `.cursor/rules/` so it applies automatically (e.g. `chain-of-thought-guide.md`).
4. **Slash command:** Create a `/cot` or `/think` command that injects the thinking block.

### 4. Is it effective and why?

1. **Yes.** Studies show gains on math, logic, and multi-step reasoning.
2. **Reason:** Models are autoregressive; explicit intermediate tokens create a better "path" to the final answer.
3. **For fiction:** Effective for plot decisions, character arcs, and structural problems — less so for trivial edits.
4. **Trade-off:** Uses more tokens and time; use selectively for high-stakes decisions.

---

## PART II: CHAIN OF THOUGHT + XML TAGS

### 5. Combining CoT with XML Tags

1. **Order:** `<thinking>` first (reasoning), then XML tags (structure), then the task.
2. **Example:**
   ```
   <thinking>
   - What does Nick want in this scene?
   - What's the power dynamic with Jackie?
   - How does this serve the class-divide theme?
   </thinking>

   <scene>
   <goal>Nick realizes Jackie's privilege protects him</goal>
   <tone>resentment beneath surface calm</tone>
   <constraint>No exposition; show through action</constraint>
   <characters>Nick, Jackie</characters>
   </scene>

   Rewrite this scene.
   ```
3. **Why combined:** CoT supplies the *why*; XML supplies the *what* (goal, tone, constraint). Together they reduce ambiguity and improve quality.

### 6. Slash Command / Cursor Prompt for CoT

**Option A: Cursor Rule (`.cursor/rules/`)**

Create `cot-fiction.mdc`:

```markdown
---
description: Chain of Thought for fiction decisions
globs: "*.txt"
alwaysApply: false
---

Before major fiction decisions, use this thinking block:

<thinking>
- Character motivations?
- Subtext and power dynamics?
- Thematic implications?
- Narrative consequences?
</thinking>
```

**Option B: Slash Command (`.cursor/commands/`)**

Create `cot-fiction.md`:

```markdown
# Chain of Thought – Fiction Decision

Before responding, think through:

<thinking>
- What does each character want in this scene?
- What's the subtext beneath the words?
- What's the power dynamic and how does it shift?
- How does this serve the theme (loss of innocence, class divide)?
- What are the narrative consequences?
</thinking>

Now proceed with the user's request.
```

**Usage:** User types `/cot-fiction` (or whatever Cursor maps) and the prompt is injected.

**Option C: Saved Prompt in `prompts.json`**

Add to `.cursor/config/prompts.json`:

```json
{
  "cot-fiction": "Before responding, think through: <thinking>Character motivations? Subtext? Power dynamics? Thematic implications? Narrative consequences?</thinking> Then proceed."
}
```

---

## PART III: CONTEXT PINNING

### 7. How effective is Context Pinning? Does it work?

1. **Yes, it works.** Pinning keeps files in the context window so the model doesn't need to re-fetch them.
2. **Effectiveness:** Highest when you pin 3–5 core files at session start (Story Bible, Directives, Current Chapter).
3. **Limitation:** Context is finite; too many pins can push out other useful content. Use 3–5 max.
4. **Evidence:** Fewer "please @mention" requests; faster responses; better consistency when Story Bible is always present.

### 8. Example of Context Pinning and why it works

**Scenario:** You're editing Chapter 12 and need Nick's voice + timeline + class-divide theme consistent.

**Without pinning:**
1. You: "Check Nick's voice in this scene."
2. Model: "Please @mention character-bible and the chapter."
3. You add @mentions.
4. Model responds. Next question: "Check timeline." Model may ask again.
5. **Result:** Multiple round-trips, slower.

**With pinning:**
1. You pin: `character-bible.md`, `walk-this-way-writing-directives.md`, `Chapter_12.txt`.
2. You: "Check Nick's voice in this scene."
3. Model uses pinned files immediately — no @mention needed.
4. You: "Check timeline." Model still has context.
5. **Result:** One-step replies, faster session.

**Why it works:** Pinned files are part of the prompt context on every message. The model doesn't "forget" them between turns.

---

## PART IV: CURSOR / CLAUDE / VS CODE TIPS AND TRICKS

### 9. Similar techniques that work in Cursor

1. **@-mentions** — Pin specific files/folders for one-time context.
2. **Cmd+K (inline edit)** — Edit selected text with instructions; good for line-level revisions.
3. **Composer** — Multi-file edits; state "apply to all" for systematic changes.
4. **Rules (`.cursor/rules/`)** — Always-on or glob-triggered instructions.
5. **`.cursorrules`** — Project-level instructions at repo root. ((.cursorrules has been deprecated and all my files are modern and updated so NEVER use .cursorrules anymore use .cursor/rules instead))
6. **MCP tools** — Extend context (Knowledge Graph, Vectara, etc.). ((what does extend context mean here?  Please provide an example))
7. **Notepads** — Scratch space the model can read; good for session notes.
8. **Chat history** — Model can reference earlier in the same chat; use for continuity. ((can model reference and effectively utilize a copy of a previous chat that I share with  new agent if I want to try an replicated a past effective chat?))

---

## PART V: SECRETS AND SUPER-SECRETS

### 10. "Secrets" people don't talk about

1. **XML structure is arbitrary** — You can invent tags; the model parses them. `<my_custom_tag>content</my_custom_tag>` works. ((explain why, when, where and how this would be helpful))
2. **Negative constraints** — `<constraint>Do NOT use the word "very"</constraint>` often works better than "avoid very."
3. **Role + task separation** — "You are a developmental editor. [Role]. Now: [Task]." Separating role from task can improve adherence.
4. **Output format forcing** — "Respond with exactly: [Structure]." Structure (e.g. bullet points, sections) steers format.
5. **Temperature via phrasing** — "One possible approach" vs "The definitive answer" nudges creativity vs certainty.
6. **Recency bias** — Information at the end of a long prompt can outweigh earlier content; put critical instructions last.
7. **Few-shot > description** — One good example often beats three paragraphs of description.

### 11. "Super-duper" secrets

1. **Nested thinking** — `<thinking><step1>...</step1><step2>...</step2></thinking>` can segment reasoning.
2. **Self-critique loop** — Ask: "Before finalizing, list 3 weaknesses of this draft. Then fix them."
3. **Contrastive prompting** — "Here's what NOT to do: [bad example]. Here's what TO do: [good example]. Now write."
4. **Chain of verification** — "Propose an answer. Then verify it against [constraint]. If it fails, revise."
5. **Meta-instructions** — "When uncertain, ask me. When confident, proceed." Reduces harmful guessing.

---

## PART VI: SECRET SAUCE — WHERE AND HOW

### 12. What and where is the "secret sauce"?

1. **XML tags** — `.cursor/rules/xml-tags-guide.md`. Structure reduces ambiguity.
2. **Chain of Thought** — `.cursor/rules/chain-of-thought-guide.md`. Reasoning before output.
3. **Few-shot examples** — `.cursor/rules/few-shot-examples-guide.md`. Concretize style.
4. **Role prompting** — `.cursor/rules/role-prompting-library.md`. Persona + expertise.
5. **Context pinning** — `.cursor/rules/context-pinning-guide.md`. Persistent context.

### 13. How to find these

1. **Cursor docs** — [cursor.com/docs](https://cursor.com/docs) for features.
2. **Community** — Reddit, Discord, X; people share prompts and rules.
3. **Experimentation** — Try variations; keep what works.
4. **MCP directory** — [mcprepository.com](https://mcprepository.com) and similar for tools.

### 14. How to define new ones

1. **Identify the pattern** — What instruction do you repeat? What format improves output?
2. **Write it down** — Create a `.md` or `.mdc` in `.cursor/rules/`.
3. **Use `globs`** — Apply only when relevant (e.g. `*.txt` for chapters).
4. **Test** — Compare output with and without the new pattern.
5. **Iterate** — Refine wording, add examples, update based on results.

---

## PART VII: IDEAS FROM CODING APPLIED TO FICTION

### 15. Coding techniques that attract favorable creative answers

1. **Test-driven prompting** — "Write the scene. Then list 3 ways it could fail [voice, continuity, theme]. Fix those."
2. **Refactoring metaphor** — "This paragraph is bloated. Refactor: same meaning, half the words."
3. **Debugging metaphor** — "Debug this scene: what's wrong with the pacing? Apply fixes."
4. **Code review role** — "You are a senior code reviewer. Review this prose for consistency and clarity."
5. **Git-style versions** — "Produce v1 (restrained) and v2 (expansive). I'll choose."
6. **Linting metaphor** — "Lint this passage: flag filter words, passive voice, vague nouns."
7. **DRY (Don't Repeat Yourself)** — "Find repeated phrases in this chapter. Consolidate or vary."

### 16. Making implicit logic explicit

1. **State it** — "The logic I'm assuming: Nick knows X, Jackie doesn't. Write accordingly."
2. **Ask for it** — "Before rewriting, list the implicit assumptions in this scene."
3. **Tag it** — `<assumption>Nick has not yet told Jackie about Dan</assumption>`
4. **Graph it** — Use Knowledge Graph MCP to store and query character knowledge.
5. **Checklist it** — "Verify: (1) Nick's age, (2) Timeline, (3) Who knows what."

---

## PART IX: FICTION-REVERSE-ENGINEERING MCP — NEXT LEVEL

### 19. Why Fiction Reverse Engineering is mind-bending

1. **Inverts the usual flow** — Instead of "write → hope it works," it's "analyze bestsellers → extract patterns → apply."
2. **Mathematical pacing** — Sentence length, dialogue ratio, tension curves become measurable.
3. **Formula extraction** — "What makes *Mystic River* work?" becomes a queryable structure.
4. **Cross-novel comparison** — Compare your draft to a target novel's metrics.
5. **Reduces guesswork** — Data replaces intuition for pacing and structure.
6. **Scalable** — Add more bestsellers to the "library" and refine the model.

### 20. Concepts for mind-bending Cursor tools, prompts, rules, commands

1. **Emotional-arc MCP** — Track valence (positive/negative) per scene; flag imbalanced acts.
2. **Voice-fingerprint MCP** — Embed character dialogue; detect drift.
3. **Thematic-consistency MCP** — Extract theme keywords; ensure scenes reinforce them.
4. **Continuity-graph MCP** — Entity-relationship graph for characters, places, objects.
5. **Pacing-prescription prompt** — "This act is 20% too slow. Suggest 3 cuts."
6. **Anti-cliché hook** — Pre-commit: scan for overused phrases; block or warn.
7. **Scalpel & Hose chain** — Sequenced prompts: Cut (scalpel) → Add (hose) → Verify.

---

## PART X: STYLE-EMULATION MCP — NEXT LEVEL

### 21. Why Style Emulation is next level

1. **Concrete target** — Instead of "write like Lehane," you *measure* against Lehane's prose.
2. **Quantifiable** — Sentence length, rhythm, dialogue ratio, vocabulary.
3. **Actionable feedback** — "Shorten sentences; increase dialogue; match terse rhythm."
4. **Reduces vagueness** — "Good style" becomes a profile the model can approximate.

### 22. Example: Style Emulation in action

**Input:** Your draft passage + Lehane profile.

**Output:**  
- Sentence length: yours 18.2 avg, Lehane 12.1 avg → "Shorten sentences."  
- Dialogue ratio: yours 15%, Lehane 28% → "Increase dialogue."  
- Filter words: 8 in your passage → "Cut 'seemed,' 'felt,' 'realized'."

**Result:** Specific, actionable edits instead of "make it more Lehane-like."

---

## PART XI: COGNEE (COGNEE_DATA_PATH) — CONNECTIONS

### 23. How Cognee sees non-obvious connections

1. **Graph-RAG** — Builds a graph of concepts from your documents.
2. **Traversal** — Queries like "How does X connect to Y?" traverse the graph.
3. **Emergent links** — Connections you didn't explicitly create can surface (e.g. "Dan's death" → "father's suicide" → "trust/betrayal").
4. **Why it works:** Embeddings capture semantic similarity; the graph captures relational structure.

### 24. Replicating in creative ways

1. **Thematic-link MCP** — "What theme does this scene reinforce?" → Traverse motif graph.
2. **Character-echo MCP** — "Which earlier scene echoes this one?" → Structure graph.
3. **Symbol-tracking** — "Where does the 'mockingbird' motif appear?" → Symbol graph.
4. **Contrast-finder** — "Find scenes that contrast (e.g. rich vs poor)." → Attribute graph.

---

## PART XII: KNOWLEDGE-GRAPH-MEMORY MCP — BREAKTHROUGH

### 25. Why Knowledge Graph Memory is groundbreaking for fiction

1. **Queryable story truth** — "Who knows about the cover-up?" returns Scout, Jem, Atticus, Tate.
2. **Timeline consistency** — "When did X happen relative to Y?" — no more contradictions.
3. **Relationship tracking** — "What is Nick's relationship to Jackie?" — explicit edges.
4. **Cross-session persistence** — Facts survive chat restarts.
5. **Single source of truth** — One graph for the whole novel.

### 26. Similar creative methods to create

1. **Character-state MCP** — Per-chapter snapshot: what each character knows, wants, fears.
2. **Plot-thread MCP** — Track open threads; flag unresolved ones.
3. **Motif-recurrence MCP** — "Frequency" appears in Ch 11, 24, 34 — ensure payoff.
4. **Echo MCP** — Scenes that mirror each other (e.g. two funerals) — ensure intentionality.

---

## PART XIII: FEW-SHOT EXAMPLES

### 27. How well does few-shot work?

1. **Very well** for style, voice, and technique — examples are concrete.
2. **Diminishing returns** — 1–3 examples often enough; more can confuse.
3. **Quality matters** — One excellent example beats three mediocre ones.
4. **Contrast helps** — GOOD vs BAD side-by-side teaches boundaries.

### 28. Training Cursor with few-shot

1. **Rules** — Add GOOD/BAD examples to `.cursor/rules/` (e.g. `few-shot-examples-guide.md`).
2. **Session start** — Load examples via @mention or pin.
3. **Prompt template** — Slash command that injects examples + task.

### 29. Slash command for few-shot fiction writing

Create `.cursor/commands/few-shot-rewrite.md`:

```markdown
# Few-Shot Rewrite

STYLE GUIDE (from Story_Bible/PROSE_DNA or author-style-library):

GOOD - Target style:
[Paste 1-2 paragraphs of your best prose]

BAD - Avoid:
[Paste 1 paragraph that doesn't work]

TASK: Rewrite the following in the GOOD style, avoiding the BAD patterns:
[User will paste text]
```

Update examples by editing the command file when your taste evolves.

---

## PART XIV: CORE 5 AGENTS VS. ONE FICTION AGENT

### 30. Order and effectiveness

1. **Core 5 in sequence** — Each agent specializes (Structure, Prose, Character, etc.). Sequential use can deepen each pass.
2. **Single fiction agent** — Faster; one model holds full context; less handoff loss.
3. **Hybrid** — Use one agent for most work; invoke specialists for problem areas (e.g. "Structural specialist: fix Act II pacing").
4. **Scalpel & Hose** — Can be one agent with two phases (Cut, then Add) or two agents.
5. **Recommendation:** Start with one strong fiction agent; add specialists when you hit limits (e.g. prose issues persist → Prose Expert).

---

## PART XV: HOOKS FOR EDITING AND CREATION

### 31. Most powerful hooks for editing

1. **Pre-save hook** — Run word count, continuity check, or "lint" (filter words, passive voice) before saving.
2. **Post-chapter hook** — After completing a chapter: generate summary, update Knowledge Graph, create linear issue.
3. **Pre-commit hook** — Verify no placeholder text (e.g. "[TK]"), run quick consistency check.
4. **Session-end hook** — Save session summary, update Story Bible if needed.

### 32. Most powerful hooks for creation

1. **Session-start hook** — Load Story Bible, Directives, current chapter; pin them.
2. **New-chapter hook** — Create chapter file from template; inject XML brief.
3. **Draft-complete hook** — Run Fiction Reverse Engineering; compare to target; generate revision plan.
4. **Research hook** — When you add a fact (date, place), prompt to update timeline/Story Bible.

---

## PART XVI: STYLE EMULATION — HOW AND WHY

### 33. How style emulation works

1. **Profile creation** — Analyze target prose (sentence length, dialogue ratio, vocabulary, rhythm).
2. **Comparison** — Your draft is scored against the profile.
3. **Gap analysis** — "You score 6/10 on rhythm; Lehane scores 9/10."
4. **Prescription** — "Shorten sentences; add dialogue; use more concrete nouns."

### 34. Is it effective and powerful?

1. **Yes** for measurable traits (sentence length, dialogue %).
2. **Partial** for "voice" — harder to quantify; may need few-shot in addition.
3. **Powerful** when combined with few-shot — metrics + examples = strong alignment.

---

## PART XVII: settings.json AND SIMPLE JSON "ANSWERS"

### 35. Learning from settings.json

1. **Simple key-value** — `.json` files with "answers" (e.g. target word count, preferred tense).
2. **Machine-readable** — Model can parse JSON; no ambiguity.
3. **Project-specific** — Different projects, different settings.
4. **Extension** — Create `fiction-settings.json`: `{"target_style": "Lehane", "pov": "close third", "avoid": ["very", "really"]}`.

### 36. Creative use of simple JSON

1. **`GOOD_BAD_EXAMPLES.json`** — Store passage IDs or snippets; model fetches when needed.
2. **`CHAPTER_BRIEF_TEMPLATE.json`** — Default fields for every chapter.
3. **`VOICE_PROFILES.json`** — Per-character: `{"Nick": {"class": "working", "traits": ["direct", "defensive"]}}`.
4. **`FLAGS.json`** — `{"filter_words": true, "passive_voice": true}` — toggles for lint rules.

---

## QUICK REFERENCE: WHERE EVERYTHING LIVES

| Technique        | Location                        |
|------------------|----------------------------------|
| Chain of Thought | `.cursor/rules/chain-of-thought-guide.md` |
| XML Tags         | `.cursor/rules/xml-tags-guide.md` |
| Context Pinning  | `.cursor/rules/context-pinning-guide.md` |
| Few-Shot         | `.cursor/rules/few-shot-examples-guide.md` |
| Role Prompting   | `.cursor/rules/role-prompting-library.md` |
| Commands         | `.cursor/commands/`             |
| Prompts          | `.cursor/config/prompts.json`   |
| Hooks            | `.cursor/hooks.json`            |

---

**Status:** Master reference. Add to it as you discover new "secret sauce."
