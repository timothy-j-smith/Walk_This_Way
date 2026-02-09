# Additional MCPs for Consideration — Categorized & Evaluated for Creative Writing

**Purpose:** Neat, ordered list of the MCPs you submitted; grouped by category with short descriptions, creative-writing applicability, overlap with your existing arsenal, and a final evaluation for the Creative Writing ecosystem.  
**Your existing arsenal:** See `COMPASS_MCP_MANIFEST.md` and `.cursor/config/mcp.json` (Knowledge Graph Memory, Vectara, Firecrawl, DuckDuckGo, Style Emulation, Dennis Lehane, Fiction Reverse Engineering, Sequential Thinking variants, COMPASS Writing Guides, GitKraken, GitHub, etc.).

---

## Category 1 — Books, Libraries & Reference (Existing Novels / Comp Titles)

### 1. Open Library MCP
**General:** Connects to Internet Archive’s Open Library database. It supports search by title, author, and ISBN; returns detailed author information and photos; retrieves book covers and metadata; and can surface publication history, edition counts, and links to preview or borrowing options. The database is very large (millions of books), metadata is rich, and access is free with no account required.  
**Creative writing:** Useful for comp title research, author bios, and checking publication dates and editions when setting a novel in a period. Book covers and author photos can support marketing or reference. No overlap with your current book-metadata MCPs; Firecrawl and DuckDuckGo are for web research, not structured book data.  
**Overlap in arsenal:** None. This adds a dedicated book/author reference layer.

### 2. Google Books MCP
**General:** Provides programmatic access to Google Books: search books, retrieve metadata, and get author information. It is a second major source of book and author data alongside Open Library.  
**Creative writing:** Same kinds of use as Open Library—comp titles, author research, “books like X,” and market positioning. Having both Open Library and Google Books gives redundancy and broader coverage.  
**Overlap in arsenal:** None for book-specific data. Vectara is semantic search over *your* docs; this is external book catalog data.

### 3. GetGather MCP
**General:** “Free your data” style MCP that can integrate personal data sources; the legacy Goodreads-only server is deprecated in favor of this main GetGather project. It can surface reading history, recommendations, and book-club style context.  
**Creative writing:** Lets the AI use your actual reading list and tastes as context for comps and voice. Useful for keeping recommendations aligned with what you read and for series/sequel planning.  
**Overlap in arsenal:** None. Knowledge Graph Memory stores story-world facts; GetGather would represent your real-world reading data.

### 4. Ebook MCP Service
**General:** Semantic search over your *local* EPUB collection using vector search (e.g., ChromaDB). You can search by content, author, themes; list books by author; and get database statistics. It turns a personal EPUB library into a queryable knowledge base.  
**Creative writing:** Lets you search your own fiction and reference library by meaning (“passages about loss of innocence,” “books set in Boston”) for theme and comp research. Fits alongside Open Library/Google Books, which are external catalogs; this is your private corpus.  
**Overlap in arsenal:** Conceptually similar to Vectara/UltraRAG over manuscripts, but scoped to EPUBs and reading library, not your draft—complementary.

### 5. Goodreads Scraper MCP
**General:** Extracts data from Goodreads: book ratings, reviews, genres, reader sentiment, recommendation data, and publication information. Typically runs via Apify or similar; provides real reader feedback and trending data.  
**Creative writing:** Supports comp research with audience sentiment, genre tags, and “readers also liked” style signals. Helps with positioning and back-cover/marketing language.  
**Overlap in arsenal:** None. GetGather is about *your* Goodreads list; this is about public Goodreads data (reviews, trends).

---

## Category 2 — Writing, Editing & Prose (Grammar, Style, Plagiarism)

### 6. Grammarly AI MCP
**General:** Exposes Grammarly’s grammar, style, and clarity checks via API so an AI can request suggestions or scores. Often requires a paid or enterprise plan for full API access.  
**Creative writing:** Adds automated grammar and clarity checks in the pipeline; can complement your Style Emulation and PROSE_DNA passes. Best used for polish rather than voice.  
**Overlap in arsenal:** Style Emulation MCP and Dennis Lehane MCP handle voice and style; Grammarly would add explicit grammar/clarity. Professional Editor MCP may already cover some of this—worth checking scope.

