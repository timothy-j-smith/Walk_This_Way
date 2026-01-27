#!/bin/bash
# Setup script for Cursor Workflow Orchestrator MCP

set -e

echo "🚀 Setting up Cursor Workflow Orchestrator MCP..."

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check Python version (MCP requires Python 3.10+)
# Try Python 3.10, 3.11, 3.12 first, then fall back to python3
PYTHON_CMD=""
for py in python3.12 python3.11 python3.10 python3; do
    if command -v $py &> /dev/null; then
        PYTHON_VERSION=$($py --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
        REQUIRED_VERSION="3.10"
        if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
            PYTHON_CMD=$py
            echo "✅ Found Python $PYTHON_VERSION ($py)"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Error: MCP requires Python 3.10+, but no compatible version found"
    echo ""
    echo "Solutions:"
    echo "1. Install Python 3.10+ via Homebrew: brew install python@3.10"
    echo "2. Or download from: https://www.python.org/downloads/"
    echo ""
    echo "After installing, run this script again"
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment with $PYTHON_CMD..."
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --quiet --upgrade pip

# Install MCP SDK
echo "📥 Installing MCP SDK..."
pip install --quiet mcp

# Make server executable
echo "🔐 Making server executable..."
chmod +x server.py

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Add this MCP to .cursor/config/mcp.json"
echo "2. Restart Cursor"
echo "3. Test with: Use cursor-workflow-orchestrator to list all available MCPs"
