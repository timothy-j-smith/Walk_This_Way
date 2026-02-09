# Fiction Writing MCP System Refresh — Systematic Summary & Next Steps

**Source:** `/Users/timothy/Desktop/FICTION WRITING MCP SYSTEM FOR CURSOR REFRESH.txt`  
**Reviewed using:** Sequential Thinking approach (step-by-step extraction of goals, MCP list, naming advice, and requested actions)  
**Date:** 2026  
**Status:** Summary and recommended next steps only. **No MCP config or renames have been applied yet.** Pending your answers to the questions below before making changes.

---

## Part 1 — Systematic Summary of the Document

### 1.1 What the Document Is

- **Title:** Revolutionary Fiction Writing MCP System — Complete Documentation & Implementation Guide  
- **Version:** Final Complete - All MCPs Integrated (January 19, 2026)  
- **Purpose:** Define and document the world’s most sophisticated AI-assisted fiction writing system for Cursor, aimed at:
  - **10 independent novels** (different characters, stories, settings)
  - Systematic, structured design
  - Multi-model orchestration (GPT-4, Gemini, O3, Claude)
  - Knowledge-graph memory for characters/plots
  - Style emulation
  - Zero conflicts between MCP servers

### 1.2 Critical Philosophy (from the Document)

- **Shift:** Move from passive `.cursor/rules` to **active, computational MCPs** with enforcement.
- **Principle:** Everything that enforces consistency, validates content, or guides style should be an MCP (executable tools), not static rules.

### 1.3 Document Structure (What It Contains)

| Section | Content |
|--------|---------|
| **Complete MCP Arsenal** | All MCPs described: roles, installation JSON, API/prereqs, sophistication level |
| **Core Memory & Reasoning** | Knowledge Graph Memory, Sequential Thinking (base, MAS, Ultra, Enhanced, Rust) |
| **Advanced Memory** | MemoryStack, scanadi/mcp-ai-memory, MemoryGraph, enhanced-mcp-memory, Supermemory |
| **Multi-Model Orchestration** | Zen MCP / PAL MCP |
| **Research & Web** | Firecrawl (PRIMARY), DuckDuckGo (quick), Brave Search (requested add), Puppeteer (optional) |
| **File & Document** | Filesystem, Pandoc |
| **Version Control** | GitHub, GitKraken |
| **Semantic Search & RAG** | Vectara, UltraRAG, RAGentA, RAGVUE, Cognee |
| **Orchestration & Tool Management** | ScaleMCP, MemTool, LLM × MapReduce-V3 |
| **Automation & Workflow** | n8n, PiloTY |
| **Memory Reinforcement** | Anki |
| **Style & Writing** | COMPASS Writing Guides, Style Emulation, Dennis Lehane, AI Writers Workshop |
| **Collaboration & Cloud** | Google Workspace |
| **Infrastructure** | Docker (optional) |
| **Strategic Naming** | !CRITICAL: Rename MCPs for distinct, purpose-specific names to avoid conflicts and improve tool selection |
| **Custom MCP Approach** | Why custom MCPs beat passive rules |
| **Style Emulation MCP** | Full implementation (code, install, test) |
| **“Please add” list** | Many MCPs explicitly requested to be added |
| **Conflict handling** | Strategic naming, different purposes, explicit instructions, disable redundancies, test selection |

### 1.4 Fact Correction Noted in the Document

- **Walk This Way timeline:** Document corrects itself: Dan Johnson dies **November 14, 1976** (Nick 15, “man of the house” at 15), not 1979. Battle of the Bands is March 1979. This aligns with your Story Bible.

---

## Part 2 — MCPs to ADD (From the Document)

Below: **only** MCPs the document explicitly asks to add or describes as “please add” / “strong addition,” plus one doc typo clarification.

### 2.1 Explicitly Requested Adds

