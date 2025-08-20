
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
