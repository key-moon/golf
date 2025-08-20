
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
