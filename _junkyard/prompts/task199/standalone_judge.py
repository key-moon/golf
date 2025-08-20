
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
