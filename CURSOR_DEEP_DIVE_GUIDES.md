# CURSOR DEEP DIVE GUIDES
## Comprehensive Exploration of Advanced Features - January 24, 2026

**Purpose:** Master Composer, Chat, Terminal, and Search & Replace  
**Methodology:** Sequential Thinking analysis where requested

---

## PART I: COMPOSER - MULTI-FILE COMPOSITION MASTERY

### What is Multi-File Composition?

**Composer** is Cursor's AI-powered editor that can work across multiple files simultaneously. Instead of editing one file at a time, you can select multiple files and have AI understand their relationships and make coordinated changes.

---

### How to Use Multi-File Composition

#### Method 1: Select Multiple Files in Composer

1. **Open Composer:**
   - Press `Cmd+L` (Composer Panel)
   - Or `Cmd+K` (Inline Composer)

2. **Select Multiple Files:**
   - Click file tabs while holding `Cmd` (Mac) or `Ctrl` (Windows)
   - Or use `@filename` in Composer to reference files
   - Or drag files into Composer

3. **Give Instructions:**
   ```
   Update Chapter 4 and Chapter 5 to reflect Nick's new guitar purchase. 
   Make sure both chapters are consistent about the guitar model.
   ```

4. **AI Understands:**
   - Relationships between files
   - Cross-file consistency
   - Dependencies

---

#### Method 2: Use @ References

**Syntax:**
```
@filename1 @filename2 @filename3
Update all three files to use consistent character descriptions.
```

**Examples:**
```
@Chapter_4.txt @Chapter_5.txt
Ensure Jackie's dialogue is consistent across both chapters.
```

```
@Story_Bible/characters.md @Chapter_4.txt
Update Chapter 4 to match the character details in Story Bible.
```

---

#### Method 3: Select Code Across Files

1. **Select code in File 1**
2. **Hold `Cmd` and select code in File 2**
3. **Open Composer** (`Cmd+L`)
4. **AI sees both selections** and understands context

---

### Advanced Multi-File Techniques

#### 1. **Coordinated Refactoring**

**Example:**
```
@Chapter_1.txt @Chapter_2.txt @Chapter_3.txt
Rename "Maxanne" to "Max" throughout all three chapters, 
maintaining consistent voice and context.
```

**What AI Does:**
- Finds all instances across files
- Maintains context
- Ensures consistency
- Updates references

---

#### 2. **Cross-File Consistency Checks**

**Example:**
```
@Chapter_4.txt @Story_Bible/timeline.md
Check if Chapter 4's timeline matches the Story Bible timeline.
Fix any inconsistencies.
```

**What AI Does:**
- Compares timelines
- Identifies conflicts
- Suggests fixes
- Updates both files

---

#### 3. **Character Voice Consistency**

**Example:**
```
@Chapter_1.txt @Chapter_5.txt @Chapter_10.txt
Review Nick's dialogue in all three chapters. 
Ensure his voice is consistent - working-class Boston, 
economical speech, defensive pride.
```

**What AI Does:**
- Analyzes dialogue patterns
- Compares voice across files
- Identifies inconsistencies
- Suggests corrections

---

#### 4. **Thematic Consistency**

**Example:**
```
@Chapter_2.txt @Chapter_7.txt @Chapter_12.txt
Review the class divide theme in these chapters. 
Ensure the theme is developed consistently and 
authentically across all three.
```

**What AI Does:**
- Analyzes thematic elements
- Tracks theme development
- Ensures consistency
- Suggests enhancements

---

### Composer Best Practices

1. **Be Specific:**
   - ✅ "Update Chapter 4 and 5 to reflect Nick's new guitar"
   - ❌ "Update files"

2. **Reference Files Explicitly:**
   - ✅ `@Chapter_4.txt @Chapter_5.txt Update dialogue`
   - ❌ "Update dialogue" (unclear which files)

3. **Provide Context:**
   - ✅ "Nick buys a 1976 Fender Stratocaster. Update both chapters to reflect this purchase."
   - ❌ "Update chapters"

4. **Use Incremental Composition:**
   - Start with 2-3 files
   - Build up to larger compositions
   - Review changes before expanding

---

### Composer Limitations & Workarounds

**Limitation:** Very large files may hit context limits  
**Workaround:** Break into smaller compositions

**Limitation:** Too many files may confuse AI  
**Workaround:** Group related files (e.g., all chapters in Act I)

**Limitation:** Complex relationships may need clarification  
**Workaround:** Explain relationships explicitly

