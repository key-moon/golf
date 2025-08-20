
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
