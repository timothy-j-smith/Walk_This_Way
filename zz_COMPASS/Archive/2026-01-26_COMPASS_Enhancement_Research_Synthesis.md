# COMPASS Enhancement Research Synthesis — January 2026
## Cursor / Novelist Research + Ultra, MAS, Enhanced & Cognee-Style Passes

**Date:** 2026-01-26  
**Location:** `zz_COMPASS/Archive/`  
**Source:** Pasted research (Cursor Jan 2026 updates, secret sauce, .cursor/rules/, 2026 roadmap, API/CLI/LSP, hidden rocks, 25+20 classics, Power Move Templates).  
**Method:** Base synthesis → Sequential Thinking Ultra (bias check), MAS (multi-perspective), Enhanced (deeper evaluation), Cognee-style (hidden connections with Cursor Secret Sauce & Cursor-native capabilities).

---

## EXECUTIVE SUMMARY

**Original synthesis:** 6 techniques to implement, 7 nuggets to document, 6 experiments to try, 5+ areas already covered.

**After Ultra / MAS / Enhanced / Cognee passes:**  
- **Additions:** Cursor native/MCP cross-check section; Cognee-style hidden connections (8 links); Elicitation; Dynamic MCP Tools; Hooks → COMPASS continuity; CLI `/rules` for COMPASS; Cognee audit of rules vs content; Multi-Agent Judging with COMPASS agents; 10-novel priority for Background Agents and Cloud (`&`).  
- **Refinements:** Agent memory in first wave (if low-friction); Plan Mode + Mermaid as technique-to-validate; Background Agents and `&` as high-priority for 10-novel Creative Director.

**Verdict:** 9 techniques to implement or validate, 10 nuggets to document, 9 experiments to try, 5+ areas already covered. No new MCPs; integrate Cursor native features and Cognee-style links into COMPASS workflow.

---

## PART I — SOURCE SUMMARY

### What the research covered

- **Cursor Jan 2026:** MCP resources, Hooks, Plan Mode, custom slash commands, Background Agents, CLI (models, MCP, rules)—“10–20x faster.”
- **“Secret sauce”:** XML-style tags, `.cursor/rules/` hierarchy, agent memory file, Composer, Dynamic MCP tools, Elicitation.
- **.cursorrules deprecated:** New model is `.cursor/rules/` with `.mdc` files, path-scoped and versioned.
- **2026 power moves:** Mermaid in Plan Mode, Multi-Agent Judging, /Generate Cursor Rules, Debug Mode for fiction, Cloud Agents (`&`), Hooks, rule inheritance.
- **“Hidden rocks”:** @Browser, learning-log, Creative Director shift, API automation, “novel-brain,” compound optimization, meta-prompt.
- **API/CLI/LSP:** Framed for a “10-novel creative director” (automation, project switching, LSP for navigation/consistency).
- **Craft material:** 25 timeless + 20 modern classics, universal truths, craft patterns—for understanding greatness, not for new tools.
- **Cursor Power Move Templates:** Full artifact (character/scene/plot/style/world/timeline, slash commands, `.cursor/rules/`).

### How it fits COMPASS

COMPASS already has: Core (agents, commands, prompts, writing directives), Writing Guides MCP, filesystem, Git, Sequential Thinking, plus Premium roadmap (DNA Memory, style MCPs, research MCPs, etc.). This research recommends **workflow and documentation enhancements**, not replacement of MCPs.

---

## PART II — TECHNIQUES TO IMPLEMENT (OR VALIDATE)

### 1. Migrate from `.cursorrules` to `.cursor/rules/` with `.mdc` files

**Status vs your system:** Research states `.cursorrules` is deprecated; COMPASS and project may still assume the old path.

**What to do:** Audit the project for `.cursorrules` and any docs that reference it. Plan migration to `.cursor/rules/` with rule files as `.mdc` (e.g. `writing-core.mdc`, `character-voice.mdc`) with path globs and `alwaysApply` / agent-requested as needed. Update COMPASS and project docs to describe the new layout.

