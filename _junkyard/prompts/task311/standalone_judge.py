
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