### 7. Word Tune MCP
**General:** Wordtune (by AI21) offers rewriting and tone adjustment. An MCP would allow the assistant to suggest alternative phrasings and tones programmatically.  
**Creative writing:** Useful for quick rephrasing and tone tweaks (e.g., more formal vs. more casual) while keeping meaning. Can support dialogue and narration polish.  
**Overlap in arsenal:** Overlaps with Style Emulation (rewrite in style) and possibly Creative Collaborator workflows; Word Tune is typically lighter-touch and tone-focused.

### 8. Winston AI MCP
**General:** Winston AI is aimed at AI-generated content detection and writing quality. An MCP would allow checks for “AI slop” or readability/quality metrics.  
**Creative writing:** Helps keep prose feeling human and publishable; can be used as a final check before submission. Complements style and grammar tools.  
**Overlap in arsenal:** No direct overlap; you don’t have an AI-detection or readability-metric MCP. Could sit alongside Style Emulation and Professional Editor.

### 9. CopyScape MCP
**General:** CopyScape focuses on plagiarism detection. An MCP would let the assistant run similarity checks against the web or other texts.  
**Creative writing:** Protects against accidental overlap with published material and helps with clearance of quotes or pastiche. Valuable before submission or publication.  
**Overlap in arsenal:** None. Your stack doesn’t include plagiarism checking.

---

## Category 3 — Research, Context & Documentation

### 10. Perplexity AI MCP
**General:** Connects to Perplexity’s AI-powered search and synthesis so the assistant can run research queries and get cited, summarized answers. Often pay-per-use or subscription.  
**Creative writing:** Good for fast, cited research (period detail, facts, “how did X work in 1975”) to keep fiction accurate. Complements Firecrawl (deep) and DuckDuckGo (quick).  
**Overlap in arsenal:** Firecrawl is primary deep research; DuckDuckGo is quick lookup. Perplexity sits in between—synthesized, cited answers. Adds value without fully replacing either.

### 11. AI Context MCP
**General:** Typically provides expanded or optimized context (e.g., retrieval, summarization, or prioritization of information) so the model gets the right background. Exact behavior depends on the specific package.  
**Creative writing:** Could improve how much of your Story Bible, timeline, or style guide is used in each request. Helps keep character and world details in context during long sessions.  
**Overlap in arsenal:** MemoryGraph and Enhanced MCP Memory already optimize context; AI Context MCP would need to be compared on features (e.g., retrieval vs. summarization) to avoid redundancy.

### 12. Saner.AI MCP
**General:** Saner.AI (or similar) often focuses on structured reasoning, fact-checking, or consistency. The exact feature set depends on the implementation.  
**Creative writing:** Could support plot and timeline consistency and fact-checking of period or technical details. Fits with Sequential Thinking for logic and Firecrawl/Perplexity for facts.  
**Overlap in arsenal:** Sequential Thinking (and variants) handle reasoning; Saner would need a clear differentiator (e.g., fact-check-only, or integration with external KBs).

### 13. Vellum MCP
**General:** Vellum is a publishing/ebook tool; an MCP would likely expose formatting, export, or project-management features so the assistant can help with structure or output.  
**Creative writing:** Could help with manuscript formatting, chapter structure, or export for submission. Complements Pandoc (conversion) and your blueprint/docs.  
**Overlap in arsenal:** Pandoc handles format conversion; Vellum MCP would add publishing-workflow and possibly structure. Low overlap if focused on Vellum’s specific features.

### 14. Context7 MCP
**General:** Provides up-to-date documentation for libraries and frameworks so the model can reference current APIs, syntax, and best practices.  
**Creative writing:** Useful if your fiction includes technical or professional detail (e.g., coding, medicine, law) and you want those references to be accurate. Keeps “technical writing inside the story” correct.  
**Overlap in arsenal:** COMPASS Writing Guides and Story Bible are about your world and craft; Context7 is about external technical docs. Niche but no overlap.

