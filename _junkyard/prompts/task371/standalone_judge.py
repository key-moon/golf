
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
