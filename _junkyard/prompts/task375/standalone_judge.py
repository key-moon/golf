
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
