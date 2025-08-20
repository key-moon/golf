
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
