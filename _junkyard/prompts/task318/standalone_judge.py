
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
