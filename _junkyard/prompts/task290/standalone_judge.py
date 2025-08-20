
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
