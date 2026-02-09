# MCP Workspace Sync: Walk This Way & Tim Cursor Experiment

**Purpose:** Both workspaces on your 2025 MacBook Air now use the **same MCP arsenal**. This doc explains what was done and how to keep them in sync.

---

## What was done

1. **Walk This Way** (this workspace)  
   - Already had the full MCP config at `.cursor/config/mcp.json`.  
   - Added a second filesystem MCP: **`tim-cursor-experiment-files`** pointing to the Tim Cursor Experiment folder, so this workspace can access both folders.

2. **Tim Cursor Experiment** (other workspace)  
   - Had no `.cursor/config/` or `mcp.json`.  
   - Created **`Tim Cursor Experiment/.cursor/config/mcp.json`** with the **same** content as Walk This Way (including both filesystem MCPs).

Result: **Identical MCP list** in both workspaces. Same servers, same env vars, same enabled/disabled state.

---

## Paths

| Workspace              | Config file                                                                 | Filesystem MCPs |
|------------------------|-----------------------------------------------------------------------------|-----------------|
| Walk This Way          | `03_Novels/Walk This Way/.cursor/config/mcp.json`                           | `walk-this-way-files` → Walk This Way folder; `tim-cursor-experiment-files` → Tim Cursor Experiment folder |
| Tim Cursor Experiment  | `Tim Cursor Experiment/.cursor/config/mcp.json`                             | Same two entries (same paths). |

COMPASS/Lehane/Professional Editor/etc. still use **absolute paths** to the Walk This Way folder, so they work from **either** workspace.

---

## Keeping them in sync

When you **add, remove, or change** an MCP in one workspace:

1. Edit **Walk This Way** `.cursor/config/mcp.json` (use this as the source of truth).
2. Copy the **entire** `mcp.json` to **Tim Cursor Experiment** `.cursor/config/mcp.json` (overwrite).

Or from Terminal (run from the Cursor iCloud folder):

```bash
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/config/mcp.json" \
   "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/Tim Cursor Experiment/.cursor/config/mcp.json"
```

Restart Cursor (or reload the window) in the workspace you changed so it picks up the new config.

---

## Env vars

All MCPs use **`env:VAR_NAME`** in the config, so the **same env vars** (e.g. in `~/.zshrc` or Cursor’s environment) are used in **both** workspaces. No need to set anything per-workspace.
