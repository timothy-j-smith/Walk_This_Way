#!/usr/bin/env python3
"""
Professional Editor MCP Server - TRIAL VERSION
Professional editorial evaluation and critique for fiction writing

⚠️ TRIAL MCP - This is a first version for evaluation and refinement.
Based on professional editorial standards used by major publishing houses.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("professional-editor")

# Configuration paths
SERVER_DIR = Path(__file__).parent
DATA_DIR = SERVER_DIR / "data"
EVALUATIONS_DIR = DATA_DIR / "evaluations"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
EVALUATIONS_DIR.mkdir(exist_ok=True)

# Professional Editorial Standards
EDITORIAL_STANDARDS = {
    "structure": {
        "excellent": "Clear scene goal, obstacle, consequence. Scene earns its place. Strong opening hook. Satisfying resolution or cliffhanger.",
        "good": "Scene has purpose but could be tighter. Opening works but not compelling. Resolution adequate.",
        "needs_work": "Unclear purpose. Weak opening. Scene could be cut or combined. Resolution unsatisfying.",
        "fails": "No clear purpose. Scene doesn't advance plot or character. Should be cut."
    },
    "prose": {
        "excellent": "Publication-ready. Strong verbs, specific details, varied rhythm. No filter words. Shows, doesn't tell.",
        "good": "Solid prose with minor issues. Some filter words or weak verbs. Mostly shows.",
        "needs_work": "Too much telling. Weak verbs. Generic descriptions. Filter words throughout.",
        "fails": "Amateur-level prose. Excessive telling. Clichés. Weak construction throughout."
    },
    "character": {
        "excellent": "Distinct voices. Clear motivations. Authentic reactions. Character drives plot.",
        "good": "Characters work but voices could be more distinct. Motivations clear but could be deeper.",
        "needs_work": "Characters sound similar. Motivations unclear. Reactions feel forced.",
        "fails": "Flat characters. No distinct voices. Motivations unclear or absent."
    },
    "dialogue": {
        "excellent": "Natural, character-specific. Rich subtext. Advances plot/character. No exposition.",
        "good": "Works but could have more subtext. Some exposition. Characters sound distinct.",
        "needs_work": "On-the-nose dialogue. Too much exposition. Characters sound similar.",
        "fails": "Unnatural dialogue. Pure exposition. All characters sound the same."
    },
    "pacing": {
        "excellent": "Perfect rhythm. Tension builds. No dragging or rushing. Scene earns its length.",
        "good": "Good pace with minor issues. Some sections drag or rush.",
        "needs_work": "Pacing issues. Too fast (skipping beats) or too slow (dragging).",
        "fails": "Severe pacing problems. Rushes through important moments or drags unnecessarily."
    },
    "theme": {
        "excellent": "Theme woven naturally. No heavy-handedness. Adds depth without preaching.",
        "good": "Theme present but could be subtler. Some heavy-handed moments.",
        "needs_work": "Theme too obvious or unclear. Heavy-handed or absent.",
        "fails": "Theme preachy or completely absent. No depth."
    }
}

# Grading Scale (Professional Editor Standard)
GRADING_SCALE = {
    "A+": (95, 100, "Publication-ready. Minor polish needed."),
    "A": (90, 94, "Strong work. Professional quality with minor issues."),
    "B+": (85, 89, "Good work. Needs revision but has strong foundation."),
    "B": (80, 84, "Solid work. Multiple areas need improvement."),
    "C+": (75, 79, "Needs significant revision. Core issues present."),
    "C": (70, 74, "Major revision required. Fundamental problems."),
    "D": (60, 69, "Extensive revision needed. Multiple critical failures."),
    "F": (0, 59, "Not ready. Requires complete rewrite or fundamental rethinking.")
}

def calculate_grade(scores: Dict[str, float]) -> tuple:
    """Calculate overall grade from category scores"""
    total_score = sum(scores.values()) / len(scores)
    
    for grade, (min_score, max_score, description) in GRADING_SCALE.items():
        if min_score <= total_score <= max_score:
            return grade, total_score, description
    
    return "F", total_score, "Unable to calculate grade"

def evaluate_structure(text: str) -> Dict[str, Any]:
    """Evaluate structural elements"""
    issues = []
    strengths = []
    score = 85.0  # Start with baseline
    
    # Check for clear opening hook
    opening = text[:200].lower()
    weak_openings = ['it was', 'the day', 'once upon', 'it had been']
    if any(opening.startswith(weak) for weak in weak_openings):
        issues.append("Weak opening - starts with generic phrase")
        score -= 5
    else:
        strengths.append("Opening engages immediately")
    
    # Check scene purpose
    has_action = bool(re.search(r'\b(?:suddenly|then|but|however|when|as)\b', text, re.IGNORECASE))
    has_dialogue = bool(re.search(r'"[^"]*"', text))
    has_internal = bool(re.search(r'\b(?:thought|wondered|realized|felt|knew)\b', text, re.IGNORECASE))
    
    if not (has_action or has_dialogue):
        issues.append("Scene lacks action or dialogue - may be too passive")
        score -= 10
    else:
        strengths.append("Scene has active elements")
    
    # Check for clear scene goal (heuristic)
    question_words = len(re.findall(r'\b(?:what|why|how|when|where|who)\b', text, re.IGNORECASE))
    if question_words < 2:
        issues.append("Scene may lack clear character goal or obstacle")
        score -= 5
    
    # Check ending
    ending = text[-200:].lower()
    if ending.endswith(('.', '!', '?')):
        if 'just' in ending and 'silence' in ending:
            strengths.append("Strong ending - creates tension through silence")
        elif any(word in ending for word in ['finally', 'then', 'suddenly']):
            strengths.append("Ending creates forward momentum")
        else:
            issues.append("Ending may lack impact or forward momentum")
            score -= 5
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

def evaluate_prose(text: str) -> Dict[str, Any]:
    """Evaluate prose quality"""
    issues = []
    strengths = []
    score = 85.0
    
    # Filter words check
    filter_words = ['saw', 'heard', 'felt', 'noticed', 'realized', 'watched', 'looked', 'seemed']
    filter_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in filter_words)
    total_words = len(text.split())
    filter_percentage = (filter_count / total_words) * 100 if total_words > 0 else 0
    
    if filter_percentage > 2:
        issues.append(f"Too many filter words ({filter_count} instances) - creates distance from character")
        score -= min(15, filter_count * 2)
    else:
        strengths.append("Minimal filter words - good directness")
    
    # Weak verbs check
    weak_verbs = ['was', 'were', 'is', 'are', 'had', 'have', 'has', 'got', 'get', 'went', 'came']
    weak_verb_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in weak_verbs)
    weak_percentage = (weak_verb_count / total_words) * 100 if total_words > 0 else 0
    
    if weak_percentage > 25:
        issues.append(f"Too many weak verbs ({weak_verb_count} instances) - prose lacks energy")
        score -= 10
    else:
        strengths.append("Good verb variety")
    
    # Sentence variety check
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if sentences:
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_length = sum(sentence_lengths) / len(sentence_lengths)
        variation = max(sentence_lengths) - min(sentence_lengths)
        
        if variation < 10:
            issues.append("Sentence length lacks variety - rhythm may be monotonous")
            score -= 5
        else:
            strengths.append("Good sentence variety - creates rhythm")
        
        # Check for short impactful sentences
        short_sentences = [s for s in sentences if len(s.split()) <= 5]
        if len(short_sentences) > len(sentences) * 0.1:
            strengths.append("Effective use of short sentences for impact")
    
    # Specificity check
    generic_words = ['nice', 'good', 'bad', 'big', 'small', 'thing', 'stuff', 'very', 'really']
    generic_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in generic_words)
    if generic_count > 10:
        issues.append(f"Too many generic words ({generic_count} instances) - lacks specificity")
        score -= 8
    else:
        strengths.append("Good use of specific details")
    
    # Show vs tell check
    telling_markers = ['was', 'were', 'felt', 'seemed', 'appeared', 'looked like']
    telling_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in telling_markers)
    if telling_count > total_words * 0.15:
        issues.append("Too much telling vs showing - needs more action and sensory details")
        score -= 12
    else:
        strengths.append("Good balance of showing vs telling")
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "excellent" if score >= 90 else "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

def evaluate_character(text: str) -> Dict[str, Any]:
    """Evaluate character development and voice"""
    issues = []
    strengths = []
    score = 85.0
    
    # Character name frequency (heuristic for POV clarity)
    name_patterns = re.findall(r'\b(?:Nick|Jackie|Patty)\b', text, re.IGNORECASE)
    if len(name_patterns) < 5:
        issues.append("Character names may be underused - POV clarity issue")
        score -= 5
    else:
        strengths.append("Clear character presence")
    
    # Internal thought/feeling markers
    internal_markers = ['thought', 'wondered', 'felt', 'knew', 'realized', 'understood']
    internal_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in internal_markers)
    
    if internal_count < 3:
        issues.append("Limited access to character's internal state - may feel distant")
        score -= 8
    else:
        strengths.append("Good access to character's internal experience")
    
    # Physical reactions (showing emotion)
    physical_reactions = ['hands', 'face', 'chest', 'shoulders', 'jaw', 'palms', 'fingers']
    physical_count = sum(len(re.findall(rf'\b{word}\b', text, re.IGNORECASE)) for word in physical_reactions)
    
    if physical_count > 5:
        strengths.append("Good use of physical reactions to show emotion")
    else:
        issues.append("Could use more physical reactions to show emotion rather than tell")
        score -= 5
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "excellent" if score >= 90 else "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

def evaluate_dialogue(text: str) -> Dict[str, Any]:
    """Evaluate dialogue quality"""
    issues = []
    strengths = []
    score = 85.0
    
    # Extract dialogue
    dialogue_lines = re.findall(r'"[^"]*"', text)
    total_sentences = len(re.split(r'[.!?]+', text))
    
    if not dialogue_lines:
        issues.append("No dialogue - scene may be too internal or narrative-heavy")
        score -= 15
    else:
        dialogue_percentage = (len(dialogue_lines) / total_sentences) * 100 if total_sentences > 0 else 0
        
        if dialogue_percentage < 10:
            issues.append("Very little dialogue - may need more character interaction")
            score -= 8
        elif dialogue_percentage > 50:
            issues.append("Very dialogue-heavy - may need more narrative/action beats")
            score -= 5
        else:
            strengths.append("Good balance of dialogue and narrative")
        
        # Check dialogue length
        dialogue_lengths = [len(d.replace('"', '').split()) for d in dialogue_lines]
        avg_dialogue_length = sum(dialogue_lengths) / len(dialogue_lengths) if dialogue_lengths else 0
        
        if avg_dialogue_length > 25:
            issues.append("Dialogue lines may be too long - real speech is shorter")
            score -= 5
        else:
            strengths.append("Dialogue length feels natural")
        
        # Check for dialogue tags
        tag_pattern = r'"[^"]*"\s*,\s*\w+\s+(?:said|asked|whispered|replied)'
        tags = re.findall(tag_pattern, text, re.IGNORECASE)
        
        if len(tags) > len(dialogue_lines) * 0.8:
            issues.append("Too many dialogue tags - consider using action beats instead")
            score -= 5
        else:
            strengths.append("Good use of action beats with dialogue")
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "excellent" if score >= 90 else "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

def evaluate_pacing(text: str) -> Dict[str, Any]:
    """Evaluate pacing and rhythm"""
    issues = []
    strengths = []
    score = 85.0
    
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if sentences:
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_length = sum(sentence_lengths) / len(sentence_lengths)
        
        # Check for variety
        variation = max(sentence_lengths) - min(sentence_lengths)
        if variation < 15:
            issues.append("Sentence length lacks variety - pacing may be monotonous")
            score -= 8
        else:
            strengths.append("Good sentence variety creates rhythm")
        
        # Check for short impactful sentences
        short_sentences = [s for s in sentences if len(s.split()) <= 5]
        if len(short_sentences) >= len(sentences) * 0.15:
            strengths.append("Effective use of short sentences for impact and pacing")
        
        # Tension markers
        tension_words = ['suddenly', 'then', 'but', 'however', 'yet', 'finally']
        tension_count = sum(1 for word in tension_words for s in sentences if word.lower() in s.lower())
        
        if tension_count < 3:
            issues.append("May lack tension markers - pacing could be more dynamic")
            score -= 5
        else:
            strengths.append("Good use of tension markers")
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "excellent" if score >= 90 else "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

def evaluate_theme(text: str) -> Dict[str, Any]:
    """Evaluate thematic elements"""
    issues = []
    strengths = []
    score = 85.0
    
    # Check for theme-related words (heuristic)
    theme_markers = ['silence', 'friendship', 'choice', 'growing up', 'class', 'divide']
    theme_count = sum(1 for marker in theme_markers if marker.lower() in text.lower())
    
    if theme_count > 0:
        strengths.append("Thematic elements present and woven into narrative")
    else:
        issues.append("Thematic elements may be underdeveloped")
        score -= 5
    
    # Check for heavy-handedness (preaching)
    preaching_markers = ['always', 'never', 'should', 'must', 'everyone knows']
    preaching_count = sum(1 for marker in preaching_markers if marker.lower() in text.lower())
    
    if preaching_count > 5:
        issues.append("Theme may be too heavy-handed - show, don't preach")
        score -= 8
    else:
        strengths.append("Theme woven naturally without preaching")
    
    return {
        "score": max(60, min(100, score)),
        "issues": issues,
        "strengths": strengths,
        "assessment": "excellent" if score >= 90 else "good" if score >= 80 else "needs_work" if score >= 70 else "fails"
    }

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available professional editor tools"""
    return [
        Tool(
            name="evaluate_manuscript",
            description="⚠️ TRIAL MCP - Professional editorial evaluation of fiction writing. Provides honest, constructive critique with grading based on publishing industry standards. Evaluates: Structure, Prose, Character, Dialogue, Pacing, Theme. Returns overall grade (A+ to F) and detailed feedback.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The manuscript text to evaluate (chapter, scene, or full novel)"
                    },
                    "title": {
                        "type": "string",
                        "description": "Optional: Title of the work for reference"
                    },
                    "focus_areas": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional: Specific areas to focus on (structure, prose, character, dialogue, pacing, theme). If not provided, evaluates all areas."
                    }
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="compare_to_published_standard",
            description="⚠️ TRIAL MCP - Compare your writing to published fiction standards (King, Lehane, etc.). Shows where you meet standards and where you fall short.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Your manuscript text"
                    },
                    "standard": {
                        "type": "string",
                        "description": "Standard to compare against: 'literary_fiction', 'commercial_fiction', 'thriller', 'literary_thriller'",
                        "default": "literary_thriller"
                    }
                },
                "required": ["text"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    
    if name == "evaluate_manuscript":
        text = arguments.get("text", "")
        title = arguments.get("title", "Untitled")
        focus_areas = arguments.get("focus_areas", ["structure", "prose", "character", "dialogue", "pacing", "theme"])
        
        if not text:
            return [TextContent(type="text", text="Error: No text provided for evaluation.")]
        
        # Run evaluations
        evaluations = {}
        scores = {}
        
        if "structure" in focus_areas:
            evaluations["structure"] = evaluate_structure(text)
            scores["structure"] = evaluations["structure"]["score"]
        
        if "prose" in focus_areas:
            evaluations["prose"] = evaluate_prose(text)
            scores["prose"] = evaluations["prose"]["score"]
        
        if "character" in focus_areas:
            evaluations["character"] = evaluate_character(text)
            scores["character"] = evaluations["character"]["score"]
        
        if "dialogue" in focus_areas:
            evaluations["dialogue"] = evaluate_dialogue(text)
            scores["dialogue"] = evaluations["dialogue"]["score"]
        
        if "pacing" in focus_areas:
            evaluations["pacing"] = evaluate_pacing(text)
            scores["pacing"] = evaluations["pacing"]["score"]
        
        if "theme" in focus_areas:
            evaluations["theme"] = evaluate_theme(text)
            scores["theme"] = evaluations["theme"]["score"]
        
        # Calculate overall grade
        if scores:
            grade, total_score, grade_description = calculate_grade(scores)
        else:
            grade, total_score, grade_description = "N/A", 0, "No evaluations run"
        
        # Build critique report
        report = {
            "title": title,
            "evaluated_at": datetime.now().isoformat(),
            "trial_mcp": True,
            "overall_grade": grade,
            "overall_score": round(total_score, 1),
            "grade_description": grade_description,
            "category_scores": {k: round(v, 1) for k, v in scores.items()},
            "evaluations": {}
        }
        
        # Build detailed feedback
        for category, eval_data in evaluations.items():
            report["evaluations"][category] = {
                "score": round(eval_data["score"], 1),
                "assessment": eval_data["assessment"],
                "standard": EDITORIAL_STANDARDS[category][eval_data["assessment"]],
                "strengths": eval_data["strengths"],
                "issues": eval_data["issues"]
            }
        
        # Save evaluation
        eval_filename = f"{title.lower().replace(' ', '-')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        eval_path = EVALUATIONS_DIR / eval_filename
        with open(eval_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Format human-readable report
        human_report = f"""
================================================================================
PROFESSIONAL EDITORIAL EVALUATION - TRIAL MCP
================================================================================
Title: {title}
Evaluated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERALL ASSESSMENT
--------------------------------------------------------------------------------
Grade: {grade} ({total_score:.1f}/100)
{grade_description}

CATEGORY BREAKDOWN
--------------------------------------------------------------------------------
"""
        
        for category, eval_data in evaluations.items():
            human_report += f"""
{category.upper()} - Score: {eval_data['score']:.1f}/100
Assessment: {eval_data['assessment'].upper()}

Standard: {EDITORIAL_STANDARDS[category][eval_data['assessment']]}

STRENGTHS:
"""
            if eval_data['strengths']:
                for strength in eval_data['strengths']:
                    human_report += f"  ✓ {strength}\n"
            else:
                human_report += "  (None identified)\n"
            
            human_report += "\nAREAS FOR IMPROVEMENT:\n"
            if eval_data['issues']:
                for issue in eval_data['issues']:
                    human_report += f"  ⚠ {issue}\n"
            else:
                human_report += "  (None identified - excellent work in this area)\n"
        
        human_report += f"""
================================================================================
RECOMMENDATIONS
--------------------------------------------------------------------------------
"""
        
        # Prioritize recommendations
        critical_issues = []
        for category, eval_data in evaluations.items():
            if eval_data['score'] < 75:
                critical_issues.append(f"{category} (Score: {eval_data['score']:.1f})")
        
        if critical_issues:
            human_report += "PRIORITY: Address these critical areas first:\n"
            for issue in critical_issues:
                human_report += f"  • {issue}\n"
            human_report += "\n"
        
        # Next steps
        if total_score >= 90:
            human_report += "This work is approaching publication-ready quality. Focus on minor polish and consistency.\n"
        elif total_score >= 80:
            human_report += "Solid foundation. Address identified issues and revise. You're on the right track.\n"
        elif total_score >= 70:
            human_report += "Needs significant revision. Address critical issues first, then work through remaining problems.\n"
        else:
            human_report += "Major revision required. Consider fundamental rethinking of problematic areas.\n"
        
        human_report += f"""
================================================================================
Evaluation saved to: {eval_path}
================================================================================
"""
        
        return [TextContent(type="text", text=human_report)]
    
    elif name == "compare_to_published_standard":
        text = arguments.get("text", "")
        standard = arguments.get("standard", "literary_thriller")
        
        # This would compare to published standards
        # For now, return a basic comparison
        return [TextContent(type="text", text=f"Comparison to {standard} standard - Feature in development for trial MCP.")]
    
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
