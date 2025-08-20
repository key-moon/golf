
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
