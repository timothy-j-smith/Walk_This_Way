#!/bin/bash

# COMPASS Character MCP Template - Setup Script
# Run this after copying template to your novel's directory

set -e  # Exit on error

echo "=========================================="
echo "COMPASS Character MCP Template Setup"
echo "=========================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
echo ""

# Check if template has been renamed
echo "Checking template setup..."
if [ -f "data/characters_template.json" ] && [ ! -f "data/characters.json" ]; then
    echo "⚠ Template not yet initialized"
    echo ""
    read -p "Copy characters_template.json to characters.json? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp data/characters_template.json data/characters.json
        echo "✓ Created data/characters.json"
        echo ""
        echo "IMPORTANT: Edit data/characters.json and replace all"
        echo "WRITE_X_HERE placeholders with your novel's character data"
        echo ""
    else
        echo "Skipping character file creation."
        echo "Remember to create data/characters.json before using MCP!"
        echo ""
    fi
elif [ -f "data/characters.json" ]; then
    echo "✓ Found data/characters.json"
    echo ""
else
    echo "ERROR: Cannot find character template file!"
    exit 1
fi

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

# Extract directory name for suggested MCP name
DIR_NAME=$(basename "$SCRIPT_DIR")
MCP_NAME=$(echo "$DIR_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/_/-/g')

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Edit data/characters.json:"
echo "   - Replace CHARACTER_NAME_1 with your character names"
echo "   - Replace all WRITE_X_HERE placeholders"
echo "   - Delete the _TEMPLATE_NOTES section"
echo ""
echo "2. Add this to your Cursor MCP settings:"
echo "   Location: ~/.cursor/mcp_settings.json"
echo ""
echo '   {'
echo '     "mcpServers": {'
echo "       \"$MCP_NAME\": {"
echo "         \"command\": \"$VENV_PYTHON\","
echo '         "args": ['
echo "           \"$SERVER_PATH\""
echo '         ]'
echo '       }'
echo '     }'
echo '   }'
echo ""
echo "3. Completely quit and restart Cursor"
echo ""
echo "4. Test with this prompt:"
echo "   'Use $MCP_NAME MCP to list all characters'"
echo ""
echo "=========================================="
echo ""
echo "Setup script finished!"
echo ""
echo "Read README.md for detailed usage instructions."
