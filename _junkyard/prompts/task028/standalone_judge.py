
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
