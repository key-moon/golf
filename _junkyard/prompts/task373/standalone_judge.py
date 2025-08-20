
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJytWFuKI0EMu84O6CdJdzI5S8j9r7FexwhZo5+FoTBYaJwqP6t6Xn9erxu43ng9wfUuWOwTI80Sv99fKOsDXMV/g6utj9JGmiUe6zu4ir+Cq63vpY00SzzWetaf1s/SRpolHmv9e6yT/LPW3bBOkqzd72tpI80SR781Ax+/bxhplnisdbefGfsubaRZ4rE+wVX8A1xtfZY20izxWO9q8ajpWbH8+FhfwBWidiltpFnisdaz/ozao7SRZomj3259ljbSLHE8uUftUtpIs8Rxb/2tz94XjDRLHOvc936WNtIscYyaZ+xR2kizxLFStds/lXpgpFniWKlurfMAa1akWnO/NcNY2f+NybQz5tZnaSPNEseM6W99MnZipFnieHL3+yhtpFnimDG31gxjZT/57bNFz4rlRzq5T+SjtJFmiWO+PWrak1j9mmrNrTVHWPlLe3uH3kobaZY49pj7/ShtpFniGHPv0LO0kWaJY77db/17rN9K1l7n99JGmiWOUfvft8P226N2ljbSLHG8gd1v/Xus30rWPpm0NrHqNt0GfpdofWDVTuoSr7WjtJFmiWPU/ORnaSPNEseTu7XuhnWSFDXPt76xsN5faW/P96W0kWaJY495vvWlgvWKSSf3jF1LG2mWONa5R+1W2kizxDHf3t96a2LdqMlvj7ne91hvgRRzj5q+NbDeISlqfpfoJMOacunkHjW9ubButRQ19/sobaRZ4jjX3Ppe2kizxPHkPhUfpY00Sxytvb/1dYj1ckwZ85NfShtpljj67XvfSxtpljjWuft9K22kWeKYMa81nUVYcyrd3z4d9BsK6/sqRc17TD3FikLa26313sO6E9Nrz621urAqL8Xc/dZZhDWn0t7eY9oXWD2TrL1atLqwKi9NB7fWCY413dPeXmv63Yr1TZusfZ7rWwPrHfIb/3fY1eJTUecB1qxI1h41/erF+iJO1u639iRWv6YOdWu9ubButffX+y8ZkwYU')).decode())

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
