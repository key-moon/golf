
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
