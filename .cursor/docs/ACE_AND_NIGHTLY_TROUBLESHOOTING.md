# ACE & Nightly Chat Export — Troubleshooting

**From your screenshots (Feb 9–10, 2026).** Use this when something doesn’t work.

---

## 1. Cursor “Tools & MCP”: extension-ace-pattern-learning shows “Error” / “No server info found”

**What you see:** Red dot next to `extension-ace-pattern-learning`, log says `No server info found`.

**What it means:** Cursor’s MCP panel expects “server info” from the ACE extension. The extension doesn’t always send that in the format Cursor wants, so the panel shows an error even when ACE is working.

**What to do:** If your **ACE dashboard** (ace-ai.app) shows your project as “VERY ACTIVE” and bullets are updating, ACE is working. You can ignore the Cursor MCP error for ACE. If `ace_learn` or other ACE features actually fail, see the config errors below.

---

## 2. ACE MCP log: “not a git repository” / “Failed to load configuration: missing required fields”

**What you see:** When Cursor starts the ACE MCP (`npx @ace-sdk/mcp`), the log shows:
- `fatal: not a git repository (or any of the parent directories): .git`
- `Failed to load configuration: missing required fields`

**What it means:** The ACE MCP is being run from a directory that isn’t your Walk This Way project (or doesn’t have a `.git` folder), or an ACE config file is missing.

**What to do:**
- Always **open the Walk This Way folder** (the project root that has `.git`) in Cursor before relying on ACE MCP. The MCP runs in the workspace context.
- If ACE’s docs mention a config file (e.g. `.ace/config` or similar), add it in the project root. Check ACE documentation for “required fields.”

---

## 3. ACE “My Devices”: “2 of 2 devices used” / “Remove a device to log in from new devices”

**What you see:** On the ACE website under **Devices**, it says 2 of 2 devices used and warns you to remove one to log in from a new device.

**What it means:** On the **free plan**, ACE only allows 2 devices. Your Mac Studio and MacBook Air are probably those two. After a **Mac Studio reconfig**, the Studio might be treated as a **new** device; ACE could block login until you remove an old device.

**What to do:**
- When you reconfig the Mac Studio, if ACE says you can’t log in: go to **ACE → Devices**, remove the old “Mac Studio” (or the device you’re not using), then log in again from the reconfigured Studio.
- You can remove a device with the trash icon; you can log back in on that machine later (it will count as one of the two again).

---

## 4. Terminal: `launchctl load` → “Load failed: 5: Input/output error”

**What you see:** You ran the two commands for the nightly chat export. The **copy** might have worked, but **`launchctl load ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist`** failed with “Load failed: 5: Input/output error”.

**What it means:** Often caused by (a) the **path inside the plist** pointing to a folder that doesn’t exist on this Mac (e.g. project not at the same path), or (b) a typo in the **copy** command so the plist wasn’t actually copied (e.g. “Walk ay” instead of “Walk This Way”).

**What to do:**
1. Check that you’re on the Mac where the project lives (e.g. same path under iCloud). If the project path is different (e.g. on MacBook Air), edit the plist: change the script path and the log path to the correct path on that Mac, then run the copy and load again.
2. When you run the **copy** command, make sure the path has **“Walk This Way”** with a space and capital T and W — no “Walk ay”.
3. After fixing, run:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
   launchctl load ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
   ```
4. Check: `launchctl list | grep walkthisway` — you should see the job listed (second column not “-” if it’s loaded).

---

## 5. “74 packages are looking for funding” in Terminal

**What you see:** After `npm install @ace-sdk/mcp`, npm prints “74 packages are looking for funding” and “run \`npm fund\` for details”.

**What it means:** Not an error. The install succeeded. npm is just saying 74 of the installed packages have funding links; `npm fund` is optional.

**What to do:** Nothing. You can ignore it or run `npm fund` if you want to see the list.

---

**Quick reference**

| Issue | Action |
|-------|--------|
| ACE MCP “Error” in Cursor | Ignore if ACE dashboard is active and bullets update. |
| “not a git repository” / “missing required fields” | Open Walk This Way (project root) in Cursor; add any ACE config the docs require. |
| “2 of 2 devices used” | Remove an old device in ACE → Devices so you can log in after reconfig. |
| `launchctl load` failed | See **FIX_LAUNCHCTL_NIGHTLY_CHAT_EXPORT.md** for exact steps. |
| “74 packages looking for funding” | Ignore; install succeeded. |
