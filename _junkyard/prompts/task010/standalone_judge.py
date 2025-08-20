
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
