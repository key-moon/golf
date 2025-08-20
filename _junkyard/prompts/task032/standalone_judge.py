
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
