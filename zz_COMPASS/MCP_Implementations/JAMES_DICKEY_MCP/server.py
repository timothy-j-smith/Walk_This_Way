"""James Dickey MCP — Deliverance-focused craft engine (stdio, JSON-RPC).

Uses stdlib only (Python 3.9+) so Cursor can run the server without the ``mcp``
PyPI package. Protocol: newline-delimited JSON-RPC 2.0 (MCP stdio).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "dickey_deliverance_analysis.json"

PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "james-dickey-deliverance"
SERVER_VERSION = "1.0.0"

_kb: dict[str, Any] | None = None


def load_kb() -> dict[str, Any]:
    global _kb
    if _kb is not None:
        return _kb
    if not DATA_PATH.is_file():
        raise FileNotFoundError(f"Missing knowledge base: {DATA_PATH}")
    with DATA_PATH.open(encoding="utf-8") as f:
        _kb = json.load(f)
    return _kb


def _norm(s: str) -> str:
    return (s or "").strip().lower()


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


def build_agent_brief(
    *,
    tool: str,
    text: str,
    mode: str,
    liberty: str,
    focus: str | None,
) -> str:
    kb = load_kb()
    mode_k = _norm(mode) or "create"
    liberty_k = _norm(liberty) or "nice"
    if mode_k not in ("create", "transform", "edit"):
        mode_k = "create"
    if liberty_k not in ("nice", "neutral", "professional"):
        liberty_k = "nice"

    mode_hint = kb.get("mode_hints", {}).get(mode_k, "")
    lib_hint = kb.get("liberty_hints", {}).get(liberty_k, "")

    shelves = kb.get("writers_toolbox", {}).get("shelves", [])
    shelf_md: list[str] = []
    for sh in shelves:
        name = sh.get("name", "")
        shelf_md.append(f"### {name}\n" + _bullet_list(sh.get("points", [])))
    shelves_block = "\n\n".join(shelf_md)

    phil = _bullet_list(kb.get("core_philosophy", []))
    df = kb.get("deliverance_focus", {})
    deliv_blocks: list[str] = []
    for key, title in (
        ("narrator_consciousness", "Narrator consciousness"),
        ("structure_pressure", "Structure / pressure"),
        ("sensory_channels", "Sensory channels"),
        ("aftermath_craft", "Aftermath"),
    ):
        lines = df.get(key, [])
        if lines:
            deliv_blocks.append(f"#### {title}\n" + _bullet_list(lines))
    deliv_md = "\n\n".join(deliv_blocks)

    tele = kb.get("telepathy", {})
    sig = _bullet_list(tele.get("signal", []))
    noise = _bullet_list(tele.get("noise", []))
    rules = _bullet_list(kb.get("hard_rules", []))

    focus_block = f"\n**User focus:** {focus}\n" if focus else ""

    quotes_note = kb.get("quotes_note")
    quotes_block = f"\n**Quotes:** {quotes_note}\n" if quotes_note else ""

    tool_cards = {
        "imagine": (
            "**Tool role — dickey_imagine (Architecture / A):** "
            "Expand situation, stakes, geography, group dynamics, moral pressure. "
            "Prefer seeds that could become a river/wilderness ordeal or social trap."
        ),
        "craft": (
            "**Tool role — dickey_craft (Brick / B):** "
            "Build and channel prose: compression, kinetic verbs, first-person filtration, "
            "sound/motion, landscape-as-psychology."
        ),
        "revise": (
            "**Tool role — dickey_revise (Scalpel + Hose / S+H):** "
            "Cut abstraction and noise; add specific sensation, aftermath, spatial clarity. "
            "Honor liberty level for delivery."
        ),
    }

    card = tool_cards.get(tool, tool_cards["imagine"])

    return f"""## James Dickey MCP — agent brief

{card}

**Routing:** mode={mode_k} | liberty={liberty_k}
**Mode guidance:** {mode_hint}
**Liberty guidance:** {lib_hint}
{focus_block}{quotes_block}
---

## Writer's toolbox (Dickey-shaped)

{shelves_block}

---

## Core philosophy (bullets)

{phil}

---

## Deliverance focus

{deliv_md}

---

## Telepathy (signal vs noise)

### Signal
{sig}

### Noise
{noise}

---

## Hard rules

{rules}

---

## Author material to work from

{text}

---

## Output contract

