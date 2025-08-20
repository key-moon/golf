
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
