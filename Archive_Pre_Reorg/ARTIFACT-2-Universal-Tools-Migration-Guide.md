# ARTIFACT 2: UNIVERSAL TOOLS MIGRATION GUIDE
## Valuable Cursor Creations for Claude.ai & Sudowrite Integration

---

**Version:** 1.0  
**Created:** December 2024  
**Purpose:** Extract and adapt valuable Cursor tools for use with Claude.ai and Sudowrite  
**Target:** Seamless migration of creative writing assets

---

## 🎯 **EXECUTIVE SUMMARY**

Your Cursor Creative Writing System contains **incredibly valuable assets** that can be adapted for any AI writing tool. This guide systematically catalogs every transferable element with specific implementation instructions.

---

## 📋 **CATEGORY 1: CORE WRITING PHILOSOPHY**

### **1.1 Writing Values Framework**
**File Source:** `.cursorrules` (Lines 3-8)  
**Universal Value:** ⭐⭐⭐⭐⭐ (Critical for all AI tools)

```
## My Writing Values (Priority Order)
1. Emotional truth over plot mechanics
2. Character consistency over convenience  
3. Showing over telling
4. Specific detail over generic descriptions
5. Subtext over explicit statement
```

**Implementation for Claude.ai:**
```
System Prompt: "You are helping me write a novel. My core writing values are: 1) Emotional truth over plot mechanics, 2) Character consistency over convenience, 3) Showing over telling, 4) Specific detail over generic descriptions, 5) Subtext over explicit statement. Always prioritize these values in your suggestions."
```

**Implementation for Sudowrite:**
- Add to "Writing Style" section in Settings
- Use as reference when using "Rewrite" or "Expand" features
- Include in character development prompts

**Benefits:**
- Maintains your unique voice across all AI interactions
- Provides consistent quality standards
- Guides AI to focus on what matters most to you

---

### **1.2 Personal Weaknesses Analysis**
**File Source:** `.cursorrules` (Lines 10-13)  
**Universal Value:** ⭐⭐⭐⭐⭐ (Essential for improvement)

```
## My Weaknesses (Help Me With These)
- I overuse "was/were" constructions
- I tell emotions instead of showing
- I repeat sentence structure
```

**Implementation for Claude.ai:**
```
Prompt Template: "Please review this passage and help me with my specific weaknesses: 1) Replace 'was/were' constructions with active voice, 2) Show emotions through actions instead of telling, 3) Vary sentence structure. Focus on these improvements."
```

**Implementation for Sudowrite:**
- Use in "Rewrite" prompts: "Fix my weaknesses: passive voice, telling emotions, repetitive sentence structure"
- Create custom prompts for each weakness
- Use in "Edit" mode instructions

**Benefits:**
- Targeted improvement in your specific problem areas
- Consistent editing guidance across all AI tools
- Measurable progress tracking

---

## 📋 **CATEGORY 2: CHARACTER DEVELOPMENT SYSTEM**

### **2.1 Character Bible Framework**
**File Source:** `.cursorrules` (Lines 43-46)  
**Universal Value:** ⭐⭐⭐⭐⭐ (Essential for consistency)

```
## CHARACTER CONSISTENCY
- Maxanne: 73-year-old radio DJ, nostalgic, wise, slightly bitter, authentic Boston voice
- Nick Johnson: Working-class, father died in construction accident, passionate about music
- Jackie Marsh: Upper-class, educated, conflicted about his privilege, talented musician
```

**Implementation for Claude.ai:**
```
Character Consistency Prompt: "When writing dialogue or actions for these characters, maintain consistency with their established personalities:

Maxanne: 73-year-old radio DJ, nostalgic, wise, slightly bitter, authentic Boston voice
Nick Johnson: Working-class, father died in construction accident, passionate about music  
Jackie Marsh: Upper-class, educated, conflicted about his privilege, talented musician

Ensure each character's voice and actions reflect their background and personality."
```

