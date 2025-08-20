
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
