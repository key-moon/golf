
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
