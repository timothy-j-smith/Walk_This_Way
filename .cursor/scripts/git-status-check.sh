#!/bin/bash
# Git Status Check and Reminder
# Checks if work needs to be committed

echo ""
echo "📦 GIT STATUS CHECK"
echo "==================="
echo ""

if ! command -v git &> /dev/null; then
    echo "Git not found. Skipping Git check."
    echo ""
    exit 0
fi

# Check if in Git repository
if [ ! -d ".git" ]; then
    echo "Not a Git repository. Skipping Git check."
    echo ""
    exit 0
fi

# Get status
STATUS=$(git status --short 2>/dev/null)

if [ -z "$STATUS" ]; then
    echo "✅ Working directory clean"
    echo "   All changes committed"
    echo ""
else
    echo "⚠️  Uncommitted changes detected:"
    echo ""
    echo "$STATUS" | head -10
    echo ""
    echo "💡 Consider committing your work:"
    echo "   git add ."
    echo "   git commit -m 'Your commit message'"
    echo "   git push"
    echo ""
fi

# Check if behind remote
BEHIND=$(git status -sb 2>/dev/null | grep -o 'behind [0-9]*' || echo "")
if [ ! -z "$BEHIND" ]; then
    echo "📥 Remote updates available"
    echo "   Consider: git pull"
    echo ""
fi

echo "✅ Git check complete"
echo ""
