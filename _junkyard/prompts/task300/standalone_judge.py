
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
