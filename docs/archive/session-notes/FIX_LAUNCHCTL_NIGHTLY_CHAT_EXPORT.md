# Fix: launchctl load → "Load failed: 5: Input/output error"

Use this on the Mac where the nightly chat export failed to load (e.g. MacBook Air, or after a typo in the copy command).

---

## Why it fails

- The **copy** command had a typo (e.g. "Walk ay" instead of **"Walk This Way"**), so the plist never made it to `~/Library/LaunchAgents`, or
- The plist was copied but the **path inside the plist** doesn’t exist on this Mac (e.g. different project location).

---

## Fix (run in Terminal on that Mac)

**1. Copy the plist — use this exact line (includes "Walk This Way" with a space and capital T and W):**

```bash
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/scripts/chat-export-nightly.plist" ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

**2. If you had tried to load before, unload first:**

```bash
launchctl unload ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

(If you see "Could not find specified service", that’s fine — it wasn’t loaded. Continue.)

**3. Load the job:**

```bash
launchctl load ~/Library/LaunchAgents/com.walkthisway.chat-export-nightly.plist
```

**4. Check it’s loaded:**

```bash
launchctl list | grep walkthisway
```

You should see a line like: `-	0	com.walkthisway.chat-export-nightly`

---

## If the project path is different on this Mac

If Walk This Way lives somewhere else (e.g. different iCloud path), edit the plist **before** copying:

- Open: `Walk This Way/.cursor/scripts/chat-export-nightly.plist`
- Replace every instance of  
  `/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way`  
  with the **full path** to Walk This Way on this Mac.
- Save, then run steps 1–4 above.

---

**Done.** The job will run at 1:00 AM every night on this Mac.
