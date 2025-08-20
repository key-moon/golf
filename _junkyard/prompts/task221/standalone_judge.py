
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
