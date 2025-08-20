
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
