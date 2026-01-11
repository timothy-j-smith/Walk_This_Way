# NOVEL MEMORY CONFIG — WALK THIS WAY

**Project:** Walk This Way  
**Version:** 0.1 (First activation)  
**Compiled:** November 9, 2025  
**Purpose:** Master reference for the Writing DNA Memory System inside the Cursor workspace. This file defines what the memory engine must capture, how SmartWrite should reason about the story, and which signals trigger alerts.

---

## 1. Plot DNA — Canon Timeline & Story Beats

| Era | Anchor Beats | Canon Notes |
| --- | --- | --- |
| **1972-1973** | Maxanne discovers Aerosmith; Nick hears “Dream On” in Dan’s truck | Music as salvation seeded |
| **1974 (Age 12-13)** | Belt-buckle showdown → Nick & Jackie alliance | Friendship grounded in music rivalry |
| **Summer 1975** | Camp Winaukee — Patty triangle, first composition of “Your Song” | Patty becomes emotional frequency keeper |
| **Spring 1976** | Middle school talent show victory | Proof of combined power |
| **April 13, 1976** | Dan Johnson dies in construction accident | Nick becomes “man of the house” |
| **1976-77** | High school sorting pressures begin | Hop Brook divide hardens |
| **November 1977** | *Chapter 11 fracture zone* — cafeteria sorting, silent drift | Class gravity overrides intention |
| **1978** | Separate rehearsal philosophies emerge | Nick raw, Jackie precision |
| **Spring 1979** | Battle of the Bands & WBCN opportunity | Authenticity vs. polish |
| **October 2024** | Maxanne final broadcast framing device | Memory lens closes the loop |

**Chapter 11 focus:** capture the first undeniable fracture (cafeteria seating, garage tension, Patty letters, silent lies by omission). Maintain timeline continuity heading into the November 1977 shatter point.

---

## 2. Character DNA — Core Voices & Emotional Truth

### Nick Johnson
- **Voice:** Working-class Boston teen; defensive pride, clipped sentences, emotion leaks through physical reaction.
- **Goals:** Keep family afloat, protect music space, resist pity.
- **Wounds:** Dan’s death, financial instability, feeling judged by wealth.
- **Chapter 11 signals:** Drawn to Rollers, “tightness in chest,” lies to Patty, avoids Jackie’s gaze.

### Jackie Marsh
- **Voice:** Educated precision; formality increases when anxious; hidden yearning for authenticity.
- **Goals:** Honor talent, earn father’s approval, keep Nick connection alive.
- **Wounds:** Class expectations, fear of mediocrity, guilt over privilege.
- **Chapter 11 signals:** Drawn to Rampers, mirrors Nick’s omission to Patty, hesitant dialogue in garage.

### Patty Lally
- **Voice:** Grounded, observational, emotionally intelligent.
- **Function:** Frequency keeper; letters expose truth gaps.
- **Chapter 11 presence:** Offstage but catalytic through correspondence.

### Maxanne Sartori (Narrative Frame)
- **Voice:** 1st-person 2024 radio cadence; nostalgic without sentimentality.
- **Function:** Historian of authenticity; ties 1970s events to 2024 corporate takeover.

**Consistency guardrails:**  
- Nick never slips into upper-class diction; Jackie never abandons polish unless emotionally cracked.  
- Patty letters always balance compassion with clarity.  
- Maxanne references era-specific radio tech and station politics.

---

## 3. World DNA — Setting, Geography, Atmosphere

- **Sudbury Geography:** Hop Brook divides working-class east (Johnson) from affluent west (Marsh). Dump = neutral ground; auto shop corridor = Roller territory; elevated cafeteria platform = Rampers.
- **Lincoln-Sudbury High (1977):** Cafeteria zones (Rampers, Rats, Regs, Rollers) enforce social taxonomy; glass corridor = semi-exile territory; auto shop smell = oil/ozone.
- **Economics:** Gas crisis ripple, late-70s stagflation, construction layoffs. One car failure threatens Johnson household stability.
- **Music Scene:** Pre-MTV vinyl dominance; WBCN as authentic voice; Queen/Aerosmith rivalry mirrors class divide.
- **Technology:** Rotary phones, cassette tapes, letters; no digital messaging.

