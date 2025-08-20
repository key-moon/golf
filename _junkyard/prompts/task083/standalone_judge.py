
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
