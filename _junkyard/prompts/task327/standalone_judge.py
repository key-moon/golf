
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
