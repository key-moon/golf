
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJydlkuOw0AIRK+TSL0ArmP5/tcYjyZtKL4ZKwtHdiHgNdAcr+Pgdf3OddC6fvfz+nO/QcX5Xq/ym7FCxbbi+13uCxXbSpZ81FJYWcWflXy+SZkXKjAvaiK0CrXi0YqdFd+EavL2ufMSQyHPyyqU4f5WRWgVmtdEngJ5e/I9QwYaPNLgQEO5UlOHqlCGNuecoSp8bUhDQxVahzL4sgok352XVWCEvVU8ZRnzkpDX817uuxIVMa+evDjyPQ0paMgYobgItVMrGqhQq35uoALz6isqVu80NyidGxr1f+b81F+U9Jeyq2lYBdZhN3szK+25abLFiqqtUBHvlJ4hJXdlZ8WJlXZP38sCd6W4OGJecJIuwnr2WoWvjSlCgjtFZ3/vi8HXNHtREWlUp5xHON1EHG6ire7vSlVEGtPspZBXtxHls5dd9PVuw8m0+X5nQwr9BMA65JEGOxrsSGW+rMKfcjdt4qb3bMeWsXol2RwmX5T44rGXOenlZzs253EU5H99nT9yn/KT')).decode())

def get_cases(case_path: str) -> list[list[list[int]]]:
  return ast.literal_eval(zlib.decompress(open(case_path, "rb").read()))

if __name__ == "__main__":
  import sys
  import warnings
  warnings.filterwarnings("ignore", category=SyntaxWarning)
  warnings.filterwarnings("ignore", category=FutureWarning)
  if len(sys.argv) < 4:
    print(f"usage: {sys.argv[1]} [path to your code] [path to case data]")
    exit(1)
  
  env = {}
  exec(open(sys.argv[1]).read(), env)
    
  if "p" not in env:
    print("'p' not found in provided file.")
    exit(1)
  if not callable(env["p"]):
    print("'p' is not callable.")
    exit(1)
  p = env["p"]

  total = len(cases)
  wrong_cases = []
  for i, (inp, ans) in enumerate(cases):
    try:
      out = p(inp)
      if out == ans: continue
      wrong_cases.append((inp, ans, out))
    except Exception as e:
      wrong_cases.append((inp, ans, [[str(e)]]))

  wrong = len(wrong_cases)
  if wrong == 0:
    print("correct!")
  else:
    print(f"Wrong: failed {wrong} cases out of {total} cases")
    print(f"<failed_cases>")
    print("<note>only first 8 cases are shown</note>")
    for i, (inp, ans, out) in enumerate(wrong_cases[:8]):
      print(f"<case{i}>")
      print("<input>")
      print("\n".join([" ".join(map(str, row)) for row in inp]))
      print("</input>")
      print("<expected>")
      print("\n".join([" ".join(map(str, row)) for row in ans]))
      print("</expected>")
      print("<actual>")
      print("\n".join([" ".join(map(str, row)) for row in out]))
      print("</actual>")
      print(f"</case{i}>")
    print("</failed_cases>")
