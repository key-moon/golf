
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
