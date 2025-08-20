
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
