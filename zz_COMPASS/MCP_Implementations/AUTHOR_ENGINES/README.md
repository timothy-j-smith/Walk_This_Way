# AUTHOR ENGINES — README

**Status:** PRIVATE & CONFIDENTIAL — Timothy's personal MFA program
**Date:** August 8, 2026
**Location:** `zz_COMPASS/MCP_Implementations/AUTHOR_ENGINES/`
**Educational use only. Not for publication.**

---

## What this is

15 author tutoring engines running from **one** server (`author_server.py`) and 15 knowledge bases (`data/*.json`). Each engine teaches through one author's craft using your canonical 3-3-3 system and A.B.S.H. method.

---

## Where these run (your question answered)

| App | Status |
|---|---|
| **Cursor** | ✅ CONNECTED — registered in `~/.cursor/mcp.json` as `author-king` … `author-harris` |
| **Claude Desktop / Cowork** | ❌ Not yet — can be added anytime by putting the same command entries in that app's MCP config |
| **Independent?** | The engines themselves are app-independent (plain Python + JSON in iCloud). Any MCP-capable app can run them. Today, only Cursor is wired up. |

**Requirements:** shared venv at `~/mcp-servers/author-engines-venv` (Python 3.10+, `mcp` package). No API keys. No internet. Fully private.

---

## How to call the right engine at the right time

**Routing phrase:** `[Author] [Mode] [Level] — [your text]`
Example: *"Russo Edit Professional — here's Chapter 12"* or just ask naturally ("give me a Dickey pass on this ordeal scene") and Cursor routes it.

### Every author has 4 tools

| Tool | Mode | A.B.S.H. | Default level | Use when |
|---|---|---|---|---|
| `_guide` | Reference | — | — | "Show me Russo's craft DNA" |
| `_imagine` | CREATE | **A**rchitecture | Nice | Seed idea → structure, stakes |
| `_craft` | TRANSFORM | **B**rick support | Neutral | Excerpt → surgical improvement |
| `_revise` | EDIT | **S**calpel + **H**ose | Professional | Chapter → deep pass |

Liberty levels: **Nice / Neutral / Professional** — tone changes, truth does not. Override anytime: *"Ondaatje Craft, professional level."*

### Who to summon when

| Need | Summon |
|---|---|
| Guilt, shame, working-class truth, kid-narrator | **King** (*Blind Willie*) |
| Fragmented time, image-first, withholding | **Ondaatje** (*English Patient*) |
| Ordeal, body under pressure, aftermath | **Dickey** (*Deliverance*) |
| Mythic register, group scenes, system-as-antagonist | **Kesey** (*Cuckoo's Nest*) |
| Small-town community, economic weather, wry warmth | **Russo** (*Empire Falls*) |
| Sentence-level grace, domestic weight | **Robinson** (*Housekeeping*) |
| Minimalism, violence as knowledge | **McCarthy** (*No Country*) |
| Plot mechanics, hooks, dialogue that works triple | **Goldman** (*Marathon Man*) |
| Teen voice, letters, trauma as silence | **Chbosky** (*Perks*) |
| Inverted mystery, lush complicity | **Tartt** (*Secret History*) |
| Compression, landscape as fate, trade language | **Proulx** (*Close Range*) |
| Restraint over atrocity, institutional calm | **Whitehead** (*Nickel Boys*) |
| Self-aware first person, knowing/doing gap | **Houston** (*Cowboys Are My Weakness*) |
| Momentum, identity-as-mystery, chapter hooks | **Ludlum** (*Bourne Identity*) |
| Calm dread, procedure, dialogue duels | **Harris** (*Silence of the Lambs*) |

Scene-level Boston grit → your existing **dennis-lehane-style** MCP (separate, already running).

---

## Toggling on/off — and should you?

**Where:** Cursor → Settings → MCP → toggle switch next to each `author-*` server. Instant, no restart needed.

**Leaving all 15 on is safe** — each is a tiny idle Python process (a few MB, zero CPU when unused). The real cost is **attention, not memory**: 15 servers × 4 tools = 60 tools in Cursor's context, which can occasionally make it pick the wrong author or slow tool selection.

**Recommended pattern:**
- **Keep the four cores ON always:** King, Ondaatje, Dickey, Kesey
- **Toggle satellites ON per session:** writing the bridge chapter? Turn on Dickey + Harris. Maxanne frame? Ondaatje + Robinson. Thriller pass? Ludlum + Goldman.
- If Cursor ever routes to the wrong author, name the author explicitly in your prompt — that always wins.

---

## Maintenance

- **Deepen an author:** edit `data/<author>.json` (add dna, moves, prompts) — changes load next Cursor restart. Full design docs live in `MCP_Library_COMPASS/Style_MCPs/AUTHOR_MCP_SUITE/`.
- **Test outside Cursor:** `~/mcp-servers/author-engines-venv/bin/python author_server.py --author russo --selftest`
- **Add an author:** create `data/<newkey>.json` (copy any existing one), add an `author-<newkey>` entry to `~/.cursor/mcp.json`, restart Cursor. ~10 minutes.
- **Add to Claude Desktop later:** copy the same `command`/`args` entries into its MCP config file.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server red in Cursor / "No module named mcp" | venv built with Python 3.9 — rebuild with `/opt/homebrew/bin/python3 -m venv ~/mcp-servers/author-engines-venv` then `pip install mcp` |
| "knowledge base not found" | iCloud hasn't synced `data/*.json` locally — open the folder in Finder to force download |
| Wrong author answers | Name the author explicitly in the prompt |

---

*PRIVATE & CONFIDENTIAL — For Timothy's use only*
