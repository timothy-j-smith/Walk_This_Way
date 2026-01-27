# AUTOMATION SYSTEM DESIGN
## Automated + Manual Access for All Scripts
**Date:** January 24, 2026  
**Purpose:** Build efficient team workflow where Claude and Timothy learn from each other

---

## AUTOMATION PHILOSOPHY

**Automated:** Things Claude should offer automatically at session start or during sessions  
**Manual:** `/command` access for anytime use  
**Team Learning:** System that captures what works and improves over time

---

## SESSION START AUTOMATIONS

### 1. Quick Wins Setup ✅ (Already Automated)
**Automated:** Claude offers at session start  
**Manual:** `/session-start` or `/start-session`  
**Status:** ✅ Complete

### 2. Session Continuity Check (Should Be Automated)
**What:** "Where did we leave off? What's next?"  
**Automated:** Claude offers at session start  
**Manual:** `/session-continuity` or `/where-were-we`  
**Script:** Check `.cursor/logs/writing-sessions.jsonl` for last entry

### 3. DNA Status Check (Should Be Automated)
**What:** Quick overview of plot, character, world status  
**Automated:** Claude offers at session start (optional)  
**Manual:** `/dna-status` or `/dna`  
**Script:** Query DNA Memory System

### 4. Recent Changes Summary (Should Be Automated)
**What:** "What changed since last session?"  
**Automated:** Claude offers at session start  
**Manual:** `/recent-changes` or `/what-changed`  
**Script:** Check Git log, session logs, file modifications

---

## DURING SESSION AUTOMATIONS

### 5. Word Count Tracking (Should Be Automated)
**What:** Track daily word count automatically  
**Automated:** Claude offers after writing sessions  
**Manual:** `/word-count` or `/wc`  
**Script:** `.cursor/scripts/word_count.sh`

### 6. Consistency Checks (Should Be Automated)
**What:** Check for plot/character/timeline inconsistencies  
**Automated:** Claude offers periodically or after major edits  
**Manual:** `/consistency-check` or `/check`  
**Script:** `.cursor/scripts/consistency_check.sh`

### 7. Character Report (Should Be Automated)
**What:** Character mention/voice consistency report  
**Automated:** Claude offers when character work is done  
**Manual:** `/character-report <name>` or `/char <name>`  
**Script:** `.cursor/scripts/character_report.sh`

### 8. Git Status Check (Should Be Automated)
**What:** "Have you committed your work?"  
**Automated:** Claude offers at session end  
**Manual:** `/git-status` or `/git`  
**Script:** Check Git status, remind to commit

---

## TEAM LEARNING SYSTEM

### What We'll Capture:
1. **What Works:** Which templates/techniques produce best results
2. **What Doesn't:** What to avoid or improve
3. **Preferences:** Your style, what you like/dislike
4. **Patterns:** When you use which tools, what helps most

### How It Works:
- Claude notes what works well
- Saves to `.cursor/logs/team-learning.jsonl`
- Improves recommendations over time
- Learns your preferences

---

## IMPLEMENTATION PLAN

### Phase 1: Session Start Automations
1. ✅ Quick Wins Setup (already done)
2. ⏳ Session Continuity Check
3. ⏳ DNA Status Check
4. ⏳ Recent Changes Summary

### Phase 2: During Session Automations
5. ⏳ Word Count Tracking
6. ⏳ Consistency Checks
7. ⏳ Character Reports
8. ⏳ Git Status Reminders

### Phase 3: Team Learning
9. ⏳ Learning system
10. ⏳ Preference tracking
11. ⏳ Pattern recognition

---

**Status:** 📋 **DESIGN COMPLETE - READY FOR IMPLEMENTATION**
