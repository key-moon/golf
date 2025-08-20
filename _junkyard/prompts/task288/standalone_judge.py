
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
