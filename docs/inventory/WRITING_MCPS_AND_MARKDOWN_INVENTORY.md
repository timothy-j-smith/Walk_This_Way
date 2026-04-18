# Writing MCPs, markdown locations, and writing advice

This document implements the portable inventory for fiction and novel workflows. Sources are `.cursor/config/mcp.json` and `COMPASS_MCP_MANIFEST.md`.

---

## Markdown paths versus a `/md` directory

1. This repository does **not** use a dedicated `/md` or `md/` documentation root. Markdown files use the `.md` extension throughout the tree.

2. If you meant “all markdown files” rather than a folder literally named `md`, use the tracked path lists in this directory (see below) or run `git ls-files '*.md'` from the repository root.

---

## Tracked markdown file lists (machine export)

Regenerate after large doc moves:

```bash
git ls-files '*.md' > docs/inventory/git-tracked-md-files.txt
git ls-files 'zz_COMPASS/**/*.md' > docs/inventory/git-tracked-md-files-zz_COMPASS.txt
```

---

## Single flat index (MCPs, then advice locations, then markdown notes)

Each entry is one line. **Disabled** means `"disabled": true` in `.cursor/config/mcp.json` at the time this file was written.

### Model Context Protocol servers (fiction and novel workflow)

1. **walk-this-way-files** — Filesystem MCP for the novel project tree.

2. **tim-cursor-experiment-files** — Filesystem MCP for a second workspace root.

3. **compass-writing-guides** — COMPASS Writing Guides MCP (`zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/`).

4. **walkthisway-characters** — Character data MCP (`zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/`).

5. **dennis-lehane-style** — Lehane-focused style MCP (`zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/`).

6. **style-emulation** — External style emulation server (`style_emulation.server`).

7. **fiction-reverse-engineering** — Structure and pattern MCP (`zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP/`).

8. **professional-editor** — Editor-style feedback MCP (`zz_COMPASS/MCP_Implementations/PROFESSIONAL_EDITOR_MCP/`).

9. **compass-intelligence** — COMPASS intelligence MCP (`zz_COMPASS/MCP_Implementations/COMPASS_INTELLIGENCE_MCP/`).

10. **pandoc** — Markdown and document conversion (`mcp-pandoc`). **Disabled.**

11. **ebook** — EPUB-oriented MCP (`ebook_mcp`). **Disabled.**

12. **open-library** — Book metadata (`@8enSmith/mcp-open-library`). **Disabled.**

13. **firecrawl** — Deep research and page extraction.

14. **duckduckgo-search** — Quick web search.

15. **fetch** — Generic HTTP fetch (`@mcpflow.io/mcp-fetch`).

16. **knowledge-graph-memory** — Persistent memory graph (`@modelcontextprotocol/server-memory`).

17. **perplexity** — Search via Perplexity API. **Disabled.**

18. **brave-search** — Brave Search API. **Disabled.**

19. **exa** — Exa search. **Disabled.**

20. **goodreads-scraper** — Apify-backed tooling. **Disabled.**

21. **vectara** — Semantic search over a corpus. **Disabled.**

22. **enhanced-mcp-memory** — Enhanced memory server. **Disabled.**

23. **supermemory** — Cross-session memory. **Disabled.**

24. **cognee-connections** — Connection and graph-style retrieval. **Disabled.**

25. **anki-flashcards** — Spaced repetition integration. **Disabled.**

26. **sequential-thinking** — Base sequential reasoning MCP.

27. **sequential-thinking-ultra** — Extended sequential reasoning with quality and budget flags.

28. **sequential-thinking-mas** — Multi-agent style sequential reasoning (uses `ANTHROPIC_API_KEY`).

29. **sequential-thinking-enhanced** — Enhanced sequential thinking server.

30. **sequential-thinking-rust** — Rust sequential thinking server binary.

31. **zen-orchestrator** — Multi-model routing. **Disabled.**

32. **cursor-workflow-orchestrator** — Workflow and MCP orchestration for Cursor. **Disabled.**

33. **github** — GitHub API MCP for issues and repository operations.

34. **gitkraken** — GitKraken MCP for Git operations.

35. **Manifest-only MCPs** — `COMPASS_MCP_MANIFEST.md` names additional premium tools (for example AI Writers Workshop, ScaleMCP, MemoryGraph, UltraRAG, RAGentA) that are **not** defined in this repository’s `mcp.json`. Treat them as roadmap entries until configured.

### Writing advice and high-signal markdown or JSON locations

36. **zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/data/writing_guides.json** — Curated craft content and quotes backing the Writing Guides MCP.

37. **zz_COMPASS/Commands/** — Per-topic command files (dialogue, voice, pacing, and related craft).

38. **zz_COMPASS/Core/ADVANCED_CURSOR_NOVEL_WRITING_TOOLS.md** — Cursor-first novel workflow and tooling narrative.

39. **zz_COMPASS/Core/WRITING_DNA_MEMORY_SYSTEM.md** — DNA, continuity, and session preparation for long-form fiction.

40. **zz_COMPASS/Core/Universal-Fiction-Templates.md** — Reusable structural templates.

41. **zz_COMPASS/Agents/Core_5/** — Specialist agent markdown (for example Strategic Writing Coordinator, Prose Polish Expert, Character Depth Coach).

42. **zz_COMPASS/Agents/Master/Agent.json** — Master orchestration JSON with embedded system prompts and workflow text.

43. **Active_Draft_2/DRAFT_2_STYLE_GUIDE.md** — Draft 2 style rules for this novel.

44. **Story_Bible/author-style-library.md** — Author-style reference for consistency.

45. **Novel_Docs/** — Guides and critique workflows (files whose names include `GUIDE` or `CRITIQUE` are the primary operational docs in that family).

46. **COMPASS_MCP_MANIFEST.md** — Which MCPs the COMPASS system expects for core and premium capabilities.

47. **zz_COMPASS/MCP_INTEGRATION.md** — How MCPs connect to COMPASS workflows and onboarding steps.

### Markdown inventory notes

48. **Repository-wide tracked markdown** — See `docs/inventory/git-tracked-md-files.txt` (full list; line count matches `wc -l` at generation time).

49. **COMPASS subtree tracked markdown** — See `docs/inventory/git-tracked-md-files-zz_COMPASS.txt` for files under `zz_COMPASS/` only.

---

## Optional diagram (writing stack versus files)

```mermaid
flowchart LR
  subgraph mcpLayer [MCP layer]
    wguides[compassWritingGuides]
    chars[walkthiswayCharacters]
    style[styleEmulation]
    lehane[dennisLehaneStyle]
    fre[fictionReverseEngineering]
    editor[professionalEditor]
    intel[compassIntelligence]
  end
  subgraph files [Markdown and JSON]
    commands[zz_COMPASS/Commands]
    core[zz_COMPASS/Core]
    wgJson[writing_guides.json]
    novelDocs[Novel_Docs and Story_Bible]
  end
  wguides --> wgJson
  wguides --> core
  chars --> novelDocs
  style --> novelDocs
  editor --> novelDocs
  commands --> core
```

---

## Related configuration paths

- **Cursor MCP config:** `.cursor/config/mcp.json`
- **COMPASS MCP manifest:** `COMPASS_MCP_MANIFEST.md`
- **COMPASS MCP integration guide:** `zz_COMPASS/MCP_INTEGRATION.md`
