
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
