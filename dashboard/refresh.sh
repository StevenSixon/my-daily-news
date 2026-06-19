#!/usr/bin/env bash
# Regenerate the dashboard data from the pipeline output and rebuild bundle.html.
# Safe to call from deploy/run.sh after the pipeline stage; designed to be
# non-fatal (callers should invoke with `|| true`) and launchd-friendly
# (resolves node/pnpm without relying on an interactive shell PATH).
set -uo pipefail

DASHBOARD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DASHBOARD_DIR"

# Public npm registry — the machine's ~/.npmrc points pnpm at a corporate
# registry that lacks create-vite/parcel.
export npm_config_registry="https://registry.npmjs.org/"

# Make nvm-installed node/pnpm reachable under launchd's restricted PATH.
NVM_BIN_DIR="$(dirname "$(ls -t "$HOME"/.nvm/versions/node/*/bin/node 2>/dev/null | head -1)" 2>/dev/null)"
[ -n "${NVM_BIN_DIR:-}" ] && export PATH="$NVM_BIN_DIR:$PATH"

NODE_BIN="$(command -v node || true)"
if [ -z "$NODE_BIN" ]; then
  echo "[dashboard] node not found; skipping refresh" >&2
  exit 0
fi

echo "[dashboard] regenerating data…"
"$NODE_BIN" scripts/gen-data.mjs || { echo "[dashboard] gen failed" >&2; exit 0; }

BUNDLE_SCRIPT="$HOME/.claude/skills/artifacts-builder/scripts/bundle-artifact.sh"
if [ ! -f "$BUNDLE_SCRIPT" ]; then
  echo "[dashboard] bundle script not found; data refreshed, skipping bundle" >&2
  exit 0
fi

[ -d node_modules ] || pnpm install >/dev/null 2>&1 || true

echo "[dashboard] rebuilding bundle.html…"
bash "$BUNDLE_SCRIPT" >/dev/null 2>&1 || { echo "[dashboard] bundle failed" >&2; exit 0; }
echo "[dashboard] refresh complete → dashboard/bundle.html"
