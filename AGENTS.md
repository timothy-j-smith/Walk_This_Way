# AGENTS.md

## Walk This Way — orientation for any agent opening this repo

This is a novel-in-progress, not a software application. If you are a Cursor
Cloud Agent reading this for the first time, read this file start to finish
before writing anything.

---

## What this repo is

A creative-writing workspace for the literary novel **Walk This Way** by
Timothy J. Smith, plus a set of MCP (Model Context Protocol) servers the
author built to support novelists working inside Cursor.

- **Setting:** Boston / Sudbury, Massachusetts, 1975–1979 (with a 2009 frame).
- **Protagonists:** Nick Johnson, Jackie Marsh, Patty Lally, Maxanne Sartori.
- **The novel honors the author's real childhood friend Nick (who passed from
  ALS) and reaches his real childhood friend Jackie (housebound with severe
  depression, 2026). This is the invisible DNA. If a sentence does not honor
  Nick or reach Jackie, rewrite it.**

---

## READ THESE FIRST, in order

Before editing a single sentence of the manuscript, read these four canon
documents. Everything else in the repo is informational; these are the laws.

1. **`Draft_3/DECISIONS_LOCKED.md`** — the 15 locked story decisions.
2. **`Draft_3/RESEARCH_INSIGHTS.md`** — Boston rock history, real people,
   real venues, real dates.
3. **`Draft_3/scalpel_hose_rewrites/_SUBAGENT_BRIEF.md`** — method,
   weave-ins, POV rules, prose models (King / Lehane / Dickey / Ondaatje).
4. **`Draft_3/scalpel_hose_rewrites/_DRAFT_32_ADDENDUM.md`** — latest canon
   updates. This supersedes earlier docs on all conflicts.

The Act III supplement at
`Draft_3/scalpel_hose_rewrites/_ACT3_BRIEF.md` is also authoritative for any
Act III editing.

---

## The manuscript

- **Live manuscript:** `Draft_3/Walk_This_Way_Draft_3_1_Complete.txt`
  (single file, ~85,000 words, 40 chapters).
- **Per-chapter rewrites** (source of truth for polished text):
  `Draft_3/scalpel_hose_rewrites/ch{NN}_rewrite.txt`
  (where NN may be zero-padded or letter-suffixed: `ch09A_rewrite.txt`,
  `ch11A_rewrite.txt`, etc.).
- **Prior drafts** (archived, for diff/history only):
  `Draft_3/Walk_This_Way_Draft_3_Complete.txt` and older versions.

When updating a chapter: write to the `ch{NN}_rewrite.txt` file first, then
integrate into `Walk_This_Way_Draft_3_1_Complete.txt` using the standard
chapter-range replacement pattern (see git history for examples).

---

## MCP servers (registered in `.cursor/mcp.json`)

All five MCPs are stdio servers. None require secrets or API keys. They load
automatically when a Cursor Cloud Agent spins up a fresh VM (after
`.cursor/setup.sh` runs).

| Name | Purpose |
| --- | --- |
| `walk_this_way_files` | Filesystem access to `Draft_3/` and `zz_COMPASS/`. Use this to read chapters on demand. |
| `stephen_king` | King's craft philosophy scored against a passage. 3 tools × 3 modes × 3 liberty levels. |
| `dennis_lehane` | Boston class-weight / *Mystic River* prose comparison. 4 tools, 11 categories. |
| `james_dickey` | *Deliverance* body-as-knower prose comparison. Stdlib Python only. |
| `walk_this_way_character` | Novel character database. 10 tools. Consult before introducing a new character or changing any character's details. |

If you need to invoke one of these from a subagent, reference the tool by
its MCP name. Example: ask the King MCP to run `king_revise` on a passage
with mode='Professional' for the sharpest feedback.

### Running MCPs manually (if you need to test outside the MCP protocol)

```bash
# King MCP — import-test
zz_COMPASS/MCP_Implementations/STEPHEN_KING_MCP/venv/bin/python -c "import server"

# Dickey MCP — stdlib only, runs on system python3
python3 zz_COMPASS/MCP_Implementations/JAMES_DICKEY_MCP/server.py < /dev/null
```

