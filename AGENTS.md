# AGENTS.md

## Cursor Cloud specific instructions

### Project Overview

This is a creative writing workspace for a novel called "Walk This Way" using Cursor IDE with custom MCP (Model Context Protocol) servers. There is no traditional web application, build system, or test framework. The "services" are Python-based MCP servers that provide writing tools to the Cursor AI assistant.

### Custom MCP Servers

All custom MCP servers live under `zz_COMPASS/MCP_Implementations/`. Each has its own Python virtual environment (`venv/`) and a `server.py` that speaks the MCP stdio protocol.

**Working servers** (correct async entry point):

- `COMPASS_Writing_Guides_MCP` — 12 tools for writing craft guidance (Stephen King, Anne Lamott, etc.)
- `WalkThisWay_Character_MCP` — 10 tools for novel character database (9 characters)
- `COMPASS_INTELLIGENCE_MCP` — 8 tools for prompt patterns and knowledge graph transforms

**Known broken servers** (pre-existing entry point bugs, not environment issues):

- `PROFESSIONAL_EDITOR_MCP` — calls `mcp.server.stdio.stdio_server(app)` directly (wrong API)
- `FICTION_REVERSE_ENGINEERING_MCP` — calls `mcp.server.stdio.run_server(app)` (nonexistent method)
- `DENNIS_LEHANE_MCP` — calls `mcp.server.stdio.stdio_server(app)` directly (wrong API)

These 3 servers need their `__main__` blocks updated to use the async context manager pattern. See `COMPASS_Writing_Guides_MCP/server.py` for the correct pattern.

### Running MCP Servers

Each server runs via its venv Python interpreter:

```bash
<SERVER_DIR>/venv/bin/python <SERVER_DIR>/server.py
```

Servers communicate over stdio using the MCP JSON-RPC protocol. They do not expose HTTP endpoints.

### Recreating Virtual Environments

If venvs are missing or broken (e.g., symlinks pointing to macOS paths), recreate them:

```bash
cd zz_COMPASS/MCP_Implementations/<SERVER_NAME>
rm -rf venv
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install mcp
```

The `python3.12-venv` system package must be installed (`sudo apt-get install python3.12-venv`).

### Lint / Test / Build

- **No linter** is configured for this codebase (content is primarily Markdown + Python MCP servers).
- **No automated test suite** exists. Verify MCP servers by connecting a stdio client and calling tools.
- **No build step** is needed. Servers run directly from source.

### MCP Configuration

`.cursor/config/mcp.json` contains MCP server definitions. The file currently uses macOS absolute paths (`/Users/timothy/...`). On Cloud Agent VMs, the workspace root is `/workspace`, so the custom MCP server paths need to be adjusted accordingly when testing.

### Key Directories

- `Chapters/` — Novel chapter drafts
- `Story_Bible/` — Character bible, timeline, music references
- `zz_COMPASS/` — COMPASS writing ecosystem (agents, commands, MCP implementations)
- `.cursor/` — Cursor IDE configuration (MCP config, rules, templates, scripts)
