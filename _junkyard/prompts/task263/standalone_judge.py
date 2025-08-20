
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
