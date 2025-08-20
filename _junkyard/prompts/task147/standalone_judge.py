
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
