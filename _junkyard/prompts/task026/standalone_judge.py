
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJytnV2OI0cMg6+TBfxQees+y6Lvf43sZtbTEvlR1Q6CABl0xuMq/ZCiVGXn518/f67X+eufv//993m9fj2v7+f16/mU59+/X/8+rz/P9e9//YevV7xf2X4er+P7+frx+uunvVtd7bR3r6vT779Wr6ukn1+rn2X188/qv59XsZ1sXeKrr9e/V3+vchSbjz/vcDTb33vvq9++UNvPP7tbsLvu+e6Do+0mr15XO79tnXf39ftP435+23KKZ+9375Hou+2ReK9ePX1HwD1f371nFcfZI1Hzhjx/gA807rdnU5xP8fwpWfpeXVebV+85vl45EtXWiombD96rv23WXM94V4Spbbqbvtue84p3z4Mb76esptxWs5AilRD3tvmwCBzFdkKUenbJbs7XEkSe33FXtqnxdq7Td1/N1nu1dWmW0erV5qOtSqv3OOpuNBKVXZb4asc2zvPOnKfZVutAxzfxfM9t93znec0q9+zCyHhW9rhr/G8EHuZ5rZiKb6+onedvvGeWcc97nPu7Z+alqsRxJ8b1GqdxT1zX+aBWHV2deZ64juOueaE1riJwNW1D8b99MceduO+E3Z1tdxPijoZ79TxVTMVzR1jfna9+yOorrk45TuxSd6vKyitsxj1rG1cbrG1UdXbPs57zuLvnmes865SJ1fPZB5PtPa7OhW/mVa1TEddt95x3tnHN2pXWar5RX1Wuo5qmakNtX+h517iJHxLT1ly/+V57Ge5diHkZI+557SZmvPe4J43rv78jMeP9ibZh1Vj1fPVVR+Ts+QWeV9udaRX/3Pfp6tPPQ7RNfTft47TmkbbJmnbGe68aifdTzve/v6SDVnV5XJ51C2ytkSCN65EgdXFcPd5U30nX6epqK3k+63lX1h531SoLfeHdxFxlfHXPea1xpCK5i7z/ftbz1EVSjk/499fXLKTVqYNWxHlWLVw95clte9ftlXW4myB1wYji+t7jXj2s8SZVSSrR2WanbSau8yycpwdJXRDP+8wqqYtDPJ9z3us7KWrHe8o6qrDV096bOMJcfWjWJaTRrFLx7btZL8a/M/Hn/fsJtnUtk/T7KZGpWTdNiY+wus8eFVE5El7fWc95zutchjRszXlW2F5hjxZ39ny3lXaT9bvqvGvQdfduqI9TfDuenylq1XOTou5xIy3DXMgqs2bdIYqauc61Dc3rmVkT12U1mc4m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')).decode())

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
