
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
