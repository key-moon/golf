
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
