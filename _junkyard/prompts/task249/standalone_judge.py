
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
