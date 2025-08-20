
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
