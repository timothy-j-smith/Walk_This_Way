#!/bin/bash

# COMPASS Writing Guides MCP - Setup Script
# Comprehensive fiction writing reference database

set -e  # Exit on error

echo "=========================================="
echo "COMPASS Writing Guides MCP Setup"
echo "=========================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
echo ""

# Check if data file exists
echo "Checking data file..."
if [ ! -f "data/writing_guides.json" ]; then
    echo "ERROR: data/writing_guides.json not found!"
    exit 1
fi
echo "✓ Found data/writing_guides.json"
echo ""

# Check Python 3 installation
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✓ Found: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Removing old one..."
    rm -rf venv
fi

python3 -m venv venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing MCP package..."
pip install --quiet --upgrade pip
pip install --quiet mcp
echo "✓ MCP package installed"
echo ""

# Make server executable
echo "Making server.py executable..."
chmod +x server.py
echo "✓ server.py is now executable"
echo ""

# Get full path to Python in venv
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"
SERVER_PATH="$SCRIPT_DIR/server.py"

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Add this to your Cursor MCP settings:"
echo "   Location: ~/.cursor/mcp.json (or .cursor/config/mcp.json)"
echo ""
echo '   {'
echo '     "mcpServers": {'
echo '       "compass-writing-guides": {'
echo "         \"command\": \"$VENV_PYTHON\","
echo '         "args": ['
echo "           \"$SERVER_PATH\""
echo '         ]'
echo '       }'
echo '     }'
echo '   }'
echo ""
echo "2. Completely quit and restart Cursor"
echo ""
echo "3. Test with this prompt:"
echo "   'Use compass-writing-guides MCP to get Stephen King's advice on adverbs'"
echo ""
echo "Available queries:"
echo "  - Get author advice (Stephen King, Anne Lamott, etc.)"
echo "  - Get topic guidance (dialogue, pacing, character, etc.)"
echo "  - Get author style guides"
echo "  - Get writing quotes"
echo "  - Get techniques"
echo "  - Get genre guidance"
echo "  - Search across all guides"
echo ""
echo "=========================================="
echo ""
echo "Setup script finished!"
echo ""
echo "Read README.md for detailed usage instructions."
