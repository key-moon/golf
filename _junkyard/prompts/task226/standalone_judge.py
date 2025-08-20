
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
