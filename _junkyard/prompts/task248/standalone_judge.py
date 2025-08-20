
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzlVlsOgzAMu84m9YOcB3H/a4wNRu3E4aGxDTYhtY1bUqdOoO2lbZvSdGVza33bd71lo1U2jrtrGXZ/en2pt0c/MgKkTPZ9pYG9bh5Y1v12HNk4GphXDpWVuZWI4bo171I0yORtY5vGkzZhphA+8seoyKsJ3IQf2Jmjrg9yPQlqAq25g48JHyY881kD5lDWy2GsVkAda1RqObrzfSe0hl+wWQv4xmglvd4+K2bmQ8Uq9b3ukaGuVFUNB8NiNseqVNWn6lScfNg5UVCpoJRQauSReFWY3UcsjIX+JD42jp7Ph08wmbPEp2VsfvOGMKzb1O56J8xy4RCIrxqu9eSPGut8YY3IYEKSCuAcmGP9p7fB7gbkCbun')).decode())

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
