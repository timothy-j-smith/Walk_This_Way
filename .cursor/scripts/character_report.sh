#!/bin/bash
# Character Mention Report
# Usage: ./character_report.sh "Character Name"

CHARACTER="$1"
if [ -z "$CHARACTER" ]; then
    echo "Usage: $0 <character_name>"
    echo "Example: $0 \"Nick Johnson\""
    exit 1
fi

echo "=== $CHARACTER Mention Report ==="
echo ""

# Total mentions
TOTAL=$(grep -roh "$CHARACTER" Draft_1/ --include="*.txt" 2>/dev/null | wc -l | tr -d ' ')
echo "Total mentions: $TOTAL"
echo ""

# By chapter
echo "By chapter:"
find Draft_1 -name "*.txt" -exec sh -c '
    count=$(grep -o "$1" "$2" 2>/dev/null | wc -l | tr -d " ")
    if [ "$count" -gt 0 ]; then
        echo "  $(basename "$2"): $count mentions"
    fi
' _ "$CHARACTER" {} \;
