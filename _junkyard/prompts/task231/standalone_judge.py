
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
