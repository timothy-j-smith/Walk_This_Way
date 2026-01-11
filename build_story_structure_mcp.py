#!/usr/bin/env python3
"""
Story Structure → MCP Converter
Converts synopsis.md and outline.md to queryable MCP format

Part of COMPASS Writing System
Author: Timothy & Hank Partnership
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import anthropic

# Configuration
BASE_DIR = Path(__file__).parent
STORY_BIBLE_DIR = BASE_DIR / "Story_Bible"
MCP_DIR = BASE_DIR / "zz_COMPASS/MCP_Implementations/WalkThisWay_Story_MCP/data"

# Source files
SYNOPSIS_FILE = STORY_BIBLE_DIR / "synopsis.md"
OUTLINE_FILE = STORY_BIBLE_DIR / "outline.md"

# Target MCP
STORY_STRUCTURE_MCP = MCP_DIR / "story_structure.json"

def convert_synopsis_and_outline():
    """Convert synopsis and outline to structured MCP format"""
    
    print("=" * 60)
    print("SYNOPSIS & OUTLINE → STORY STRUCTURE MCP")
    print("=" * 60)
    
    # Read files
    synopsis = ""
    outline = ""
    
    if SYNOPSIS_FILE.exists():
        synopsis = SYNOPSIS_FILE.read_text()
        print(f"✓ Loaded synopsis ({len(synopsis)} chars)")
    else:
        print(f"⚠ Synopsis file not found: {SYNOPSIS_FILE}")
        print("  Create Story_Bible/synopsis.md with your story synopsis")
    
    if OUTLINE_FILE.exists():
        outline = OUTLINE_FILE.read_text()
        print(f"✓ Loaded outline ({len(outline)} chars)")
    else:
        print(f"⚠ Outline file not found: {OUTLINE_FILE}")
        print("  Create Story_Bible/outline.md with your story outline")
    
    if not synopsis and not outline:
        print("\n✗ No source files found. Exiting.")
        return None
    
    # Get API key
    import os
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        api_key = input("\nEnter Anthropic API key: ").strip()
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Convert using Claude
    print("\nConverting to MCP format...")
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=12000,
            temperature=0,
            messages=[{
                "role": "user",
                "content": f"""Convert this synopsis and outline to structured Story Structure MCP format.

SYNOPSIS:
{synopsis}

OUTLINE:
{outline}

OUTPUT FORMAT (JSON only):
{{
  "synopsis": {{
    "logline": "one-sentence story description",
    "premise": "paragraph description",
    "themes": ["theme1", "theme2"]
  }},
  "acts": {{
    "act_1": {{
      "chapters": "1-12",
      "focus": "what happens in this act",
      "key_beats": [
        {{
          "chapter": 1,
          "beat": "beat description",
          "purpose": "why this matters"
        }}
      ]
    }},
    "act_2": {{ ... }},
    "act_3": {{ ... }}
  }},
  "scenes": [
    {{
      "chapter": 1,
      "scene": "scene description",
      "characters": ["Character Name"],
      "location": "where",
      "time": "when",
      "purpose": "narrative purpose",
      "emotional_beat": "emotional state",
      "status": "written/to_write/outline_only"
    }}
  ],
  "last_updated": "{datetime.now().strftime('%Y-%m-%d')}"
}}

Extract all structural information. Output ONLY valid JSON."""
            }]
        )
        
        response_text = message.content[0].text.strip()
        
        # Clean response
        if response_text.startswith('```'):
            response_text = response_text.split('```')[1]
            if response_text.startswith('json'):
                response_text = response_text[4:]
        
        # Parse JSON
        story_structure = json.loads(response_text)
        
        print(f"✓ Conversion complete")
        print(f"  Acts: {len(story_structure.get('acts', {}))}")
        print(f"  Scenes: {len(story_structure.get('scenes', []))}")
        
        return story_structure
        
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        return None

def main():
    story_data = convert_synopsis_and_outline()
    
    if story_data:
        # Write to MCP
        MCP_DIR.mkdir(parents=True, exist_ok=True)
        
        # Backup existing
        if STORY_STRUCTURE_MCP.exists():
            backup = STORY_STRUCTURE_MCP.with_suffix('.json.backup')
            STORY_STRUCTURE_MCP.rename(backup)
            print(f"✓ Backup created: {backup.name}")
        
        # Write new
        STORY_STRUCTURE_MCP.write_text(json.dumps(story_data, indent=2))
        print(f"✓ Wrote: {STORY_STRUCTURE_MCP}")
        print("\n✓ Story Structure MCP created successfully!")
        
        return 0
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
