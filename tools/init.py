#!/usr/bin/env python3
import os
import sys
import subprocess

from public_data import get_scores_per_task

def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <case_id>", file=sys.stderr)
    sys.exit(1)

  try:
    case_id = int(sys.argv[1])
    padded = f"{int(case_id):03d}"
  except ValueError:
    print("Error: <case_id> must be an integer.", file=sys.stderr)
    sys.exit(1)

  USER = os.getlogin()

  source = ""
  scores = get_scores_per_task()[case_id - 1]
  best = scores[0]["score"]
  names = [score["name"] for score in scores if score["score"] == best]
  if best <= 120:
    best_banner = f" best {best} by {', '.join(names)} "
    if best - 10 < len(best_banner):
      best_banner = f" best: {best} "
    source += "# " + best_banner.center(best - 2, "=") + "\n"
  source += "def p(g):\n return g\n"

  base_path = { "keymoon": "base_keymoon", "yu212": "base_yu" }[USER]
  file_path = f"./{base_path}/task{padded}.py"
  with open(file_path, "w") as f:
    f.write(source)

  subprocess.run(["code", file_path], check=True)
  if USER == "yu212":
    subprocess.run(["code", f"./vis_output/task{padded}.png"], check=True)
    subprocess.run(["python", "checker.py", "base_yu", str(case_id)], check=True)
  else:
    subprocess.run(["code", f"./vis_many/task{padded}.png"], check=True)

if __name__ == "__main__":
  main()
