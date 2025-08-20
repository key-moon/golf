
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
