
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzlVlsOgyAQvE6b8OH+eRfD/a9Rggo7u4OW9EFNYwLLoOxjGGG5LcsUphi6W0lt6pY5SB7Nqe2z4z2s3vdVX+ol91tE2VNqd49bv/rum1dRVn9vtGSz1shrDDWqPc7cG0y/98y3kI2O5GO2FLtwgzHpSHVOOitl1xyBN7JOXd9kHWisF0GFoHXv6EdUzQoGlSyYQ5ENwJCL+o1mxaGAIVOAOuya/wnO4YAx7Bb9j+FMWr7trjiYd4pl7FveLeMtpTI1/BjmdElUydTHdEoq31Ij0yJTItMhUyHToGcFa/CVkaovniQ2N8we64MVbMxJY03tT1rVOT3v+61BN4Q4+E54pLjhiFG70XrjRPU6P3mH7GCub69ur22v7L+9DcYH9eLM1w==')).decode())

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
