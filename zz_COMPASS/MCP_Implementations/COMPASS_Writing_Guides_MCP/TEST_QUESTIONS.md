# COMPASS Writing Guides MCP - Test Questions

**Purpose:** Comprehensive test queries to verify all MCP functionality

---

## 🎯 Basic Functionality Tests

### Author Advice Queries

**Test 1: Get author advice (simple)**
```
Use compass-writing-guides MCP to get Stephen King's advice
```

**Test 2: Get author advice with topic filter**
```
Use compass-writing-guides MCP to get Stephen King's advice on adverbs
```

**Test 3: Get advice from multiple authors**
```
Use compass-writing-guides MCP to get Ernest Hemingway's advice, then Raymond Carver's advice
```

**Test 4: List all authors**
```
Use compass-writing-guides MCP to list all available authors
```

---

## 📚 Topic Guidance Tests

**Test 5: Get topic guidance (simple)**
```
Use compass-writing-guides MCP to get guidance on dialogue
```

**Test 6: Get multiple topics**
```
Use compass-writing-guides MCP to get guidance on pacing and character development
```

**Test 7: List all topics**
```
Use compass-writing-guides MCP to list all available topics
```

**Test 8: Get the new voice development topic**
```
Use compass-writing-guides MCP to get guidance on developing_your_voice
```

---

## 🎨 Author Style Guide Tests

**Test 9: Get complete author style guide**
```
Use compass-writing-guides MCP to get Stephen King's style guide
```

**Test 10: Get style guides for comparison**
```
Use compass-writing-guides MCP to get Richard Russo's style guide and Dennis Lehane's style guide
```

**Test 11: Get Hemingway and Carver styles (new additions)**
```
Use compass-writing-guides MCP to get Ernest Hemingway's style guide
```

```
Use compass-writing-guides MCP to get Raymond Carver's style guide
```

---

## 💡 Quote Tests

**Test 12: Get quotes by author**
```
Use compass-writing-guides MCP to get quotes from Stephen King
```

**Test 13: Search quotes by keyword**
```
Use compass-writing-guides MCP to get quotes about revision
```

**Test 14: Get quotes from new authors**
```
Use compass-writing-guides MCP to get quotes from Ernest Hemingway
```

```
Use compass-writing-guides MCP to get quotes from Raymond Carver
```

---

## 🔧 Technique Tests

**Test 15: Get writing techniques**
```
Use compass-writing-guides MCP to get dialogue techniques
```

**Test 16: Get multiple technique types**
```
Use compass-writing-guides MCP to get pacing techniques and prose techniques
```

---

## 📖 Genre Guidance Tests

**Test 17: Get genre guidance**
```
Use compass-writing-guides MCP to get guidance for literary_fiction
```

**Test 18: Compare genres**
```
Use compass-writing-guides MCP to get guidance for crime_mystery and horror_supernatural
```

---

## 🔍 Search Tests

**Test 19: Search across all content**
```
Use compass-writing-guides MCP to search for advice on character motivation
```

**Test 20: Search for specific concepts**
```
Use compass-writing-guides MCP to search for iceberg theory
```

**Test 21: Search for methodology keywords**
```
Use compass-writing-guides MCP to search for scalpel hose
```

---

## 🎯 Methodology Tests

**Test 22: Get complete methodology**
```
Use compass-writing-guides MCP to get the Scalpel & Hose methodology
```

**Test 23: Get specific methodology section**
```
Use compass-writing-guides MCP to get the Scalpel & Hose process section
```

**Test 24: Get COMPASS tools methodology**
```
Use compass-writing-guides MCP to get the COMPASS advanced tools methodology
```

**Test 25: List all methodologies**
```
Use compass-writing-guides MCP to list all available methodologies
```

---

## 💬 Writing Tip Tests

**Test 26: Get random writing tip**
```
Use compass-writing-guides MCP to get a writing tip
```

**Test 27: Get tip by topic**
```
Use compass-writing-guides MCP to get a writing tip on dialogue
```

**Test 28: Get tip by author**
```
Use compass-writing-guides MCP to get a writing tip from Stephen King
```

---

## 🔥 Real-World Usage Scenarios

### Scenario 1: Before Writing Dialogue
```
Use compass-writing-guides MCP to get guidance on dialogue, then help me write authentic dialogue for this scene between Nick and Jackie.
```

### Scenario 2: Stuck on Pacing
```
Use compass-writing-guides MCP to get pacing techniques, then help me improve the pacing of this action scene.
```

### Scenario 3: Adopting an Author's Voice
```
Use compass-writing-guides MCP to get Richard Russo's style guide, then help me rewrite this scene with Russo's working-class empathy and community focus.
```

### Scenario 4: Editing with Scalpel & Hose
```
Use compass-writing-guides MCP to get the Scalpel & Hose methodology, then help me apply it to edit this chapter.
```

### Scenario 5: Developing Your Voice
```
Use compass-writing-guides MCP to get guidance on developing_your_voice, then help me understand how to learn from Stephen King while maintaining my own style.
```

### Scenario 6: Revision Guidance
```
Use compass-writing-guides MCP to get Stephen King's advice on adverbs, then help me identify and fix adverb overuse in this passage.
```

### Scenario 7: Multiple References
```
Use compass-writing-guides MCP to get Dennis Lehane's style guide and Stephen King's style guide. I want to combine Lehane's Boston grit with King's accessible prose for this scene.
```

### Scenario 8: Character Development
```
Use compass-writing-guides MCP to get guidance on character development, then help me deepen Maxanne's emotional journey in this chapter.
```

---

## ⚠️ Edge Case Tests

**Test 29: Non-existent author**
```
Use compass-writing-guides MCP to get advice from J.K. Rowling
```
*(Should return error with available authors list)*

**Test 30: Non-existent topic**
```
Use compass-writing-guides MCP to get guidance on worldbuilding
```
*(Should return error with available topics list)*

**Test 31: Topic with typo**
```
Use compass-writing-guides MCP to get guidance on dialouge
```
*(Should handle gracefully)*

**Test 32: Empty query**
```
Use compass-writing-guides MCP to search for ""
```
*(Should handle gracefully)*

---

## 🎯 Comprehensive Integration Test

**Test 33: Complete workflow example**
```
I'm writing a dialogue scene between two working-class characters. Use compass-writing-guides MCP to:
1. Get guidance on dialogue
2. Get Raymond Carver's advice on dialogue (he's great with working-class voices)
3. Get the Scalpel & Hose character depth hierarchy
4. Then help me write the scene applying all of this guidance.
```

---

## 📊 Success Criteria

Each test should:
- ✅ Return relevant, accurate information
- ✅ Handle errors gracefully with helpful messages
- ✅ Provide actionable guidance
- ✅ Integrate smoothly with writing workflow
- ✅ Return data in useful format (JSON that can be interpreted)

---

## 🚀 Recommended Testing Order

1. **Start Simple:** Tests 1-4 (basic author queries)
2. **Topics:** Tests 5-8 (topic guidance)
3. **Styles:** Tests 9-11 (author style guides)
4. **Quotes:** Tests 12-14 (quotes)
5. **Methodologies:** Tests 22-25 (your unique methodologies)
6. **Search:** Tests 19-21 (search functionality)
7. **Real Scenarios:** Scenarios 1-8 (actual usage)
8. **Edge Cases:** Tests 29-32 (error handling)

---

**Note:** After setup and Cursor restart, work through these tests systematically to verify all functionality works as expected.
