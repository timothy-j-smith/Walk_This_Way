#!/bin/bash
# Daily Word Count Tracker
# Usage: ./word_count.sh

TOTAL=$(find Draft_1 -name "*.txt" -exec cat {} + 2>/dev/null | wc -w)
TODAY=$(date +"%Y-%m-%d")
LOG_FILE=".cursor/logs/word_count.log"

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Append to log
echo "$TODAY: $TOTAL words" >> "$LOG_FILE"

# Display result
echo "📊 Word Count Report"
echo "==================="
echo "Total words: $TOTAL"
echo "Date: $TODAY"
echo ""
echo "Logged to: $LOG_FILE"
