#!/usr/bin/env bash
# Walk This Way — Cloud Agent startup script
# Builds the local Python virtual environments required by the repo's
# stdio MCP servers. Called by Cursor Cloud Agents on fresh VM spin-up.
# Idempotent — safe to re-run.

set -euo pipefail

echo "[setup] Walk This Way Cloud Agent tooling setup starting..."

# Ensure python3.12 with venv is available.
if ! command -v python3 >/dev/null 2>&1; then
  echo "[setup] ERROR: python3 not found in PATH." >&2
  exit 1
fi

PY_VERSION="$(python3 -c 'import sys;print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
echo "[setup] Python $PY_VERSION available."

# MCPs that need a venv with the `mcp` package installed.
# (james_dickey uses stdlib only, no venv required.)
declare -a MCPS=(
  "zz_COMPASS/MCP_Implementations/STEPHEN_KING_MCP"
  "zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP"
  "zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP"
)

for dir in "${MCPS[@]}"; do
  if [[ ! -d "$dir" ]]; then
    echo "[setup] WARN: $dir missing, skipping."
    continue
  fi

  if [[ ! -d "$dir/venv" ]]; then
    echo "[setup] Creating venv in $dir ..."
    python3 -m venv "$dir/venv"
  fi

  # Install deps. Prefer requirements.txt if present; otherwise install the
  # legacy MCP API required by these servers.
  if [[ -f "$dir/requirements.txt" ]]; then
    "$dir/venv/bin/pip" install -q --upgrade pip
    "$dir/venv/bin/pip" install -q -r "$dir/requirements.txt"
  else
    "$dir/venv/bin/pip" install -q --upgrade pip
    "$dir/venv/bin/pip" install -q "mcp<2"
  fi

  # Import the server so dependency/API failures in module-level decorators
  # are caught during setup rather than when Cursor starts the MCP.
  "$dir/venv/bin/python" -c \
    "import runpy; runpy.run_path('$dir/server.py')"
  echo "[setup] OK  $dir"
done

# Verify the filesystem MCP dependency (Node/npx) is available. Not fatal if
# missing — the server will just error on first invocation.
if command -v npx >/dev/null 2>&1; then
  echo "[setup] OK  npx available for @modelcontextprotocol/server-filesystem"
else
  echo "[setup] WARN: npx not found; filesystem MCP will not work until Node is installed."
fi

echo "[setup] Complete."
