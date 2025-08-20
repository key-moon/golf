
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
