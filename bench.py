from checker import check
import argparse
from utils import get_task, parse_range_str

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Checker script for golf tasks.")
  parser.add_argument("range_str", nargs="?", default="1-400", help="Range string for tasks")
  args = parser.parse_args()

  range_str = args.range_str
  r = parse_range_str(range_str)

  for i in r:
    task = get_task(i)
    res = check(f"dist/task{i:03d}.py", task, False, resume_tqdm=True, timeout=3600)
    assert res.correct == 1.0, f"task {i} failed"
    print(f"{i:03d}: {res.exec_time:.2f}s")
