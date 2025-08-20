
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
