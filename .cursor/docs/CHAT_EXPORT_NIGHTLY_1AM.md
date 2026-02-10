# Chat backup nightly at 1 AM (Mac Studio and MacBook Air)

Chat export runs automatically every night at **1:00 AM** on whichever machine you install it on. Install once on **Mac Studio** and once on **MacBook Air** so both machines back up their chats into the same Walk This Way project (iCloud).

---

## One-time setup (do this on each Mac)

**You don’t type `~/Library/LaunchAgents` by itself** — that’s just the folder on your Mac where the job file will live. Do this instead:

1. Open **Terminal** (Spotlight: type `Terminal` and press Enter).
2. **Copy-paste the first command below** into Terminal, press **Enter**.
3. **Copy-paste the second command**, press **Enter**.

That’s it. The first command **copies** the schedule file (plist) from your Walk This Way project into macOS’s `LaunchAgents` folder. The second command **tells macOS to run it** every night at 1 AM.

---

### Command 1 — Copy the plist into LaunchAgents

Paste this whole line into Terminal and press Enter:

```bash
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/scripts/chat-export-nightly.plist" ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

(If the project is somewhere else on that Mac, the path in quotes may need to be different; you can check in Finder where “Walk This Way” lives inside iCloud Drive.)

---

### Command 2 — Load the job

Paste this and press Enter:

```bash
launchctl load ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

### Command 3 — Check it’s loaded (optional)

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
