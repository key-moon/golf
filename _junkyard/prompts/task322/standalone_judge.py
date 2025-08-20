
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
