
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
