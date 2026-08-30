# Priority MCP errors — 22 Aug 2026

They were not “disconnected.” Cursor still tried to spawn them. The launch commands pointed at binaries, folders, and npm packages that are gone from this Mac.

Shared root cause: `/Users/timothy/mcp-servers` was missing, Homebrew `python3` / `uvx` / `gk` were not on the paths in `mcp.json`, and several npm package names were wrong.

Reload MCP after this pass: Cursor Settings → MCP, or reload the window.

## What was wrong (from Cursor logs)

| MCP | Log error | Cause |
| --- | --- | --- |
| author-dickey / kesey / king / mccarthy / ondaatje / robinson / russo | `spawn …/author-engines-venv/bin/python ENOENT` | Shared venv directory missing |
| chain-of-draft | `Cannot find module …/mcp-chain-of-draft-server/build/index.js` | Global npm install gone |
| ebook | `spawn python ENOENT` | Cursor PATH has no `python` |
| git | `spawn /opt/homebrew/bin/uvx ENOENT` | `uv` / `uvx` not installed |
| gitkraken | `spawn /opt/homebrew/bin/gk ENOENT` | GitKraken CLI lives under Application Support, not Homebrew |
| GitKraken | gk-alpha missing | Desktop injected `gk-alpha`; that binary is not on disk |
| goodreads-scraper | npm 404 `apify-mcp@latest` | That package name does not exist |
| google-books | `cd: …/google-books-mcp/repo: No such file` | Cloned server directory missing |
| google-workspace | `spawn uvx ENOENT` | Same missing `uvx`; also `"disabled": true` does not stop Cursor from launching it |
| gutenberg | `Cannot find module …/@cyanheads/gutenberg-mcp-server/dist/index.js` | Global npm install gone |
| open-library | npm 404 `@8enSmith/mcp-open-library` | Scoped name is invalid (capital letters); real package is `mcp-open-library` |
| sequential-thinking | *(already connected)* | Working |
| sequential-thinking-enhanced | `spawn …/enhanced-sequential-thinking-server ENOENT` | `mcp-servers` missing |
| mem0 (“moss”) | HTTP 401 `invalid_token` | Plugin needs `MEM0_API_KEY`; not a workspace `mcp.json` server |

## What was restored on disk

- Recreated `/Users/timothy/mcp-servers/author-engines-venv` with Python 3.12 and `mcp<2`. King / Dickey / Ondaatje / Kesey / McCarthy / Robinson / Russo `--selftest` all passed. Config paths for `author-*` were already correct.
- Installed Homebrew `uv` / `uvx` at `/opt/homebrew/bin/uvx`.
- Installed `ebook-mcp` and `book-metadata-mcp` into `/Users/timothy/mcp-venvs/walk-this-way-writing`.
- Installed Node packages locally at `/Users/timothy/mcp-servers/node-mcps/` (chain-of-draft, gutenberg, open-library).
- GitKraken CLI found at `/Users/timothy/Library/Application Support/GitKrakenCLI/gk`.
- Cloned BeehiveInnovations PAL (formerly Zen) to `/Users/timothy/mcp-servers/zen-mcp-server` with Python 3.12 venv; pinned `mcp` 1.29. Handshake: server name `PAL`, version 9.8.2.

## Config changes in `.cursor/config/mcp.json`

