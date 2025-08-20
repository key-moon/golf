
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
