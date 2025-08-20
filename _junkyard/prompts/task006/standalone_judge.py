
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
