
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztlmsKwjAQhK+j0B8ivU3o/a9hbcXsbvYxUwRBSympUbMz32zTtktr9+m2HWJcprZ/Vuc2q373PJZ1Wqwxb8e+xiz+P7/XeH2v17hOvpI++pr66avrY6RTVXAU92tfe18LcZHxxXij/K3Gyl2Wj10Xd2oygHxzuXojykTPY4T0NcZLz/P0OG4cMZYVR4nj45MZ3Y8OPRej0lENlkXNv2aOcK7Z1jy57sI7C+8qpqPwbsI7qSaQu86dVu5yR7mLWPn3n8haga5sK+pKusJ/PyWtJ6t+1GkV2doVz4xixi4nlnHK6KDpI9kjyWO5I6kjmf/2e6yn3FPrK/RUeUrOd0vkPvrUuyVDjaHFUWLoMFSO9BLbR2wP8f3D9g7bNxmliEbkOnYXuYjUMtmhmaFZ4Rmh2aCZWNfSmVSvFUoVstKxvZTfSfl99Mguyu+h/A6aE4vJxAQyp7GjWPmqcHkAT+vccw==')).decode())

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
