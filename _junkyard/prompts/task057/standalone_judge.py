
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
