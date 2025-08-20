
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'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')).decode())

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
