
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
