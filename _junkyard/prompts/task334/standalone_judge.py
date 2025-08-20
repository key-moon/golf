
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