**Alert hooks:**  
1. Location mismatches (e.g., Rampers not on elevated platform).  
2. Anachronistic tech or slang.  
3. Misaligned cost references (must reflect 1977 dollars).

---

## 4. Session Continuity — Live Tracking Prompts

| Key | Description | Example Cue |
| --- | --- | --- |
| `Last_Written` | File + paragraph where session stopped | `"Test_Draft_Copy/Act_I/Chapter_11..." paragraph about garage tension` |
| `Next_Target` | Upcoming beat to draft/rewrite | `"Show Patty letter revelation before November shatter"` |
| `Open_Threads` | Unresolved beats needing follow-up | `["Nick hiding car trouble", "Jackie parental pressure convo"]` |
| `Emotional_Tone` | Desired mood for next pass | `"Strained nostalgia, under-the-surface grief"` |
| `Craft_Direction` | Specific craft notes | `["Keep sentences shorter in Nick’s POV", "Let Jackie slip into formal diction when nervous"]` |

Populate these after each session via `.cursor/logs/writing-sessions.jsonl`.

---

## 5. Consistency Checks — Automatic & Manual

| Check | Scope | Trigger |
| --- | --- | --- |
| **Timeline Sync** | Confirms date references (e.g., Dan’s death 1976 vs 1977) | Auto |
| **Voice Integrity** | Flags diction mismatches per character DNA | Auto |
| **World Continuity** | Validates location usage, geography, period details | Auto |
| **Letter Honesty** | Highlights discrepancies between letters and lived events | Manual: `consistency check letters` |
| **Zen Mode** | `Cmd+O` to silence non-critical alerts mid-draft | Manual |

Manual command glossary (use in Composer/Text Editor prompts):
- `"DNA status"` → quick strand summary  
- `"Plot report"` → chapter-by-chapter timeline  
- `"Character report"` → voice & arc updates  
- `"World report"` → setting cross-check  
- `"Consistency check"` → aggregated alerts  
- `"Session prep"` → next-session briefing

---

## 6. Chapter 11 — Test Protocol Snapshot

1. **Load Context:** Pull Chapter 11 draft + Patty letter reference.
2. **Memory Prime:** Ensure Nick/Jackie voice deltas captured before SmartWrite suggestions.
3. **SmartWrite Pass:** Start with `liberty: conservative` to maintain canonical beats, then escalate to `moderate` for subtext tuning. Reserve `high` or optional `blue-sky` liberty for clearly labeled exploratory drafts only.
4. **Logging:** After each pass, append entry to `.cursor/logs/writing-sessions.jsonl` using template in Section 7.
5. **Report Back:** Summarize findings in Transition Document appendix and `WRITING_DNA_MEMORY_SYSTEM.md`.

---

## 7. Session Log Template

Append one JSON object per session to `.cursor/logs/writing-sessions.jsonl`:

```json
{
  "date": "2025-11-09T18:45:00-05:00",
  "chapter": "Act_I/Chapter_11_The_First_Fracture",
  "focus": ["memory-prime", "smartwrite-pass"],
  "dna_updates": {
    "plot": ["Logged cafeteria seating fracture"],
    "character": ["Captured Nick chest-tightening tell", "Jackie omission motif"],
    "world": ["Reconfirmed Rampers platform detail"],
    "session": ["Next_Target: Patty letter reveal draft"],
    "consistency": ["No alerts", "ZenMode": false]
  },
  "observations": [
    "SmartWrite conservative pass preserved class tension while tightening prose.",
    "Moderate liberty pass added subtext about letters without breaking canon."
  ],
  "next_steps": [
    "Draft Patty letter insert",
    "Prep Chapter 12 setup"
  ]
}
```

---

## 8. Maintenance Notes

- Update this config after major plot decisions or voice evolutions.  
- Keep character voice micro-notes synced with `.cursor/docs/References/character-voices.md`.  
- When new strands (e.g., Agent Review alerts) emerge, append under Consistency Checks.

---

**Ready State:** ✅ Memory system primed for Chapter 11 testing. Activate SmartWrite next and capture findings for the Transition Document.  
**Owner:** Timothy + Hank (Creative Collaborator)  
**Last Reviewed:** November 9, 2025

