
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJyVVFmuwzAIvE6fxIf35SxR7n+NhzHE4FZJ+2MHMQHPePDxOo4MGdwJuDvIuDuK8ePw5/kHiGiYaZRphJzxQARG2H+llkY48OAJMXePiNklXoh2dWncxSISJKqOKyRCpu2kq3/euBTVZXJoipNGVKiEwBUqIerWJWAmUCYQcsaabTNK6S5So0AhBK5QCFHeuESIlJl7/KjYPZdxduFQmZOtYfvLeezNRcpEdZ5fFXPQoVNm7v0DF081vPLJzqUToqtaOyJdvkjsk72LOChtDlpcNAfhZPUQpcp2c+XreXn2+vCWeCywx3bE8njmmbOIofJSCjj+dW6fJmpM8rox4NjWkDkJam7szS0tC7vQchnuX+4Dji2Xp3esGx20g/zVRVfXXhfE8xsUzKug2a4a+l+pZRUT99VtopbqWm09L15N1P2Le/+Onf+v33/u')).decode())

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
