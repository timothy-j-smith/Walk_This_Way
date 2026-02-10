# ACE Learn — Session Capture
**Session:** 2026-02-10 (pre–Mac Studio reconfig: execution — chat backup, Desktop copy, nightly job, push)  
**AI-Trail:** MCP:44 Shell:437 Edits:136 Responses:120. Git: main (f446de1)

---

## ace_learn payload (use with ace_learn MCP in Cursor)

```json
{
  "task": "Execute pre-reconfig: run chat backup, copy all 10 Desktop folders into project, set up nightly 1 AM chat export, push to GitHub",
  "trajectory": [
    "Clarified 'A files': old name (A_FILES/Cursor_Claude) from earlier plan; not on current Desktop; current Desktop has 10 differently named folders",
    "Ran EXPORT_ALL_CHATS.sh — 36 chats already exported (up to date)",
    "Copied all Desktop folders automatically: for d in ~/Desktop/*/; do cp -R into .cursor/docs/Desktop_Archive_PreReconfig_2026/",
    "Updated Desktop archive README: listed 10 folder names, explained A files, noted copied Feb 9 2026",
    "Created chat-export-nightly.plist (StartCalendarInterval Hour=1 Minute=0), CHAT_EXPORT_NIGHTLY_1AM.md install instructions",
    "Installed launchd job on Mac Studio: cp plist to ~/Library/LaunchAgents, launchctl load",
    "Added .gitignore entry for nightly_export.log; git add, commit, push to origin main (f446de1)"
  ],
  "output": "Chat export current. All 10 Desktop folders in Desktop_Archive_PreReconfig_2026 (in repo). Nightly 1 AM export installed on Mac Studio; same plist + doc for MacBook Air when needed. One-command Desktop copy pattern: loop over ~/Desktop/*/ and cp -R into project archive. User ready to reconfig.",
  "success": true
}
```

---

## Patterns to reuse

- **Bulk Desktop save:** Copy all Desktop folders in one go: `for d in ~/Desktop/*/; do [ -d "$d" ] && cp -R "$d" "$ARCHIVE/"; done`. No manual Finder copy when agent has shell access.
- **Nightly chat export:** launchd plist with StartCalendarInterval (Hour=1, Minute=0); ProgramArguments run script with quoted path; install via cp to ~/Library/LaunchAgents + launchctl load. Document one-time setup per machine in project doc.
- **Legacy names:** When user asks 'What is X?' and X was from an older plan/screenshot, clarify it’s not in current state; list what *is* current (e.g. 10 folders) and proceed with that.
