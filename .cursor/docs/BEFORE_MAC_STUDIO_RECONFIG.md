# Before Mac Studio Reconfiguration — Checklist
**Created:** February 9, 2026  
**Purpose:** Minimal steps so you can safely reconfig and resurrect Walk This Way

---

## Your workspace is in good shape

- **Walk This Way** lives under **iCloud Drive** (`Mobile Documents/com~apple~CloudDocs/...`), so the **whole folder syncs**.
- **Git + GitHub** are set up (personal account, token with no expiration).
- **Chat export** is automated and fixed (script restores cursor-view if needed).

You don’t need hours to “fix” the file system before reconfig. Do the short checklist below, then reconfig. You can change any folder structure you don’t like **after** you’re back up.

---

## Before reconfig — do these

### 1. Export chats (so you don’t lose them)

**In Cursor:** You can say **"Export my chats"** and the agent will run it for you.

**Or in Terminal:**
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/docs/Chat_History" && ./EXPORT_ALL_CHATS.sh
```

- Exports **this machine’s** chats (Mac Studio) into the project. Run on MacBook Air when you use it to capture Air chats too.
- Chats are saved into this project (iCloud), so they’ll be there after reconfig.
- **Not automated** — you run it when you want; see `.cursor/docs/CHAT_EXPORT_AND_DESKTOP_SAVE_ANSWERS.md` for nightly option and MacBook Air details.

### 2. Save your Desktop folders

- You have **Cursor_Claude** and **A_FILES** (and maybe others) on your Mac Studio Desktop. The Desktop is not in iCloud by default, so they will be wiped on reconfig.
- **Copy** those folders into:  
  **Walk This Way → .cursor → docs → Desktop_Archive_PreReconfig_2026**  
  (There’s a README in that folder with exact steps.)
- **Optional but recommended:** Also copy the same folders to your 2TB external drive.

### 3. Push everything to GitHub

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
git add -A
git status
git commit -m "Pre-reconfig snapshot: Walk This Way workspace"
git push origin main
```

- Use GitKraken Pro if you prefer; same idea: **commit + push**.

### 4. (Optional) Note current top-level layout

If you want a reminder of how things were laid out:

- **Active_Draft_2** — Draft 2 chapters and materials  
- **Agent_Work** — Agent folders (HANK, CAROLINA, etc.)  
- **Chat_Summaries** — Chat summary JSONs  
- **DNA** — HANK_DNA, TIMOTHY_WORKING_STYLE_DNA  
- **Draft_1** — Draft 1 chapters  
- **Novel_Docs** — Novel-related docs  
- **Scene_Workshop** — Scene/chapter workshop files  
- **Session_Summaries** — Session summary markdown  
- **Story_Bible** — Character bible, timeline, etc.  
- **zz_COMPASS** — COMPASS system and MCPs  
- **.cursor** — Cursor config, rules, commands, Chat_History  

You can reorganize later; this is just for your memory.

---

## What *doesn’t* sync (and that’s OK)

- **Cursor app data** (e.g. `~/Library/Application Support/Cursor/`) does **not** sync.  
  After reconfig you’ll have a fresh Cursor; your **project files** are in iCloud + Git.
- **cursor-view** runs from `/tmp/cursor-view`; the export script can re-clone it when needed.

---

## Summary

1. **Export chats** (say "Export my chats" in Cursor or run the command above).  
2. **Save Desktop folders** (Cursor_Claude, A_FILES) into `.cursor/docs/Desktop_Archive_PreReconfig_2026` and optionally to 2TB.  
3. **Commit and push** to GitHub (or push in GitKraken).  
4. (Optional) Skim this doc and the “after reconfig” doc.  
5. Do your Mac Studio reconfig.  
6. Use **AFTER_RECONFIG_RESURRECTION.md** to open the project and get back to work.

**More detail:** See **CHAT_EXPORT_AND_DESKTOP_SAVE_ANSWERS.md** for: Is chat export nightly? MacBook Air vs Mac Studio chats? External 2TB? Easy "Export my chats" prompt.

Your 4 months of work are in **iCloud + GitHub**. Reorganization can be adjusted later.