1. Stay honest at the chosen liberty level; nice is never dishonest.
2. Teach in-context: tie recommendations to phrases in the author material.
3. No long verbatim quotation from *Deliverance* or other copyrighted sources.
4. If mode is **edit**, offer optional `<<Agent note: ...>>` suggestions and a short revision report grouping notes by category (image, pacing, aftermath, dialogue, class/material detail).
"""


_TOOL_SCHEMA = {
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
            "description": "Author material: seed idea, draft passage, or manuscript excerpt.",
        },
        "mode": {
            "type": "string",
            "enum": ["create", "transform", "edit"],
            "description": "Workflow mode (Create / Transform / Edit).",
        },
        "liberty": {
            "type": "string",
            "enum": ["nice", "neutral", "professional"],
            "description": "Feedback delivery level (honest at all levels).",
        },
        "focus": {
            "type": "string",
            "description": "Optional narrow focus (e.g. aftermath, river sound, class cues).",
        },
    },
    "required": ["text"],
}


def _tool_imagine(args: dict[str, Any]) -> str:
    return build_agent_brief(
        tool="imagine",
        text=str(args.get("text", "")),
        mode=str(args.get("mode", "create")),
        liberty=str(args.get("liberty", "nice")),
        focus=args.get("focus"),
    )


def _tool_craft(args: dict[str, Any]) -> str:
    return build_agent_brief(
        tool="craft",
        text=str(args.get("text", "")),
        mode=str(args.get("mode", "create")),
        liberty=str(args.get("liberty", "nice")),
        focus=args.get("focus"),
    )


def _tool_revise(args: dict[str, Any]) -> str:
    return build_agent_brief(
        tool="revise",
        text=str(args.get("text", "")),
        mode=str(args.get("mode", "transform")),
        liberty=str(args.get("liberty", "neutral")),
        focus=args.get("focus"),
    )


TOOLS: list[dict[str, Any]] = [
    {
        "name": "dickey_imagine",
        "description": (
            "Architecture phase: situations, wilderness stakes, group pressure, "
            "moral predicament (A.B.S.H. Architecture). Returns an agent brief + author text."
        ),
        "inputSchema": _TOOL_SCHEMA,
    },
    {
        "name": "dickey_craft",
        "description": (
            "Brick phase: voice, image, compression, first-person consciousness, "
            "river/wild embodiment (A.B.S.H. Brick)."
        ),
        "inputSchema": _TOOL_SCHEMA,
    },
    {
        "name": "dickey_revise",
        "description": (
            "Scalpel + Hose: cut noise, add sensation and aftermath; deep edit in edit mode "
            "(A.B.S.H. Scalpel & Hose)."
        ),
        "inputSchema": _TOOL_SCHEMA,
    },
]

TOOL_CALL: dict[str, Callable[[dict[str, Any]], str]] = {
    "dickey_imagine": _tool_imagine,
    "dickey_craft": _tool_craft,
    "dickey_revise": _tool_revise,
}


def _rpc_result(req_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def _rpc_error(req_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": code, "message": message},
    }


def _write(msg: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(msg, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _handle_initialize(req_id: Any, _params: dict[str, Any]) -> dict[str, Any]:
    return _rpc_result(
        req_id,
        {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        },
    )


def _handle_tools_list(req_id: Any, _params: dict[str, Any]) -> dict[str, Any]:
    return _rpc_result(req_id, {"tools": TOOLS})


def _handle_tools_call(req_id: Any, params: dict[str, Any]) -> dict[str, Any]:
    name = params.get("name")
    if not isinstance(name, str) or name not in TOOL_CALL:
        return _rpc_error(req_id, -32602, f"Unknown tool: {name!r}")

    raw_args = params.get("arguments")
    args: dict[str, Any] = raw_args if isinstance(raw_args, dict) else {}

    try:
        text_out = TOOL_CALL[name](args)
    except FileNotFoundError as e:
        return _rpc_error(req_id, -32603, str(e))
    except Exception as e:
        return _rpc_error(req_id, -32603, f"Tool error: {e}")

    return _rpc_result(
        req_id,
        {"content": [{"type": "text", "text": text_out}], "isError": False},
    )


def _handle_request(req: dict[str, Any]) -> dict[str, Any] | None:
    method = req.get("method")
    req_id = req.get("id")
    params = req.get("params") if isinstance(req.get("params"), dict) else {}

    if method == "initialize":
        return _handle_initialize(req_id, params)
    if method == "tools/list":
        return _handle_tools_list(req_id, params)
    if method == "tools/call":
        return _handle_tools_call(req_id, params)

    if req_id is None:
        return None

    return _rpc_error(req_id, -32601, f"Method not found: {method!r}")


def run_stdio() -> None:
    load_kb()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            _write(_rpc_error(None, -32700, "Parse error"))
            continue

        if not isinstance(req, dict):
            _write(_rpc_error(None, -32600, "Invalid Request"))
            continue

        if "id" not in req:
            _handle_request(req)
            continue

        resp = _handle_request(req)
        if resp is not None:
            _write(resp)


def main() -> None:
    run_stdio()


if __name__ == "__main__":
    main()
