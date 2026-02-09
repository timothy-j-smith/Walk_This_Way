# Top Fiction MCPs Status Check

**Checked against:** `.cursor/config/mcp.json`  
**Date:** 2026  
**List source:** Marathon Man / Deliverance fiction MCP guide — “Top 15 fiction MCPs not in your original list”

---

## Status: Do You Have These Set Up?

| MCP from guide | In your config? | Your config name | Status | API required? |
|----------------|-----------------|------------------|--------|----------------|
| **Book Series MCP** | Yes (placeholder) | `book-series` | **Disabled** — Python + PostgreSQL; `POSTGRES_URI` | Yes (PostgreSQL) |
| **Mem0 / OpenMemory** | Partial | No “Mem0” or “OpenMemory” by name | You have **knowledge-graph-memory**, **memorygraph**, **enhanced-mcp-memory**, **supermemory** — similar “memory” role; Mem0/OpenMemory not installed as such | Mem0 hosted: yes; local: no |
| **Google Drive MCP** | Partial | `google-workspace` | **Disabled** — Google Workspace (can include Drive); needs OAuth (GOOGLE_OAUTH_CLIENT_ID/SECRET) | Yes (Google OAuth) |
| **Brave Search MCP** | Yes | `brave-search` | **Added, enabled** — `BRAVE_API_KEY` required | Yes (API key) |
| **Exa MCP** | Yes | `exa` | **Added, enabled** — `EXA_API_KEY` required | Yes (Exa account) |
| **Figma MCP** | Yes | `figma` | **Added, enabled** — `FIGMA_ACCESS_TOKEN` required | Yes (Figma token) |
| **GitHub MCP** | Yes | `github` | **Enabled** — uses `GITHUB_TOKEN` | Yes (GitHub token) |
| **Linear MCP** | Yes | `linear` | **Added, enabled** — remote mcp.linear.app; first use may prompt login | Yes (OAuth) |
| **Puppeteer MCP** | Yes | `puppeteer` | **Added, enabled** — no API | No |
| **Filesystem MCP** | Yes | `walk-this-way-files` | **Enabled** — `@modelcontextprotocol/server-filesystem` pointed at Walk This Way project | No |
| **Fetch MCP** | Yes | `fetch` | **Added, enabled** — `@mcpflow.io/mcp-fetch`; no API | No |
| **Slack MCP** | Yes | `slack` | **Added, enabled** — `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` required | Yes (Slack App) |
| **PostgreSQL MCP** | No (as standalone) | — | No generic “PostgreSQL MCP”. **book-series** and **scanadi-mcp-ai-memory** use `POSTGRES_URI` and are disabled | Yes (Postgres connection) |

---

## Summary

- **Already set up and enabled:** Filesystem (`walk-this-way-files`), GitHub (`github`).
- **Newly added and enabled:** Brave Search (`brave-search`), Exa (`exa`), Figma (`figma`), Linear (`linear`), Puppeteer (`puppeteer`), Fetch (`fetch`), Slack (`slack`). Set required API keys (see **MCP_API_KEYS_AND_SETUP_REFERENCE.md**).
- **In config but disabled:** Book Series (`book-series`), Google Workspace (`google-workspace`), OpenMemory (`openmemory`).
- **Covered by alternatives:** Memory → Knowledge Graph + Memorygraph + Enhanced + Supermemory; OpenMemory added as optional disabled placeholder.
- **Not in config (standalone):** PostgreSQL MCP (book-series/scanadi use Postgres; no generic Postgres MCP added).

---

## Quick add reference (from guide)

| To add | Install / API |
|--------|----------------|
| Brave Search | brave.com/search/api → `BRAVE_API_KEY`; npm package if available |
| Exa | exa.ai → API; mcp.exa.ai or community Exa MCP |
| Figma | figma.com; OAuth or access token |
| Linear | linear.app → Settings → Personal API Keys → `LINEAR_API_KEY` |
| Mem0/OpenMemory | app.openmemory.dev or self-host |
| Slack | api.slack.com → token |
| Puppeteer | Community MCP; usually no API |
| Fetch | Often part of toolbox or a small HTTP MCP |

Use `MCP_API_KEYS_AND_SETUP_REFERENCE.md` in this project for env vars and setup details.
