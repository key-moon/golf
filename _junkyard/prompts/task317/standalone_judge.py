
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