**Implementation for Sudowrite:**
- Add to Character Sheets in Sudowrite
- Use in "Rewrite in Character Voice" features
- Reference in dialogue generation prompts

**Benefits:**
- Maintains character consistency across long projects
- Prevents character drift over time
- Provides clear reference for AI assistance

---

### **2.2 Character Voice Commands**
**File Source:** `.cursor/commands/voice.md`  
**Universal Value:** ⭐⭐⭐⭐ (Highly transferable)

```
# CHARACTER VOICE COMMAND
Ensure authentic character voice consistency:
- Maintain the character's unique speech patterns, vocabulary, and syntax
- Reflect their background, education, age, and personality through dialogue
- Keep narrative voice consistent with the POV character's perspective
- Use appropriate slang, idioms, and cultural references for the time period
```

**Implementation for Claude.ai:**
```
Voice Consistency Prompt: "Help me maintain authentic character voice by ensuring: 1) Unique speech patterns and vocabulary, 2) Background-appropriate dialogue, 3) Consistent POV perspective, 4) Period-appropriate language (1970s)."
```

**Implementation for Sudowrite:**
- Use in "Change Tone" feature
- Apply to dialogue generation
- Use in character-specific rewrites

**Benefits:**
- Maintains authentic character voices
- Prevents generic dialogue
- Ensures period authenticity

---

## 📋 **CATEGORY 3: SETTING & WORLD-BUILDING**

### **3.1 Setting Authenticity Framework**
**File Source:** `.cursorrules` (Lines 48-53)  
**Universal Value:** ⭐⭐⭐⭐⭐ (Critical for period accuracy)

```
## SETTING AUTHENTICITY
- 1979 Boston music scene
- WBCN radio station details
- Sudbury, Massachusetts geography
- Hop Brook as class divider
- Authentic period details (clothing, technology, culture)
```

**Implementation for Claude.ai:**
```
Setting Prompt: "When describing scenes, maintain 1979 Boston authenticity: WBCN radio station details, Sudbury geography, Hop Brook as class divider, period-appropriate clothing/technology/culture. Ensure all details feel authentic to the time and place."
```

**Implementation for Sudowrite:**
- Add to "World Building" section
- Use in "Expand" prompts for scene details
- Reference in description generation

**Benefits:**
- Maintains historical accuracy
- Creates immersive period atmosphere
- Prevents anachronistic details

---

## 📋 **CATEGORY 4: CREATIVE WRITING COMMANDS**

### **4.1 Prose Enhancement Command**
**File Source:** `.cursor/commands/prose.md`  
**Universal Value:** ⭐⭐⭐⭐⭐ (Core writing improvement)

```
# PROSE ENHANCEMENT COMMAND
Transform this text into rich, literary prose with:
- Vivid sensory details (sight, sound, smell, touch, taste)
- Metaphorical language and imagery
- Varied sentence structure (short punchy sentences mixed with flowing, lyrical ones)
- Emotional resonance and subtext
- Poetic rhythm and musicality
- Show, don't tell - use concrete details to convey abstract concepts
```

**Implementation for Claude.ai:**
```
Prose Enhancement Prompt: "Transform this text into rich, literary prose with: 1) Vivid sensory details, 2) Metaphorical language, 3) Varied sentence structure, 4) Emotional resonance, 5) Show don't tell approach. Maintain the original meaning while enhancing the literary quality."
```

**Implementation for Sudowrite:**
- Use in "Rewrite" feature
- Apply to "Improve Writing" prompts
- Use in "Expand" for sensory details

**Benefits:**
- Elevates prose quality consistently
- Maintains literary standards
- Provides systematic improvement approach

---

### **4.2 Dialogue Enhancement Command**
**File Source:** `.cursor/commands/dialogue.md`  
**Universal Value:** ⭐⭐⭐⭐ (Essential for authentic dialogue)

```
# DIALOGUE ENHANCEMENT COMMAND
Make this dialogue more authentic and compelling:
- Ensure each character has a distinct voice and speaking pattern
- Use subtext - what characters really mean vs. what they say
- Include realistic interruptions, hesitations, and speech patterns
- Add character-specific vocabulary, slang, and cultural references
```

