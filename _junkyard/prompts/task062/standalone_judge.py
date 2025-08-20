
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
