#!/bin/bash
# ACE Stop Wrapper - Debounces the ACE stop hook to once per day (86400 seconds)
# This wrapper calls the real ace_stop_hook.sh but only allows the followup_message
# to appear once every 24 hours. Data is still saved silently every time.

DEBOUNCE_SECONDS=86400
ace_dir=".cursor/ace"
timestamp_file="$ace_dir/.last_summary_time"
now=$(date +%s)

# Read stdin (hook input) and save it for passthrough
input=$(cat)

# Always silently save transcript path (don't lose data)
transcript_path=$(echo "$input" | jq -r '.transcript_path // empty' 2>/dev/null)
if [ -n "$transcript_path" ]; then
  mkdir -p "$ace_dir"
  echo "{\"transcript_path\": \"$transcript_path\", \"saved_at\": \"$(date -Iseconds)\"}" > "$ace_dir/last_transcript.json" 2>/dev/null
fi

# Check debounce
if [ -f "$timestamp_file" ]; then
  last_time=$(head -1 "$timestamp_file" 2>/dev/null || echo "0")
  elapsed=$((now - last_time))
  if [ "$elapsed" -lt "$DEBOUNCE_SECONDS" ]; then
    # Suppressed - too soon since last notification
    echo '{}'
    exit 0
  fi
fi

# Debounce passed - update timestamp and run the real hook
echo "$now" > "$timestamp_file" 2>/dev/null

# Pass input to the real ACE stop hook
echo "$input" | bash .cursor/scripts/ace_stop_hook.sh