---

## PART II: CHAT - ADVANCED CONTEXT FEATURES

### Sequential Thinking Analysis

**Base Sequential Thinking:**
"What makes Chat advanced? Context awareness, file references, memory integration, and persistent conversations."

**MAS Multi-Perspective:**
- **Factual:** Chat has context awareness, file references, memory
- **Creative:** Can use for creative brainstorming with context
- **System-Building:** Perfect for system questions with full context
- **Optimistic:** Very powerful when used correctly

**Ultra Bias Check:** ✅ No bias - These are real features

**Enhanced Sequential Thinking:**
- **Creative Mode:** Chat perfect for creative exploration with context
- **Evaluative Mode:** Chat excellent for analysis with full context

**Verdict:** 👍 **POWERFUL FEATURE** - Master context usage

---

### Advanced Context Techniques

#### 1. **File References in Chat**

**Syntax:**
```
@filename
What does this file tell us about Nick's character?
```

**Multiple Files:**
```
@Chapter_4.txt @Story_Bible/characters.md
Compare Nick's characterization in Chapter 4 with the Story Bible.
Are they consistent?
```

**Wildcards:**
```
@Chapter_*.txt
Analyze pacing across all chapters.
```

---

#### 2. **Code Selection Context**

**How to Use:**
1. Select code/text in editor
2. Open Chat (`Cmd+L`)
3. Ask question
4. AI sees selected code automatically

**Example:**
```
[Select dialogue from Chapter 4]
Does this dialogue sound authentic for Nick's character?
How can I improve it?
```

---

#### 3. **Multi-File Context**

**How to Use:**
```
@Chapter_4.txt @Chapter_5.txt @Chapter_6.txt
Analyze the three-chapter arc from Chapter 4 to 6.
What themes emerge? How does the pacing work?
```

**What AI Sees:**
- All three files
- Relationships between them
- Patterns across files
- Context from all files

---

#### 4. **Memory Integration**

**How It Works:**
- Chat automatically uses your Memory sources
- References `.cursor/NOVEL_MEMORY_CONFIG.md`
- Loads relevant context automatically
- Remembers past conversations

**Example:**
```
What did we decide about Nick's guitar in our last conversation?
[AI references memory automatically]
```

---

#### 5. **Persistent Conversations**

**How It Works:**
- Chat history persists across sessions
- AI remembers context from previous messages
- Can reference earlier parts of conversation

**Best Practice:**
- Start new chat for new topics
- Continue chat for related topics
- Use chat history for context

---

#### 6. **Context Pinning**

**How to Use:**
1. Open file
2. Pin it (may have pin icon)
3. Chat always has access to pinned files
4. Useful for reference files

**Example:**
- Pin `Story_Bible/characters.md`
- Chat always knows character details
- No need to reference repeatedly

---

#### 7. **Chat Templates**

**Create Reusable Prompts:**
1. Save common questions as templates
2. Reuse for similar tasks
3. Customize as needed

**Example Template:**
```
Character Consistency Check:
@[SELECT_FILE]
Review [CHARACTER]'s voice and characterization.
Check for consistency with Story Bible.
Suggest improvements.
```

---

### Advanced Chat Workflows

#### Workflow 1: Character Analysis

```
@Chapter_4.txt @Story_Bible/characters.md
Analyze Nick's character development in Chapter 4.
Compare with Story Bible characterization.
Identify any inconsistencies or opportunities for enhancement.
```

---

#### Workflow 2: Thematic Analysis

```
@Chapter_1.txt @Chapter_5.txt @Chapter_10.txt
Analyze the class divide theme across these three chapters.
How does it develop? Are there opportunities to strengthen it?
```

---

#### Workflow 3: Pacing Analysis

```
@Act_I/*.txt
Analyze pacing across Act I.
Identify slow sections and fast sections.
Suggest pacing improvements.
```

---

#### Workflow 4: Research Integration

```
@Chapter_4.txt
This chapter mentions 1976 Boston. 
Research historical accuracy and suggest improvements.
[AI uses Firecrawl MCP automatically]
```

---

### Chat Best Practices

1. **Be Specific:**
   - ✅ "Analyze Nick's dialogue in Chapter 4"
   - ❌ "Analyze dialogue"

2. **Reference Files:**
   - ✅ `@Chapter_4.txt Analyze this`
   - ❌ "Analyze this" (unclear what "this" is)

3. **Provide Context:**
   - ✅ "Nick is working-class Boston. Does this dialogue match?"
   - ❌ "Does this dialogue match?"

