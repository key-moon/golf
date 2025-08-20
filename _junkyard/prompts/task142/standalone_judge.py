
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
