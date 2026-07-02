#!/usr/bin/env python3
"""
Fiction Reverse Engineering MCP Server
Extract structural DNA from bestsellers to improve your writing

⚠️ IMPORTANT: This is a LEARNING TOOL, not a formula to copy.
Use to understand patterns, not to replace your creative voice.
"""

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("fiction-reverse-engineering")

# Configuration paths
SERVER_DIR = Path(__file__).parent
PROJECT_ROOT = SERVER_DIR.parent.parent.parent
DATA_DIR = SERVER_DIR / "data"
FORMULAS_DIR = DATA_DIR / "formulas"
PATTERNS_DIR = DATA_DIR / "patterns"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
FORMULAS_DIR.mkdir(exist_ok=True)
PATTERNS_DIR.mkdir(exist_ok=True)

# Usage warning
USAGE_WARNING = """
⚠️ USAGE WARNING:
This MCP is a LEARNING TOOL, not a formula to copy.
- Use to understand patterns in bestsellers
- Learn pacing techniques mathematically
- Compare your work objectively
- Extract insights for improvement
- DO NOT copy formulas blindly
- DO NOT replace creative intuition with formulas
- DO NOT force your writing into rigid patterns
- ALWAYS maintain your unique voice
"""

def analyze_structure(text: str) -> Dict[str, Any]:
    """Analyze basic structure of text"""
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    # Estimate chapters (look for chapter markers)
    chapter_markers = re.findall(r'(?i)(?:chapter|act)\s+\d+', text)
    chapter_count = len(chapter_markers) if chapter_markers else 1
    
    # Find dialogue
    dialogue_lines = re.findall(r'"[^"]*"', text)
    
    # Estimate plot points (look for dramatic markers)
    plot_point_markers = re.findall(r'(?:suddenly|then|finally|meanwhile|however)', text, re.IGNORECASE)
    
    return {
        'total_words': len(text.split()),
        'total_sentences': len(sentences),
        'total_paragraphs': len(paragraphs),
        'total_dialogue': len(dialogue_lines),
        'chapter_count': chapter_count,
        'plot_points': len(plot_point_markers),
        'avg_sentence_length': len(text.split()) / len(sentences) if sentences else 0,
        'dialogue_percentage': (len(dialogue_lines) / len(sentences) * 100) if sentences else 0
    }

