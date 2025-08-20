
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
