
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
