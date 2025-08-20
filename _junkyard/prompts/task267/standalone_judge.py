
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