### MCPs NOT registered (available in repo but not in `.cursor/mcp.json`)

These live under `zz_COMPASS/MCP_Implementations/` for historical or optional
use. Entry points were fixed (async stdio pattern); they are simply not wired
into the default Cloud Agent config:

- `PROFESSIONAL_EDITOR_MCP` — professional editing evaluation tools.
- `FICTION_REVERSE_ENGINEERING_MCP` — fiction pattern analysis tools.
- `CURSOR_WORKFLOW_ORCHESTRATOR_MCP` — MCP workflow orchestration (disabled
  by default).
- `COMPASS_INTELLIGENCE_MCP` — knowledge graph transforms and prompt patterns.
- `COMPASS_Writing_Guides_MCP` — craft-reference lookups (Stephen King, Anne
  Lamott, etc.). Activate in `.cursor/mcp.json` if needed.
- `COMPASS_Character_MCP_Template` — template for building character MCPs for
  future novels. Not a runtime server.

Canonical entry point pattern: see
`COMPASS_Writing_Guides_MCP/server.py`.

---

## Cloud Agent startup

`.cursor/setup.sh` builds the three Python venvs that back the registered
MCP servers. It is idempotent. Run it on a fresh VM:

```bash
bash .cursor/setup.sh
```

The script installs `mcp` into each MCP's `venv/` from its `requirements.txt`
(or falls back to `pip install mcp` if no requirements file exists). It
smoke-tests each `server.py` with `py_compile`. If a smoke test fails, the
script exits non-zero and prints the offending directory.

If venvs are missing or broken (e.g., symlinks pointing to macOS paths),
recreate them per server:

```bash
cd zz_COMPASS/MCP_Implementations/<SERVER_NAME>
rm -rf venv
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install mcp   # or: pip install -r requirements.txt
```

The `python3.12-venv` system package must be installed on Linux VMs
(`sudo apt-get install python3.12-venv`).

---

## Editorial method (brief)

- **Scalpel** = cut. Telling-after-showing, adverbs, passive voice,
  on-the-nose dialogue, over-explanation, narrator captioning, repeated
  beats. The #1 cut is telling-after-showing.
- **Hose** = add. Sensory place details, character voice (Nick=blunt,
  Jackie=precise, Grace=tired/direct, Dr. Marsh=measured, Maxanne=radio
  cadence), money sentences (4–6 per chapter), physical grounding, period
  period period.
- **Prose models:** Stephen King (*Blind Willie*), Dennis Lehane
  (*Mystic River*), James Dickey (*Deliverance*), Michael Ondaatje
  (*The English Patient*).
- **POV locks:** Maxanne booth chapters are first-person present; everything
  else is close third past. See `_SUBAGENT_BRIEF.md` for detail.
- **Chapter titles:** applied at the very end, pre-1980 rock songs. They do
  **not** influence the prose. Write the chapter on its merits; rename later.

---

## Lint and checks

Available (optional; not wired to CI):

- **Markdown lint:** `markdownlint '**/*.md' --ignore '**/venv/**' --ignore '.cursor/**'`
- **Spell check:** `cspell '**/*.md'`
- **Python syntax:** `venv/bin/python -m py_compile server.py` (per MCP dir).

No test framework or CI is configured. The novel's quality gate is manual
review by the author (Timothy) and (since April 2026) the Super Master Agent
polish pass.

---

## Git

- **Primary branch:** `main`.
- **Commit pattern:** one logical change per commit. Always push after commit.
- **Never force-push or amend.** Author's standing rule.
- **Session summaries:** per `.cursor/rules/after_each_chat.mdc`, write a
  JSON summary to `tmp/summary-{timestamp}.json` at the end of each chat.
  `tmp/` is gitignored — these are local-only artifacts.

---

## Invisible DNA

Honor Nick. Reach Jackie. If both, it stays. If no to either, rewrite.
