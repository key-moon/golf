
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztneuK2zAQRl+nC/lRx7HjPMuS93+N2rqMvpmRoC20aD6CMNk9GQzKiay78v3j+/vnzaX3LSC9O3rixLf0nrxKtLpCUMjJ+/11I7JX02rsNb6l91YXHY+eOaG09wCK9h5njh/51USXKxBNOaGztxha7S1nfpf2CtFwBaGSEzp7mO7uyVn5NoiORrnsPR3N9p7n9/V6T14lWl0hKOSEzN5rYO915vV6T14lWl0hKOSEzF5NnzbnbEb+lKZy2Kn38re2Fx2PMto7gKK94/R25FcTXa5ANOWEzp5pt4g9026BaLiCUMkJlT3XZin2XJsllT3XMpB7zExVTqjs4f8r2NM8tVs60fEoV9nDvFWK9qTFqeq99db7jGan+TvIZO/o0MsetFag1QJtAmgbzE5VTqjs1b9hrFOVPRwh1NF6NDECzaO1jPZqOjr1Xua9cc5jeI95Kau90nNw9nSPAaPjUc5WC8zwGXsyw+ei49EzJ6T2ah57T86c7150PMpmz7Q7xZ5trbVoPx41O20tZzZ7ZpYIyp6eW8FoPQ8TgdZ5Lj57yp96cuqRMoxu41FRKPdI2ZX2QY9h7/YY9uE95qXM9q4VBT17daVBfMpnT7VbwJ5qt6houcLQkhNCe8qgKXst3zY6Ht1I7e1A0d5Z36X3dL23tysQ3UjrPbWXAezpHQAYrXcLRKB1Nwabvd3Qag/KHXyX91vvGz47bU8QNnst7coe8jP33eh4lM3eZx/DbEb+ht6Nvca3zr6AUr8Eo7z2ctoHvXX/JIpJOe1J28XYkxrfRcejG609Gac29vQuFIyORxl3oayGVnuwGhBW2K233rq72Wlb18hm70rQX1dlD/rrJtq3DWanG+Huy93RbM/01Us9YnrEQSjkhMzew9FsD84bgHUisKs/EIWcUNlbO/SyZ+q8shLe1Cyldpmd6tqbyV7+S422QL2nRltUtFxhaMkJob3PeS3zGfkd6mq9Ys/Vesmeq1vkHjNTlRMqe2ZuT+yZub3b/zlP7F9R1nPKnLtiz7lLZc99QnKPmanKCZU9/H8He5rj7CxGx6NsYy2uz1DsuT6DRKsrBIWckNlz/XUpe7a+b9G+ZTc7bW0vNns6vQbze/70mpiUz546sQXs6fPZMFqf5RaB1rPy+OzldDh7leMOMIyOR7menG6GodhzMwypx+DG8eUeM1O9rpHJntt7KWXPnfkh0X63wOwUd2Nw2WvpoewhxzYnRsejXE/OlrNGmz09M4bRcoWhdZaSz96VpN1pyp4+2Rij41G+k41tWgf9vXUQHY2y2itrAp29uuPbR8ejjPVeTmWG3dnT+xgwOh7lsrd06GXP7EApp8yZfR7lM5qd6r00TPbaf+LRlL22IsRGx6Mb4bqWl6HVnj0TuEX7U1Fmp+3UGTZ7ZkUulD29jhWj/V6P2WldU8xnr6a7sdc47lvH6HiUyd6zQy977leIUqvF/daP3GNmqn+XgMmeJk+xZ/nWOXvIj2hEoLz2rrQMxlqWQXQ0ymzv0S17eXS+Hx2NMttbBvaWrj0/ojE/5bLnRluKPTfaItF+r8fsFPfScNnT6TUoe69u2fNjwfNTNntmNbzYs2vIW7TfXzw7bev52ezpdB+0OX3vNyZltrcOnpxr98m5Du8xL2W0B2Muyp4ea8Fo/4sjs1PmsRap/UzZ0/v3MDoeZdu/p0la29l5cupzqTE6HuW1l3aDdezlvVO96HiU117quXfs6TMjMDoe5bWXa/tem/PZbXM+h/eYlzLbS6uNu/09/5taMSmfPbX7GezpPcMYrfcXR6Abfb13pWNQ9nwbLiZ9f71/AaeAGJU=')).decode())

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
