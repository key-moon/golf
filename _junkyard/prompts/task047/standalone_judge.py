
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