| # | MCP | Document request | Your current config | Suggested action |
|---|-----|------------------|----------------------|-------------------|
| 1 | **Brave Search** | “Brave Search MCP (please add) strong addition to existing MCP search engines” | Not present | **ADD** — Gives a second quick-reference search alongside DuckDuckGo. |
| 2 | **MemoryStack** | Described in arsenal; “please add” implied by inclusion | Not present | **ADD** (if you want pattern/consolidation memory) — Document lists npm/package; exact package name needs verification. |
| 3 | **MemTool** | Full spec and JSON in document | Not present | **ADD** — Short-term memory / context optimization (`@memtool/mcp-server`). |
| 4 | **PiloTY** (terminal-control) | Full spec and JSON | Not present | **ADD** (optional) — Only if you want AI-driven terminal/infra control. |
| 5 | **RAGVUE** | Full spec and JSON | Not present | **ADD** (optional) — RAG diagnostics; useful if you rely on Vectara/UltraRAG/RAGentA. |
| 6 | **LLM × MapReduce-V3** | Full spec and JSON | Not present | **ADD** (optional) — Meta-orchestrator; requires Python package `llm_mapreduce_v3` (verify exists). |
| 7 | **Puppeteer** (puppeteer-automation) | In arsenal; “consider for advanced use” | Not present | **ADD** (optional, disabled by default) — For browser automation if ever needed. |
| 8 | **Docker** (docker-containers) | In arsenal; “flexibility,” “disabled: true” in doc | Not present | **ADD** (optional, disabled by default) — For containerized workflows if needed. |
| 9 | **Sequential Thinking Rust** | In arsenal | Not present | **ADD** (optional) — Only if you have Rust/cargo and want performance variant. |

### 2.2 “Please add this MCP” List (Document Lines ~831–846)

These are listed with **no installation details** in the document. Treat as **candidates**; each needs package/repo verification before adding:

| # | MCP name in document | Note |
|---|----------------------|-----|
| 1 | PostgreSQL MCP | Need package name and config. |
| 2 | SQLite MCP | Need package name and config. |
| 3 | Airtable MCP | Need package name and config. |
| 4 | Fetch MCP | Need package name and config. |
| 5 | Slack MCP | Need package name and config. |
| 6 | Adobe Creative Cloud MCP | Need package name and config. |
| 7 | Imagen3 MCP | Need package name and config. |
| 8 | DeepSeek Thinker MCP | Need package name and config. |
| 9 | AssemblyAI MCP | Need package name and config. |
| 10 | Chain of Draft MCP | Need package name and config. |
| 11 | Figma MCP | Need package name and config. |
| 12 | Jupyter Notebook MCP | Need package name and config. |
| 13 | Vizro MCP | Need package name and config. |
| 14 | Label Studio MCP | Need package name and config. |
| 15 | GrowthBook MCP | Need package name and config. |
| 16 | Multi-Agent Debate MCP | Need package name and config. |

### 2.3 Sequential Thinking Ultra — No Add Needed

- Document says “Sequential Thinking Ultra MCP (please add)” in the same block as PostgreSQL/SQLite.
- **Your config already has** `sequential-thinking-ultra` (npx `@sequential-thinking/ultra`).  
- **Action:** None. Consider this a document slip; no second Ultra add.

---

## Part 3 — MCPs to RENAME (Document’s Strategic Naming Advice)

The document says: **“!CRITICAL: STRATEGIC NAMING IMPLEMENTATION”** and **“This naming strategy should be applied to every MCP in the configuration.”**

### 3.1 Document’s Suggested Naming Convention

- **Memory:** `series-memory` (permanent), `session-memory` (temporary), `semantic-search-memory` (Vectara).
- **Style:** `style-emulation`, `dennis-lehane-style`, `compass-writing-guides`.
- **Character/plot:** `character-consistency`, `plot-timeline` (or similar).
- **Example “zero conflicts” set:** `walk-this-way-memory`, `session-memory`, `zen-orchestrator`, `sequential-thinking`, `manuscripts`, `version-control`, `web-search`.

### 3.2 Your Current Names vs. Document Suggestions

