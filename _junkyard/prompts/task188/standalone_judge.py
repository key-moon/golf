
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
