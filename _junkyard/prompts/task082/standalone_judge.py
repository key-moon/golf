
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
