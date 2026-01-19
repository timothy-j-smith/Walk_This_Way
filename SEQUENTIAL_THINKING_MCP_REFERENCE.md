# Sequential Thinking MCP Server - Reference Guide

**Status:** ✅ Enabled in your project  
**Purpose:** Structured, step-by-step problem-solving for complex creative and analytical tasks

---

## 🎯 What It Does

The Sequential Thinking MCP Server helps you break down complex problems into manageable steps through a structured thinking process. It's like having a thinking partner that helps you organize your thoughts systematically.

---

## 🔑 Key Features

### 1. **Structured Problem-Solving**
Organizes thoughts through standard cognitive stages:
- **Problem Definition**: Clearly define what you're trying to solve
- **Research**: Gather relevant information
- **Analysis**: Break down and examine the components
- **Synthesis**: Combine insights into solutions
- **Conclusion**: Reach actionable decisions

### 2. **Thought Tracking**
- Records sequential thoughts with metadata
- Maintains clear progression of ideas
- Shows how you arrived at conclusions

### 3. **Branching and Revision**
- Explore alternative lines of thought
- Revise previous steps as understanding deepens
- Keep track of different approaches

### 4. **Session Management**
- Create and manage thinking sessions
- Export sessions in Markdown, JSON, or plain text
- Review past problem-solving processes

---

## 📝 Practical Applications for Writing

### For Your Novel ("Walk This Way")

#### **Plot Development**
```
"Help me think through the character arc for Jackie in Chapter 25"
"Break down the problem of balancing disco authenticity with modern appeal"
```

#### **Scene Construction**
```
"Walk me through the steps of revising the disco club scene"
"Help me analyze why this dialogue feels flat"
```

#### **Character Development**
```
"Let's work through Jackie's internal conflict systematically"
"Help me define the relationship dynamics between these characters"
```

#### **Story Structure**
```
"Break down how to restructure Act II for better pacing"
"Think through the consequences of moving this plot point earlier"
```

#### **Research Planning**
```
"Help me organize my research approach for 1979 disco culture"
"Structure my fact-checking process for historical accuracy"
```

---

## 🚀 How to Use It

### Starting a Thinking Session

Simply ask Claude to help you think through something:

**Examples:**
- "I need to think through how to introduce a new character in Chapter 12"
- "Help me work through the logic of this plot twist"
- "Let's analyze why this scene isn't working"
- "Walk me through planning the next three chapters"

### During the Session

The server will help you:
1. **Define** the problem clearly
2. **Explore** relevant context and constraints
3. **Analyze** different aspects systematically
4. **Generate** potential solutions or approaches
5. **Evaluate** options and trade-offs
6. **Conclude** with actionable next steps

### Advanced Usage

**Branch into alternatives:**
- "Let's explore a different approach to this problem"
- "What if we consider this from another angle?"

**Revise earlier thinking:**
- "I need to reconsider that second step"
- "Let's revisit the problem definition with new information"

**Export your thinking:**
- "Can you show me our full thinking process as Markdown?"
- "Export this session so I can review it later"

---

## 💡 Example Workflow

### Problem: "Chapter 25 feels rushed"

**Step 1: Problem Definition**
```
User: "Help me think through why Chapter 25 feels rushed"

Sequential Thinking will help you clearly define:
- What specifically feels rushed?
- What should the pacing feel like?
- What are the constraints?
```

**Step 2: Research/Analysis**
```
Sequential Thinking helps you examine:
- Current scene count and length
- Key moments that need space to breathe
- Pacing compared to similar chapters
- Reader experience expectations
```

**Step 3: Synthesis**
```
Combines insights:
- Not enough sensory detail in the disco scene
- Character reactions compressed
- Missing transition between emotional beats
```

**Step 4: Conclusion**
```
Actionable decisions:
- Add 500 words of sensory detail in the club
- Create a separate scene for the confrontation
- Insert a quiet moment before the climax
```

---

## 🎯 Best Practices

### When to Use Sequential Thinking

✅ **Good for:**
- Complex plot problems
- Character arc planning
- Scene restructuring decisions
- Multi-chapter story planning
- Thematic development
- Resolving plot holes
- Balancing multiple storylines

❌ **Not needed for:**
- Simple questions with clear answers
- Quick fact checks
- Minor word choice decisions
- Routine editing tasks

### Tips for Best Results

1. **Be specific**: "Help me think through Jackie's motivation in Scene 3" is better than "Help me with Jackie"

2. **Let it guide you**: Trust the structured process even if it seems slow at first

3. **Don't skip steps**: The value is in working through each stage methodically

4. **Use for tough decisions**: Save it for problems where you're genuinely stuck

5. **Export important sessions**: Keep records of major story decisions

---

## 🔄 Integration with Your Workflow

### Pair With COMPASS Agents

**Example Flow:**
1. Use **Sequential Thinking** to analyze a problem
2. Use **STRATEGIC_WRITING_COORDINATOR** to plan execution
3. Use **PROSE_POLISH_EXPERT** to implement the solution

### Pair With Research

**Enable together:**
```json
"sequential-thinking": { "disabled": false },
"duckduckgo-search": { "disabled": false }
```

**Then ask:**
"Let's research 1979 disco fashion and think through how to incorporate it authentically"

---

## 🧪 Test Commands

Try these to see Sequential Thinking in action:

```
"Help me think through the structure of Act III"

"I'm stuck on how to reveal the secret about Hank's past. Let's work through this systematically."

"Walk me through analyzing whether this plot twist works"

"Help me make a decision about splitting Chapter 15 into two chapters"
```

---

## ⚙️ Technical Details

**Server Type:** NPX-based (no installation required)  
**Command:** `npx -y @modelcontextprotocol/server-sequential-thinking`  
**Network:** No network access required  
**Performance:** Lightweight, minimal overhead

**Configuration in `.cursor/config/mcp.json`:**
```json
"sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
  "disabled": false
}
```

---

## 📚 Learn More

- **GitHub Repository:** [github.com/arben-adm/mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)
- **Model Context Protocol:** [modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## 🎉 You're Ready

Sequential Thinking MCP is now active in your project. Just start a conversation and ask for help thinking through complex problems. The structured approach will help you work through difficult creative and analytical challenges systematically.

**Remember:** After enabling, you need to **restart Cursor** for the server to become active!

---

**Last Updated:** January 12, 2026,  
**Your Configuration:** Enabled alongside `walk-this-way-files`
