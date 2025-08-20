
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztXVtuAyEMvE4j8ZGkeTRnWXH/azRQBD/URNrRaMzygVwhxI4HzMt2un1t2zmcw084h39lDNvfX0Z5tzH7SDK+GxG/9lk//vDEUyijdi31XZn7ugazfNjG/E6SdWR1EOG+dVy92kz7LvVdmfv6DmYBtjGxJFlnoy/UXDyLn738NOtYu6cfPG3UHqW+K3Nfj2CWdxuzjyTrqHG+9lk//vCsnejIK+3ix+YHuxMx23B3PS3N9DAvnlV4bhb9LPVdmft6BrMA25hYkqzW6gs1F8/iZy8/2DO83jmfe/bm3Rf86aV578CcYhXvJj7P54gzvB7mOXnGnqzGeyfyRITbqb3haaP2KvVdmft6BbMA25hYkqyj7ws1F8/iZy8/zToupb4rc1+XYBZyGxNvktWC5tNMD/PiWYVnzf0Os3oq7ok+9wXE3qGHeU6em0XfSn1X5r5uwSzANiaWJKu1+kLNxbP42cuPpnVguFa0IJ+zCDHT9DDPyTPfg8l9i+O+j/He9PzpxfcGzutV9OnFY3kD9TDPyTM/nm0cRRTJcWjcuKaj6qUZOak3G/VGFjH6ix+bH36moc9sRL3MPkT23+LH5qdZx73Ud2Xu6x7MAmxjYkmyWocv1Fw8i5+9/PA9mGO/USR7HrmerKPqxV+Hx9bIXmO568NR9dLc8X3OWJ8zhDXT9DDPyTM/cnIcrxbJEY/cCLqj6qX5loK5mSu+t/h8c0C8S+hhnpNnTb/z2CMYBX3Ken7Mxc8+fviZs+N8xUjOeOVmUB5VL+ytfHzPQd6Ucbcqb3iw78Pct1/c+6c3PNhVnbti41Ytb3iw0fXjeOUIjHjHRUd7w4N9MRjfwZC3eNyNzxsefiYL1x65NsKza396af5GnM9MDZ+ZEawMCz3Mc/KM9UZxPU04b4s3PJq/vsIdfR5qLp7Fz15+1n+rUfuvLrPqFU/xF7uivKs=')).decode())

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
