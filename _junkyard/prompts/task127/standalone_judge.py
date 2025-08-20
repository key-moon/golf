
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
