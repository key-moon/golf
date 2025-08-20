
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
