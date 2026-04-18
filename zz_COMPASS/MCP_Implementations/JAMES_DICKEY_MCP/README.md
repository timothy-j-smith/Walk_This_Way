# James Dickey MCP — Deliverance Craft Engine

**PRIVATE & CONFIDENTIAL** — for your local use only. Do not publish this folder or push it to a public repository.

## What it does

This MCP exposes three tools aligned with your A.B.S.H. system and your Stephen King MCP pattern:

| Tool | Role |
|------|------|
| `dickey_imagine` | Architecture — situation, stakes, wilderness/group pressure |
| `dickey_craft` | Brick — voice, image, compression, first-person embodiment |
| `dickey_revise` | Scalpel + Hose — cut noise, add sensation and aftermath |

Each tool returns a single **markdown agent brief**: craft principles from `data/dickey_deliverance_analysis.json`, mode/liberty hints, plus your pasted **author material**. The model in Cursor is expected to follow that brief (honesty protocol, no long copyrighted quotations).

Natural-language aliases you can still use in chat (not enforced by the server): **Dickey Create Nice**, **Dickey Transform Neutral**, **Dickey Edit Professional**, etc. Map them to `mode` + `liberty` arguments below.

## Requirements

- **Python 3.9+** on your PATH (`python3`). No pip install is required.

## Run locally (stdio)

From this directory:

```bash
python3 server.py
```

The server speaks **newline-delimited JSON-RPC** (MCP stdio). It is meant to be launched by Cursor, not run interactively.

## Cursor configuration

In **Cursor Settings → MCP**, add a server entry. Example (adjust paths if you move the folder):

```json
{
  "mcpServers": {
    "james-dickey-deliverance": {
      "command": "python3",
      "args": ["/Users/timothy/zz_COMPASS/MCP_Implementations/JAMES_DICKEY_MCP/server.py"],
      "cwd": "/Users/timothy/zz_COMPASS/MCP_Implementations/JAMES_DICKEY_MCP"
    }
  }
}
```

Using an absolute path to `server.py` avoids ambiguity about working directory.

## Tool parameters

All three tools accept the same argument object:

| Argument | Type | Default (imagine / craft / revise) | Notes |
|----------|------|-------------------------------------|--------|
| `text` | string | _(required)_ | Seed, paragraph, or longer excerpt |
| `mode` | `create` \| `transform` \| `edit` | `create` / `create` / `transform` | Matches Create / Transform / Edit |
| `liberty` | `nice` \| `neutral` \| `professional` | `nice` / `nice` / `neutral` | Feedback delivery level |
| `focus` | string | optional | e.g. `aftermath`, `river sound`, `class cues` |

### Examples (conceptual)

- **Dickey Create Nice** → `dickey_imagine` with `mode: "create"`, `liberty: "nice"`.
- **Dickey Transform Neutral** → `dickey_revise` with `mode: "transform"`, `liberty: "neutral"`.
- **Dickey Edit Professional** → `dickey_revise` with `mode: "edit"`, `liberty: "professional"`.

## Knowledge base

Edit [`data/dickey_deliverance_analysis.json`](data/dickey_deliverance_analysis.json) to add verified short quotations (`quotes` array), tighten rules, or extend *Deliverance*-specific notes. Restart Cursor or toggle the MCP server after edits.

## Design document

See [`JAMES_DICKEY_MCP_DESIGN.md`](JAMES_DICKEY_MCP_DESIGN.md) for the full 3×3×3 mirror of your Stephen King MCP (modes, liberty levels, scenarios, agent guidelines).

## Troubleshooting

- **`FileNotFoundError` for the JSON path** — ensure `cwd` in the MCP config points at this folder (the parent of `data/`).
- **No response in Cursor** — confirm `python3` resolves to the intended interpreter in the environment Cursor uses.

---

*Private — James Dickey MCP, April 2026*
