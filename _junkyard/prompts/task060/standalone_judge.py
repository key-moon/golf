
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
