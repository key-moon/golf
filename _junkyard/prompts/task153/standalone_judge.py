
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
