
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
