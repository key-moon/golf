
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