**Verdict:** Implement—highest priority (deprecation risk).

---

### 2. XML-style tags in prompts and rules

**Status:** JAZZ and research both recommend it.

**What to do:** In COMPASS prompts and rule text, use tags like `<scene_context>`, `<character_state>`, `<goal>`, `<tone>`, `<constraint>`. Add a short “XML tag convention” to the writing-assistant rule or a dedicated `prompting.mdc`. Use the same pattern in COMPASS Enhancement Research prompts.

**Verdict:** Implement—zero cost, high clarity.

---

### 3. Context pinning discipline

**Status:** Cursor UI feature; not an MCP.

**What to do:** In COMPASS workflow docs, state standard pins: e.g. Story Bible (or main character/world refs), Draft 2 blueprint, style guide. Pin these at session start (or document “pin these when doing continuity/structure work”). Optionally one sentence in `.cursor/rules/writing-assistant.mdc` reminding use of pinned project context.

**Verdict:** Implement as documented COMPASS workflow.

---

### 4. Agent memory / session-continuity file

**Status:** Research suggests `_context/agent_memory.md` (or similar) updated after major sessions and referenced in prompts/rules.

**What to do:** Define a lightweight “session memory” file (name and path in COMPASS: e.g. `_context/agent_memory.md` or under `Story_Bible/`). In COMPASS workflow: “After major sessions, append: What we did, current focus, decisions made.” In rules or pinning: “When doing continuity or long rewrites, @ this file.”

**Refinement (Enhanced):** If implementation is “create file + one rule line,” this can sit in the first wave.

**Verdict:** Implement as COMPASS convention; document in Core/workflow.

---

### 5. Use /Generate Cursor Rules when decisions crystallize

**Status:** Cursor feature; not yet in COMPASS workflow.

**What to do:** In COMPASS workflow (or Enhancement Research Guide): “When a chat produces a stable rule (e.g. ‘never do X in this project’, ‘always use Y for Z’), run /Generate Cursor Rules so it becomes a `.cursor/rules/` rule.” Document as the standard way to turn “rules we now follow” into persisted rules.

**Verdict:** Implement as documented step in COMPASS workflow.

---

### 6. Nested `.cursor/rules/` for POV, act, or folder

**Status:** Research describes subfolders (e.g. `chapters/.cursor/rules/`, `act-one-tone.mdc`) scoped by path.

**What to do:** For multi-POV or multi-act projects, add a “Nested rules” section to COMPASS (or to the rules-migration doc). Explain: “You can add `.cursor/rules/` under act or POV folders with path-scoped `.mdc` files.” Optionally one example (e.g. `act-one-tone.mdc` for Act I tone).

**Verdict:** Implement as advanced option in COMPASS rules documentation.

---

### 7. Hooks → COMPASS continuity (technique to validate)

**Source:** Cognee-style pass. Hooks run before/after the agent loop.

**What to do:** Once Hooks are in use, document “after every chapter save, run a small continuity check or append to agent_memory” as a COMPASS technique. Cursor Hooks become the trigger for COMPASS continuity workflow.

**Verdict:** Technique to implement once Hooks are validated.

---

### 8. Cursor CLI `/rules` for COMPASS rules

**Source:** Cognee-style pass. Cursor CLI supports `/rules` for creating/editing rules.

**What to do:** In COMPASS workflow: “Use Cursor CLI `/rules` when updating COMPASS rule files”—faster iteration from terminal.

**Verdict:** Implement as documented step in COMPASS rules workflow.

---

### 9. Plan Mode + Mermaid → COMPASS structural input (technique to validate)

**Source:** MAS + Enhanced + Cognee-style. Plan Mode can output Mermaid; COMPASS has plot_master, timeline, structural docs.

**What to do:** After validating Plan Mode + Mermaid as an experiment, add “ingest Plan Mode + Mermaid output as a structural doc (or graph) that COMPASS agents/rules reference” as a technique. Cursor native planning feeds COMPASS structure.