---

## Category 4 — Memory, Data & Character/Plot Systems

### 15. Vectara MCP
**General:** Semantic search and RAG over your documents; supports meaning-based queries and retrieval-augmented generation. You already have it in the manifest; it needs API keys to be active.  
**Creative writing:** Enables queries like “scenes where Nick feels betrayed by class” or “passages about loss of innocence” across your manuscript and notes. Core for theme and continuity.  
**Overlap in arsenal:** You already list Vectara in COMPASS (Premium Research). UltraRAG and RAGentA add domain adaptation and attributed QA; Vectara is the base semantic-search layer.

### 16. scanadi/mcp-ai-memory MCP
**General:** PostgreSQL + pgvector memory with semantic search, caching, graph-style relationships, and memory aging (decay/archival). Research-grade, with strong memory-lifecycle behavior.  
**Creative writing:** Could maintain long-term character/plot/world facts and age out old draft decisions. Good for multi-book series and long-running continuity.  
**Overlap in arsenal:** Knowledge Graph Memory and MemoryGraph already cover persistent memory and efficiency; scanadi adds PostgreSQL and explicit aging. You previously archived it as redundant; only reconsider if you need SQL or fine-grained aging.

### 17. Book Series MCP
**General:** Suite of servers for writing project management: character management (development, relationships), plot tracking (arcs, timelines), world-building (locations, rules, history), research and continuity, and writing production. Purpose-built for series writers; typically requires PostgreSQL.  
**Creative writing:** Reduces plot holes and keeps character and world consistent across many books. Aligns with COMPASS goals but implemented as dedicated tools.  
**Overlap in arsenal:** Your Knowledge Graph Memory, Story Bible, COMPASS Writing Guides, and AI Writers Workshop already cover character, plot, and continuity. Book Series MCP would duplicate much of that; add only if you want a single, DB-backed suite and are willing to migrate workflows.

### 18. Writer MCP
**General:** Character knowledge and relationship manager with rich descriptions, knowledge facts with semantic search, and relationship tracking. Lighter than Book Series; often uses PostgreSQL and OpenAI for embeddings.  
**Creative writing:** Keeps character facts and relationships queryable and consistent. Good for single novels or smaller series.  
**Overlap in arsenal:** Overlaps with Knowledge Graph Memory (character/relations) and Character Bible + COMPASS. Add only if you want a dedicated character DB and semantic search on characters specifically.

---

## Category 5 — Auth, Infrastructure & Back End

### 19. Supabase MCP
**General:** Supabase (Postgres + auth + storage + APIs) exposed via MCP for database operations, auth, and file storage. Geared toward app back ends.  
**Creative writing:** Only relevant if you build custom apps (e.g., reader-facing tools, submission trackers) or need a shared DB for multiple tools. Not needed for manuscript-only workflows.  
**Overlap in arsenal:** You don’t use Supabase today. Knowledge Graph Memory and filesystem cover story data; Supabase would be for custom apps, not core COMPASS.

### 20. Clerk MCP
**General:** Clerk provides authentication (sign-up, login, sessions). An MCP would let the assistant interact with user and session data for apps.  
**Creative writing:** Only relevant if you add a web app or dashboard that requires login (e.g., for beta readers or co-authors). Not needed for solo fiction writing.  
**Overlap in arsenal:** None. Your workflow doesn’t depend on Clerk.

### 21. GIT MCP
**General:** Standard Git operations (status, diff, commit, branch, log) exposed to the assistant. Lighter and more generic than GitKraken.  
**Creative writing:** Useful for versioning drafts, branching by act or draft, and keeping a clear history of changes.  
**Overlap in arsenal:** You use GitKraken MCP (and GitHub MCP). GitKraken adds AI and GUI-oriented features; a plain GIT MCP would be redundant unless you want a minimal, CLI-style fallback.

