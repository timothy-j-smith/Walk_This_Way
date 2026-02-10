# Export Chats
**Command:** `/export-chats` or say **"Export my chats"**

**Action:** Run the chat export script so all Cursor chats from this machine are saved as markdown files in the project (iCloud). New chats are added; already-exported chats are skipped.

**Command to run (Terminal):**
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/.cursor/docs/Chat_History" && ./EXPORT_ALL_CHATS.sh
```

**When to use:**
- Before Mac Studio reconfig (to capture Mac Studio chats).
- After a long session on MacBook Air (run on Air to capture Air chats).
- Whenever you want a permanent, date-organized copy of your Cursor chats.

**Output:** Markdown files in `.cursor/docs/Chat_History/HANK/` and `Other/` (date-first naming). They sync to iCloud and can be committed to Git.

---

**Status:** Ready to use. In chat you can say "Export my chats" and the agent can run this for you.
