
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
