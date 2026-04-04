# AGENTS

## Cursor Cloud specific instructions

### Project overview

This is a creative writing workspace for the novel "Walk This Way" by Timothy J. Smith, not a traditional software application. The codebase contains:

- Novel chapters, story bible, and supporting markdown/text files
- 8 custom Python MCP (Model Context Protocol) servers under `zz_COMPASS/MCP_Implementations/`
- The COMPASS portable writing ecosystem under `zz_COMPASS/`

There is no web app, no frontend, no backend API, no database, and no build system. The "application" is the set of MCP servers that provide AI-assisted writing tools.

### MCP servers

All MCP servers are Python-based and live under `zz_COMPASS/MCP_Implementations/`. Each has its own `venv/` with the `mcp` pip package installed.

Working servers (start correctly via stdio):

- `COMPASS_Writing_Guides_MCP` — writing craft reference database (12 tools)
- `WalkThisWay_Character_MCP` — novel character database (10 tools)
- `COMPASS_Character_MCP_Template` — reusable character MCP template
- `COMPASS_INTELLIGENCE_MCP` — knowledge graph transforms, prompt patterns (8 tools)
- `STEPHEN_KING_MCP` — "The Writer's Toolbox" craft education engine (3 tools: king_imagine, king_craft, king_revise; 3 modes; 3 liberty levels)

Servers with pre-existing API issues (venv + import works, but `server.py` entrypoint uses deprecated MCP API):

- `PROFESSIONAL_EDITOR_MCP` — uses `mcp.server.stdio.stdio_server(app)` incorrectly
- `FICTION_REVERSE_ENGINEERING_MCP` — uses nonexistent `mcp.server.stdio.run_server(app)`
- `DENNIS_LEHANE_MCP` — same issue as Professional Editor
- `CURSOR_WORKFLOW_ORCHESTRATOR_MCP` — tries to mkdir `/.cursor/logs` (permission denied at root)

### Running MCP servers

Each server runs via its venv Python and communicates over stdio:

```bash
cd zz_COMPASS/MCP_Implementations/<SERVER_DIR>
venv/bin/python server.py
```

For functional testing without the MCP protocol, import directly:

```python
cd zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP
venv/bin/python -c "
import asyncio, json
from server import call_tool
result = asyncio.run(call_tool('list_authors', {}))
print(json.loads(result[0].text))
"
```

### Lint and test

No test framework or CI is configured. Available lint checks:

- **Markdown lint**: `markdownlint '**/*.md' --ignore '**/venv/**' --ignore '.cursor/**'` (config in `.markdownlint.json`)
- **Spell check**: `cspell '**/*.md'` (config in `.cspell.json`)
- **Python syntax**: `venv/bin/python -m py_compile server.py` (run from each MCP server directory)

### Dependencies

Each MCP server's sole dependency is the `mcp` pip package, specified in its `requirements.txt`. The system requires `python3.12-venv` to be installed at the OS level.
