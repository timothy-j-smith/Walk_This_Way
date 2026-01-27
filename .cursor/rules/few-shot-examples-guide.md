# FEW-SHOT EXAMPLES FOR STYLE CONSISTENCY
## Show, Don't Tell - Style Examples
**Created:** January 24, 2026  
**Purpose:** Use examples to lock in style, voice, and technique

---

## THE CONCEPT

**Show Claude examples of what you want instead of describing it.**

**Why It Works:**
- Examples are concrete (descriptions are abstract)
- Shows exact style, not approximate
- Locks in voice, rhythm, technique
- Dramatically improves consistency

---

## BASIC FORMAT

### Simple Version:
```
GOOD EXAMPLE:
[Your best writing]

BAD EXAMPLE:
[Writing that doesn't work]

Now apply this style to:
[Your new text]
```

### Detailed Version:
```
STYLE GUIDE:

GOOD - Maxanne's Voice (1st Person, Radio DJ):
"The music didn't just play. It lived. It breathed. And in 1973, when I first put Aerosmith's 'Dream On' on the air, I knew something was happening. Not just in Boston. In me."

BAD - Too Formal:
"The music was significant. In 1973, when I played Aerosmith's 'Dream On' on the radio, I recognized its importance."

Now rewrite this passage in Maxanne's voice:
[Your text]
```

---

## USE CASES FOR "WALK THIS WAY"

### 1. Character Voice Examples

**Nick's Voice (Working-Class, Direct):**
```
GOOD - Nick's Voice:
"I didn't need his help. I could handle it. My old man taught me that much before he died."

BAD - Too Polished:
"I did not require his assistance. I was capable of managing the situation independently. My father had instilled this self-reliance in me prior to his passing."

Now write Nick's dialogue:
[Your dialogue]
```

**Jackie's Voice (Upper-Class, Precise):**
```
GOOD - Jackie's Voice:
"I cannot simply abandon my training. It would be... irresponsible. My father has invested considerable resources in my musical education."

BAD - Too Casual:
"I can't just quit. That'd be wrong. My dad spent a lot of money on my lessons."

Now write Jackie's dialogue:
[Your dialogue]
```

**Maxanne's Voice (Radio DJ, Reflective):**
```
GOOD - Maxanne's Voice:
"The station was dying. We all knew it. Corporate suits in suits, talking about demographics and market share. They didn't understand. Music wasn't a product. It was a revolution."

BAD - Too Expositional:
"The radio station was being taken over by corporate executives who focused on demographics and market share rather than the music itself."

Now write Maxanne's narration:
[Your narration]
```

### 2. Prose Style Examples

