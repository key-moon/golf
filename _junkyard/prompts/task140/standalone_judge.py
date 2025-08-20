
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
