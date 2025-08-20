
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
