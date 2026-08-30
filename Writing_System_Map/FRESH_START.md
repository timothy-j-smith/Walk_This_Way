# If you started over in Cursor tomorrow

Chart only. No new repos tonight. Old folders stay until the new window writes a chapter without hunting.

**Print:** this `.md` → `Cmd+Shift+V` to read. For paper, File → Print from **Preview** on a PDF, not Command-P inside Cursor.

---

## Verdict

Start fresh. Do not finagle Walk This Way into becoming a clean toolbox. It already mixed the book and the machines.

Keep every old repo. Copy what still works. Delete only after you trust the new shape.

**Repo** = one git folder. **Workspace** = the Cursor window (a `.code-workspace` can open two folders). **User-level** = this Mac (`~/.cursor/skills`, plugins, `~/mcp-servers`).

Do not open all eight novels in one workspace. That is how a ninth draft starts.

Do not “go through COMPASS” as a project. `zz_COMPASS` and `yy_Archive` are quarry. Mine working servers later. Do not rebuild the name.

---

## Three layers

1. **Workspace** — one book + Writing Tools, side by side.
2. **Repo A — the novel** — pages, story bible, this book’s locks.
3. **Repo B — Writing Tools** — new name. Not COMPASS. Not MCP.
4. **This Mac** — MFA skill, Google plugins, running servers.

Google / Gmail / Calendar do not need a third git repo.

---

## Repo A — novel workspace (only what you need)

```
walk-this-way/
  README.md
  .gitignore
  project-hub.md
  chapters/          (or Draft_06/ while this book still uses that name)
  story-bible/
  vault.md
  Walk-This-Way.code-workspace
  .cursor/
    rules/this-book.mdc    ← canon locks only
    mcp.json               ← short: this book + ~8 daily tools
```

README says: where the book is, how to open the workspace, do not move folders from here.

One project rule: cassette, Nick Army, Maxanne 59, Draft_05 frozen. Not 56 commands. Not XML-tag tutorials.

You already have this shape in `private-mfa-program/novel-pack/`.

---

## Repo B — Writing Tools

Working name: **Writing Tools**. One copy. Senseless and the next novel point here. No paste.

```
writing-tools/
  README.md
  servers/           ← only servers that still handshake
  faculty/           ← author JSON
  kits/daily.txt     ← the ~10 names
  kits/research.txt
  .cursor/mcp.json   ← the long list lives here, not in the novel
```

Lift later, not wholesale: Goodreads, author engines, writing-guides if they still run, character-MCP *template*. Leave Core_5 agents, HANK, SmartWrite, and stale READMEs in the quarry.

---

## Critical vs skip

| Thing | Fresh start |
| --- | --- |
| Private MFA skill (`~/.cursor/skills/`) | Keep |
| User rule `fiction-writing-mfa` | Keep |
| One this-book canon rule | Keep |
| Novel pack / project-hub | Keep |
| Short mcp.json + Customize toggles | Keep (~10 on) |
| Git + GitHub (simple, no hooks required) | Keep |
| 56 slash commands | Skip |
| Tutorial rules (XML, few-shot, CoT) | Skip |
| Git hooks / autopilot.json | Skip |
| cspell.json | Optional later |
| Session summary | On request only → `Session_Summaries/` |
| zz_COMPASS tree | Quarry. Do not copy the tree |

---

## Move, then delete

1. Agree the names (Writing Tools + one workspace per novel).
2. Create empty `writing-tools` repo. Do not copy zz_COMPASS yet.
3. New Walk This Way workspace: this book + Writing Tools. Old repo stays.
4. Lift only proven servers. Test a chapter in Draft_06.
5. Point Senseless at the same Writing Tools folder.
6. When you can edit without hunting: hide zz_COMPASS, then later delete quarry.

No folders were created or deleted when this chart was written. 22 Aug 2026.
