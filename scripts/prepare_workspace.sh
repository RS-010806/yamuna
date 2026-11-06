#!/usr/bin/env bash
# Creates the working directory the executed notebook expects and links this
# checkout into it, so notebooks/yamuna_encroachment.ipynb runs unmodified.
#
# The notebook's first code cell does os.chdir("/home/claude/yamuna") and then
# resolves data/, src/ and figures/ beneath that path. Rather than edit the
# executed notebook (which would desynchronize its source from its stored
# outputs), this script makes that path valid.
#
# Usage:   bash scripts/prepare_workspace.sh [TARGET]
#          TARGET defaults to /home/claude/yamuna, the path in the notebook.
set -euo pipefail

TARGET="${1:-/home/claude/yamuna}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ "$REPO" = "$TARGET" ]; then
  mkdir -p "$TARGET/figures"
  echo "This checkout is already at $TARGET. Nothing to link."
  exit 0
fi

mkdir -p "$TARGET" "$TARGET/figures"
for d in data src figures; do
  if [ -e "$TARGET/$d" ] && [ ! -L "$TARGET/$d" ]; then
    echo "refusing to replace existing non-link $TARGET/$d" >&2
    exit 1
  fi
done
ln -sfn "$REPO/data"    "$TARGET/data"
ln -sfn "$REPO/src"     "$TARGET/src"
ln -sfn "$REPO/figures" "$TARGET/figures"

echo "Workspace ready at $TARGET"
echo "  data    -> $REPO/data    (floodplain shapefile; .npy caches are written here)"
echo "  src     -> $REPO/src     (nn.py)"
echo "  figures -> $REPO/figures (figure output)"
echo
echo "Now run: jupyter lab $REPO/notebooks/yamuna_encroachment.ipynb"
