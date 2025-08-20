
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
