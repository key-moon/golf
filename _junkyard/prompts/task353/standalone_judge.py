
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
