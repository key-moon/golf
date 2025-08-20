
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
