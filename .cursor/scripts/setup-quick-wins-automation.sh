#!/bin/bash
# SETUP QUICK WINS AUTOMATION
# One-time setup script to configure Quick Wins automation

echo ""
echo "🚀 QUICK WINS AUTOMATION SETUP"
echo "================================"
echo ""

# Create example library directories
echo "📁 Creating example library directories..."
mkdir -p ".cursor/examples/character-voices"
mkdir -p ".cursor/examples/prose-styles"
mkdir -p ".cursor/examples/scene-types"
echo "✅ Example library directories created"

# Make scripts executable
echo ""
echo "🔧 Making scripts executable..."
chmod +x ".cursor/scripts/session-start.sh"
chmod +x ".cursor/scripts/auto-pin-reminder.sh"
echo "✅ Scripts are executable"

# Verify files exist
echo ""
echo "✅ Verifying Quick Wins files..."
if [ -f ".cursor/rules/quick-wins-templates.md" ]; then
    echo "   ✅ Template library exists"
else
    echo "   ⚠️  Template library not found"
fi

if [ -f ".cursor/QUICK_WINS_QUICK_REFERENCE.md" ]; then
    echo "   ✅ Quick reference card exists"
else
    echo "   ⚠️  Quick reference card not found"
fi

if [ -f ".cursor/scripts/session-start.sh" ]; then
    echo "   ✅ Session start script exists"
else
    echo "   ⚠️  Session start script not found"
fi

echo ""
echo "================================"
echo "✅ QUICK WINS AUTOMATION SETUP COMPLETE"
echo ""
echo "📋 NEXT STEPS:"
echo "   1. Run './.cursor/scripts/session-start.sh' at beginning of each session"
echo "   2. Pin files in Cursor UI (Story Bible, Directives, Current Chapter)"
echo "   3. Use '/quick-wins' command in Cursor Chat to open templates"
echo "   4. Build your example library in .cursor/examples/"
echo ""
echo "📖 Quick Reference: .cursor/QUICK_WINS_QUICK_REFERENCE.md"
echo ""
