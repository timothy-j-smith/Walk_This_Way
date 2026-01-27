# TERMINAL AUTOMATION CHEAT SHEET
**Quick Reference for Common Automation Tasks**

---

## 📊 WORD COUNT & STATISTICS

### Total Word Count
```bash
find Draft_1 -name "*.txt" -exec cat {} + | wc -w
```

### Word Count by Act
```bash
for act in Draft_1/Act_*; do
    echo "$(basename $act):"
    find "$act" -name "*.txt" -exec cat {} + | wc -w
done
```

### Word Count by Chapter
```bash
find Draft_1 -name "*.txt" -exec sh -c 'echo "$(basename "$1"): $(wc -w < "$1") words"' _ {} \;
```

### Daily Word Count (Script)
```bash
.cursor/scripts/word_count.sh
```

---

## 🔍 CHARACTER ANALYSIS

### Count Character Mentions
```bash
grep -roh "Nick Johnson" Draft_1/ --include="*.txt" | wc -l
```

### Character Report (Script)
```bash
.cursor/scripts/character_report.sh "Nick Johnson"
```

### Find Character Dialogue
```bash
grep -n "\"Nick" Draft_1/Act_I/Chapter_*.txt
```

### Character Mentions by Chapter
```bash
find Draft_1 -name "*.txt" -exec sh -c 'count=$(grep -o "$1" "$2" | wc -l); if [ $count -gt 0 ]; then echo "$(basename "$2"): $count"; fi' _ "Nick" {} \;
```

---

## ✅ CONSISTENCY CHECKS

### Consistency Check (Script)
```bash
.cursor/scripts/consistency_check.sh
```

### Find Age Mentions
```bash
grep -i "age\|years old" Draft_1/ --include="*.txt"
```

### Find Date Mentions
```bash
grep -rn "197[0-9]\|198[0-9]" Draft_1/ --include="*.txt"
```

### Find Location Mentions
```bash
grep -rn "Boston\|Sudbury" Draft_1/ --include="*.txt"
```

### Find Repeated Words
```bash
grep -roh "[A-Z][a-z]* [a-z]* [a-z]*" Draft_1/ --include="*.txt" | sort | uniq -d | head -20
```

---

## 📝 TEXT ANALYSIS

### Count Dialogue Lines
```bash
grep -c '".*"' Draft_1/Act_I/Chapter_*.txt
```

### Find Long Sentences (100+ chars)
```bash
grep -E '.{100,}' Draft_1/Act_I/Chapter_*.txt | wc -l
```

### Find Paragraph Count
```bash
for file in Draft_1/Act_I/*.txt; do
    echo "$(basename $file): $(grep -c '^$' $file) paragraphs"
done
```

---

## 🔧 FILE OPERATIONS

### Find All Chapters
```bash
find Draft_1 -name "*.txt" -type f
```

### List Files by Size
```bash
find Draft_1 -name "*.txt" -exec ls -lh {} \; | awk '{print $9, $5}'
```

### Find Empty Files
```bash
find Draft_1 -name "*.txt" -empty
```

### Count Files
```bash
find Draft_1 -name "*.txt" | wc -l
```

---

## 🔄 GIT AUTOMATION

### Quick Commit
```bash
git add -A && git commit -m "WIP: $(date +%Y-%m-%d)"
```

### View Changes
```bash
git diff Draft_1/Act_I/Chapter_4.txt
```

### Find When Character First Mentioned
```bash
git log -p -S "Nick Johnson" -- Draft_1/ | head -50
```

### View Recent Commits
```bash
git log --oneline -10
```

---

## 📋 TODO TRACKING

### Find TODO Comments
```bash
grep -rn "TODO\|FIXME" . --include="*.txt" --include="*.md"
```

### Count TODOs
```bash
grep -r "TODO\|FIXME" . --include="*.txt" --include="*.md" | wc -l
```

---

## 🚀 QUICK SCRIPTS

### Run All Scripts
```bash
cd .cursor/scripts && for script in *.sh; do echo "Running $script..."; ./$script; echo ""; done
```

### Make All Scripts Executable
```bash
chmod +x .cursor/scripts/*.sh
```

---

## 💡 TIPS

1. **Save Common Commands:**
   - Add to this cheat sheet
   - Create aliases in `.zshrc` or `.bashrc`

2. **Create Scripts:**
   - Save reusable commands as scripts
   - Make them executable: `chmod +x script.sh`

3. **Document:**
   - Add notes to notepads
   - Update this cheat sheet

4. **Test First:**
   - Test commands on small files first
   - Use version control (Git)

---

**Last Updated:** January 24, 2026
