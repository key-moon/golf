
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