**Visceral Detail (Show, Don't Tell):**
```
GOOD - Visceral Detail:
"Nick's knuckles split against the garage door. Blood mixed with rust. He didn't feel it. Not yet. The pain would come later, when the anger faded."

BAD - Telling:
"Nick was angry and hit the garage door, hurting his hand."

Now rewrite with visceral detail:
[Your text]
```

**Subtext in Dialogue:**
```
GOOD - Subtext:
'You coming to practice?' Jackie asked.
Nick didn't look up. 'Maybe.'
'Your mom said you were working.'
'She tell you that?'

BAD - Exposition:
'Are you coming to practice?' Jackie asked.
'Maybe,' Nick said, avoiding eye contact because he was angry about his father's death.
'Your mother informed me that you were working,' Jackie said.
'Did she tell you that?' Nick asked defensively.

Now write dialogue with subtext:
[Your dialogue]
```

**Working-Class Authenticity:**
```
GOOD - Authentic:
"Five hundred bucks. That's what studio time cost. Five hundred bucks I didn't have. Five hundred bucks that might as well have been five million."

BAD - Inauthentic:
"Studio time was expensive, costing five hundred dollars, which was an amount I could not afford."

Now rewrite with working-class authenticity:
[Your text]
```

### 3. Scene Type Examples

**Tension Building:**
```
GOOD - Tension:
"The garage door creaked. Nick froze. Not his mother. She'd call first. Not Jackie. He'd knock. This was different. This was wrong."

BAD - Flat:
"Nick heard the garage door open and became concerned because it was unexpected."

Now write a tension scene:
[Your scene]
```

**Emotional Depth:**
```
GOOD - Emotional:
"Patty remembered. Of course she remembered. She was the keeper. The one who held onto what everyone else let slip away. And in that moment, watching Nick and Jackie circle each other like wounded animals, she understood what they'd lost."

BAD - Surface:
"Patty remembered the past and understood that Nick and Jackie had lost their friendship."

Now write with emotional depth:
[Your scene]
```

**Music Description:**
```
GOOD - How Musicians Experience It:
"The guitar didn't just play. It screamed. Raw power, unfiltered, straight from Nick's fingers to the amp. No polish. No production. Just pure sound that made your chest vibrate."

BAD - How Critics Describe It:
"The guitar performance demonstrated technical proficiency and emotional intensity."

Now describe music:
[Your description]
```

---

## COMBINING WITH OTHER TECHNIQUES

### Few-Shot + XML Tags:
```
<scene>
<goal>Rewrite in Maxanne's voice</goal>
<tone>melancholic, reflective</tone>
</scene>

GOOD EXAMPLE:
"The music didn't just play. It lived. It breathed."

BAD EXAMPLE:
"The music was significant and important."

Now rewrite:
[Your text]
```

### Few-Shot + Role Prompting:
```
You are a line editor specializing in working-class authenticity.

GOOD - Authentic Voice:
"I didn't need his help. I could handle it."

BAD - Inauthentic:
"I did not require his assistance."

Now improve:
[Your text]
```

### Few-Shot + Chain of Thought:
```
<thinking>
- What makes the good example work?
- What's the rhythm?
- What's the voice?
</thinking>

GOOD EXAMPLE:
[Your best writing]

BAD EXAMPLE:
[Writing that doesn't work]

Now apply this style:
[Your text]
```

---

## BUILDING YOUR EXAMPLE LIBRARY

### Create Example Files:

**1. Character Voice Examples**
```
Location: Story_Bible/character-voice-examples.md
Content: Good/Bad examples for each character
```

**2. Prose Style Examples**
```
Location: Story_Bible/prose-style-examples.md
Content: Good/Bad examples for each prose technique
```

**3. Scene Type Examples**
```
Location: Story_Bible/scene-type-examples.md
Content: Good/Bad examples for each scene type
```

**4. Style Emulation Examples**
```
Location: Story_Bible/style-emulation-examples.md
Content: Good/Bad examples for each target author
```

---

## WHEN TO USE

**Use Few-Shot Examples For:**
- ✅ Character voice consistency
- ✅ Prose style matching
- ✅ Scene type guidance
- ✅ Style emulation requests
- ✅ When you have good examples

**Don't Need Few-Shot Examples For:**
- ❌ Simple questions (fact checks)
- ❌ Quick edits (single word changes)
- ❌ When you don't have good examples yet

---

## TESTING

**Without Examples:**
```
"Write dialogue for Nick in a working-class voice."
→ Generic, may miss authenticity
```

**With Examples:**
```
GOOD - Nick's Voice:
"I didn't need his help. I could handle it."

BAD - Too Polished:
"I did not require his assistance."

Now write Nick's dialogue:
→ Matches exact voice, rhythm, authenticity
```

---

## QUICK REFERENCE

**Copy/Paste Template:**
```
GOOD EXAMPLE:
[Your best writing]

BAD EXAMPLE:
[Writing that doesn't work]

Now apply this style to:
[Your new text]
```

**Build Library:**
- Save your best examples
- Create Good/Bad pairs
- Reference in future prompts

---

**Status:** ✅ **READY TO USE**  
**Start:** Find one good example of your writing, pair it with a bad version, use in next prompt!
