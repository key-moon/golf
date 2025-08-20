
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
