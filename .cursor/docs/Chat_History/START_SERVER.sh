#!/bin/bash
# Simple script to start the cursor-view server
# Run this whenever you want to view your chats

echo "🚀 Starting cursor-view server..."
echo ""

cd /tmp/cursor-view

# Check if server is already running
if curl -s http://localhost:5001/api/chats > /dev/null 2>&1; then
    echo "✅ Server is already running!"
    echo ""
    echo "🌐 Open in your browser:"
    echo "   http://localhost:5001"
    echo ""
    exit 0
fi

# Start the server
echo "⏳ Starting server on port 5001..."
python3 server.py --port 5001