---

## Category 6 — Speech, Code Execution & Meta

### 22. AssemblyAI MCP
**General:** AssemblyAI provides speech-to-text (transcription). An MCP would allow the assistant to process audio (e.g., dictation, interviews) into text.  
**Creative writing:** Enables dictation workflows and transcription of research interviews or voice notes. Helpful if you draft by voice or capture ideas verbally.  
**Overlap in arsenal:** None. You have no other transcription MCP; add if voice input or interview transcription matters.

### 23. YepCode MCP
**General:** Executes LLM-generated code in a sandbox; a “meta” MCP that lets the model run code it suggests.  
**Creative writing:** Could run one-off scripts (e.g., word counts, simple consistency checks, file renames). Useful for power users who want automation from natural language.  
**Overlap in arsenal:** Cursor and Toolbox already run code; YepCode is specifically “model suggests code, then runs it.” Overlaps with terminal and Toolbox; add only if you want that pattern formalized.

---

## Numbered Summary (All MCPs in One List)

1. **Open Library MCP** — Books & reference  
2. **Google Books MCP** — Books & reference  
3. **GetGather MCP** — Books & reference (your reading data)  
4. **Ebook MCP Service** — Books & reference (local EPUB search)  
5. **Goodreads Scraper MCP** — Books & reference (Goodreads public data)  
6. **Grammarly AI MCP** — Writing & editing  
7. **Word Tune MCP** — Writing & editing  
8. **Winston AI MCP** — Writing & editing  
9. **CopyScape MCP** — Writing & editing (plagiarism)  
10. **Perplexity AI MCP** — Research & context  
11. **AI Context MCP** — Research & context  
12. **Saner.AI MCP** — Research & context  
13. **Vellum MCP** — Research & context (publishing)  
14. **Context7 MCP** — Research & context (technical docs)  
15. **Vectara MCP** — Memory & data (already in arsenal; needs API)  
16. **scanadi/mcp-ai-memory MCP** — Memory & data  
17. **Book Series MCP** — Memory & data (character/plot/world suite)  
18. **Writer MCP** — Memory & data (character/relationships)  
19. **Supabase MCP** — Auth & infrastructure  
20. **Clerk MCP** — Auth & infrastructure  
21. **GIT MCP** — Auth & infrastructure (version control)  
22. **AssemblyAI MCP** — Speech & code  
23. **YepCode MCP** — Code execution & meta  

---

## Evaluation for the Creative Writing Ecosystem

**\<thinking\>**  
For a creative writing ecosystem like COMPASS and Walk This Way, the highest-impact additions are: **Open Library MCP** and **Google Books MCP** (comp titles and author reference with no current overlap); **Perplexity AI MCP** (cited research between Firecrawl and DuckDuckGo); **Ebook MCP Service** (semantic search over your own reading library); and, if you care about plagiarism and polish, **CopyScape MCP** and **Grammarly AI MCP** (or Winston AI). **Book Series MCP** and **Writer MCP** duplicate character/plot/memory functions you already have in Knowledge Graph Memory, Story Bible, and AI Writers Workshop unless you explicitly want a separate DB-backed suite. **Vectara** is already in your manifest—ensure it’s enabled with API keys. **GIT MCP**, **Supabase**, **Clerk**, **scanadi/mcp-ai-memory**, **AI Context**, **Saner.AI**, **Context7**, and **YepCode** are optional or redundant unless you have a specific need (e.g., dictation → AssemblyAI; app back end → Supabase/Clerk).  
**\</thinking\>**

**In short:** Prioritize **book/reference MCPs** (Open Library, Google Books, optionally GetGather and Ebook MCP) and **research/perception** (Perplexity); then **writing quality and safety** (Grammarly or Winston, CopyScape). Treat **Book Series** and **Writer** MCPs as optional only if you want a dedicated character/plot DB alongside COMPASS; otherwise your current memory and story-bible setup already covers that role.