| Current name (mcp.json) | Document suggestion / intent | Recommendation |
|-------------------------|-----------------------------|----------------|
| **walk-this-way-files** | “manuscripts” or keep project-specific | **Keep** or rename to `manuscripts` only if you want a generic name for multi-novel portability. |
| **knowledge-graph-memory** | `series-memory` (permanent storage) | **Optional rename** to `series-memory` if you want to match doc exactly; current name is already clear. |
| **vectara** | `semantic-search-memory` | **Optional rename** to `semantic-search-memory` for clarity vs. other memory MCPs. |
| **style-emulation** | `style-emulation` | **Keep** — Already matches. |
| **dennis-lehane-style** | `dennis-lehane-style` | **Keep** — Already matches. |
| **compass-writing-guides** | `compass-writing-guides` | **Keep** — Already matches. |
| **github** | “version-control” (example) | **Keep** — Standard and clear; renaming could break expectations. |
| **gitkraken** | (no change) | **Keep**. |
| **duckduckgo-search** | “web-search” (example) | **Optional rename** to `web-search` or keep; “duckduckgo-search” is already descriptive. |
| **sequential-thinking** | `sequential-thinking` | **Keep**. |
| **sequential-thinking-mas** | (no specific rename) | **Keep**. |
| **sequential-thinking-ultra** | (no specific rename) | **Keep**. |
| **enhanced-sequential-thinking** | (no specific rename) | **Keep**. |
| **memorygraph** | (no specific rename) | **Keep** or consider `context-optimized-memory` if you want to stress role. |
| **enhanced-mcp-memory** | (no specific rename) | **Keep**. |
| **supermemory** | (no specific rename) | **Keep**. |
| **firecrawl** | (no specific rename) | **Keep**. |
| **pandoc** | (no specific rename) | **Keep**. |
| **cognee-connections** | (no specific rename) | **Keep**. |
| **ultrarag** | (no specific rename) | **Keep**. |
| **ragenta** | (no specific rename) | **Keep**. |
| **scalemcp** | (no specific rename) | **Keep**. |
| **ai-writers-workshop** | (no specific rename) | **Keep**. |
| **anki-flashcards** | (no specific rename) | **Keep**. |
| **workflow-automation** | (no specific rename) | **Keep**. |
| **zen-orchestrator** | `zen-orchestrator` | **Keep**. |
| **toolbox** | (no specific rename) | **Keep**. |
| **cursor-workflow-orchestrator** | (no specific rename) | **Keep**. |
| **fiction-reverse-engineering** | (no specific rename) | **Keep**. |
| **professional-editor** | (no specific rename) | **Keep**. |

### 3.3 Summary of Rename Recommendations

- **No renames required** for correctness; your names are already purpose-specific.
- **Optional renames** only if you want to align 100% with the document:
  - `knowledge-graph-memory` → `series-memory`
  - `vectara` → `semantic-search-memory`
  - `walk-this-way-files` → `manuscripts` (only if you want a project-agnostic name)
  - `duckduckgo-search` → `web-search` (optional)

---

## Part 4 — Cursor Next Steps (Checklist)

Use this **after** you answer the questions in Part 5.

### 4.1 MCPs to add (in order of impact)

1. **Brave Search** — Add with npx (exact package to be confirmed, e.g. Brave Search MCP from npm).
2. **MemTool** — Add (`@memtool/mcp-server`).
3. **MemoryStack** — Add after confirming npm package name.
4. **RAGVUE** — Add if you use RAG heavily (Python `ragvue`).
5. **PiloTY** — Add only if you want terminal/infra control (Python `piloty_mcp`).
6. **LLM MapReduce-V3** — Add only if you want meta-orchestration (verify Python package).
7. **Puppeteer** — Add disabled by default, for optional browser automation.
8. **Docker** — Add disabled by default, for optional container use.
9. **Sequential Thinking Rust** — Add only if you use Rust and want the performance variant.

### 4.2 Optional renames (only if you choose)

- [ ] `knowledge-graph-memory` → `series-memory`
- [ ] `vectara` → `semantic-search-memory`
- [ ] `walk-this-way-files` → `manuscripts`
- [ ] `duckduckgo-search` → `web-search`

