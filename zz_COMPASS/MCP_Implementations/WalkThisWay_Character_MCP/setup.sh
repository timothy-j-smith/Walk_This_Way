#!/bin/bash

# Walk This Way - Character MCP Setup Script
# Run this to automatically set up the MCP server

set -e  # Exit on error

echo "=========================================="
echo "Walk This Way - Character MCP Setup"
echo "=========================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
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
echo "1. Add this to your Cursor MCP settings file:"
echo "   Location: ~/.cursor/mcp_settings.json"
echo ""
echo "   Add this configuration:"
echo ""
echo '   {'
echo '     "mcpServers": {'
echo '       "walkthisway-characters": {'
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
echo "   'Use walkthisway-characters MCP to list all characters'"
echo ""
echo "=========================================="
echo ""

# Optionally test the server
read -p "Would you like to test the server now? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Testing server (press Ctrl+C to stop)..."
    echo "If you see no errors, the server is working!"
    echo ""
    sleep 2
    timeout 3 python3 server.py || true
    echo ""
    echo "✓ Server test complete (no errors = success)"
fi

echo ""
echo "Setup script finished!"
