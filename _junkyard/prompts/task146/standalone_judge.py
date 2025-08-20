
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
