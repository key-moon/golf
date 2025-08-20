
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzlmF1qwzAQhK/Tgh76EHwZ4/tfo4pIRJTs7HyyDWkJIcEIW5qfnbWU9WtdL+WnPH23UkdfPnX05c46WofX5WFk6XMs7bnht88xPLFt36UiCWZXWBqa4O4bnmANhajNFOC/ztRQxatoVDELodJt9RhVzCJBlSHL0OUIm0MCpfb0Pqt21uPVLj9glmtrbXPfB50T5Hl9chbF1O2AKmVEeN1Xy6tojl9eWU8cLTbGUidkvP5/vYUlw2vu1XY6O4U/IiO7HXp77wLppu50RmhGnnTqV2cNEp97J/c2Ex7JvY1+Ax72wGtPNPdae409I5uLAyxsLg4l2leKYESzhjpYX5/ngmYNKYCq8QSmqBpdRcNeB99BzMFTvCPdLPdLc9L+ZL5o1NoHnim8kzwxR3gnSXalE92D9g7aOXjfoF2D9gzH2pw3dzIy583d76Y/eTqeVlYjzXCm6Vb5ATUPzikHaxucU8gZcKoi3vlPjtyjTjgu96g7UkMTRPTjes6kzHMM07f9ArFPMb0=')).decode())

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
