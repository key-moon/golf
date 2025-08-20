
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
