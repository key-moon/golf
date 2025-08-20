
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJyVWFtuwzAMu84G5MPTTw8T5P7XaIe2iSTz4fwsK6raskRSdPaffY9tbHFs++vvNl7P9+fXP/vfcfxun4jvN+OM/I94pIg4f4vWGGmN927js8a1S5yr14gHiBgk4rt/LORxPfMaK5nmb3DFotUjSB4jRd6vaZyrs3pEy5Tn4eqRn0F2CbLLSl+i7RKt6iPVAaOw/hZ1LmMLV72eMmd6H4WKUQ7rYxslUxQRDae9YpHwgVHY8TH3tu7PTqvx0fsSoHPRItRpr8qhPPITR+TO4dOG7Mt1BozCKBEeY3yNuluPqH1xayDeVkZhDapsYMq/vguqelisVzbMve26rtSBIWhmFEfQKhs81pHSRcOH55zSQnYWlgdnpcI61qA6edy89RVja6zrWF6r16NPdadBDB+zd+Dc52uw+TKrw0o9OKM897Ge9t5eu9xxW67qlY0qU6Uws+JqfPg81lQK+7GgfZnV0ukY0uQ7eqodva6H09OuQWyKqdPOKqUdCsJp11PXfaW4nJWrKOQepvZ0zcM4Z4B5W+8NXNc5byujYjpLtKorBPEZ1XuL2BBpDZyp55ybt/f9Keec6y33H5VJzqFgzs27eOfInBLvLfJ0Wh0UTp2Ohc2Dr4G6z/0pR6H3/DUP1hfutpC3dFNMZbqOMY1kpUH+XQ7vbVd+7ulcX/RE1i6nT0Kex4pa5rq4evAI53IUCp3CdA/j3LjvCz8tr9h8WqVjDutqElbeKlZy/XAOdu6cR6F/96nff3DnmCvGsc5Z6bjfOce95cqM0hXTs6Heo/wU4+6COccAuzj/wV2fqli/E7K3LFy1Y1pDZ6q0kKvUrHRO+VlEncxOHbSOqb4wtUR5uIpxNnAU9gg2kfV86ZOQO4NVvqje8puWZ7Z242i+uFuj7xybYrxz/bRYP/SbTaTJ3kk7n6zUQXupWn2VB57q/d7A3p96p8Q0qNZSKS6vWIA8/P3W8UVNU36/1T6oT9O6xvEE4H02UA==')).decode())

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
