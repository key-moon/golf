
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