4. **Use Memory:**
   - Chat automatically uses Memory
   - But you can reference it explicitly
   - "According to Story Bible, Nick..."

5. **Chain Questions:**
   - Build on previous answers
   - Reference earlier in conversation
   - Deep dive into topics

---

## PART III: TERMINAL - AUTOMATION CHEAT SHEET

### Essential Terminal Commands for Fiction Writing

#### File Operations

```bash
# Count words in all chapters
find Draft_1 -name "*.txt" -exec wc -w {} + | tail -1

# Count words per chapter
for file in Draft_1/Act_I/*.txt; do
    echo "$(basename $file): $(wc -w < "$file") words"
done

# Find all mentions of character
grep -r "Nick Johnson" Draft_1/ --include="*.txt" | wc -l

# List all chapters with word counts
find Draft_1 -name "*.txt" -exec sh -c 'echo "$(basename "$1"): $(wc -w < "$1") words"' _ {} \;
```

---

#### Character Analysis

```bash
# Count character mentions
grep -roh "Nick\|Jackie\|Maxanne" Draft_1/ --include="*.txt" | sort | uniq -c | sort -rn

# Find character dialogue
grep -n "\"Nick" Draft_1/Act_I/Chapter_*.txt

# Character consistency check
grep -i "nick.*age\|nick.*years old" Draft_1/ --include="*.txt"
```

---

#### Text Analysis

```bash
# Find repeated phrases
grep -roh "[A-Z][a-z]* [a-z]* [a-z]*" Draft_1/ --include="*.txt" | sort | uniq -d | head -20

# Count dialogue lines
grep -c '".*"' Draft_1/Act_I/Chapter_*.txt

# Find long sentences (over 100 characters)
grep -E '.{100,}' Draft_1/Act_I/Chapter_*.txt | wc -l
```

---

#### Project Management

```bash
# Total word count
find Draft_1 -name "*.txt" -exec cat {} + | wc -w

# Chapter statistics
for act in Draft_1/Act_*; do
    echo "$(basename $act):"
    find "$act" -name "*.txt" -exec cat {} + | wc -w
done

# Find TODO comments
grep -rn "TODO\|FIXME" . --include="*.txt" --include="*.md"

# Find inconsistencies (example: age mentions)
grep -rn "age\|years old" Draft_1/ --include="*.txt"
```

---

#### Git Operations (via Terminal)

```bash
# Quick commit all changes
git add -A && git commit -m "WIP: Chapter 4 revisions"

# View changes
git diff Draft_1/Act_I/Chapter_4.txt

# Find when character was first mentioned
git log -p -S "Nick Johnson" -- Draft_1/ | head -50
```

---

#### Automation Scripts

**Script 1: Daily Word Count**
```bash
#!/bin/bash
# Save as: .cursor/scripts/word_count.sh

TOTAL=$(find Draft_1 -name "*.txt" -exec cat {} + | wc -w)
TODAY=$(date +"%Y-%m-%d")
echo "$TODAY: $TOTAL words" >> .cursor/logs/word_count.log
echo "Total words: $TOTAL"
```

**Script 2: Character Mention Report**
```bash
#!/bin/bash
# Save as: .cursor/scripts/character_report.sh

CHARACTER="$1"
if [ -z "$CHARACTER" ]; then
    echo "Usage: $0 <character_name>"
    exit 1
fi

echo "=== $CHARACTER Mention Report ==="
echo "Total mentions: $(grep -roh "$CHARACTER" Draft_1/ --include="*.txt" | wc -l)"
echo ""
echo "By chapter:"
find Draft_1 -name "*.txt" -exec sh -c 'count=$(grep -o "$1" "$2" | wc -l); if [ $count -gt 0 ]; then echo "$(basename "$2"): $count"; fi' _ "$CHARACTER" {} \;
```

**Script 3: Consistency Check**
```bash
#!/bin/bash
# Save as: .cursor/scripts/consistency_check.sh

echo "=== Age Mentions ==="
grep -rn "age\|years old" Draft_1/ --include="*.txt" | head -20

echo ""
echo "=== Date Mentions ==="
grep -rn "197[0-9]\|198[0-9]" Draft_1/ --include="*.txt" | head -20

echo ""
echo "=== Location Mentions ==="
grep -rn "Boston\|Sudbury" Draft_1/ --include="*.txt" | head -20
```

---

#### Python Automation (via Terminal)

