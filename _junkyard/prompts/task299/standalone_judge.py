
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztlksOwjAMRK8DUhZV1IXvEuX+1wDalMQl/qYRQkJZDa2cp2FqO91SWsJ+ICw5nFQMsej2maSeUqz6OmuIH89ole9howV0K4hEEd1C0XJVW7VR74d986At9M2t0GE4K9r36i1Xta/erjeOwAW0tNPfoh3NrZWIU5UW0K1AEGnZD1quKqCqa5Nb6k0rrTUJOlotu5dW1xNmeSt3MInP1sG0PYvqYJK3HtpxN6kklF/JWVJvsdBKVW2TzTvLJN9ts0ybkv/kxUmYNct+Zwfjv14/7byeYEmCdjqM/vfeHczXb2dtNVJuenyar0zTb7GiM21Ngn06zEmCZweTvb16B8sPasUAIQ==')).decode())

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
