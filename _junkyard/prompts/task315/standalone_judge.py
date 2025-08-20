
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