**Script: Chapter Statistics**
```python
#!/usr/bin/env python3
# Save as: .cursor/scripts/chapter_stats.py

import os
from pathlib import Path

def analyze_chapter(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        words = len(text.split())
        chars = len(text)
        paragraphs = text.count('\n\n') + 1
        dialogue = text.count('"') // 2
        return {
            'words': words,
            'chars': chars,
            'paragraphs': paragraphs,
            'dialogue': dialogue
        }

# Analyze all chapters
for act_dir in Path('Draft_1').glob('Act_*'):
    print(f"\n{act_dir.name}:")
    for chapter in sorted(act_dir.glob('*.txt')):
        stats = analyze_chapter(chapter)
        print(f"  {chapter.name}: {stats['words']} words, "
              f"{stats['paragraphs']} paragraphs, "
              f"{stats['dialogue']} dialogue exchanges")
```

**Run:**
```bash
python3 .cursor/scripts/chapter_stats.py
```

---

### Terminal Automation Best Practices

1. **Create Scripts Directory:**
   ```bash
   mkdir -p .cursor/scripts
   ```

2. **Make Scripts Executable:**
   ```bash
   chmod +x .cursor/scripts/*.sh
   ```

3. **Add to PATH (optional):**
   ```bash
   export PATH="$PATH:$(pwd)/.cursor/scripts"
   ```

4. **Document Scripts:**
   - Add comments
   - Include usage examples
   - Document in notepads

---

## PART IV: SEARCH & REPLACE - REGEX & MULTI-FILE MASTERY

### Sequential Thinking Analysis

**Base Sequential Thinking:**
"Regex is pattern matching. Multi-file replace applies changes across multiple files. Both are powerful for large-scale edits."

**MAS Multi-Perspective:**
- **Factual:** Regex is standard pattern matching. Multi-file replace exists in Cursor.
- **Creative:** Can use for creative text transformations.
- **System-Building:** Essential for refactoring and consistency.
- **Optimistic:** Very powerful when mastered.

**Ultra Bias Check:** ✅ No bias - These are real, powerful features

**Enhanced Sequential Thinking:**
- **Creative Mode:** Regex can help with creative text transformations.
- **Evaluative Mode:** Essential for consistency and accuracy.

**Verdict:** 👍 **ESSENTIAL SKILL** - Master this for efficiency

---

### Regex Fundamentals

#### Basic Patterns

**Literal Text:**
```
Nick Johnson
```
Matches: "Nick Johnson" exactly

**Character Classes:**
```
[0-9]     # Any digit
[a-z]     # Any lowercase letter
[A-Z]     # Any uppercase letter
[0-9a-z]  # Digit or lowercase letter
```

**Quantifiers:**
```
*         # Zero or more
+         # One or more
?         # Zero or one
{3}       # Exactly 3
{3,5}     # 3 to 5
{3,}      # 3 or more
```

**Anchors:**
```
^         # Start of line
$         # End of line
\b        # Word boundary
```

**Special Characters:**
```
.         # Any character (except newline)
\.        # Literal period
\d        # Digit (same as [0-9])
\w        # Word character (letter, digit, underscore)
\s        # Whitespace
\n        # Newline
\t        # Tab
```

---

### Common Regex Patterns for Fiction Writing

#### 1. Find Character Names

**Pattern:**
```
\bNick\b
```
Matches: "Nick" as whole word (not "Nickname")

**Case Insensitive:**
```
(?i)\bnick\b
```

---

#### 2. Find Dialogue

**Pattern:**
```
"[^"]*"
```
Matches: Text in quotes (dialogue)

**With Speaker:**
```
Nick said, "[^"]*"
```

---

#### 3. Find Numbers/Dates

**Pattern:**
```
\b197[0-9]\b
```
Matches: Years 1970-1979

**Pattern:**
```
\b\d{1,2}\/\d{1,2}\/\d{4}\b
```
Matches: Dates like "11/14/1976"

---

#### 4. Find Repeated Words

**Pattern:**
```
\b(\w+)\s+\1\b
```
Matches: Same word twice (e.g., "the the")

---

#### 5. Find Long Sentences

**Pattern:**
```
[^.!?]{100,}[.!?]
```
Matches: Sentences over 100 characters

---

#### 6. Find Inconsistent Capitalization

**Pattern:**
```
\bnick\b
```
Matches: Lowercase "nick" (should be "Nick")

---

### Multi-File Search & Replace

#### How to Use

