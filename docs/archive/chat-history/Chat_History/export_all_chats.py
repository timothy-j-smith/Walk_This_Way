#!/usr/bin/env python3
"""
Automated Chat Export Script
Exports ALL chats from cursor-view to markdown files in iCloud folder
These files will automatically sync to MacBook Air
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import urllib.parse
import urllib.request

# Configuration
API_BASE = "http://localhost:5001"
PROJECT_DIR = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
CHAT_HISTORY_DIR = PROJECT_DIR / ".cursor/docs/Chat_History"
HANK_DIR = CHAT_HISTORY_DIR / "HANK"
OTHER_DIR = CHAT_HISTORY_DIR / "Other"

# Keywords that indicate HANK chats
HANK_KEYWORDS = ["HANK", "COMPASS", "DISCO", "MCP", "agent", "super agent"]

def check_server():
    """Check if the server is running"""
    try:
        req = urllib.request.Request(f"{API_BASE}/api/chats")
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except:
        return False

def get_all_chats():
    """Get all chats from the API"""
    try:
        req = urllib.request.Request(f"{API_BASE}/api/chats")
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        print(f"❌ Error fetching chats: {e}")
        return None

def format_date(timestamp):
    """Convert timestamp to readable date"""
    try:
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d")
    except:
        return "unknown-date"

def is_hank_chat(chat):
    """Determine if a chat is a HANK chat based on content"""
    messages = chat.get("messages", [])
    project_name = chat.get("project", {}).get("name", "")
    
    # Check project name
    if "HANK" in project_name.upper():
        return True
    
    # Check message content
    for msg in messages[:5]:  # Check first 5 messages
        content = msg.get("content", "").upper()
        if any(keyword in content for keyword in HANK_KEYWORDS):
            return True
    
    return False

def get_existing_session_ids(output_dir):
    """Get all session IDs from already exported files"""
    existing_ids = set()
    if not output_dir.exists():
        return existing_ids
    
    for file_path in output_dir.glob("*.md"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Look for Session ID in the file
                if "**Session ID:**" in content:
                    for line in content.split("\n"):
                        if "**Session ID:**" in line:
                            session_id = line.split("**Session ID:**")[1].strip()
                            existing_ids.add(session_id)
                            break
        except:
            continue
    
    return existing_ids

def create_markdown_filename(chat):
    """Create a filename for the chat"""
    date = format_date(chat.get("date", 0))
    project = chat.get("project", {}).get("name", "Unknown")
    
    # Get first user message as topic hint
    topic = "Chat"
    for msg in chat.get("messages", []):
        if msg.get("role") == "user":
            content = msg.get("content", "")[:50]
            # Clean up content for filename
            topic = "".join(c if c.isalnum() or c in (" ", "-", "_") else "" for c in content)
            topic = topic.replace(" ", "_")[:40]
            break
    
    return f"{date}_{topic}.md"

def export_chat_to_markdown(chat, output_path):
    """Export a single chat to markdown"""
    date = format_date(chat.get("date", 0))
    project = chat.get("project", {}).get("name", "Unknown Project")
    session_id = chat.get("session_id", "unknown")
    
    with open(output_path, "w", encoding="utf-8") as f:
        # Write header
        f.write(f"# Chat Export\n")
        f.write(f"**Date:** {date}\n")
        f.write(f"**Project:** {project}\n")
        f.write(f"**Session ID:** {session_id}\n")
        f.write(f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\n---\n\n")
        
        # Write messages
        messages = chat.get("messages", [])
        for i, msg in enumerate(messages, 1):
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            
            if role == "user":
                f.write(f"## User Message {i}\n\n")
            else:
                f.write(f"## Assistant Response {i}\n\n")
            
            f.write(f"{content}\n\n")
            f.write("---\n\n")

def main():
    print("🔍 Checking if server is running...")
    if not check_server():
        print("❌ Server is not running!")
        print("   Please start it first:")
        print("   cd /tmp/cursor-view && python3 server.py --port 5001")
        sys.exit(1)
    
    print("✅ Server is running")
    print("")
    
    print("📥 Fetching all chats...")
    chats = get_all_chats()
    
    if not chats:
        print("❌ No chats found or error occurred")
        sys.exit(1)
    
    print(f"✅ Found {len(chats)} chats")
    print("")
    
    # Create directories
    HANK_DIR.mkdir(parents=True, exist_ok=True)
    OTHER_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get already exported session IDs to avoid duplicates
    existing_hank_ids = get_existing_session_ids(HANK_DIR)
    existing_other_ids = get_existing_session_ids(OTHER_DIR)
    
    # Export each chat
    hank_count = 0
    other_count = 0
    skipped_count = 0
    
    for i, chat in enumerate(chats, 1):
        session_id = chat.get("session_id", "unknown")
        is_hank = is_hank_chat(chat)
        output_dir = HANK_DIR if is_hank else OTHER_DIR
        existing_ids = existing_hank_ids if is_hank else existing_other_ids
        
        # Skip if already exported
        if session_id in existing_ids:
            skipped_count += 1
            if is_hank:
                print(f"  ⏭️  [{i}/{len(chats)}] HANK: Already exported (skipped)")
            else:
                print(f"  ⏭️  [{i}/{len(chats)}] Other: Already exported (skipped)")
            continue
        
        filename = create_markdown_filename(chat)
        output_path = output_dir / filename
        
        # Handle duplicate filenames (shouldn't happen now, but just in case)
        counter = 1
        original_path = output_path
        while output_path.exists():
            stem = original_path.stem
            output_path = output_dir / f"{stem}_{counter}.md"
            counter += 1
        
        export_chat_to_markdown(chat, output_path)
        
        if is_hank:
            hank_count += 1
            print(f"  ✅ [{i}/{len(chats)}] HANK: {filename}")
        else:
            other_count += 1
            print(f"  ✅ [{i}/{len(chats)}] Other: {filename}")
    
    print("")
    print("=" * 60)
    print("✅ EXPORT COMPLETE!")
    print("=" * 60)
    print(f"📊 Total chats processed: {len(chats)}")
    print(f"   - New HANK chats: {hank_count}")
    print(f"   - New Other chats: {other_count}")
    print(f"   - Already exported (skipped): {skipped_count}")
    print("")
    print(f"📁 Location: {CHAT_HISTORY_DIR}")
    print("")
    print("💾 These files are in your iCloud folder and will")
    print("   automatically sync to your MacBook Air!")
    print("")

if __name__ == "__main__":
    main()
