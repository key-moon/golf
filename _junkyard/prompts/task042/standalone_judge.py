
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
