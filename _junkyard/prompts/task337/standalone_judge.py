
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
