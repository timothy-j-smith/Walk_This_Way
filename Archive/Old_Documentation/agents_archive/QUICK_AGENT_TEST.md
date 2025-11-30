# QUICK AGENT TEST - COPY/PASTE THIS

**30-Second Verification Test**

---

## 📋 TEST PROMPT (Copy/Paste This):

```
I want to verify you're set up correctly. Please tell me:

1. Your exact role and mission
2. The correct folder for current drafts (should be Test_Draft_Copy, NOT Working_Chapters)
3. The master theme of Walk This Way
4. Your process for working with me
5. Where you save your work
```

---

## ✅ WHAT TO LOOK FOR:

### **1. Role and Mission:**
- ✅ Should state specific role (e.g., "Strategic Writing Coordinator")
- ✅ Should mention mission or purpose
- ❌ Generic "I'm an AI assistant" = NOT WORKING

### **2. Correct Folder:**
- ✅ Should say "Test_Draft_Copy/" 
- ❌ "Working_Chapters/" = OUTDATED, NEEDS FIX

### **3. Master Theme:**
- ✅ Should say "Lost Innocence"
- ✅ Should mention core themes (Class Divide, Friendship, etc.)
- ❌ Doesn't know themes = NOT LOADING Agent.json

### **4. Process:**
- ✅ Should describe step-by-step process
- ✅ Should mention how it collaborates
- ❌ Generic process = NOT WORKING

### **5. Save Location:**
- ✅ Should mention "Agent_Work/[Agent_Name]/"
- ❌ Doesn't know where it saves = INCOMPLETE SETUP

---

## 🎯 PASS/FAIL CRITERIA:

**✅ PASS:** Agent answers all 5 correctly
**❌ FAIL:** Agent misses any question or gives generic responses

---

## 🔧 IF IT FAILS:

1. Check JSON file exists in `.cursor/agents/`
2. Verify JSON syntax is valid
3. Enable MCP in Custom Agent Settings
4. Restart Cursor
5. Try @ mention: `@.cursor/agents/[AGENT].json`

---

**Quick test = 30 seconds. If agent passes, you're good to go!**

