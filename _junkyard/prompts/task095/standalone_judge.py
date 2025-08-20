
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
