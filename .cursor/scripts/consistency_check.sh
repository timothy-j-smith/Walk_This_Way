#!/bin/bash
# Consistency Check Script
# Usage: ./consistency_check.sh

echo "=== Consistency Check Report ==="
echo ""

echo "📅 Age Mentions:"
grep -rn "age\|years old" Draft_1/ --include="*.txt" 2>/dev/null | head -20
echo ""

echo "📅 Date Mentions:"
grep -rn "197[0-9]\|198[0-9]" Draft_1/ --include="*.txt" 2>/dev/null | head -20
echo ""

echo "📍 Location Mentions:"
grep -rn "Boston\|Sudbury" Draft_1/ --include="*.txt" 2>/dev/null | head -20
echo ""

echo "✅ Check complete!"
