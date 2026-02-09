# MCPs Awaiting Your Decision & Sharing MCPs Across Folders

**Purpose:** (1) List MCPs still not set up and waiting for a decision. (2) How to use the same MCPs in different folders/programs on the same computer.

---

## 1. MCPs still not set up / waiting for your decision

These are in your **`.cursor/config/mcp.json`** with **`"disabled": true`**. For each, you can: **enable** (set API key/install, then `"disabled": false`), **leave disabled**, or **remove** the entry.

### Need API key + enable

| MCP | Decision | To enable |
|-----|----------|-----------|
| **openmemory** (Mem0/OpenMemory) | Use persistent memory across sessions? | Get key at [app.openmemory.dev](https://app.openmemory.dev) → set `OPENMEMORY_API_KEY` → set `"disabled": false`. |
| **google-workspace** (Drive, etc.) | Use Google Drive/Workspace from Cursor? | Set `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET` (OAuth) → set `"disabled": false`. |
| **google-books** | Need Google Books lookup? | Clone [mcp-google-books](https://github.com/juanbeniteza/mcp-google-books), install, set `GOOGLE_API_KEY`, fix command/args in mcp.json → set `"disabled": false`. |
| **goodreads-scraper** | Need Goodreads/book data? | Set `APIFY_API_TOKEN` → set `"disabled": false`. (Confirm package: `apify-mcp@latest`.) |
| **grammarly-ai** | Use Grammarly from Cursor? | Set `GRAMMARLY_API_KEY` → set `"disabled": false`. |
| **word-tune** | Use Wordtune? | Set `AI21_API_KEY` → set `"disabled": false`. |
| **winston-ai** | Use Winston AI? | Set `WINSTON_AI_API_KEY` → set `"disabled": false`. |
| **copyscape** | Use Copyscape? | Set `COPYSCAPE_API_KEY` → set `"disabled": false`. |
| **vellum** | Use Vellum? | Set `VELLUM_API_KEY` (confirm package exists) → set `"disabled": false`. |
| **clerk** | Use Clerk auth? | Set `CLERK_SECRET_KEY` → set `"disabled": false`. Package is real: `@clerk/clerk-mcp`. |
| **yepcode** | Use YepCode? | Set `YEPCODE_API_KEY` (confirm package name) → set `"disabled": false`. |

### Need install + API/key (Python or Postgres) — **now enabled**

| MCP | Status | To get working |
|-----|--------|----------------|
| **book-series** | **Enabled** | Install (e.g. `pip install book-series-mcp` or clone repo), set `POSTGRES_URI`. See MCP_API_KEYS_AND_SETUP_REFERENCE.md. |
| **scanadi-mcp-ai-memory** | **Enabled** | Install mcp-ai-memory (PostgreSQL + pgvector), set `POSTGRES_URI`. |
| **writer-mcp** | **Enabled** | Install writer-mcp, set `POSTGRES_URI`, `OPENAI_API_KEY`. |
| **getgather** | **Enabled** | Install [mcp-getgather](https://github.com/mcp-getgather/mcp-getgather), ensure `python -m mcp_getgather` works. |
| **ebook** | **Enabled** | Install ebook MCP, set `EPUB_LIBRARY_PATH` if required. |

### Unclear package / need to confirm — **now enabled**

| MCP | Status | To get working |
|-----|--------|----------------|
| **ai-context** | **Enabled** | If server fails, find real npm package for `ai-context-mcp` and update mcp.json. |
| **saner-ai** | **Enabled** | If server fails, find real npm package for `saner-ai-mcp` and update mcp.json. |

---

## 2. How to share MCPs on the same computer with a different folder (program)

You have two ways to use the same MCPs in multiple projects/folders on the same machine.

### Option A: Global MCP config (one setup, all projects)

MCPs configured **globally** in Cursor are available in **every** folder/workspace you open.

**Steps:**

1. Open **Cursor Settings** (e.g. **Cmd + ,** on Mac or **File → Preferences → Settings**).
2. Search for **MCP** or go to **Features → MCP**.
3. Add or edit **global** MCP servers there. These apply to all projects.

**Where Cursor stores global MCP config:**  
On macOS it is often **`~/.cursor/mcp.json`** or managed inside Cursor’s app data (e.g. **~/Library/Application Support/Cursor/...**). The Settings UI is the reliable place to edit global MCPs.

**Result:** Any folder you open in Cursor will see the same global MCPs. No need to copy config into each project.

### Option B: Project-level config (copy into each folder)

Your current setup is **project-level**: **`.cursor/config/mcp.json`** inside **Walk This Way**. That file only applies when this project is open.

To use the **same** MCP set in another folder/program:

1. Copy your **`mcp.json`** (or the entries you want) into that project:
   - **Other Cursor project:**  
     Create (or use) **`<other-project>/.cursor/config/mcp.json`** and paste the same `mcpServers` content (and adjust any project-specific paths, e.g. filesystem paths).
   - **Same machine, different “program”:**  
     If the other program is also Cursor, use the same as above. If it’s another app (e.g. Claude Desktop), that app has its own config file/location; put the same server definitions there.

2. **Environment variables:**  
   Ensure the same env vars (`BRAVE_API_KEY`, `EXA_API_KEY`, etc.) are available to that other folder/app (e.g. set in `~/.zshrc` or that app’s env).

**Result:** Each project has its own `.cursor/config/mcp.json`; they can be identical or different per project.

### Summary

| Goal | What to do |
|------|------------|
| Same MCPs in **every** Cursor project on this computer | Use **Cursor Settings → MCP** and configure **global** MCP servers (Option A). |
| Same MCPs in **a few** Cursor projects | Copy **`.cursor/config/mcp.json`** into each project’s **`.cursor/config/`** (Option B). |
| Same MCPs in **another app** (e.g. Claude Desktop) on this computer | Add the same server definitions to that app’s MCP config file; set env vars so that app can read them. |

---

**Reference:** Full list of disabled MCPs and API notes: **`MCP_API_KEYS_AND_SETUP_REFERENCE.md`** (in this project).
