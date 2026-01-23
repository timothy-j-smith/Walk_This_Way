#!/bin/bash
# Export All Chats to iCloud - Automated Script
# This exports ALL your chats to markdown files in your iCloud folder
# They will automatically sync to your MacBook Air

echo "🚀 Starting chat export process..."
echo ""

# Get the project directory (iCloud location)
PROJECT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
CHAT_HISTORY_DIR="$PROJECT_DIR/.cursor/docs/Chat_History"

# Create directories if they don't exist
mkdir -p "$CHAT_HISTORY_DIR/HANK"
mkdir -p "$CHAT_HISTORY_DIR/Other"

# Check if server is running
if ! curl -s http://localhost:5001/api/chats > /dev/null 2>&1; then
    echo "⚠️  Server is not running. Starting it now..."
    cd /tmp/cursor-view
    python3 server.py --port 5001 &
    SERVER_PID=$!
    echo "⏳ Waiting for server to start..."
    sleep 5
    
    # Check if server started successfully
    if ! curl -s http://localhost:5001/api/chats > /dev/null 2>&1; then
        echo "❌ Failed to start server. Please start it manually:"
        echo "   cd /tmp/cursor-view && python3 server.py --port 5001"
        exit 1
    fi
    echo "✅ Server started (PID: $SERVER_PID)"
    echo ""
fi

# Run the Python export script
echo "📥 Exporting all chats..."
cd "$PROJECT_DIR"
python3 "$PROJECT_DIR/.cursor/docs/Chat_History/export_all_chats.py"

# Clean up: stop server if we started it
if [ ! -z "$SERVER_PID" ]; then
    echo ""
    echo "🛑 Stopping server..."
    kill $SERVER_PID 2>/dev/null
fi

echo ""
echo "✅ Export complete!"
echo ""
echo "📁 Your chats are saved to:"
echo "   $CHAT_HISTORY_DIR"
echo ""
echo "💾 These files will automatically sync to your MacBook Air via iCloud!"
echo ""