**Verdict:** Technique to implement once the experiment succeeds.

---

## PART III — NUGGETS TO DOCUMENT

1. **Creative Director vs writer** — Capture in COMPASS Core or TIMOTHY_WORKING_STYLE_DNA; reference in workflows (vision/taste/judgment vs execution).
2. **Rule inheritance** — Rules including other rules via `@filename.mdc`; note in “Modern .cursor/rules/” so rule design can use it.
3. **Compound optimization** — Voice memo → AI draft → automated checks → polish; describe as target workflow in COMPASS.
4. **Learning loop** — “Learning-log” / “what I changed and why” feeding style guide; frame as COMPASS Premium / “writing DNA” practice.
5. **Cross-project intelligence (10 novels)** — Portfolio view, cross-novel themes, project switching; document as future COMPASS use case.
6. **“Debug Mode for fiction”** — Using Cursor’s Debug Mode (or similar) for narrative bugs: flat chapters, pacing drops, motivation gaps; document as experimental usage idea.
7. **Meta-prompt pattern** — How to instruct Claude on working style, energy, and feedback preferences; add as “how to get Claude to adapt to you” in COMPASS Core or Archive.
8. **Dynamic MCP Tools / add_tools** *(from Enhanced)* — Cursor’s approach to tool limits and “always-available” vs dynamic tools; relevant for COMPASS-style MCPs that want to expose different tool sets (e.g. by task or Liberty Level).
9. **Elicitation as COMPASS UX** *(from MAS + Cognee-style)* — MCPs requesting structured input (e.g. “Which POV?” or “Liberty Level?”) via forms; reduces prompt friction for COMPASS choices.
10. **Cognee as session↔graph bridge** *(from Cognee-style)* — Using Cognee to surface links between session memory, Story Bible, and knowledge graph; Cognee as bridge between session continuity and persistent memory.

---

## PART IV — EXPERIMENTS TO TRY

1. **Plan Mode + Mermaid** — Use Plan Mode on one structural doc (e.g. one act or one strand) and ask for a Mermaid plot/structure diagram.
2. **Multi-Agent Judging** — For one scene, ask for 3 versions and let Cursor pick one and explain why. *(Cognee-style: use as meta layer when multiple COMPASS agents run in parallel.)*
3. **Background Agents** — Trigger a non-urgent task (e.g. “check timeline for Ch3–5”) while you keep writing. **10-novel priority:** treat as high-priority experiment or “technique to validate,” not only “when convenient.”
4. **@Browser** — Use @Browser once for something small (e.g. period detail or competitor back-cover copy). *(Cognee-style: augments COMPASS Research for live sites.)*
5. **Hooks** — If available, try one post-save hook (e.g. “run a small continuity check” or “append to agent_memory”). Document result.
6. **Cloud Agents (`&`)** — Send one “overnight” job with `&` (e.g. “analyze Acts I–II for pacing”). **10-novel priority:** treat as high-priority experiment for Creative Director workflow.
7. **Elicitation for COMPASS choices** *(from MAS + Cognee-style)* — Try an MCP that supports Elicitation for at least one COMPASS decision type (e.g. Liberty Level or POV).
8. **Cognee audit of rules vs content** *(from Cognee-style)* — Use Cognee (or similar) to find connections and conflicts between COMPASS rules and novel content.
9. **Multi-Agent Judging with COMPASS agents** *(from Cognee-style)* — Run multiple COMPASS agents in parallel once and use Cursor’s “pick best” behavior to select output.

---

## PART V — WHAT'S ALREADY COVERED (DO NOT DUPLICATE)

