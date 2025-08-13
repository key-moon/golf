#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <case_id>" >&2
  exit 1
fi

case_id="$1"
padded="$(printf "%03d" "$case_id")"
file="./base_yu/task${padded}.py"
printf 'def p(g):\n return g\n' > "$file"
code "$file"
python checker.py base_yu "$case_id"
code "./vis_output/task${padded}.png"
