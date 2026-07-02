# Mac Studio Reconfig — Steps (Print This)

**Walk This Way • February 2026**

---

## PART A: BEFORE RECONFIG (already done if you did the pre-reconfig session)

- [ ] **1.** Export chats (in Cursor say “Export my chats” or run `EXPORT_ALL_CHATS.sh` from `.cursor/docs/Chat_History`) — *Done in session*
- [ ] **2.** Desktop folders saved into `.cursor/docs/Desktop_Archive_PreReconfig_2026` — *Done in session*
- [ ] **3.** Git push: from project root run `git add -A`, `git commit -m "Pre-reconfig snapshot"`, `git push origin main` — *Done in session*

---

## PART B: DO THE MAC STUDIO RECONFIG

- [ ] **4.** Back up anything else you need (e.g. 2TB copy of Desktop archive if you want).
- [ ] **5.** Run macOS recovery / erase and reinstall (or your chosen reconfig method).
- [ ] **6.** Set up the Mac (Apple ID, iCloud, user account, etc.) so iCloud Drive is available.
- [ ] **7.** Install Cursor from [cursor.com](https://cursor.com) if it’s not restored by your setup.

---

## PART C: AFTER RECONFIG — RESURRECT WALK THIS WAY

- [ ] **8.** Open the project: **File → Open Folder** → go to **iCloud Drive → Cursor → 03_Novels → Walk This Way** (or `~/Library/Mobile Documents/.../Walk This Way`).
- [ ] **9.** Git pull: open Terminal, run  
  `cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"`  
  then  
  `git pull origin main`  
  (Use personal GitHub account and token if prompted.)
- [ ] **10.** Nightly chat export (optional): run the two commands from **`.cursor/docs/CHAT_EXPORT_NIGHTLY_1AM.md`** (Command 1 = copy plist, Command 2 = launchctl load).  
  *If you get “Load failed: 5”, use **`.cursor/docs/FIX_LAUNCHCTL_NIGHTLY_CHAT_EXPORT.md`** and run the exact copy-paste commands there.*
- [ ] **11.** Test COMPASS (optional): in Cursor Chat run **`/compass-status`**, then open a chat with **HANK** and use **`zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/TEST_QUESTIONS.md`** to run tests.

---

## Quick reference

| Step | Action |
|------|--------|
| Open project | File → Open Folder → iCloud … Walk This Way |
| Git pull | `cd "...Walk This Way"` then `git pull origin main` |
| Nightly export fix | See FIX_LAUNCHCTL_NIGHTLY_CHAT_EXPORT.md |
| Full “after” guide | AFTER_RECONFIG_RESURRECTION.md |

---

**You’re not starting over — you’re opening the same workspace from iCloud.**
