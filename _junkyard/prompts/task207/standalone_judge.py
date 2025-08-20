
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
