
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
