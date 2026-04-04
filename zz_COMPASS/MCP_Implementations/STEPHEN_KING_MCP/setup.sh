#!/bin/bash

# Stephen King MCP — "The Writer's Toolbox" — Setup Script
# PRIVATE & CONFIDENTIAL

set -e

echo "=========================================="
echo "Stephen King MCP — The Writer's Toolbox"
echo "=========================================="
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
echo ""

# Check data file
echo "Checking data file..."
if [ ! -f "data/king_analysis.json" ]; then
    echo "ERROR: data/king_analysis.json not found!"
    exit 1
fi
echo "✓ Found data/king_analysis.json"
echo ""

# Check Python 3
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✓ Found: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Removing old virtual environment..."
    rm -rf venv
fi

python3 -m venv venv
echo "✓ Virtual environment created"
echo ""

# Activate and install
echo "Installing dependencies..."
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet mcp
echo "✓ MCP package installed"
echo ""

chmod +x server.py

VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"
SERVER_PATH="$SCRIPT_DIR/server.py"

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Add to Cursor MCP settings (~/.cursor/mcp.json):"
echo ""
echo '  {'
echo '    "mcpServers": {'
echo '      "stephen-king-toolbox": {'
echo "        \"command\": \"$VENV_PYTHON\","
echo '        "args": ['
echo "          \"$SERVER_PATH\""
echo '        ]'
echo '      }'
echo '    }'
echo '  }'
echo ""
echo "Then restart Cursor and test with:"
echo "  'Use stephen-king-toolbox to imagine a story about a kid afraid of the dark'"
echo ""
echo "3 Tools: king_imagine, king_craft, king_revise"
echo "3 Modes: create, transform, edit"
echo "3 Levels: nice, neutral, professional"
echo ""
echo "=========================================="