**Implementation for Claude.ai:**
```
Dialogue Enhancement Prompt: "Improve this dialogue by: 1) Giving each character a distinct voice, 2) Adding subtext and hidden meanings, 3) Including realistic speech patterns, 4) Using period-appropriate vocabulary and slang."
```

**Implementation for Sudowrite:**
- Use in "Dialogue" improvement features
- Apply to character voice rewrites
- Use in conversation generation

**Benefits:**
- Creates authentic, engaging dialogue
- Develops character voice consistency
- Adds depth through subtext

---

### **4.3 Emotional Depth Command**
**File Source:** `.cursor/commands/emotion.md`  
**Universal Value:** ⭐⭐⭐⭐ (Critical for character development)

```
# EMOTIONAL DEPTH COMMAND
Deepen emotional resonance and character psychology:
- Show emotions through physical sensations and body language
- Use specific, concrete details to convey abstract feelings
- Layer emotions - characters often feel multiple things simultaneously
- Connect emotions to character backstory and motivations
```

**Implementation for Claude.ai:**
```
Emotional Depth Prompt: "Deepen the emotional resonance by: 1) Showing emotions through physical sensations, 2) Using concrete details for abstract feelings, 3) Layering multiple emotions, 4) Connecting to character backstory."
```

**Implementation for Sudowrite:**
- Use in "Add Emotion" features
- Apply to character development scenes
- Use in internal monologue generation

**Benefits:**
- Creates deeper character psychology
- Moves beyond surface-level emotions
- Connects feelings to character history

---

## 📋 **CATEGORY 5: TEMPLATE SYSTEMS**

### **5.1 Universal Fiction Templates**
**File Source:** `Universal-Fiction-Templates.md`  
**Universal Value:** ⭐⭐⭐⭐ (Reusable prompt patterns)

```
## EMOTIONAL ARC TEMPLATES
EMOTIONAL ARC: [Character] moves from [emotion1] to [emotion2] to [emotion3]
EMOTIONAL ARC: [Character] starts [emotional state] and ends [different emotional state]

## SENSORY FOCUS TEMPLATES
SENSORY FOCUS: Emphasize [sound/smell/touch/taste/sight] in this scene
SENSORY FOCUS: Use [specific sense] to create atmosphere

## DIALOGUE SUBTEXT TEMPLATES
DIALOGUE SUBTEXT: [Character] wants [X] but says [Y]
DIALOGUE SUBTEXT: [Character] means [X] but says [Y]
```

**Implementation for Claude.ai:**
- Copy templates directly into prompts
- Fill in brackets with specific details
- Use for consistent scene development

**Implementation for Sudowrite:**
- Create custom prompts using templates
- Use in "Expand" and "Rewrite" features
- Build library of reusable patterns

**Benefits:**
- Provides consistent prompt structures
- Saves time on prompt creation
- Ensures comprehensive scene development

---

## 📋 **CATEGORY 6: STYLE EMULATION SYSTEM**

### **6.1 Author Style Commands**
**File Source:** Multiple `.cursor/commands/` files  
**Universal Value:** ⭐⭐⭐ (Useful for specific scenes)

**Available Styles:**
- Stephen King (`/king`) - Conversational, accessible
- James Dickey (`/dickey`) - Poetic, lyrical
- Marilynne Robinson (`/robinson`) - Contemplative, philosophical
- Stephen Chbosky (`/chbosky`) - Intimate, confessional
- William Goldman (`/goldman`) - Witty, cinematic

**Implementation for Claude.ai:**
```
Style Emulation Prompt: "Rewrite this passage in the style of [AUTHOR], focusing on [specific style elements]. Maintain the original meaning while adopting their distinctive voice and techniques."
```

**Implementation for Sudowrite:**
- Use in "Change Tone" feature
- Apply to specific scenes requiring different styles
- Create custom style prompts

