# COMPASS MCP Manifest
## MCPs That Support COMPASS (Core + Premium)
**Date:** January 26, 2026  
**Status:** 📋 DRAFT — Review and decide  
**Purpose:** Portable list of MCPs that COMPASS requires or recommends. Use when setting up a new COMPASS project or when splitting COMPASS from a novel project.

---

## WHY THIS DOCUMENT

- **COMPASS-first:** MCPs are chosen to support COMPASS capabilities, not the other way around.
- **Portable:** When COMPASS is extracted to its own folder, this manifest travels with it.
- **Onboarding:** A new project using COMPASS knows which MCPs to enable (Core vs optional Premium).
- **Evaluation anchor:** When evaluating new research, compare against the MCPs listed here for each capability.

**Source of truth for full mapping:** `COMPASS_PREMIUM_ROADMAP.md` Part 2.

---

## COMPASS CORE — Required for COMPASS to function

| MCP | Purpose | Notes |
|-----|---------|-------|
| **walk-this-way-files** (or project filesystem) | File access — read Story Bible, chapters, blueprints | Foundation; keep enabled for most tasks |
| **compass-writing-guides** | Writing craft guidance, style rules | COMPASS-native; core to the system |
| **github** | Version control, repo management | Needs `GITHUB_TOKEN` |
| **gitkraken** | Enhanced Git with AI | Optional but recommended |
| **sequential-thinking** (base) | Basic step-by-step reasoning | Core analysis |

**Note:** "walk-this-way-files" is project-specific naming; a future project would use its own filesystem MCP config. The *role* (file access) is what COMPASS requires.

---

## COMPASS PREMIUM — By capability

*All Premium MCPs are optional relative to Core. Enable per project need and API availability.*

### DNA Memory System (Premium Feature 1)
| MCP | Role | Status |
|-----|------|--------|
| Knowledge Graph Memory | Official Anthropic memory | ✅ Active |
| MemoryGraph | Ultra-efficient context | ✅ Active |
| Enhanced MCP Memory | Style/workflow learning | ✅ Active |
| Supermemory | Cross-platform continuity | ✅ Active |
| Cognee Connections | Hidden connections | ✅ Active |
| UltraRAG | Adaptive RAG | ✅ Active |
| RAGentA | Multi-agent RAG | ✅ Active |

### Research System (Premium Feature 9)
| MCP | Role | Status |
|-----|------|--------|
| Firecrawl | PRIMARY deep research | ⚠️ Needs API |
| DuckDuckGo Search | Quick reference lookups | ✅ Active |
| Vectara | Semantic search | ⚠️ Needs API |

### Style System (Premium Feature 8)
| MCP | Role | Status |
|-----|------|--------|
| Style Emulation | Mathematical style analysis | ✅ Active |
| Dennis Lehane Style | Lehane-specific guidance | ✅ Active |
| Fiction Reverse Engineering | Bestseller formula extraction | ✅ Active |

### Multi-Model Orchestration (Premium Feature 6)
| MCP | Role | Status |
|-----|------|--------|
| ZEN Orchestrator | Route to optimal AI models | ✅ Installed; needs API keys |

### Agent Choreography / Advanced Reasoning (Premium Feature 3)
| MCP | Role | Status |
|-----|------|--------|
| Sequential Thinking MAS | Multi-agent reasoning | ✅ Active |
| Sequential Thinking Ultra | Bias detection, quality | ✅ Active |
| Enhanced Sequential Thinking | Advanced reasoning | ✅ Active |

### Workflow Automation (Premium Feature 10)
| MCP | Role | Status |
|-----|------|--------|
| Cursor Workflow Orchestrator | MCP management | ✅ Active |
| Toolbox | Tool container | ✅ Active |
| n8n | Low-code automation | ⚠️ Needs API / setup |

### Supporting Tools
| MCP | Role | Status |
|-----|------|--------|
| Pandoc | Document conversion | ✅ Active |
| Anki Flashcards | Spaced repetition | ✅ Active |
| AI Writers Workshop | Narrative/storytelling | ✅ Active |
| ScaleMCP | Dynamic tool selection | ✅ Active |

---

## PROJECT-SPECIFIC VS COMPASS-SYSTEM

| Type | Examples | Travels with COMPASS? |
|------|----------|------------------------|
| **COMPASS-system** | Writing Guides, Sequential Thinking, memory/style/research MCPs above | ✅ Yes — this manifest |
| **Project-specific** | WalkThisWay_Character_MCP (data from *this* novel's Story Bible), project-named filesystem | ❌ No — stays with the novel project |
| **Generic** | GitHub, GitKraken, Pandoc, DuckDuckGo | ✅ Yes — part of COMPASS Core/Supporting |

When you split: COMPASS folder gets this manifest + Core/Premium MCP *list*. Each novel project keeps its own Character MCP (if any), filesystem config, and blueprint/style docs.

---

## HOW TO USE THIS MANIFEST

1. **New COMPASS project:** Enable Core MCPs first; add Premium MCPs by capability as needed.
2. **Evaluating new research:** For each candidate, ask "Which COMPASS capability does this serve?" Then compare to the MCPs in that row above — augment, replace, or reject.
3. **Splitting COMPASS from Walk This Way:** Move COMPASS (including this manifest); leave Walk This Way–specific MCPs and data in the novel project; point configs at the right places.

---

*Draft for review. After you approve, we can fold this into `zz_COMPASS/` or keep at project root until the split — your call.*
