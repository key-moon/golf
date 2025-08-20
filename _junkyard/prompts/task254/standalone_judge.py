
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