- **Character consistency** — WalkThisWay Character MCP + Story Bible. Don’t add a second system.
- **Style analysis** — Style Emulation, Dennis Lehane, Fiction Reverse Engineering MCPs. Use existing MCPs; cite research in COMPASS docs if useful.
- **Deep research** — Firecrawl (when API is in place) + DuckDuckGo. @Browser is complementary; treat as experiment, not replacement.
- **Memory** — Knowledge Graph + DNA Memory design. “Novel-brain,” “second brain,” “agent memory” are workflow patterns on top; don’t rebuild memory infrastructure.
- **Reverse-engineering methodology** — Fiction Reverse Engineering MCP + your critique/analysis workflow. The 25+20 classics and “universal truths” are **reading and craft references**—add as “Craft & canon” or “Reading for craft” in COMPASS/Archive, not a new MCP or module.

---

## PART VI — CURSOR NATIVE / BUILT-IN FEATURES AND MCP CROSS-CHECK

*(From Ultra + MAS + Cognee-style passes.)*

Map Cursor-native capabilities to COMPASS so we don’t duplicate and we use them as integration points.

| Cursor native / built-in | Role | COMPASS relationship |
|---------------------------|------|----------------------|
| **CLI** (`/rules`, `/plan`, `/ask`, `/models`, `/mcp`) | Create/edit rules, run Plan Mode, switch models, manage MCPs from terminal | Use `/rules` for COMPASS rule iteration; use `/plan` for structure; document in workflow. |
| **Plan Mode** | Build plans (and Mermaid) inside the editor | Feed output into COMPASS structural docs (plot_master, timeline, or dedicated structural doc). |
| **Hooks** | Run scripts before/after agent loop | Trigger “after save” continuity or agent_memory update; link to COMPASS continuity. |
| **Pinned Chats** | Pin chats in agent sidebar for reference | Pin critical writing decisions; document in COMPASS workflow. |
| **/Generate Cursor Rules** | Turn chat decisions into `.cursor/rules/` rules | Use when a COMPASS rule crystallizes in chat; document in workflow. |
| **Context Pinning** | Pin files so they stay in context | Pin Story Bible, blueprint, style guide; document as COMPASS discipline. |
| **@Browser** | Agent interacts with live browser (screenshot, DOM, etc.) | Augment COMPASS Research for live sites, competitor copy, or marketing; experiment. |
| **Multi-Agent Judging** | Cursor evaluates multiple runs and picks “best” + explains why | Use when multiple COMPASS agents run in parallel; meta layer for Agent Choreography. |
| **Background Agents** | Tasks run independently while you work | Use for research or continuity checks while writing; 10-novel priority. |
| **Cloud Agents (`&`)** | Send message to cloud, pick up on web/mobile later | Use for overnight analysis (e.g. pacing, structure); 10-novel priority. |
| **Elicitation** *(when supported by MCP)* | MCP requests structured user input via forms | Could surface “Which POV?” or “Liberty Level?” and cut prompt friction. |

**Principle:** Use Cursor-native features as the “control plane”; COMPASS rules, agents, and MCPs as the “content plane.” Document each link so COMPASS and Cursor evolve together.

---

## PART VII — COGNEE-STYLE HIDDEN CONNECTIONS

*(From Cognee-style pass. Cognee = “hidden connections” / graph-RAG; applied here to Cursor Secret Sauce ↔ Cursor capabilities ↔ COMPASS.)*

1. **Cursor rules ↔ Cognee** — Rule inheritance (`@file` in rules) + graph-style reasoning can expose links or conflicts between COMPASS rules and novel content. **Use:** Cognee (or similar) to audit or discover connections between COMPASS rules and Story Bible / plot / timeline.
2. **Plan Mode + Mermaid ↔ COMPASS structure** — Plan Mode output can be ingested as a structural artifact that COMPASS agents or rules reference.
3. **Hooks ↔ COMPASS continuity** — A Hook can run “after every chapter save” a small continuity step or append to agent_memory.
4. **Elicitation ↔ COMPASS Liberty Levels / Draft Modes** — Liberty Level or “Which POV?” could be requested via Elicitation (when an MCP supports it).
5. **Multi-Agent Judging ↔ COMPASS agents** — Multi-Agent Judging as meta layer when several COMPASS agents run in parallel.
6. **@Browser ↔ COMPASS Research** — @Browser augments COMPASS Research for live sites, competitor copy, or marketing.
7. **Cursor CLI `/rules` ↔ COMPASS rules** — COMPASS rule iteration via Cursor CLI.
8. **Cognee ↔ Session memory + Story Bible** — Cognee surfaces links between “what we accomplished,” Story Bible, and the knowledge graph.

