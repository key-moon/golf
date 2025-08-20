
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
