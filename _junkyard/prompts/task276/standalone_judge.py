
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
