# ACE Learn — Session Capture
**Session:** 2026-01-22 (pre–Mac Studio reconfig: Desktop save + chat export)  
**AI-Trail:** MCP:44 Shell:430 Edits:129 Responses:118. Git: main (38407a5)

---

## ace_learn payload (run when ACE MCP is available)

```json
{
  "task": "Pre–Mac Studio reconfig: Desktop folder save, chat-export UX, and before-reconfig checklist updates",
  "trajectory": [
    "Clarified chat export: not automated; user runs it; 'Export my chats' in Cursor or run EXPORT_ALL_CHATS.sh",
    "Clarified MacBook Air vs Mac Studio: Cursor DB is per-machine; run export on each machine to get both into same project (iCloud)",
    "Created .cursor/docs/Desktop_Archive_PreReconfig_2026/ with README: copy Cursor_Claude and A_FILES from Desktop into this folder, then commit/push; optional copy to 2TB",
    "Added .cursor/commands/export-chats.md so user can say 'Export my chats' and agent runs the script",
    "Updated BEFORE_MAC_STUDIO_RECONFIG.md: step 2 = save Desktop folders into Desktop_Archive_PreReconfig_2026 (and optionally 2TB); renumbered summary 1–6; linked CHAT_EXPORT_AND_DESKTOP_SAVE_ANSWERS.md",
    "Recommended 2TB for Desktop folders and optional one-time full Walk This Way copy; iCloud + GitHub sufficient for writing"
  ],
  "output": "Desktop archive folder and README; export-chats command doc; BEFORE_MAC_STUDIO_RECONFIG.md updated with Desktop save step and summary. Pattern: pre-reconfig = export chats (this machine) → copy Desktop folders into project + optional 2TB → git add/commit/push. Chat export stays manual; 'Export my chats' is the UX. Run export on MacBook Air when used so Air chats land in same project.",
  "success": true
}
```

---

## Patterns to reuse

- **Pre-reconfig checklist:** (1) Export chats on current machine, (2) Save Desktop folders into a project archive folder (and optionally external drive), (3) Git commit and push. Desktop is not in iCloud by default, so it gets wiped on reconfig.
- **Chat export UX:** Document a single phrase ("Export my chats") and the script path so the agent can run it on request; keep date-first naming for chat files.
- **Multi-machine:** Cursor chat DB is per machine; export on each machine to consolidate into one project (iCloud) and commit.
