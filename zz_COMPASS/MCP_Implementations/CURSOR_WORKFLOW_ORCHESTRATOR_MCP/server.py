#!/usr/bin/env python3
"""
Cursor Workflow Orchestrator MCP Server
Intelligent MCP management and workflow orchestration with interactive checklist system
"""

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Initialize server
app = Server("cursor-workflow-orchestrator")

# Configuration paths - Use relative path from server location
SERVER_DIR = Path(__file__).parent
PROJECT_ROOT = SERVER_DIR.parent.parent.parent  # Go up to project root
MCP_CONFIG_PATH = PROJECT_ROOT / ".cursor" / "config" / "mcp.json"
USAGE_LOG_PATH = PROJECT_ROOT / ".cursor" / "logs" / "orchestrator-usage.jsonl"

# Ensure log directory exists
USAGE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

def load_mcp_config() -> dict:
    """Load MCP configuration from mcp.json"""
    if not MCP_CONFIG_PATH.exists():
        return {}
    with open(MCP_CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_mcp_config(config: dict) -> bool:
    """Save MCP configuration to mcp.json"""
    try:
        MCP_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(MCP_CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        return False

def log_usage(action: str, details: dict):
    """Log orchestrator usage for learning"""
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "details": details
    }
    try:
        with open(USAGE_LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')
    except:
        pass

def get_available_mcps() -> List[str]:
    """Get list of all available MCPs from config"""
    config = load_mcp_config()
    return list(config.get("mcpServers", {}).keys())

def analyze_context(task: str, current_file: Optional[str] = None) -> dict:
    """Analyze task/question to determine required capabilities"""
    context = {
        "task": task.lower(),
        "file_type": None,
        "writing_phase": None,
        "task_type": None,
        "required_capabilities": []
    }
    
    # Detect file type
    if current_file:
        if current_file.endswith('.txt'):
            context["file_type"] = "chapter"
        elif 'Story_Bible' in current_file or 'bible' in current_file.lower():
            context["file_type"] = "story_bible"
        elif 'Agent_Work' in current_file:
            context["file_type"] = "agent_work"
    
    # Detect writing phase
    task_lower = task.lower()
    if any(word in task_lower for word in ["draft", "write", "create", "compose"]):
        context["writing_phase"] = "drafting"
    elif any(word in task_lower for word in ["edit", "revise", "improve", "polish"]):
        context["writing_phase"] = "editing"
    elif any(word in task_lower for word in ["check", "verify", "validate", "consistency"]):
        context["writing_phase"] = "quality_check"
    
    # Detect task type
    if any(word in task_lower for word in ["character", "nick", "jackie", "maxanne"]):
        context["task_type"] = "character"
        context["required_capabilities"] = ["character_analysis", "memory", "consistency"]
    elif any(word in task_lower for word in ["plot", "story", "narrative", "structure"]):
        context["task_type"] = "plot"
        context["required_capabilities"] = ["plot_analysis", "structure", "sequential_thinking"]
    elif any(word in task_lower for word in ["style", "voice", "prose", "lehane"]):
        context["task_type"] = "style"
        context["required_capabilities"] = ["style_analysis", "emulation", "writing_guides"]
    elif any(word in task_lower for word in ["research", "fact", "check", "historical"]):
        context["task_type"] = "research"
        context["required_capabilities"] = ["web_search", "fact_checking", "research"]
    elif any(word in task_lower for word in ["python", "code", "script", "json"]):
        context["task_type"] = "code"
        context["required_capabilities"] = ["code_execution", "toolbox"]
    
    return context

def recommend_mcps(context: dict) -> dict:
    """Recommend MCPs based on context analysis"""
    recommendations = {
        "essential": [],
        "recommended": [],
        "optional": []
    }
    
    # Character-related tasks
    if context["task_type"] == "character":
        recommendations["essential"].extend([
            "knowledge-graph-memory",
            "compass-writing-guides"
        ])
        recommendations["recommended"].extend([
            "dennis-lehane-style",
            "enhanced-mcp-memory"
        ])
    
    # Plot/structure tasks
    if context["task_type"] == "plot" or "structure" in context["required_capabilities"]:
        recommendations["essential"].extend([
            "sequential-thinking",
            "walk-this-way-files"
        ])
        recommendations["recommended"].extend([
            "sequential-thinking-ultra",
            "ai-writers-workshop"
        ])
    
    # Style tasks
    if context["task_type"] == "style":
        recommendations["essential"].extend([
            "dennis-lehane-style",
            "style-emulation",
            "compass-writing-guides"
        ])
    
    # Research tasks
    if context["task_type"] == "research":
        recommendations["essential"].extend([
            "firecrawl",
            "duckduckgo-search"
        ])
        recommendations["recommended"].extend([
            "vectara",
            "cognee-connections"
        ])
    
    # Code tasks
    if context["task_type"] == "code":
        recommendations["essential"].extend([
            "toolbox",
            "walk-this-way-files"
        ])
    
    # Always include filesystem for file access
    if "walk-this-way-files" not in recommendations["essential"]:
        recommendations["essential"].append("walk-this-way-files")
    
    # Remove duplicates
    for key in recommendations:
        recommendations[key] = list(set(recommendations[key]))
    
    return recommendations

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available orchestrator tools"""
    return [
        Tool(
            name="analyze_context",
            description="Analyze a task or question to determine required MCPs and capabilities. Use this first to understand what MCPs are needed.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "The task or question you want to accomplish"
                    },
                    "current_file": {
                        "type": "string",
                        "description": "Optional: Current file path for context"
                    }
                },
                "required": ["task"]
            }
        ),
        Tool(
            name="recommend_mcps",
            description="Get MCP recommendations based on context analysis. Returns essential, recommended, and optional MCPs with reasoning.",
            inputSchema={
                "type": "object",
                "properties": {
                    "context": {
                        "type": "object",
                        "description": "Context analysis result from analyze_context tool"
                    }
                },
                "required": ["context"]
            }
        ),
        Tool(
            name="show_checklist",
            description="Display interactive checklist of recommended MCPs with checkboxes. Shows reasoning for each recommendation.",
            inputSchema={
                "type": "object",
                "properties": {
                    "recommendations": {
                        "type": "object",
                        "description": "Recommendations from recommend_mcps tool"
                    },
                    "task": {
                        "type": "string",
                        "description": "Original task for context"
                    }
                },
                "required": ["recommendations", "task"]
            }
        ),
        Tool(
            name="enable_mcps",
            description="Enable selected MCPs by setting disabled=false in mcp.json. Requires list of MCP names to enable.",
            inputSchema={
                "type": "object",
                "properties": {
                    "mcp_names": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of MCP names to enable (e.g., ['knowledge-graph-memory', 'firecrawl'])"
                    }
                },
                "required": ["mcp_names"]
            }
        ),
        Tool(
            name="disable_mcps",
            description="Disable MCPs by setting disabled=true in mcp.json. Requires list of MCP names to disable.",
            inputSchema={
                "type": "object",
                "properties": {
                    "mcp_names": {
                        "type": "array",
                                               "items": {"type": "string"},
                        "description": "List of MCP names to disable"
                    }
                },
                "required": ["mcp_names"]
            }
        ),
        Tool(
            name="list_available_mcps",
            description="List all available MCPs in your configuration with their current enabled/disabled status.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_mcp_status",
            description="Get current status of all MCPs (enabled/disabled) and their configurations.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    
    if name == "analyze_context":
        task = arguments.get("task", "")
        current_file = arguments.get("current_file")
        context = analyze_context(task, current_file)
        log_usage("analyze_context", {"task": task, "context": context})
        return [TextContent(
            type="text",
            text=json.dumps(context, indent=2)
        )]
    
    elif name == "recommend_mcps":
        context = arguments.get("context", {})
        recommendations = recommend_mcps(context)
        log_usage("recommend_mcps", {"context": context, "recommendations": recommendations})
        return [TextContent(
            type="text",
            text=json.dumps(recommendations, indent=2)
        )]
    
    elif name == "show_checklist":
        recommendations = arguments.get("recommendations", {})
        task = arguments.get("task", "")
        
        checklist_text = f"""
# MCP Activation Recommendations

**Based on your task:** {task}

## Essential MCPs (Pre-checked)
"""
        for mcp in recommendations.get("essential", []):
            checklist_text += f"\n☑ {mcp}\n"
        
        checklist_text += "\n## Recommended MCPs (Pre-checked)\n"
        for mcp in recommendations.get("recommended", []):
            checklist_text += f"\n☑ {mcp}\n"
        
        checklist_text += "\n## Optional MCPs (Unchecked)\n"
        for mcp in recommendations.get("optional", []):
            checklist_text += f"\n☐ {mcp}\n"
        
        checklist_text += """
## Instructions
- Review the recommendations above
- Use `enable_mcps` tool with list of MCPs you want to enable
- Use `disable_mcps` tool with list of MCPs you want to disable
- After enabling/disabling, restart Cursor for changes to take effect
"""
        
        log_usage("show_checklist", {"task": task, "recommendations": recommendations})
        return [TextContent(type="text", text=checklist_text)]
    
    elif name == "enable_mcps":
        mcp_names = arguments.get("mcp_names", [])
        config = load_mcp_config()
        
        enabled = []
        not_found = []
        
        for mcp_name in mcp_names:
            if mcp_name in config.get("mcpServers", {}):
                config["mcpServers"][mcp_name]["disabled"] = False
                enabled.append(mcp_name)
            else:
                not_found.append(mcp_name)
        
        success = save_mcp_config(config)
        
        result = {
            "success": success,
            "enabled": enabled,
            "not_found": not_found,
            "message": f"Enabled {len(enabled)} MCP(s). Restart Cursor for changes to take effect."
        }
        
        log_usage("enable_mcps", {"mcp_names": mcp_names, "result": result})
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "disable_mcps":
        mcp_names = arguments.get("mcp_names", [])
        config = load_mcp_config()
        
        disabled = []
        not_found = []
        
        for mcp_name in mcp_names:
            if mcp_name in config.get("mcpServers", {}):
                config["mcpServers"][mcp_name]["disabled"] = True
                disabled.append(mcp_name)
            else:
                not_found.append(mcp_name)
        
        success = save_mcp_config(config)
        
        result = {
            "success": success,
            "disabled": disabled,
            "not_found": not_found,
            "message": f"Disabled {len(disabled)} MCP(s). Restart Cursor for changes to take effect."
        }
        
        log_usage("disable_mcps", {"mcp_names": mcp_names, "result": result})
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "list_available_mcps":
        config = load_mcp_config()
        mcps = []
        
        for name, config_data in config.get("mcpServers", {}).items():
            mcps.append({
                "name": name,
                "disabled": config_data.get("disabled", False),
                "command": config_data.get("command", "unknown")
            })
        
        log_usage("list_available_mcps", {"count": len(mcps)})
        return [TextContent(type="text", text=json.dumps(mcps, indent=2))]
    
    elif name == "get_mcp_status":
        config = load_mcp_config()
        status = {
            "total_mcps": len(config.get("mcpServers", {})),
            "enabled": [],
            "disabled": []
        }
        
        for name, config_data in config.get("mcpServers", {}).items():
            if config_data.get("disabled", False):
                status["disabled"].append(name)
            else:
                status["enabled"].append(name)
        
        log_usage("get_mcp_status", status)
        return [TextContent(type="text", text=json.dumps(status, indent=2))]
    
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