def analyze_pacing(text: str) -> Dict[str, Any]:
    """Analyze pacing mathematically"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Calculate sentence length variation (pacing indicator)
    sentence_lengths = [len(s.split()) for s in sentences]
    avg_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    
    # Find tension markers
    tension_words = ['suddenly', 'then', 'finally', 'meanwhile', 'however', 'but', 'yet']
    tension_count = sum(1 for word in tension_words for s in sentences if word.lower() in s.lower())
    tension_frequency = tension_count / len(sentences) if sentences else 0
    
    # Find reveal markers
    reveal_words = ['discovered', 'realized', 'understood', 'learned', 'found', 'revealed']
    reveal_count = sum(1 for word in reveal_words for s in sentences if word.lower() in s.lower())
    reveal_frequency = reveal_count / len(sentences) if sentences else 0
    
    # Dialogue pacing
    dialogue_lines = re.findall(r'"[^"]*"', text)
    dialogue_frequency = len(dialogue_lines) / len(sentences) if sentences else 0
    
    return {
        'tension_pattern': 'high' if tension_frequency > 0.1 else 'moderate' if tension_frequency > 0.05 else 'low',
        'tension_frequency': round(tension_frequency, 3),
        'reveal_frequency': round(reveal_frequency, 3),
        'dialogue_frequency': round(dialogue_frequency, 3),
        'avg_sentence_length': round(avg_length, 1),
        'sentence_variation': round(max(sentence_lengths) - min(sentence_lengths), 1) if sentence_lengths else 0,
        'issues': [],
        'recommendations': []
    }

def extract_dialogue_patterns(text: str) -> Dict[str, Any]:
    """Extract dialogue patterns"""
    dialogue_lines = re.findall(r'"[^"]*"', text)
    
    # Find dialogue tags
    tag_patterns = re.findall(r'"[^"]*"\s*,\s*(\w+\s+said|\w+\s+asked|\w+\s+whispered)', text, re.IGNORECASE)
    
    # Count tag types
    tag_counts = {}
    for tag in tag_patterns:
        tag_type = tag.split()[0].lower() if tag.split() else 'unknown'
        tag_counts[tag_type] = tag_counts.get(tag_type, 0) + 1
    
    # Average dialogue length
    dialogue_lengths = [len(d.replace('"', '').split()) for d in dialogue_lines]
    avg_dialogue_length = sum(dialogue_lengths) / len(dialogue_lengths) if dialogue_lengths else 0
    
    return {
        'total_dialogue': len(dialogue_lines),
        'avg_dialogue_length': round(avg_dialogue_length, 1),
        'tag_usage': tag_counts,
        'beat_pattern': 'frequent' if len(dialogue_lines) > len(text.split()) * 0.1 else 'moderate',
        'exchange_rhythm': 'fast' if avg_dialogue_length < 10 else 'moderate' if avg_dialogue_length < 20 else 'slow',
        'subtext_markers': [],
        'examples': dialogue_lines[:5] if dialogue_lines else []
    }

def detect_chapter_formula(chapter_text: str) -> Dict[str, Any]:
    """Detect chapter-level patterns"""
    structure = analyze_structure(chapter_text)
    pacing = analyze_pacing(chapter_text)
    
    # Look for hooks (opening patterns)
    opening_sentences = chapter_text.split('.')[:3]
    has_hook = any(word in ' '.join(opening_sentences).lower() for word in ['suddenly', 'then', 'when', 'as'])
    
    # Look for cliffhangers (ending patterns)
    ending_sentences = chapter_text.split('.')[-3:]
    has_cliffhanger = any(word in ' '.join(ending_sentences).lower() for word in ['but', 'however', 'then', 'suddenly'])
    
    return {
        'word_count': structure['total_words'],
        'has_hook': has_hook,
        'has_cliffhanger': has_cliffhanger,
        'pacing': pacing['tension_pattern'],
        'dialogue_percentage': round(structure['dialogue_percentage'], 1),
        'structure': 'dialogue_heavy' if structure['dialogue_percentage'] > 30 else 'balanced' if structure['dialogue_percentage'] > 15 else 'narrative_heavy'
    }

def compare_structures(your_structure: Dict, your_patterns: Dict, 
                       bestseller_structure: Dict, bestseller_patterns: Dict,
                       bestseller_formula: Dict) -> Dict[str, Any]:
    """Compare your structure to bestseller formula"""
    # Calculate match score
    match_score = 0.0
    total_comparisons = 0
    
    # Compare pacing
    if 'pacing' in bestseller_formula and 'tension_pattern' in your_patterns:
        if your_patterns['tension_pattern'] == bestseller_formula['pacing'].get('tension_pattern'):
            match_score += 1.0
        total_comparisons += 1
    
    # Compare dialogue frequency
    if 'dialogue_frequency' in bestseller_patterns and 'dialogue_frequency' in your_patterns:
        your_dialogue = your_patterns['dialogue_frequency']
        bestseller_dialogue = bestseller_patterns.get('dialogue_frequency', 0)
        if abs(your_dialogue - bestseller_dialogue) < 0.1:
            match_score += 1.0
        total_comparisons += 1
    
    # Calculate overall match
    overall_match = (match_score / total_comparisons * 100) if total_comparisons > 0 else 0
    
    return {
        'match_score': round(overall_match, 1),
        'what_works': ['Pacing matches genre expectations'] if overall_match > 70 else [],
        'deviations': ['Pacing differs from bestseller pattern'] if overall_match < 70 else [],
        'critical_issues': []
    }

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available reverse engineering tools"""
    return [
        Tool(
            name="reverse_engineer_novel",
            description=f"{USAGE_WARNING}Reverse engineer a bestselling novel to extract its structural formula. Use this to LEARN from masters, not to copy formulas. Analyze patterns, pacing, and structure to understand what makes bestsellers work.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Full novel text (80,000+ words recommended for best results)"
                    },
                    "title": {
                        "type": "string",
                        "description": "Novel title"
                    },
                    "author": {
                        "type": "string",
                        "description": "Author name"
                    },
                    "genre": {
                        "type": "string",
                        "description": "Genre (thriller, mystery, romance, fantasy, etc.)",
                        "default": "thriller"
                    }
                },
                "required": ["text", "title", "author"]
            }
        ),
        Tool(
            name="compare_to_bestseller",
            description=f"{USAGE_WARNING}Compare your writing to a reverse-engineered bestseller formula. Use this for DIAGNOSTIC analysis when something feels off, or for REFINEMENT during revision. Shows where your structure deviates and how to improve while maintaining your unique voice.",
            inputSchema={
                "type": "object",
                "properties": {
                    "your_text": {
                        "type": "string",
                        "description": "Your manuscript (chapter or full novel)"
                    },
                    "bestseller_title": {
                        "type": "string",
                        "description": "Title of analyzed bestseller to compare against"
                    },
                    "detailed": {
                        "type": "boolean",
                        "description": "Include specific line-by-line recommendations",
                        "default": True
                    }
                },
                "required": ["your_text", "bestseller_title"]
            }
        ),
        Tool(
            name="analyze_pacing",
            description=f"{USAGE_WARNING}Analyze pacing mathematically - tension curves, reveal frequency, dialogue rhythm. Use this for OBJECTIVE analysis during revision, not during creative drafting. Provides data to inform decisions, not replace intuition.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Your manuscript (chapter or full novel)"
                    },
                    "target_formula": {
                        "type": "string",
                        "description": "Optional: Bestseller formula title to compare against"
                    }
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="extract_dialogue_formula",
            description=f"{USAGE_WARNING}Extract dialogue patterns - rhythm, beat patterns, tag usage. Use this to LEARN dialogue techniques from masters, not to copy their style. Understand patterns, then adapt to your voice.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Novel text to analyze"
                    },
                    "author": {
                        "type": "string",
                        "description": "Optional: Author name for context"
                    }
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="find_chapter_formula",
            description=f"{USAGE_WARNING}Extract chapter-level formulas - structure, hooks, cliffhangers. Use this to UNDERSTAND chapter patterns, not to force every chapter into the same structure. Learn techniques, maintain variety.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Novel text"
                    },
                    "chapter_num": {
                        "type": "integer",
                        "description": "Optional: Specific chapter to analyze (1-based index)"
                    }
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="list_available_formulas",
            description="List all reverse-engineered bestseller formulas available for comparison.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    
    if name == "reverse_engineer_novel":
        text = arguments.get("text", "")
        title = arguments.get("title", "")
        author = arguments.get("author", "")
        genre = arguments.get("genre", "thriller")
        
        # Analyze structure
        structure = analyze_structure(text)
        
        # Analyze pacing
        pacing = analyze_pacing(text)
        
        # Extract dialogue patterns
        dialogue_patterns = extract_dialogue_patterns(text)
        
        # Create formula
        formula = {
            'pacing': {
                'tension_pattern': pacing['tension_pattern'],
                'reveal_frequency': pacing['reveal_frequency'],
                'description': f"Tension pattern: {pacing['tension_pattern']}, Reveals: {pacing['reveal_frequency']}"
            },
            'dialogue': dialogue_patterns,
            'structure': structure,
            'key_insights': [
                f"Average sentence length: {structure['avg_sentence_length']:.1f} words",
                f"Dialogue percentage: {structure['dialogue_percentage']:.1f}%",
                f"Tension frequency: {pacing['tension_frequency']:.3f}",
                f"Chapter count: {structure['chapter_count']}"
            ]
        }
        
        # Save formula
        formula_data = {
            'title': title,
            'author': author,
            'genre': genre,
            'analyzed_at': datetime.now().isoformat(),
            'structure': structure,
            'patterns': {
                'pacing': pacing,
                'dialogue': dialogue_patterns
            },
            'formula': formula,
            'warning': 'This formula is a LEARNING TOOL, not a template. Use to understand patterns, not to copy formulas.'
        }
        
        formula_filename = f"{title.lower().replace(' ', '-').replace('/', '-')}.json"
        formula_path = FORMULAS_DIR / formula_filename
        
        with open(formula_path, 'w', encoding='utf-8') as f:
            json.dump(formula_data, f, indent=2, ensure_ascii=False)
        
        result = {
            'status': 'success',
            'warning': '⚠️ Remember: This formula is a LEARNING TOOL. Use to understand patterns, not to copy formulas.',
            'novel': f"{title} by {author}",
            'summary': {
                'total_chapters': structure['chapter_count'],
                'plot_points': structure['plot_points'],
                'pacing_formula': formula['pacing']['description'],
                'tension_pattern': formula['pacing']['tension_pattern'],
                'reveal_frequency': pacing['reveal_frequency']
            },
            'key_findings': formula['key_insights'][:5],
            'saved_to': str(formula_path)
        }
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "compare_to_bestseller":
        your_text = arguments.get("your_text", "")
        bestseller_title = arguments.get("bestseller_title", "")
        detailed = arguments.get("detailed", True)
        
        # Load formula
        formula_filename = f"{bestseller_title.lower().replace(' ', '-').replace('/', '-')}.json"
        formula_path = FORMULAS_DIR / formula_filename
        
        if not formula_path.exists():
            # List available formulas
            available = [f.stem for f in FORMULAS_DIR.glob("*.json")]
            result = {
                'error': f"Formula not found for '{bestseller_title}'",
                'available_formulas': available,
                'hint': 'Run reverse_engineer_novel first to create a formula'
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        with open(formula_path, 'r', encoding='utf-8') as f:
            formula_data = json.load(f)
        
        # Analyze your text
        your_structure = analyze_structure(your_text)
        your_pacing = analyze_pacing(your_text)
        your_dialogue = extract_dialogue_patterns(your_text)
        
        your_patterns = {
            'pacing': your_pacing,
            'dialogue': your_dialogue
        }
        
        # Compare
        comparison = compare_structures(
            your_structure,
            your_patterns,
            formula_data['structure'],
            formula_data['patterns'],
            formula_data['formula']
        )
        
        # Generate recommendations
        recommendations = []
        if comparison['match_score'] < 70:
            recommendations.append("Consider adjusting pacing to better match genre expectations")
            recommendations.append("Review dialogue frequency - may need more or less dialogue")
        if your_pacing['tension_frequency'] < 0.05:
            recommendations.append("Tension markers are low - consider adding more dramatic moments")
        if your_dialogue['total_dialogue'] < 10:
            recommendations.append("Dialogue is sparse - consider adding more character interaction")
        
        result = {
            'warning': '⚠️ Use this comparison to LEARN and REFINE, not to copy formulas. Maintain your unique voice.',
            'comparison_to': f"{formula_data['title']} by {formula_data['author']}",
            'overall_match': comparison['match_score'],
            'strengths': comparison['what_works'],
            'deviations': comparison['deviations'],
            'critical_issues': comparison['critical_issues'],
            'recommendations': recommendations[:10] if detailed else recommendations[:5],
            'your_metrics': {
                'tension_pattern': your_pacing['tension_pattern'],
                'dialogue_frequency': your_dialogue['dialogue_frequency'],
                'avg_sentence_length': your_structure['avg_sentence_length']
            },
            'bestseller_metrics': {
                'tension_pattern': formula_data['formula']['pacing']['tension_pattern'],
                'dialogue_frequency': formula_data['patterns']['dialogue']['dialogue_frequency'],
                'avg_sentence_length': formula_data['structure']['avg_sentence_length']
            }
        }
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "analyze_pacing":
        text = arguments.get("text", "")
        target_formula = arguments.get("target_formula")
        
        pacing = analyze_pacing(text)
        
        if target_formula:
            formula_filename = f"{target_formula.lower().replace(' ', '-').replace('/', '-')}.json"
            formula_path = FORMULAS_DIR / formula_filename
            if formula_path.exists():
                with open(formula_path, 'r', encoding='utf-8') as f:
                    formula_data = json.load(f)
                pacing['comparison'] = {
                    'your_tension': pacing['tension_pattern'],
                    'bestseller_tension': formula_data['formula']['pacing']['tension_pattern'],
                    'match': pacing['tension_pattern'] == formula_data['formula']['pacing']['tension_pattern']
                }
        
        result = {
            'warning': '⚠️ Use this data to INFORM decisions, not replace creative intuition.',
            'tension_pattern': pacing['tension_pattern'],
            'tension_frequency': pacing['tension_frequency'],
            'reveal_frequency': pacing['reveal_frequency'],
            'dialogue_frequency': pacing['dialogue_frequency'],
            'avg_sentence_length': pacing['avg_sentence_length'],
            'pacing_issues': pacing['issues'],
            'recommendations': pacing['recommendations']
        }
        
        if 'comparison' in pacing:
            result['comparison'] = pacing['comparison']
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "extract_dialogue_formula":
        text = arguments.get("text", "")
        author = arguments.get("author")
        
        dialogue_formula = extract_dialogue_patterns(text)
        
        result = {
            'warning': '⚠️ Learn dialogue patterns, then adapt to your unique voice. Don\'t copy style.',
            'beat_pattern': dialogue_formula['beat_pattern'],
            'exchange_rhythm': dialogue_formula['exchange_rhythm'],
            'tag_usage': dialogue_formula['tag_usage'],
            'avg_dialogue_length': dialogue_formula['avg_dialogue_length'],
            'total_dialogue': dialogue_formula['total_dialogue'],
            'examples': dialogue_formula['examples'][:5]
        }
        
        if author:
            result['author'] = author
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "find_chapter_formula":
        text = arguments.get("text", "")
        chapter_num = arguments.get("chapter_num")
        
        # Split into chapters (simple approach - look for chapter markers)
        chapter_markers = list(re.finditer(r'(?i)(?:chapter|act)\s+\d+', text))
        
        if chapter_markers:
            chapters = []
            for i, marker in enumerate(chapter_markers):
                start = marker.end()
                end = chapter_markers[i+1].start() if i+1 < len(chapter_markers) else len(text)
                chapters.append(text[start:end].strip())
        else:
            # No chapter markers - treat as single chapter
            chapters = [text]
        
        if chapter_num and chapter_num <= len(chapters):
            formula = detect_chapter_formula(chapters[chapter_num - 1])
            result = {
                'warning': '⚠️ Chapter formulas are patterns to learn, not templates to copy.',
                'chapter': chapter_num,
                'formula': formula
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        # Analyze all chapters
        formulas = [detect_chapter_formula(ch) for ch in chapters]
        
        # Find patterns
        avg_words = sum(f['word_count'] for f in formulas) / len(formulas) if formulas else 0
        hooks_percentage = sum(1 for f in formulas if f['has_hook']) / len(formulas) * 100 if formulas else 0
        cliffhangers_percentage = sum(1 for f in formulas if f['has_cliffhanger']) / len(formulas) * 100 if formulas else 0
        
        result = {
            'warning': '⚠️ Chapter patterns are guides, not rules. Maintain variety in your structure.',
            'total_chapters': len(chapters),
            'meta_formula': {
                'avg_chapter_length': round(avg_words, 0),
                'hooks_percentage': round(hooks_percentage, 1),
                'cliffhangers_percentage': round(cliffhangers_percentage, 1),
                'insights': [
                    f"Average chapter length: {round(avg_words, 0)} words",
                    f"Hooks in {round(hooks_percentage, 1)}% of chapters",
                    f"Cliffhangers in {round(cliffhangers_percentage, 1)}% of chapters"
                ]
            },
            'chapter_formulas': formulas[:3]  # First 3 as examples
        }
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "list_available_formulas":
        if not FORMULAS_DIR.exists():
            result = {'message': 'No formulas yet. Run reverse_engineer_novel first to create formulas.'}
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        formulas = []
        for path in FORMULAS_DIR.glob("*.json"):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                formulas.append({
                    'title': data.get('title', 'Unknown'),
                    'author': data.get('author', 'Unknown'),
                    'genre': data.get('genre', 'Unknown'),
                    'analyzed': data.get('analyzed_at', 'Unknown')
                })
            except:
                continue
        
        result = {
            'total_formulas': len(formulas),
            'formulas': formulas,
            'note': 'Use these formulas to LEARN patterns, not to copy structures.'
        }
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
