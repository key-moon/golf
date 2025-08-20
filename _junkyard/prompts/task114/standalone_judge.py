
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
