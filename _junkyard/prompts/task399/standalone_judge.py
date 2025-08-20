
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
