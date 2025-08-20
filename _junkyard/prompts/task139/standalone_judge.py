
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