**Benefits:**
- Adds variety to prose style
- Helps develop different narrative voices
- Useful for specific scene requirements

---

## 📋 **CATEGORY 7: WORKFLOW OPTIMIZATION**

### **7.1 Response Format Preferences**
**File Source:** `.cursorrules` (Lines 15-17)  
**Universal Value:** ⭐⭐⭐⭐ (Improves AI interaction efficiency)

```
## Response Format I Prefer
- For creative requests: Just give me the prose, no explanation
- For Analysis: Quote the problem, show the fix, explain WHY something doesn't work
```

**Implementation for Claude.ai:**
```
Format Instructions: "For creative writing requests, provide only the enhanced prose without explanations. For analysis requests, quote the problem, show the fix, and explain why the original didn't work."
```

**Implementation for Sudowrite:**
- Use in prompt instructions
- Apply to different feature types
- Customize based on request type

**Benefits:**
- Streamlines AI interactions
- Reduces unnecessary explanations
- Focuses on actionable results

---

## 📋 **CATEGORY 8: SCENE TYPE DIRECTIVES**

### **8.1 Scene-Specific Instructions**
**File Source:** `.cursorrules` (Lines 24-27)  
**Universal Value:** ⭐⭐⭐⭐ (Ensures appropriate pacing)

```
## SCENE TYPE DIRECTIVES
@SCENE_TYPE:Dialogue - Make it authentic to character backgrounds and time period
@SCENE_TYPE:Action - Use short, punchy sentences with visceral details
@SCENE_TYPE:Reflection - Allow longer, flowing sentences with emotional depth
```

**Implementation for Claude.ai:**
```
Scene Type Prompt: "This is a [DIALOGUE/ACTION/REFLECTION] scene. Apply appropriate techniques: Dialogue=authentic character voices, Action=short punchy sentences, Reflection=longer flowing sentences with emotional depth."
```

**Implementation for Sudowrite:**
- Use in scene-specific rewrites
- Apply to different narrative modes
- Customize pacing based on scene type

**Benefits:**
- Ensures appropriate pacing for scene types
- Maintains narrative variety
- Improves scene effectiveness

---

## 🎯 **MIGRATION IMPLEMENTATION STRATEGY**

### **Phase 1: Core Setup (Day 1)**
1. Export `.cursorrules` content
2. Set up Claude.ai system prompts
3. Configure Sudowrite writing style settings
4. Create character sheets in Sudowrite

### **Phase 2: Command Integration (Day 2-3)**
1. Convert Cursor commands to Claude.ai prompts
2. Create Sudowrite custom prompts
3. Set up template libraries
4. Test each command adaptation

### **Phase 3: Workflow Optimization (Day 4-5)**
1. Establish new AI interaction patterns
2. Create prompt libraries for quick access
3. Test and refine each adaptation
4. Document successful patterns

---

## 📊 **VALUE ASSESSMENT SUMMARY**

| Category | Universal Value | Claude.ai Ready | Sudowrite Ready | Implementation Effort |
|----------|----------------|-----------------|-----------------|---------------------|
| Writing Philosophy | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Low |
| Character Development | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Medium |
| Setting Framework | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Low |
| Prose Commands | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Medium |
| Dialogue Commands | ⭐⭐⭐⭐ | ✅ | ✅ | Medium |
| Template Systems | ⭐⭐⭐⭐ | ✅ | ✅ | Low |
| Style Emulation | ⭐⭐⭐ | ✅ | ✅ | High |
| Workflow Optimization | ⭐⭐⭐⭐ | ✅ | ✅ | Low |

---

## 🚀 **IMMEDIATE ACTION ITEMS**

1. **Export `.cursorrules`** to `My-Writing-Style-Guide.md`
2. **Create Claude.ai system prompt** using writing values
3. **Set up Sudowrite character sheets** with your character bible
4. **Convert top 5 commands** to prompt templates
5. **Test each adaptation** with sample text

---

**END OF ARTIFACT 2**