1. **Open Search:**
   - `Cmd+Shift+F` (Search)
   - `Cmd+Option+F` (Replace)

2. **Enable Regex:**
   - Click `.*` button (regex toggle)
   - Or use `Alt+Cmd+R` (Mac)

3. **Select Files:**
   - Use "files to include" field
   - Examples:
     - `Draft_1/**/*.txt` - All text files in Draft_1
     - `**/Chapter_*.txt` - All chapter files
     - `Story_Bible/**` - All Story Bible files

4. **Exclude Files:**
   - Use "files to exclude" field
   - Example: `**/node_modules/**`

5. **Preview Changes:**
   - Review before replacing
   - See all matches
   - Verify context

6. **Replace:**
   - Click "Replace All"
   - Or replace one by one

---

### Practical Examples

#### Example 1: Fix Character Name Consistency

**Find:**
```
\bnick\b
```
**Replace:**
```
Nick
```
**Files:** `Draft_1/**/*.txt`

**Result:** All lowercase "nick" → "Nick"

---

#### Example 2: Update Year References

**Find:**
```
\b1976\b
```
**Replace:**
```
1977
```
**Files:** `Draft_1/Act_II/**/*.txt`

**Result:** Update year in Act II only

---

#### Example 3: Fix Dialogue Formatting

**Find:**
```
"([^"]*)"\s*,\s*said\s+Nick
```
**Replace:**
```
"$1," Nick said
```
**Files:** `Draft_1/**/*.txt`

**Result:** Standardize dialogue format

---

#### Example 4: Remove Extra Spaces

**Find:**
```
\s{2,}
```
**Replace:**
```
 
```
**Files:** `Draft_1/**/*.txt`

**Result:** Multiple spaces → single space

---

#### Example 5: Fix Repeated Words

**Find:**
```
\b(\w+)\s+\1\b
```
**Replace:**
```
$1
```
**Files:** `Draft_1/**/*.txt`

**Result:** "the the" → "the"

---

#### Example 6: Standardize Date Format

**Find:**
```
\b(\d{1,2})\/(\d{1,2})\/(\d{4})\b
```
**Replace:**
```
$3-$1-$2
```
**Files:** `Draft_1/**/*.txt`

**Result:** "11/14/1976" → "1976-11-14"

---

### Advanced Regex Techniques

#### Capture Groups

**Pattern:**
```
(\w+)\s+said, "([^"]*)"
```
**Groups:**
- `$1` = Speaker name
- `$2` = Dialogue

**Replace:**
```
"$2," $1 said
```
**Result:** Reorder dialogue and speaker

---

#### Lookahead/Lookbehind

**Positive Lookahead:**
```
\bNick\b(?=\s+said)
```
Matches: "Nick" only if followed by " said"

**Negative Lookahead:**
```
\bNick\b(?!\s+Johnson)
```
Matches: "Nick" not followed by " Johnson"

---

#### Non-Greedy Matching

**Greedy (default):**
```
".*"
```
Matches: Longest possible match

**Non-Greedy:**
```
".*?"
```
Matches: Shortest possible match

---

### Search & Replace Best Practices

1. **Always Preview:**
   - Review matches before replacing
   - Check context
   - Verify accuracy

2. **Start Small:**
   - Test on one file first
   - Then expand to multiple files
   - Use version control (Git)

3. **Use Version Control:**
   - Commit before large replaces
   - Easy to revert if needed
   - Track changes

4. **Document Patterns:**
   - Save useful regex patterns
   - Document in notepads
   - Share with team

5. **Be Careful:**
   - Regex is powerful but dangerous
   - Test thoroughly
   - Backup important files

---

### Regex Testing

**Test Regex Online:**
- https://regex101.com/
- https://regexr.com/

**Test in Cursor:**
- Use Search with regex enabled
- Preview matches
- Verify before replacing

---

## SUMMARY & NEXT STEPS

### ✅ Setup Complete:
- Notepads directory created
- Discovery journal started

### 🎯 Mastery Priorities:

1. **Composer Multi-File:**
   - Practice with 2-3 files
   - Use @ references
   - Build up to larger compositions

2. **Chat Advanced Context:**
   - Use @ file references
   - Leverage memory integration
   - Chain questions for deep dives

3. **Terminal Automation:**
   - Create scripts directory
   - Build automation scripts
   - Document in notepads

4. **Search & Replace:**
   - Practice regex patterns
   - Test before replacing
   - Build pattern library

---

**Created:** January 24, 2026  
**Status:** Ready for exploration and mastery
