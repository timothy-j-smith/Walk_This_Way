# HOW AGENTS KNOW TO USE JSON PROMPTS

**Understanding the Connection Between Agents and the Prompt Library**

---

## 🔗 THE CONNECTION MECHANISM

### **How Agents Know About JSON Prompts:**

1. **Agent Definition References prompts.json:**
   - Agent JSON includes `.cursor/prompts.json` in `contextFiles` array
   - Agent JSON includes `.cursor/prompts.json` in `filesIUse` array
   - This tells the agent WHERE to find the prompts

2. **Agent System Prompt Instructs About Prompts:**
   - Agent's `systemPrompt` mentions "JSON Prompts Library"
   - Lists specific prompts (@scene_creation, @pov_conversion, etc.)
   - Tells agent it CAN and SHOULD use these prompts

3. **Agent Reads prompts.json:**
   - When agent loads, it should read `.cursor/prompts.json`
   - This gives agent the actual prompt definitions
   - Agent now knows WHAT each prompt does

4. **Agent Uses Prompts When Appropriate:**
   - When you mention `@scene_creation`, agent knows what to do
   - Agent can also suggest prompts when appropriate
   - Agent applies the prompt technique to your text

---

## 📋 CURRENT SETUP

### **In Agent JSON Files:**

**contextFiles Array:**
```json
"contextFiles": [
  ".cursor/agents/Agent.json",
  ".cursor/prompts.json",  ← Agent knows where prompts are
  "Test_Draft_Copy/",
  ...
]
```

**filesIUse Array:**
```json
"filesIUse": [
  ".cursor/prompts.json (JSON prompts library)",  ← Explicit reference
  ...
]
```

**System Prompt:**
```json
"systemPrompt": "...You deploy Smart Rewrites, JSON Prompts, DNA Memory integration...\n\nYour tools:\n- JSON Prompts Library (@scene_creation, @pov_conversion, @inner_dialogue, etc.)..."
```

---

## ⚠️ THE GAP: AGENTS NEED TO ACTUALLY READ prompts.json

### **Current Situation:**
- ✅ Agents KNOW prompts.json exists (via contextFiles)
- ✅ Agents KNOW they should use prompts (via systemPrompt)
- ⚠️ Agents may NOT automatically read prompts.json on load

### **Solution: Explicit Instruction**

**Option 1: Tell Agent to Read It:**
```
@.cursor/prompts.json
What JSON prompts are available and how do I use them?
```

**Option 2: Include in Agent's Initial Load:**
Add to agent's system prompt:
```
"Read .cursor/prompts.json to see available JSON prompts. When user mentions @prompt_name, use the corresponding prompt definition from prompts.json."
```

**Option 3: Use @ Mention:**
When you want to use a prompt:
```
@.cursor/prompts.json
@scene_creation [your outline here]
```

---

## 🎯 HOW IT ACTUALLY WORKS

### **The Reality (From Your Breakthrough Session):**

> "Prompts are techniques the agent uses, not computer commands"

**What This Means:**
1. `@scene_creation` is NOT a computer command
2. It's a TECHNIQUE the agent knows how to apply
3. The agent reads prompts.json to understand the technique
4. The agent applies the technique to your text

### **Example Flow:**

```
YOU: @scene_creation Nick walks into Jackie's house for the first time

AGENT: [Reads prompts.json, sees scene_creation definition]
       [Applies technique: "Transform outlines into complete scenes 
        with rich sensory details, authentic dialogue, and emotional depth"]
       [Generates scene using that technique]
```

---

## 🔧 ENSURING AGENTS USE PROMPTS

### **Method 1: Explicit @ Mention (Most Reliable)**
```
@.cursor/prompts.json
@scene_creation [your outline]
```

### **Method 2: Ask Agent to Use Prompt**
```
Use @scene_creation to transform this outline into a complete scene:
[your outline]
```

### **Method 3: Agent Suggests Prompt**
```
This passage needs work. What should I do?

AGENT: "This needs @scene_creation for sensory details. 
        Let me apply it. Here are 3 options..."
```

---

## 📝 CURRENT prompts.json STRUCTURE

```json
{
  "prompts": {
    "scene_creation": "Take this outline and build a complete scene...",
    "pov_conversion": "Convert this passage to 3rd person omniscient...",
    "inner_dialogue": "Enhance the inner dialogue to show character thoughts...",
    ...
  }
}
```

**Key Points:**
- Prompts are stored as key-value pairs
- Key = prompt name (e.g., "scene_creation")
- Value = prompt definition/instructions
- Agent reads this to understand what each prompt does

---

## ✅ VERIFICATION: DOES AGENT KNOW PROMPTS?

### **Test Question:**
```
What JSON prompts are available? How do I use @scene_creation?
```

### **Good Response:**
- Lists available prompts from prompts.json
- Explains what @scene_creation does
- Shows how to use it

### **Bad Response:**
- Doesn't know about prompts
- Generic response
- ❌ Agent hasn't read prompts.json

---

## 🚀 RECOMMENDED WORKFLOW

### **For Maximum Reliability:**

1. **Start Chat with Agent:**
   ```
   @.cursor/agents/CREATIVE_COLLABORATOR.json
   ```

2. **Explicitly Load Prompts:**
   ```
   @.cursor/prompts.json
   What prompts are available?
   ```

3. **Use Prompt:**
   ```
   @scene_creation [your outline]
   ```

### **Or Combine:**
```
@.cursor/agents/CREATIVE_COLLABORATOR.json
@.cursor/prompts.json
Use @scene_creation to transform this outline: [your outline]
```

---

## 🔍 THE TECHNICAL TRUTH

### **How Cursor Actually Works:**

1. **@ Mentions = File References:**
   - `@.cursor/prompts.json` = "Read this file"
   - Agent gets file content in context

2. **Prompt Names = Techniques:**
   - `@scene_creation` = "Use the scene_creation technique"
   - Agent looks up technique in prompts.json

3. **Agent Applies Technique:**
   - Agent reads prompt definition
   - Agent applies technique to your text
   - Agent generates result

### **The Key Insight:**
**Agents don't automatically execute prompts - they APPLY prompt techniques when you reference them or when appropriate.**

---

## 📋 SUMMARY

**How Agents Know About JSON Prompts:**

1. ✅ **Agent Definition** - References `.cursor/prompts.json` in contextFiles
2. ✅ **System Prompt** - Tells agent about JSON Prompts Library
3. ⚠️ **Agent Must Read** - Agent needs to actually read prompts.json (via @ mention or explicit instruction)
4. ✅ **Agent Uses** - Agent applies prompt techniques when you reference them

**To Ensure It Works:**
- Use `@.cursor/prompts.json` to explicitly load prompts
- Or ask agent: "What JSON prompts are available?"
- Then use: `@scene_creation [your text]`

**The Connection:**
- Agent JSON → References prompts.json
- Agent System Prompt → Mentions JSON Prompts
- You → Use @ mention to load prompts
- Agent → Applies prompt techniques

---

**Last Updated:** November 1, 2025
**Key Insight:** Prompts are techniques, not commands. Agents need to read prompts.json to know the techniques.

