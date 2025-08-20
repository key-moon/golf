
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
