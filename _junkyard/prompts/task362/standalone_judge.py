
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