---

## PART VIII — CONSENSUS AND PRIORITY ORDER

### First wave (implement soon, no Cursor config risk)

1. Document `.cursor/rules/` migration—audit for `.cursorrules`, plan migration, update COMPASS docs.  
2. Add XML tag convention to COMPASS prompts and rules; document in prompting guide.  
3. Document context pinning in COMPASS workflow (what to pin, when).  
4. Write nuggets 1–7 (and 8–10 as needed) into COMPASS Core/Archive/working-style.  
5. **Agent memory** — If it’s “one file + one rule line,” add to first wave; define path and one rule reference.

### Second wave (when changing behavior or settings)

6. Introduce session memory file and “update after major sessions” + “@ when doing continuity” in workflow.  
7. Use /Generate Cursor Rules when COMPASS rules crystallize in chat; document in workflow.  
8. Add nested rules subsection to COMPASS rules documentation.  
9. **Hooks → COMPASS continuity** — Document as technique once Hooks are in use.  
10. **Cursor CLI `/rules`** — Document as standard for COMPASS rule updates.

### Third wave (experiments; 10-novel priorities)

11. Run **Plan Mode + Mermaid**, **Multi-Agent Judging**, **Elicitation**, **Cognee audit**, **Multi-Agent Judging with COMPASS agents**.  
12. **10-novel Creative Director:** Treat **Background Agents** and **Cloud (`&`)** as high-priority experiments or “techniques to validate,” not only “when convenient.”  
13. **Plan Mode + Mermaid → COMPASS structure** — Once experiment succeeds, add as technique (ingest output into COMPASS structural docs).

### Fourth wave (reference only)

14. **25+20 classics and “universal truths”** — Store as craft/reading reference (e.g. in `zz_COMPASS/Archive/` or a “Craft & canon” doc).  
15. **Cursor Power Move Templates** — Compare to existing COMPASS templates; merge gaps, don’t replace COMPASS.

---

## PART IX — WHAT NOT TO DO

- **Do not** add new MCPs or rebuild character/style/research/memory/reverse-engineering inside COMPASS on the basis of this research alone.  
- **Do not** change Cursor settings, Hooks, or API/CLI until you’ve decided which recommendations to adopt.  
- **Do not** treat the 25+20 classics material as a new “COMPASS module”—treat as reference.  
- **Do not** replace current COMPASS templates with the Power Move Templates artifact; merge only where it clearly improves COMPASS.

---

## SYNTHESIS METHODOLOGY

- **Base synthesis:** Catalog research → map to COMPASS → techniques / nuggets / experiments / already covered → priority order.  
- **Ultra pass:** Bias check (confirmation, status-quo, anchoring, availability) → Cursor native cross-check, 10-novel priority for Background Agents and Cloud (`&`).  
- **MAS pass:** Multi-perspective (Factual, Critical, Synthesis) → Elicitation, Plan Mode + Mermaid as technique-to-validate.  
- **Enhanced pass:** Deeper evaluation (Evaluative, Creative, Dialectical) → Agent memory in first wave, Dynamic MCP Tools nugget, 10-novel priority.  
- **Cognee-style pass:** Hidden connections (Cursor Secret Sauce ↔ Cursor capabilities ↔ COMPASS) → 8 links, new techniques-to-validate, new experiments, new nuggets.

---

**Status:** Merged synthesis complete. Use this document when updating COMPASS and Cursor workflow; store future syntheses in `zz_COMPASS/Archive/` with date-prefixed filenames (e.g. `YYYY-MM-DD_Description.md`).

---

*Created: 2026-01-26 | Last updated: 2026-01-26*
