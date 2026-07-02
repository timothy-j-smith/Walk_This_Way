# HOW TO EXPORT CHAT HISTORY FROM CURSOR
**Created:** January 21, 2026  
**Purpose:** Step-by-step guide for exporting chat transcripts

---

## 📋 EXPORT STEPS

### **Method 1: Using Cursor's Built-in Export**

1. **Open your chat in Cursor**
   - Make sure the chat panel is visible
   - Scroll to the conversation you want to export

2. **Look for Export Option:**
   - In the chat panel, look for:
     - Three dots menu (⋯)
     - Export button
     - Download icon
     - Right-click menu
   - Or check: Chat panel → Menu → Export

3. **Export the Transcript:**
   - Click export/download
   - Choose format (Markdown or Text)
   - Save the file

4. **Save to Organized Location:**
   - **HANK chats:** `.cursor/docs/Chat_History/HANK/`
   - **Other chats:** `.cursor/docs/Chat_History/Other/`
   - **Naming:** `YYYY-MM-DD_Topic_Description.md`

---

## 📁 WHERE TO SAVE

### **For HANK Chats:**
```
.cursor/docs/Chat_History/HANK/
├── 2026-01-21_COMPASS_Writing_Guides_MCP.md
├── 2026-01-10_COMPASS_Encyclopedia.md
└── 2025-11-29_Reorganization_Session.md
```

### **For Other Chats:**
```
.cursor/docs/Chat_History/Other/
├── 2026-01-20_Character_Development.md
└── 2026-01-15_Research_Session.md
```

---

## 🎯 WHEN TO EXPORT

**Export after:**
- ✅ Major sessions (new features, breakthroughs)
- ✅ Technical troubleshooting sessions
- ✅ Creative collaboration sessions
- ✅ DISCO moments
- ✅ Important decisions or learnings
- ✅ End of major work sessions

**Pro tip:** Export at natural break points (end of topics, end of sessions)

---

## 📝 FILE NAMING CONVENTION

**Format:**
```
YYYY-MM-DD_Topic_Key_Details.md
```

**Examples:**
- `2026-01-21_COMPASS_Writing_Guides_MCP.md`
- `2026-01-10_COMPASS_Encyclopedia_Creation.md`
- `2025-11-29_Reorganization_Session.md`
- `2026-01-20_Character_Development_Session.md`

---

## ✅ AFTER EXPORTING

1. **Move file to correct location:**
   - HANK chats → `Chat_History/HANK/`
   - Other chats → `Chat_History/Other/`

2. **Commit to Git:**
   ```bash
   git add .cursor/docs/Chat_History/
   git commit -m "Export chat: [Topic] - [Date]"
   git push
   ```

3. **Update BREAKTHROUGH_LOG.md:**
   - If it was a DISCO moment, add it to the log!

---

## 💡 TIPS

- **Export regularly** - Don't wait until you have months of chat
- **Name descriptively** - Future you will thank you
- **Keep organized** - Separate HANK from other chats
- **Commit to Git** - Permanent backup

---

## 🚨 IF EXPORT DOESN'T WORK

**Alternative Method:**
1. Select all text in chat (Cmd+A)
2. Copy (Cmd+C)
3. Paste into new markdown file
4. Save with proper naming
5. Move to correct location

**Note:** This method may not preserve formatting perfectly, but captures the content.

---

**Remember:** The `state.vscdb` backup is for restoration after clean install. The exported markdown files are for reading and reference!
