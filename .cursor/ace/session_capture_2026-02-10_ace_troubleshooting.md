# ACE Learn — Session Capture
**Session:** 2026-02-10 (ACE setup, troubleshooting from screenshots, COMPASS test guidance)  
**AI-Trail:** MCP:44 Shell:437 Edits:148 Responses:122. Git: main (f446de1)

---

## ace_learn payload (use with ace_learn MCP in Cursor)

```json
{
  "task": "ACE and nightly troubleshooting from user screenshots; clarify MacBook Air Terminal steps; add COMPASS evaluation steps after reconfig",
  "trajectory": [
    "Clarified CHAT_EXPORT_NIGHTLY_1AM.md: user does not type ~/Library/LaunchAgents alone; copy-paste Command 1 then Command 2 in Terminal; explained copy = plist from project into LaunchAgents folder",
    "Answered ACE MCP 'Error' / 'No server info found': Cursor panel expects server metadata ACE extension doesn't send; if ACE dashboard shows VERY ACTIVE and bullets updating, ignore Cursor error",
    "Answered npm '74 packages looking for funding': not an error; install succeeded; optional funding message",
    "Recommended post-reconfig COMPASS testing: HANK + /compass-status + zz_COMPASS/.../TEST_QUESTIONS.md; added Section 7 and table row to AFTER_RECONFIG_RESURRECTION.md",
    "User shared screenshots: analyzed MCP errors, ACE dashboard (161 bullets, VERY ACTIVE), ACE Devices (2 of 2 used), launchctl Load failed 5, npm message",
    "Created ACE_AND_NIGHTLY_TROUBLESHOOTING.md: No server info (ignore if dashboard active), git repo/config errors (open project root, add ACE config if required), device limit 2/2 (remove device after reconfig to log in again), launchctl failure (fix path in plist or copy command e.g. 'Walk This Way' not 'Walk ay'), npm funding (ignore)"
  ],
  "output": "CHAT_EXPORT_NIGHTLY_1AM.md step-by-step clarity. AFTER_RECONFIG section 7: Test COMPASS with HANK, /compass-status, TEST_QUESTIONS.md. ACE_AND_NIGHTLY_TROUBLESHOOTING.md documents all screenshot-derived issues and fixes. Pattern: when user reports MCP/ACE errors, distinguish dashboard health (ACE cloud) vs Cursor MCP panel vs device limit vs config/path; device limit on free plan requires removing a device before logging in from reconfigured Mac.",
  "success": true
}
```

---

## Patterns to reuse

- **Terminal instructions:** Avoid 'copy to ~/path'; give exact copy-paste commands and say 'paste this whole line, press Enter'. Explain what each command does (e.g. 'copies the plist from project into LaunchAgents').
- **ACE vs Cursor MCP:** ACE extension can work (dashboard active, bullets) while Cursor Tools & MCP shows Error / No server info — Cursor expects server metadata. Ignore panel error if ACE features work.
- **ACE device limit:** Free plan = 2 devices. After reconfig, remove old device in ACE → Devices so new login succeeds; document in troubleshooting.
- **launchctl load failure (5):** Often wrong path in plist or typo in cp (e.g. 'Walk ay'). Verify full path 'Walk This Way'; unload then load after fix.
- **Screenshot troubleshooting:** Create a single doc that maps each visible error to cause and action; include quick-reference table.
