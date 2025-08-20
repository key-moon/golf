
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
