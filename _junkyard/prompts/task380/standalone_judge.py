
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
