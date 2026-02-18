# ACE Learn — Session Capture
**Session:** 2026-02-10 (final pre-reconfig: ACE wording, launchctl fix, printable steps, push)  
**AI-Trail:** MCP:44 Shell:440 Edits:155 Responses:124. Git: main (ee77046)

---

## ace_learn payload (use with ace_learn MCP in Cursor)

```json
{
  "task": "Final pre-reconfig: fix ACE payload wording, add launchctl fix doc, create printable reconfig outline, final git push",
  "trajectory": [
    "Clarified session capture headings: changed 'run when ACE MCP is available' to 'use with ace_learn MCP in Cursor' in all three .cursor/ace/session_capture_*.md files so user knows payload is ready to use with connected ACE",
    "Created FIX_LAUNCHCTL_NIGHTLY_CHAT_EXPORT.md: exact copy-paste commands (correct 'Walk This Way' path), unload-then-load, check step; note for different project path on other Mac",
    "Created MAC_STUDIO_RECONFIG_STEPS_PRINT_THIS.md: Part A (before, with 'already done' checks), Part B (do reconfig), Part C (after: open project, git pull, ACE, nightly, COMPASS); checkboxes and quick-reference table",
    "Linked ACE_AND_NIGHTLY_TROUBLESHOOTING quick-reference to FIX_LAUNCHCTL doc",
    "Git add, commit 'Pre-reconfig final: ACE wording fix, launchctl fix doc, printable reconfig steps, troubleshooting link', push origin main (ee77046)"
  ],
  "output": "User can: (1) use ace_learn with session payloads without confusion; (2) fix Load failed 5 on any Mac via FIX_LAUNCHCTL doc; (3) print MAC_STUDIO_RECONFIG_STEPS_PRINT_THIS.md and follow Parts A–C. Pattern: before 'go to bed' / major transition, deliver one printable checklist and one focused fix doc; standardize ACE payload heading across captures.",
  "success": true
}
```

---

## Patterns to reuse

- **ACE payload docs:** Use heading 'use with ace_learn MCP in Cursor' (not 'run when available') so it's clear the payload is for immediate use when ACE is connected.
- **Pre-transition handoff:** One printable numbered outline (checkboxes) + one targeted fix doc (exact commands) + final git push so user can proceed without reopening the chat.
