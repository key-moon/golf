
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
