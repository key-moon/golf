
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
