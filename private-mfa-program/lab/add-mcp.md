# Add an MCP

Toolbox. Called when needed. Never all at once.

This file is the arsenal index for the MFA. Those paths replace the earlier diagnosis that `/Users/timothy/mcp-servers` was gone.

## Merge applied (2026-08-15)

Walk This Way `.cursor/mcp.json` (symlink to `.cursor/config/mcp.json`) is now the **merged** file.

- Backup: `.cursor/config/mcp.json.bak-20260815-185422`
- Before: 83 Walk This Way servers
- Restored paste: 53 servers
- After: 104 unique servers
- Preferred restored: Sequential Thinking Ultra/MAS (DeepSeek via `~/.cursor/.env.mcp`), all 15 `author-*` engines (`author-engines-venv` + `AUTHOR_ENGINES/author_server.py`), gitkraken (`/opt/homebrew/bin/gk`), plus github/firecrawl/pandoc/toolbox/context7/slack/puppeteer/blender/airtable/chain-of-draft/duckduckgo/sequential-thinking
- Added from restore only: gutenberg, internet-archive, ollama, dictionary, wikipedia, wikidata, poetrydb, google-books, apify, mcp-mermaid, memory, Firebase, Netlify, Vale, mcp-open-library, cognee-local, sequential-thinking-visual, n8n, hyperagent, git, airtable-user-mcp, GitKraken (gk-alpha kepler)
- Collapsed: `walk-this-way` into `walk-this-way-files` (same filesystem, same novel path)
- Kept both: `gitkraken` and `GitKraken` (different binaries); `n8n` and `n8n-workflow`; `memory` and `knowledge-graph-memory`; `mcp-open-library` and `open-library`; `cognee-local` and `cognee-connections`; `git` and `tim-cursor-experiment-files`
- Omitted: `sequential-thinking-rust`
- Slack auth uses `env:SLACK_CLIENT_ID` — do not put the client id in this README
- Timothy deactivates tonight. Do not call the whole list in one chat.

## How to add later

1. Confirm the binary or venv actually runs
2. Add a row below (name, path, when the Dean calls it, when not)
3. Do not turn it on in every chat
4. If it duplicates a native Cursor tool, say so and prefer one

## Sequential thinking (four, plus one extra)

Skip rust. Visual is extra, not a replacement.

| Name | Restored path | When the Dean calls it |
| --- | --- | --- |
| Anthropic sequential-thinking | `npx -y @modelcontextprotocol/server-sequential-thinking` | Straight-line reasoning, bias check, quality metrics |
| Ultra | `/Users/timothy/mcp-servers/sequential-thinking-ultra/dist/index.js` | Hard craft or plot knot; budgeted deep think |
| MAS | `/Users/timothy/mcp-servers/sequential-thinking-mas/venv/bin/mcp-server-mas-sequential-thinking` (FradSer 0.8.0) | High-stakes decision. Specialist agents in parallel, then synthesis. Needs `DEEPSEEK_API_KEY` in Cursor’s environment. Not a substitute for Anthropic sequential-thinking |
| Enhanced | `/Users/timothy/mcp-servers/sequential-thinking-enhanced/venv/bin/python` + `app/enhanced_sequential_thinking_server.py` (VitalyMalakanov, 19 modes) | Mode switch: linear, creative, evaluative. Not a substitute for Anthropic sequential-thinking |
| Visual (extra) | sequential-thinking-visual | Diagram a knot. Not a substitute for the four |

Do not call more than one sequential-thinking flavor in the same pass unless the Dean names why.

## Author engines

**Venv (restored, prefer this):** `/Users/timothy/mcp-servers/author-engines-venv/bin/python`

**Stale (do not prefer):** `/Users/timothy/mcp-venvs/walk-this-way-writing/bin/python`

**Server:** `AUTHOR_ENGINES/author_server.py --author [slug]`

Fifteen engines exist (king, ondaatje, dickey, kesey, russo, robinson, mccarthy, goldman, chbosky, tartt, proulx, whitehead, houston, ludlum, harris). Call the one in the room. Russo, Tartt, Whitehead stay off the wall even if the binary exists.

Deep labs (richer than generic engines; Dean routes here when that lens is in the room):

- english-patient
- james-dickey-deliverance

Long-term: fold those into one Ondaatje / one Dickey standing ground. Do not invent a third personality meanwhile.

## Research

| Name | When |
| --- | --- |
| Firecrawl | Default live research (period fact, place, news) |
| Exa | Alternate search / fetch when Firecrawl is the wrong shape |
| DuckDuckGo | Light lookup |
| Wikipedia / Wikidata | Quick factual scaffold — still verify |
| Google Books / Open Library / Gutenberg / Internet Archive | Source hunt, not wholesale paste |
| PoetryDB / Dictionary | Word and line checks |

Do not invent period facts. Research is material, not plot.

## Writing lab (call by job)

| Job | Tools |
| --- | --- |
| See the seam | fiction-reverse-engineering, style-emulation |
| Line pressure | professional-editor, Vale |
| Memory across files | cognee-local, memory |
| Structure picture | mcp-mermaid |
| Export / convert | pandoc |
| Short reasoning draft | chain-of-draft |
| Catch-all utilities | toolbox |

## Restored and available — not always on

gutenberg, internet-archive, ollama, dictionary, wikipedia, wikidata, poetrydb, google-books, apify, walk-this-way filesystem, gitkraken, mcp-mermaid, sequential-thinking (Anthropic), memory, duckduckgo, github, firecrawl, Firebase, Netlify, Vale, mcp-open-library, cognee-local, sequential-thinking-visual, blender, slack, n8n, airtable, hyperagent, git (Tim Cursor Experiment), airtable-user-mcp, pandoc, context7, puppeteer, chain-of-draft, toolbox, all 15 author-* engines, GitKraken kepler.

Filesystem MCP is insurance beside native Read. Prefer native Read for daily chapter work. Do not run two filesystems on the same folder in one pass.

## Skip

- sequential-thinking-rust
- Clerk and other non-writing app servers unless today's job is actually that app
- Enabling the full list "so they are ready"

## Git

Regular named commits after a real chunk. Dean offers the message. Chapter files are the daily draft UI. Git is backup, not the place Timothy hunts yesterday's paragraph.
