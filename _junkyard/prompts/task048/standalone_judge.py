
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
