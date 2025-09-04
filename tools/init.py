#!/usr/bin/env python3
import os
import sys
import subprocess

from public_data import get_scores_per_task
from utils import openable_uri

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

  base_path = { "keymoon": "base_keymoon", "yu212": "base_yu" }[USER]
  file_path = f"./{base_path}/task{padded}.py"

  if os.path.exists(file_path):
    print("Error: File already exists.")
    sys.exit(1)

  source = ""
  scores = get_scores_per_task()[case_id - 1]
  best = scores[0]["score"]
  names = [score["name"] for score in scores if score["score"] == best]
  others = ', '.join([f'{score["score"]}({score["name"]})' for score in scores if score['score'] != best][:5])
  source += f"# best: {best}({', '.join(names)}) / others: {others}\n"
  if best <= 150:
    source += "# " + f" {best} ".center(best - 2, "=") + "\n"

  source += "def p(g):\n return g\n"
  with open(file_path, "w") as f:
    f.write(source)

  subprocess.run(["code", file_path], check=True)
  print(openable_uri("cases", f"http://localhost:5000/tasks/{padded}"))

if __name__ == "__main__":
  main()
