# MCP API Keys & Setup Reference

**Purpose:** Single place to see which MCPs require API keys or extra setup after being added to `.cursor/config/mcp.json`.  
**Config file:** `.cursor/config/mcp.json`

---

## Just added to mcp.json (fiction MCPs from status check)

| MCP | Requires API / token? | Env var(s) | Notes |
|-----|------------------------|------------|--------|
| **brave-search** | Yes | `BRAVE_API_KEY` | [Brave Search API](https://brave.com/search/api/). Free tier: 2,000 queries/month. Package: `@brave/brave-search-mcp-server`. |
| **exa** | Yes | `EXA_API_KEY` | [Exa dashboard](https://dashboard.exa.ai/api-keys). Package: `exa-mcp-server`. |
| **figma** | Yes | `FIGMA_ACCESS_TOKEN` | [Figma → Settings → Personal access tokens](https://www.figma.com/settings). Package: `figma-developer-mcp`; read-only token is enough. |
| **linear** | Yes (OAuth) | — | Remote server: `https://mcp.linear.app/mcp`. First connection may prompt for Linear login. [Linear MCP docs](https://linear.app/docs/mcp). |
| **slack** | Yes | `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` | Create Slack App, OAuth scopes: `channels:history`, `channels:read`, `chat:write`, `reactions:write`, `users:read`. Package: `@modelcontextprotocol/server-slack` (deprecated but functional). |
| **puppeteer** | No | — | Browser automation. Package: `@modelcontextprotocol/server-puppeteer`. No API key. |
| **fetch** | No | — | Fetch URL content as markdown. Package: `@mcpflow.io/mcp-fetch`. No API key. |
| **openmemory** | Yes (hosted) | `OPENMEMORY_API_KEY` | Mem0/OpenMemory; **disabled** by default. [app.openmemory.dev](https://app.openmemory.dev). Package may be `@openmemory/mcp-server`; if not found, use installer: `npx @openmemory/install --client cursor`. |

---

## Previously added (non-duplicate from your list)

| MCP | Requires API / token? | Env var(s) | Notes |
|-----|------------------------|------------|--------|
| **open-library** | No | — | Internet Archive Open Library; free, no key. |
| **perplexity** | Yes | `PERPLEXITY_API_KEY` | Get at [perplexity.ai](https://www.perplexity.ai/settings/api). |
| **context7** | Maybe | Check [@upstash/context7-mcp](https://www.npmjs.com/package/@upstash/context7-mcp) | Upstash free tier may allow limited use without key. |
| **supabase** | Yes | `SUPABASE_ACCESS_TOKEN` | Personal Access Token from [Supabase Dashboard → Account → Access Tokens](https://supabase.com/dashboard/account/tokens). |
| **assemblyai** | Yes | `ASSEMBLYAI_API_KEY` | Get at [assemblyai.com](https://www.assemblyai.com/app/account). |

---

## Already in your config (API / setup)

| MCP | Requires API / token? | Env var(s) |
|-----|------------------------|------------|
| **firecrawl** | Yes | `FIRECRAWL_API_KEY` |
| **vectara** | Yes | `VECTARA_API_KEY`, `VECTARA_ENV` |
| **github** | Yes | `GITHUB_TOKEN` |
| **workflow-automation** (n8n) | Yes | `N8N_API_KEY` |
| **zen-orchestrator** | Yes | `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY` |
| **style-emulation** | Yes | `ANTHROPIC_API_KEY` |
| **google-workspace** | Yes | `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET` (OAuth) |

---

## Now enabled – API or install required (book-series, scanadi, writer-mcp, getgather, ebook, ai-context, saner-ai)

These MCPs are **enabled** in `.cursor/config/mcp.json`. Set the env var(s) and/or install the package so they run. If a server fails to start, install per the notes and fix command/args if needed.

| MCP | Requires API? | Env var(s) | Notes |
|-----|----------------|------------|--------|
| **book-series** | Yes | `POSTGRES_URI` | Python + PostgreSQL. Install: `pip install book-series-mcp` (or clone [book-series-mcp](https://github.com/rlryals/book-series-mcp)); set `POSTGRES_URI`. |
| **scanadi-mcp-ai-memory** | Yes | `POSTGRES_URI` | Python + PostgreSQL + pgvector. Install per [scanadi/mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory) (or similar); set `POSTGRES_URI`. |
| **writer-mcp** | Yes | `POSTGRES_URI`, `OPENAI_API_KEY` | Python + PostgreSQL. Install per writer-mcp project docs; set both env vars. |
| **getgather** | Depends | — | Python: [mcp-getgather/mcp-getgather](https://github.com/mcp-getgather/mcp-getgather). Clone, install (`pip install -e .` or per README), ensure `python -m mcp_getgather` works. |
| **ebook** | No (or path) | `EPUB_LIBRARY_PATH` | Python: Ebook MCP. Install (`pip install ebook_mcp` or per repo); set path to EPUB library if required. |
| **ai-context** | Depends | — | npm: `ai-context-mcp@latest`. If package not found, search npm for `ai-context-mcp` and update package name in mcp.json. |
| **saner-ai** | Depends | — | npm: `saner-ai-mcp@latest`. If package not found, search npm for `saner-ai-mcp` and update package name in mcp.json. |

---

## Disabled placeholders in mcp.json

These MCPs are in `.cursor/config/mcp.json` with **`"disabled": true`**. Set the env var(s), then set `"disabled": false` when ready.

| MCP | Requires API? | Env var(s) in config | Notes |
|-----|----------------|----------------------|--------|
| **google-books** | Yes | `GOOGLE_API_KEY` | Python: [juanbeniteza/mcp-google-books](https://github.com/juanbeniteza/mcp-google-books). Clone, install, then replace `args` with repo run command. |
| **goodreads-scraper** | Yes | `APIFY_API_TOKEN` | Placeholder uses `apify-mcp@latest`; confirm npm package or use Apify-based server. |
| **grammarly-ai** | Yes | `GRAMMARLY_API_KEY` | Placeholder uses `grammarly-mcp@latest`; confirm npm package name. |
| **word-tune** | Yes | `AI21_API_KEY` | Placeholder uses `wordtune-mcp@latest`; confirm package (AI21/Wordtune). |
| **winston-ai** | Yes | `WINSTON_AI_API_KEY` | Placeholder uses `winston-ai-mcp@latest`; confirm npm package. |
| **copyscape** | Yes | `COPYSCAPE_API_KEY` | Placeholder uses `copyscape-mcp@latest`; confirm npm package. |
| **vellum** | Depends | `VELLUM_API_KEY` | Placeholder uses `vellum-mcp@latest`; confirm if Vellum MCP exists. |
| **clerk** | Yes | `CLERK_SECRET_KEY` | Package **@clerk/clerk-mcp** is real. Set key; set `disabled: false`. |
| **yepcode** | Depends | `YEPCODE_API_KEY` | Placeholder uses `yepcode-mcp@latest`; confirm package and env var name. |
| **openmemory** | Yes | `OPENMEMORY_API_KEY` | Mem0/OpenMemory. See [OpenMemory docs](https://docs.mem0.ai/openmemory). |

---

## Summary: require API or token (all MCPs)

**Enabled in config (need keys to work):**  
firecrawl, vectara, github, workflow-automation, zen-orchestrator, style-emulation, google-workspace, perplexity, supabase, assemblyai, **brave-search**, **exa**, **figma**, **slack**

**Newly added (fiction) and need keys:**  
- **brave-search** — `BRAVE_API_KEY` ([brave.com/search/api](https://brave.com/search/api))  
- **exa** — `EXA_API_KEY` ([dashboard.exa.ai](https://dashboard.exa.ai/api-keys))  
- **figma** — `FIGMA_ACCESS_TOKEN` (Figma → Settings → Personal access tokens)  
- **slack** — `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` (Slack App OAuth)  
- **linear** — remote; first use may prompt for Linear login  

**No API needed (fiction, now enabled):** puppeteer, fetch  

**Now enabled (need API or install to run):**  
book-series, scanadi-mcp-ai-memory, writer-mcp, getgather, ebook, ai-context, saner-ai. See "Now enabled – API or install required" section above.

**Disabled placeholders (need keys + install, then set `disabled: false`):**  
google-books, goodreads-scraper, grammarly-ai, word-tune, winston-ai, copyscape, vellum, clerk, yepcode, openmemory.

Set env vars in your shell profile (e.g. `~/.zshrc`) or in Cursor’s environment so they’re available to MCPs. Use `env:VAR_NAME` in `mcp.json` so the config stays key-free.
