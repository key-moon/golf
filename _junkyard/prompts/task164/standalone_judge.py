
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
