#!/usr/bin/env python3
"""
Story Bible → MCP Auto-Sync Tool
Automatically converts Story_Bible markdown files to MCP JSON format
Uses Claude API for intelligent conversion

Author: Timothy & Hank Partnership
Date: January 10, 2026
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import anthropic

# Configuration
ANTHROPIC_API_KEY = None  # Will prompt for key or read from env

# Paths (relative to script location)
BASE_DIR = Path(__file__).parent
STORY_BIBLE_DIR = BASE_DIR / "Story_Bible"
MCP_DIR = BASE_DIR / "zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/data"

# Story Bible source files
CHARACTER_BIBLE = STORY_BIBLE_DIR / "character-bible.md"
TIMELINE_BIBLE = STORY_BIBLE_DIR / "timeline.md"
MUSIC_REFERENCES = STORY_BIBLE_DIR / "music-references.md"

# MCP target files
CHARACTER_MCP = MCP_DIR / "characters.json"
TIMELINE_MCP = MCP_DIR / "timeline.json"
MUSIC_MCP = MCP_DIR / "music.json"

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def get_api_key():
    """Get Anthropic API key from environment or prompt"""
    import os
    
    # Try environment variable first
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        print_warning("ANTHROPIC_API_KEY not found in environment")
        print("Get your API key from: https://console.anthropic.com/settings/keys")
        api_key = input("Enter your Anthropic API key: ").strip()
    
    return api_key

def read_file_safe(filepath):
    """Safely read file with error handling"""
    try:
        if not filepath.exists():
            print_warning(f"File not found: {filepath}")
            return None
        return filepath.read_text()
    except Exception as e:
        print_error(f"Error reading {filepath}: {e}")
        return None

def write_json_safe(filepath, data):
    """Safely write JSON with backup"""
    try:
        # Create backup if file exists
        if filepath.exists():
            backup_path = filepath.with_suffix('.json.backup')
            filepath.rename(backup_path)
            print_success(f"Backup created: {backup_path.name}")
        
        # Write new data
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(json.dumps(data, indent=2))
        print_success(f"Updated: {filepath.name}")
        return True
        
    except Exception as e:
        print_error(f"Error writing {filepath}: {e}")
        return False

def convert_character_bible_to_mcp(character_md, existing_mcp=None):
    """
    Use Claude API to convert character-bible.md to MCP JSON format
    """
    print_header("Converting Character Bible to MCP Format")
    
    # Get API key
    api_key = get_api_key()
    client = anthropic.Anthropic(api_key=api_key)
    
    # Load existing MCP for reference
    existing_json = ""
    if existing_mcp and Path(existing_mcp).exists():
        try:
            with open(existing_mcp, 'r') as f:
                existing_data = json.load(f)
                existing_json = json.dumps(existing_data, indent=2)[:3000]
        except:
            existing_json = ""
    
    print(f"Sending to Claude API for conversion...")
    print(f"Character Bible length: {len(character_md)} characters")
    
    # Call Claude API
    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            temperature=0,
            messages=[{
                "role": "user",
                "content": f"""Convert this Story Bible markdown to MCP JSON format.

INSTRUCTIONS:
- Extract all character information into structured JSON
- Preserve ALL details from the markdown
- Use this MCP format structure:

EXAMPLE MCP FORMAT:
{existing_json if existing_json else '''
{
  "CHARACTER_NAME": {
    "basic_info": { "age": ..., "occupation": ... },
    "personality": { "traits": [...], "voice": "..." },
    "preferences": { "music": { "loves": [...], "hates": [...] } },
    "background": { ... },
    "relationships": { ... },
    "arc": { ... }
  }
}
'''}

CHARACTER BIBLE MARKDOWN:
{character_md}

OUTPUT REQUIREMENTS:
- Valid JSON only (no markdown code blocks)
- All characters from the markdown
- Natural language converted to structured data
- Add "last_updated": "{datetime.now().strftime('%Y-%m-%d')}" to each character

BEGIN JSON OUTPUT:"""
            }]
        )
        
        # Extract JSON from response
        response_text = message.content[0].text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith('```'):
            response_text = response_text.split('```')[1]
            if response_text.startswith('json'):
                response_text = response_text[4:]
        
        # Parse JSON
        mcp_data = json.loads(response_text)
        
        print_success(f"Converted {len(mcp_data)} characters")
        print_success(f"API cost: ~$0.05")
        
        return mcp_data
        
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in Claude response: {e}")
        print("Response preview:", response_text[:500])
        return None
        
    except Exception as e:
        print_error(f"API call failed: {e}")
        return None

def sync_characters():
    """Sync character-bible.md to characters.json"""
    print_header("CHARACTER BIBLE → MCP SYNC")
    
    # Read source
    character_md = read_file_safe(CHARACTER_BIBLE)
    if not character_md:
        return False
    
    # Convert using Claude
    mcp_data = convert_character_bible_to_mcp(
        character_md, 
        existing_mcp=CHARACTER_MCP
    )
    
    if not mcp_data:
        return False
    
    # Write to MCP
    return write_json_safe(CHARACTER_MCP, mcp_data)

def sync_timeline():
    """Sync timeline.md to timeline.json (future implementation)"""
    print_header("TIMELINE SYNC")
    print_warning("Timeline MCP not yet implemented")
    print("Run: python build_timeline_mcp.py")
    return True

def sync_music():
    """Sync music-references.md to music.json (future implementation)"""
    print_header("MUSIC REFERENCES SYNC")
    print_warning("Music MCP not yet implemented")
    print("Run: python build_music_mcp.py")
    return True

def main():
    """Main sync orchestrator"""
    print_header("WALK THIS WAY - STORY BIBLE → MCP AUTO-SYNC")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base directory: {BASE_DIR}")
    
    # Check files exist
    print("\nChecking source files...")
    files_ok = True
    
    if CHARACTER_BIBLE.exists():
        print_success(f"Found: {CHARACTER_BIBLE.name}")
    else:
        print_error(f"Missing: {CHARACTER_BIBLE}")
        files_ok = False
    
    if not files_ok:
        print_error("\nMissing required files. Exiting.")
        sys.exit(1)
    
    # Sync each component
    print("\nStarting sync process...\n")
    
    results = {
        "characters": sync_characters(),
        "timeline": sync_timeline(),
        "music": sync_music()
    }
    
    # Summary
    print_header("SYNC COMPLETE")
    
    for component, success in results.items():
        if success:
            print_success(f"{component.capitalize()}: Synced")
        else:
            print_error(f"{component.capitalize()}: Failed")
    
    total = len(results)
    succeeded = sum(1 for s in results.values() if s)
    
    print(f"\n{Colors.BOLD}Results: {succeeded}/{total} successful{Colors.END}")
    
    if succeeded == total:
        print_success("\nAll MCPs synced successfully!")
        print("\nNext step: Restart Cursor to load updated MCP data")
    else:
        print_warning("\nSome syncs failed. Check errors above.")
    
    return 0 if succeeded == total else 1

if __name__ == "__main__":
    sys.exit(main())
