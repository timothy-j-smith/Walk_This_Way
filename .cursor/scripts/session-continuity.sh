#!/bin/bash
# Session Continuity Check
# Shows where you left off and what's next

LOG_FILE=".cursor/logs/writing-sessions.jsonl"

echo ""
echo "📖 SESSION CONTINUITY CHECK"
echo "============================"
echo ""

if [ ! -f "$LOG_FILE" ] || [ ! -s "$LOG_FILE" ]; then
    echo "No previous session found."
    echo "This appears to be a new project or first session."
    echo ""
    exit 0
fi

# Get last session entry
LAST_SESSION=$(tail -1 "$LOG_FILE" 2>/dev/null)

if [ -z "$LAST_SESSION" ]; then
    echo "No session data found."
    echo ""
    exit 0
fi

# Extract key information (basic parsing)
echo "Last Session Summary:"
echo "---------------------"
echo "$LAST_SESSION" | python3 -m json.tool 2>/dev/null || echo "$LAST_SESSION"
echo ""

# Check for recent file modifications
echo "Recent File Activity:"
echo "-------------------"
find . -name "*.md" -o -name "*.txt" -type f -mtime -7 2>/dev/null | head -10
echo ""

echo "✅ Use '/session-continuity' in Cursor Chat for detailed analysis"
echo ""
