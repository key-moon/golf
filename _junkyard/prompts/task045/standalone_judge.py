
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
