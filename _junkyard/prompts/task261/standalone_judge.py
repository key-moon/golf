
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