### 4.3 “Please add” list — no action until verified

- Research and confirm package/repo for each of: PostgreSQL, SQLite, Airtable, Fetch, Slack, Adobe CC, Imagen3, DeepSeek Thinker, AssemblyAI, Chain of Draft, Figma, Jupyter, Vizro, Label Studio, GrowthBook, Multi-Agent Debate.
- Add only those that are (a) available, (b) compatible with Cursor MCP, and (c) useful for your fiction workflow.

### 4.4 Documentation updates (after config changes)

- Update `COMPASS_MCP_MANIFEST.md` with any new MCPs and any renames.
- Update `MCP_COMPLETE_ACTIVE_LIST.md` with new entries and status (ready / needs API / disabled).
- Optionally add a short “Fiction Writing MCP Refresh” section to your COMPASS docs that points to this summary and the strategic naming rationale.

---

## Part 5 — Discrepancies and Questions for You

### 5.1 Discrepancies

| # | Issue | Detail |
|---|--------|--------|
| 1 | **Enhanced Sequential Thinking command** | Document shows **two** configs: (A) `"command": "python", "args": ["-m", "mcp_thinking"]` and (B) npx `@vitalymalakanov/mcp-enhanced-sequential-thinking`. Your current config uses (B). The Python version implies a different package (`mcp_thinking`). Unclear which is the intended “canonical” install. |
| 2 | **Sequential Thinking Ultra “please add”** | Document says “please add” in the same bullet as PostgreSQL/SQLite. You already have `sequential-thinking-ultra`. Interpreted as doc error; no add. Confirm if you want any change. |
| 3 | **Firecrawl default** | Document example shows `"disabled": true` for Firecrawl; your mcp.json has `"disabled": false`. Assumed your choice (enabled) is intentional. |
| 4 | **MemoryStack package** | Document describes MemoryStack but does not give exact npm package or install command. Need to look up “MemoryStack MCP” to add safely. |

### 5.2 Questions for You (please answer before we apply changes)

1. **Renames:** Do you want to apply any of the optional renames (`knowledge-graph-memory` → `series-memory`, `vectara` → `semantic-search-memory`, `walk-this-way-files` → `manuscripts`, `duckduckgo-search` → `web-search`), or keep all current names?
2. **Brave Search:** Confirm you want Brave Search MCP added. Should I look up the official/canonical npm package name and add it?
3. **MemoryStack:** Do you want MemoryStack added? If yes, should I search for the correct package and propose a config block?
4. **MemTool / RAGVUE / PiloTY / LLM MapReduce:** Which of these do you want added? (MemTool = context optimization; RAGVUE = RAG debugging; PiloTY = terminal/infra; LLM MapReduce = meta-orchestrator.)
5. **Puppeteer and Docker:** Add both as **disabled** by default for future use, or skip them?
6. **Sequential Thinking Rust:** Add only if you have Rust/cargo and want this variant? (Yes/No.)
7. **“Please add” long list (PostgreSQL, SQLite, Airtable, etc.):** Should I (a) ignore for now, (b) research and add only the ones that clearly support fiction writing (e.g. Slack, Jupyter, Multi-Agent Debate), or (c) research all and come back with a short “recommended” subset?
8. **Enhanced Sequential Thinking:** Keep current npx config, or do you want to switch to the Python `mcp_thinking` version from the document (after we confirm the package exists)?

---

## Part 6 — What Has Not Been Done Yet

- **No changes** have been made to `.cursor/config/mcp.json`.
- **No renames** have been applied.
- **No new MCPs** have been added.
- **No updates** have been made to `COMPASS_MCP_MANIFEST.md` or `MCP_COMPLETE_ACTIVE_LIST.md`.

Once you answer the questions in Part 5, the next step is to apply only the adds and renames you approve and then update the two manifest/list docs accordingly.

---

*Summary produced by systematic review of the Fiction Writing MCP System For Cursor Refresh document. Sequential Thinking used to extract: document purpose, full MCP list, naming rules, explicit “add” requests, and conflicts/uncertainties.*
