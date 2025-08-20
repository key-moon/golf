
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
