
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
