
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
