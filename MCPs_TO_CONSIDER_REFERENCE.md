# MCPs You Have Not Considered (or Should Re-Consider) — Reference

**Purpose:** One place for every MCP your codebase says to "consider," "research," or "evaluate" so you don’t lose them.  
**Where the chat lives:** Your discussion is captured in **Session Summaries** and **evaluation docs** below; the original chat may be in exported HANK/Other chats.

---

## Where Your "MCPs to Consider" Chat Is Documented

You said you recall a chat on MCPs to consider but can’t find it. Here’s where that work shows up in the codebase:

| Source | What it contains |
|--------|-------------------|
| **Session_Summaries/2026-01-17_2230_PST_MCP_Setup_And_Dennis_Lehane_MCP_Foundation.md** | Session where you said *"I have some additional MCPs that I have researched"* → led to comprehensive MCP evaluation (30+ MCPs), Tier 1/2/3, Add Immediately / Add Soon / **Research** / Skip. |
| **MCP_COMPREHENSIVE_EVALUATION.md** | Full evaluation (if present in project): Tier 1 (add now), Tier 2 (add soon), **Tier 3 (Research): AI Context MCP, Saner.AI MCP, Vellum MCP**. |
| **REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md** | Long doc with your and Claude’s decisions: what to keep, what to "archive shelf," and explicit "consider" / API items (Grammarly, Perplexity, etc.). |
| **MCP_UNINSTALLED_SUMMARY.md** | Sequential Thinking analysis of 91 uninstalled MCPs + **"RECOMMENDED ADDITIONAL MCPs TO CONSIDER"** at the end (Perplexity, Grammarly, AssemblyAI). |
| **.cursor/docs/Chat_History/** | Exported chats (HANK/, Other/). The **conversation** where you discussed "MCPs I have researched" is likely in a HANK chat from **Jan 17–20, 2026** or in the run-up to creating the Revolutionary Fiction Writing MCP doc. See **HANK/CHAT_ARCHIVE_INDEX.md** for HANK chat list. |

So: the **decisions and lists** are in the Session Summary and the markdown docs above; the **exact chat** is in the Chat_History exports (HANK or Other) from that timeframe.

---

## Book / Novel / Library–Related MCPs (You Asked About This)

You remembered something like a **"book" MCP**, **"novel" MCP**, or **book library** reference. Here’s what’s in your codebase:

| MCP | What it is | Where it’s discussed | Decision |
|-----|------------|----------------------|----------|
| **Novel Memory MCP (Custom)** | A *novel-specific* memory system (characters, plot, world-building per novel). | **REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md** (archive-shelf list); **MCP_UNINSTALLED_SUMMARY.md**; **MCP_UNINSTALLED_SEQUENTIAL_ANALYSIS.md** | **Archived.** Decided redundant with **Knowledge Graph Memory MCP**, which already handles novel-specific memory with better structure and querying. So the chat where you considered “Novel Memory” is the same one that produced the big archive-shelf list in the Revolutionary doc. |
| **Obsidian MCP** | Personal knowledge base / note library (wiki-style notes, links). | Same docs (archive list) | **Archived.** Redundant with Filesystem MCP + Knowledge Graph Memory for your writing system. |
| **Notion MCP** | Workspace/data and docs (could be used as a “library” of planning docs). | Same docs (archive list) | **Archived.** COMPASS Writing Guides + Filesystem provide writing-specific knowledge; Notion adds complexity without clear benefit for fiction. |
| **Anytype MCP** | Collaborative wiki. | REVOLUTIONARY doc (Hidden/Secret MCPs + archive list) | **Archived.** Redundant with Knowledge Graph Memory + Filesystem. |

**No separate "Book MCP" or "book library" MCP** appears in your project or in the Fiction Writing MCP Refresh doc. The closest match is **Novel Memory MCP** (custom, novel-specific memory), which you discussed and then shelved.

**Where to find the chat:** The conversation where you decided to archive **Novel Memory MCP** (and the other “library”-like ones like Obsidian, Notion, Anytype) is reflected in **REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md** and **MCP_UNINSTALLED_SUMMARY.md**. The actual chat is likely in **.cursor/docs/Chat_History/HANK/** (e.g. **2026-01-19** or **2026-01-20** — Walk This Way + COMPASS with HANK) or in the long session that produced the Revolutionary doc. Search those chat files for: **"Novel Memory"**, **"archive shelf"**, **"Knowledge Graph"**, or **"redundant"** to jump to the right place.

---

## Goodreads / Existing Novels / Book Data — Best MCPs for Fiction Writers

You asked about **Goodreads** or MCPs that **reference or connect to existing novels** for fiction writing. Here are the ones that exist and are relevant:

| MCP | What it does | Fiction-writing use | Status / Install |
|-----|----------------|----------------------|------------------|
| **Open Library MCP** (`@8enSmith/mcp-open-library`) | Search books by title; get book details by ID (ISBN, etc.); search authors by name; get author details; book covers & author photos (URLs). Uses Internet Archive Open Library API. | Comp titles, author research, "books like X," period/category checks, cover reference. | **Active.** Install via Smithery or npm; no account. Works with Cursor. |
| **Google Books MCP** (`juanbeniteza/mcp-google-books`) | Book search, metadata, author info via Google Books API. | Same — comp titles, author corpus context, market/positioning. | **Active.** Python; check repo for Cursor/MCP setup. |
| **GetGather MCP** (main: `mcp-getgather/mcp-getgather`) | "Free your data" — can include Goodreads-style data (reading history, recommendations). | Your reading list / Goodreads library as context (tastes, comps). | **Active.** Old Goodreads-only server deprecated; use main GetGather MCP. |
| **Goodreads (legacy)** (`mcp-getgather-goodreads`) | Used to pull your Goodreads library (get_books) with credentials. | Personal book list as context. | **Archived/deprecated.** Use GetGather MCP instead. |

**Recommendation for fiction:** **Open Library MCP** is the most straightforward for existing novels (search title/author, metadata, covers, no account). Add **Google Books MCP** for a second source. If you want your **Goodreads/reading list** in the loop, use **GetGather MCP** (main repo). None of these appear in your codebase yet — they are net-new options.

---

## MCPs Explicitly Marked "Consider" or "Research" in Your Codebase

### 1. Tier 3 (Research) — from Session Summary Jan 17, 2026

- **AI Context MCP** — Research
- **Saner.AI MCP** — Research  
- **Vellum MCP** — Research  

*Source: Session_Summaries/2026-01-17_2230_PST_MCP_Setup_And_Dennis_Lehane_MCP_Foundation.md*

---

### 2. Recommended Additional MCPs to Consider — from MCP_UNINSTALLED_SUMMARY.md

After evaluating 91 uninstalled MCPs, the doc recommends considering:

1. **Perplexity AI MCP** — Complement Firecrawl for research (AI-powered search and synthesis).
2. **Grammarly API MCP** — Complement Style Emulation MCP for grammar checking.
3. **AssemblyAI MCP** — Optional; useful if you want dictation (was excluded as non-priority but "might be valuable").

*Source: MCP_UNINSTALLED_SUMMARY.md (bottom section)*

---

### 3. "Consider" / API items in REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md

- **Grammarly API** — Consider for grammar checking (cost may require enterprise).
- **Perplexity AI API** — Consider for research (pay-per-use).

*Source: REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md (around lines 1032, 1040)*

---

### 4. Alternative MCPs to Consider — from MCP_POWERHOUSE_INTEGRATION_ANALYSIS.md

- **Story Structure MCP** — If it exists (narrative structure).
- **Character Consistency MCP** — You have custom; doc says "if exists."
- **Prose Analysis MCP** — If it exists (prose checking).

Verdict in doc: most don’t exist yet; Sequential Thinking is more general-purpose.

*Source: MCP_POWERHOUSE_INTEGRATION_ANALYSIS.md — "Alternative MCPs to Consider"*

---

### 5. Unresolved question: .git MCP alongside GitHub and GitKraken

You asked: *"Should we add the '.git' MCP to go alongside GitHub and GitKraken MCPs? Please confirm. If YES, please add here with like MCPs and include detailed description and installation."*

- **Decision in doc:** Git MCP was later **archived** as redundant with GitKraken MCP (GitKraken provides enhanced Git + AI). So the codebase answer is "no" unless you want a second, lighter-weight Git MCP for some reason.

*Source: REVOLUTIONARY_FICTION_WRITING_MCP_SYSTEM_COMPLETE.md (GitHub section); MCP_UNINSTALLED_SUMMARY.md (Git MCP)*

---

### 6. Optional / "Research & Consider" in REVOLUTIONARY doc

- **MemoryStack MCP** — Status: Research & Consider (pattern detection, consolidate_memories).
- **scanadi/mcp-ai-memory** (PostgreSQL + pgvector, memory aging) — Research & Consider.
- **Sequential Story MCP** — May not exist or may be redundant with Sequential Thinking; "research needed."
- **Spotify MCP** — Research needed (API); moved to archive shelf (ambient writing music).
- **YepCode MCP** — "META-MCP, SHOULD WE CONSIDER THIS ONE??" (execute LLM-generated code).
- **Multi-Agent Debate MCP** — Document lists as "revolutionary for plot decisions" but MCP_UNINSTALLED_SUMMARY later excluded it (Sequential Thinking MAS covers multi-agent).

---

## Summary Table: MCPs to Consider or Research

| MCP | Where mentioned | Suggested action |
|-----|-----------------|------------------|
| **Perplexity AI MCP** | MCP_UNINSTALLED_SUMMARY, REVOLUTIONARY doc | Consider for research (complement Firecrawl). |
| **Grammarly API MCP** | MCP_UNINSTALLED_SUMMARY, REVOLUTIONARY doc | Consider for grammar (complement Style Emulation). |
| **AssemblyAI MCP** | MCP_UNINSTALLED_SUMMARY, REVOLUTIONARY doc | Consider if you want dictation. |
| **AI Context MCP** | Session 2026-01-17 (Tier 3 Research) | Research. |
| **Saner.AI MCP** | Session 2026-01-17 (Tier 3 Research) | Research. |
| **Vellum MCP** | Session 2026-01-17 (Tier 3 Research) | Research. |
| **Story Structure MCP** | MCP_POWERHOUSE_INTEGRATION_ANALYSIS | Consider if it exists. |
| **Character Consistency MCP** | MCP_POWERHOUSE_INTEGRATION_ANALYSIS | You have custom; consider if another adds value. |
| **Prose Analysis MCP** | MCP_POWERHOUSE_INTEGRATION_ANALYSIS | Consider if it exists. |
| **MemoryStack MCP** | REVOLUTIONARY doc (Research & Consider) | Research; Fiction Refresh doc says add (package TBD). |
| **scanadi/mcp-ai-memory** | REVOLUTIONARY doc (Research & Consider) | Research (PostgreSQL + memory aging). |
| **Sequential Story MCP** | REVOLUTIONARY doc | Research if it exists / overlaps Sequential Thinking. |
| **YepCode MCP** | REVOLUTIONARY doc | Explicit "should we consider?" — meta-MCP, execute LLM code. |
| **Multi-Agent Debate MCP** | REVOLUTIONARY doc (revolutionary for plot) vs UNINSTALLED (excluded) | Re-evaluate if you want debate-for-plot separate from Sequential MAS. |
| **Git / .git MCP** | REVOLUTIONARY doc (your question) | Decided redundant with GitKraken; only reconsider if you want minimal Git. |

---

## Conflict with Fiction Writing MCP Refresh Doc

Your **FICTION WRITING MCP SYSTEM FOR CURSOR REFRESH** (Desktop) asks to **add Brave Search**. Your **MCP_UNINSTALLED_SUMMARY** and **REVOLUTIONARY** doc **archived Brave Search** as redundant with DuckDuckGo + Firecrawl. So:

- **Refresh doc:** Add Brave Search.
- **Current codebase decision:** Don’t add (redundant).

If you want to align with the Refresh, you can add Brave Search and leave DuckDuckGo enabled; both are quick-reference search. If you prefer to avoid redundancy, keep the current "no Brave" decision.

---

## How to Find the Exact Chat

1. **HANK chats:** `.cursor/docs/Chat_History/HANK/` — check **2026-01-19** and **2026-01-20** (Walk This Way + COMPASS, Super Agent HANK). See **CHAT_ARCHIVE_INDEX.md** for filenames.
2. **Session Summary:** **Session_Summaries/2026-01-17_2230_PST_MCP_Setup_And_Dennis_Lehane_MCP_Foundation.md** — summarizes the session where "additional MCPs I have researched" led to the comprehensive evaluation.
3. **Search:** In Cursor, search under `.cursor/docs/Chat_History` for phrases like *"additional MCPs"*, *"researched"*, *"Tier 3"*, *"Research"*, *"Saner"*, *"Vellum"*, *"Perplexity"*, *"Grammarly"* to locate the specific chat file.

---

*This file was generated from a codebase search for MCP mentions (consider, recommend, research, evaluate, archive shelf, Tier 3, alternative MCPs) so you have one reference for "MCPs I have not considered and should consider."*
