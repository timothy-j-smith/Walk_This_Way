#!/bin/bash

# MCP Setup Script for Walk This Way
# Installs GitKraken CLI and sets up GitHub token

set -e  # Exit on error

echo "=========================================="
echo "MCP Setup - GitKraken & GitHub"
echo "=========================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
echo ""

# ============================================
# STEP 1: GitKraken CLI Setup
# ============================================

echo "----------------------------------------"
echo "STEP 1: GitKraken CLI"
echo "----------------------------------------"
echo ""

# Check if GitKraken CLI is already installed
if command -v gk &> /dev/null; then
    echo "✓ GitKraken CLI is already installed"
    gk --version
    echo ""
else
    echo "GitKraken CLI is not installed."
    echo ""
    echo "To install GitKraken CLI:"
    echo ""
    echo "1. Open GitKraken application"
    echo "2. Go to Preferences → CLI"
    echo "3. Click 'Enable CLI' button"
    echo "4. Follow the instructions to add to your PATH"
    echo ""
    echo "OR install via Homebrew:"
    echo "  brew install --cask gitkraken-cli"
    echo ""
    read -p "Press ENTER after you've installed GitKraken CLI, or type 'skip' to skip: " answer
    
    if [ "$answer" = "skip" ]; then
        echo "⏭️  Skipping GitKraken CLI setup"
    else
        # Check again after user claims to have installed
        if command -v gk &> /dev/null; then
            echo "✓ GitKraken CLI detected!"
            gk --version
        else
            echo "⚠️  GitKraken CLI still not found. You can set it up later."
            echo "   The gitkraken MCP server will remain disabled until CLI is installed."
        fi
    fi
    echo ""
fi

# ============================================
# STEP 2: GitHub Token Setup
# ============================================

echo "----------------------------------------"
echo "STEP 2: GitHub Token"
echo "----------------------------------------"
echo ""

# Check if GITHUB_TOKEN is already set
if [ -n "$GITHUB_TOKEN" ]; then
    echo "✓ GITHUB_TOKEN environment variable is set"
    echo "  (Token is hidden for security)"
    echo ""
else
    echo "GITHUB_TOKEN environment variable is not set."
    echo ""
    echo "To create a GitHub token:"
    echo ""
    echo "1. Go to: https://github.com/settings/tokens"
    echo "2. Click 'Generate new token' → 'Generate new token (classic)'"
    echo "3. Name it: 'Cursor MCP Walk This Way'"
    echo "4. Select scopes:"
    echo "   - repo (Full control of private repositories)"
    echo "   - read:org (Read org and team membership)"
    echo "5. Click 'Generate token'"
    echo "6. COPY the token (you won't see it again!)"
    echo ""
    read -p "Enter your GitHub token (or press ENTER to skip): " token
    
    if [ -z "$token" ]; then
        echo "⏭️  Skipping GitHub token setup"
        echo ""
        echo "You can set it up later by adding to your shell profile:"
        echo "  export GITHUB_TOKEN='your-token-here'"
        echo ""
    else
        # Add to shell profile
        SHELL_PROFILE=""
        if [ -f "$HOME/.zshrc" ]; then
            SHELL_PROFILE="$HOME/.zshrc"
        elif [ -f "$HOME/.bash_profile" ]; then
            SHELL_PROFILE="$HOME/.bash_profile"
        elif [ -f "$HOME/.bashrc" ]; then
            SHELL_PROFILE="$HOME/.bashrc"
        fi
        
        if [ -n "$SHELL_PROFILE" ]; then
            # Check if already exists
            if grep -q "GITHUB_TOKEN" "$SHELL_PROFILE"; then
                echo "⚠️  GITHUB_TOKEN already exists in $SHELL_PROFILE"
                echo "   Please update it manually or remove the old entry first."
            else
                echo "" >> "$SHELL_PROFILE"
                echo "# GitHub Token for Cursor MCP (Walk This Way)" >> "$SHELL_PROFILE"
                echo "export GITHUB_TOKEN='$token'" >> "$SHELL_PROFILE"
                echo ""
                echo "✓ Added GITHUB_TOKEN to $SHELL_PROFILE"
                echo ""
                echo "⚠️  IMPORTANT: You need to restart your terminal or run:"
                echo "   source $SHELL_PROFILE"
                echo ""
                echo "   Then restart Cursor for the MCP server to pick up the token."
            fi
        else
            echo "⚠️  Could not find shell profile (.zshrc, .bash_profile, or .bashrc)"
            echo "   Please manually add to your shell profile:"
            echo "   export GITHUB_TOKEN='$token'"
        fi
        echo ""
    fi
fi

# ============================================
# STEP 3: Verification
# ============================================

echo "----------------------------------------"
echo "STEP 3: Verification"
echo "----------------------------------------"
echo ""

# Check GitKraken
if command -v gk &> /dev/null; then
    echo "✅ GitKraken CLI: INSTALLED"
else
    echo "❌ GitKraken CLI: NOT INSTALLED"
fi

# Check GitHub Token
if [ -n "$GITHUB_TOKEN" ]; then
    echo "✅ GitHub Token: SET"
else
    echo "❌ GitHub Token: NOT SET"
    echo "   (You may need to restart terminal after adding to shell profile)"
fi

echo ""

# ============================================
# STEP 4: Enable MCP Servers
# ============================================

echo "----------------------------------------"
echo "STEP 4: Enable MCP Servers"
echo "----------------------------------------"
echo ""

MCP_CONFIG=".cursor/config/mcp.json"

if [ ! -f "$MCP_CONFIG" ]; then
    echo "⚠️  MCP config file not found: $MCP_CONFIG"
    echo "   Skipping auto-enable"
else
    echo "To enable GitKraken or GitHub MCP servers:"
    echo ""
    echo "1. Open: $MCP_CONFIG"
    echo "2. Change 'disabled: true' to 'disabled: false' for:"
    
    if command -v gk &> /dev/null; then
        echo "   - gitkraken (if you want to use it)"
    else
        echo "   - gitkraken (SKIP - CLI not installed)"
    fi
    
    if [ -n "$GITHUB_TOKEN" ]; then
        echo "   - github (if you want to use it)"
    else
        echo "   - github (SKIP - token not set)"
    fi
    
    echo ""
    echo "3. Restart Cursor completely for changes to take effect"
    echo ""
fi

# ============================================
# DONE
# ============================================

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. If you set up GitHub token, restart your terminal or run:"
echo "   source ~/.zshrc"
echo ""
echo "2. Enable MCP servers in .cursor/config/mcp.json (see Step 4 above)"
echo ""
echo "3. Restart Cursor completely"
echo ""
echo "4. Test with prompts like:"
echo "   - 'Show me recent git commits' (GitKraken)"
echo "   - 'Show me the README from my GitHub repo' (GitHub)"
echo ""