- **ebook** — absolute Python, run `ebook_mcp.main` (the `ebook-mcp` CLI entry creates an empty server).
- **git** — local `~/mcp-servers/git-mcp` venv; **no `--repository`**. Tools take `repo_path` on each call (any git repo, including the CLI’s current tree). It is not locked to Walk This Way.
- **gitkraken** / **GitKraken** — real `gk` binary.
- **goodreads-scraper** — Cursor ignored the hosted Apify `url` and kept spawning **stdio**, then exited: `APIFY_TOKEN is required`. Local FastMCP at `~/mcp-servers/goodreads-scraper/server.py` (writing venv). Handshake: `goodreads_search`, `goodreads_book`, `goodreads_reviews` against public Goodreads pages. No token. Plugin Apify still has the paid Store Actors if you want those.
- **zen-orchestrator** — BeehiveInnovations **PAL** 9.8.2 (the product formerly called Zen) cloned to `~/mcp-servers/zen-mcp-server`. `mcp` pinned to 1.29 (`mcp` 2.0 has no `list_tools`). Handshake: server name `PAL`, 12 tools with code-heavy tools disabled. Needs `GEMINI_API_KEY` or `OPENAI_API_KEY` (Cursor env or `~/mcp-servers/zen-mcp-server/.env`). PAL does not take Anthropic as a native provider. `"disabled": true` does not stop Cursor from launching a server; the slot is now `disabled: false`.
- **google-books** — `book-metadata-mcp` (Google Books + Open Library metadata).
- **google-workspace** — `/opt/homebrew/bin/uvx workspace-mcp`; env interpolation fixed to `${env:…}`. First run still needs Google OAuth client id/secret in the environment.
- **gutenberg** / **open-library** / **chain-of-draft** — local Node entry files under `~/mcp-servers/node-mcps`.
- **sequential-thinking-enhanced** — VitalyMalakanov MCP Thinking (19 modes: linear, tree, creative, evaluative, etc.). Not a copy of Anthropic sequential-thinking. Pinned `pydantic<2.12` + FastMCP 2.3.5; class-method tools re-registered as module-level wrappers so FastMCP can load them. Launch: `~/mcp-servers/sequential-thinking-enhanced/venv/bin/python …/app/enhanced_sequential_thinking_server.py`.
- **sequential-thinking-mas** — FradSer Multi-Agent System 0.8.0 (not Anthropic). Specialist agents in parallel, then synthesis. Binary: `~/mcp-servers/sequential-thinking-mas/venv/bin/mcp-server-mas-sequential-thinking`. Needs `DEEPSEEK_API_KEY` in Cursor’s environment for actual thought processing.

## Still needs a key from you

### mem0

Plugin HTTP MCP at `https://mcp.mem0.ai/mcp`. Logs: 401 invalid token. `MEM0_API_KEY` is not set.

1. Get a key at [https://app.mem0.ai/dashboard/api-keys](https://app.mem0.ai/dashboard/api-keys) (`m0-…`).
2. Cursor → Settings → MCP / plugin env, or add `MEM0_API_KEY` to the environment Cursor inherits.
3. Reinstall the Mem0 plugin if it never prompted for the key.

### goodreads / Apify

The named slot is a **local** Goodreads MCP (no token). After reload you should see `goodreads_search`, `goodreads_book`, and `goodreads_reviews`.

The workspace `apify` stdio entry still needs `APIFY_TOKEN`. Plugin Apify is already connected for Store Actors.

### zen-orchestrator (PAL)

Spawn path is restored. PAL will still refuse to start until one provider key exists:

1. Easiest: put `GEMINI_API_KEY=...` or `OPENAI_API_KEY=...` in `~/mcp-servers/zen-mcp-server/.env` (PAL reads that file itself).
2. Or add the same variable to the environment Cursor inherits.

Then reload MCP. Tools: `chat`, `thinkdeep`, `planner`, `consensus`, plus `listmodels` / `version`.

### google-workspace

`uvx workspace-mcp` launches. OAuth still needs `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET`. Plugin Google Drive is already connected in this session if you only need Drive.

### ebook library path

`EPUB_LIBRARY_PATH` is unset. The server will start; pass a folder when you call tools, or set the env var to your EPUB library.

## Reload without quitting Cursor

Try these in order. You do **not** start with Cmd+Q.

1. **Per-server reconnect:** Cursor Settings (`Cmd+Shift+J`) → MCP (or Customize → MCPs). Find the server. Toggle it off and on, or use **Reload MCP Server** if you see that control. This restarts the process. It is the right first move after a spawn-path fix.
2. **Reload Window:** `Cmd+Shift+P` → type `Developer: Reload Window` → Enter. Cursor stays open. Tabs come back. This is the shorter alternative to Cmd+Q.
3. **Full quit** (`Cmd+Q`, reopen) only if the server is still red or the tool list is stale. Cursor currently caches MCP tool lists; staff have said a full quit is the reliable last step when 1 and 2 do not pick up new tools.

`Cmd+R` is New Chat, not reload.
