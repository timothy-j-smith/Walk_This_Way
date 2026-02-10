# Chat backup nightly at 1 AM (Mac Studio and MacBook Air)

Chat export runs automatically every night at **1:00 AM** on whichever machine you install it on. Install once on **Mac Studio** and once on **MacBook Air** so both machines back up their chats into the same Walk This Way project (iCloud).

---

## One-time setup (do this on each Mac)

### 1. Copy the plist into LaunchAgents

On **Mac Studio** (or **MacBook Air**), run in Terminal:

```bash
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/scripts/chat-export-nightly.plist" ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

(If the project lives somewhere else on that Mac, edit the plist after copying and fix the paths, then copy the edited plist.)

### 2. Load the job

```bash
launchctl load ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

### 3. Check it’s loaded (optional)

```bash
launchctl list | grep walkthisway
```

You should see `com.walkthisway.chat-export-nightly`.

---

## What it does

- Every night at **1:00 AM** it runs `EXPORT_ALL_CHATS.sh`.
- Exports **that machine’s** Cursor chats into `.cursor/docs/Chat_History/` (in the project).
- New chats get new files; already-exported chats are skipped.
- Log is written to `.cursor/docs/Chat_History/nightly_export.log`.

---

## After reconfig

Re-run the **one-time setup** on each Mac after you’ve restored the project and paths (e.g. from iCloud). The plist is in the repo, so you can copy it again from the project and load it.

---

## Turn it off

```bash
launchctl unload ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

You can delete the plist from `~/Library/LaunchAgents/` if you don’t want it anymore.
