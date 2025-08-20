
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJylm12O2zAMhK/TAn4IROU0Qe5/jXo3ljikguhjin1wHqzK4s+QM1Qffx6Pdpx/z+Nh59N+n+ff8/zxuB+343b+uB3363n+ej7/Hueq11vHo1+r+3H++l31estXvf6V16qft/r1tj9fe92vVbe51y3tFZ+7VXkvdq7x9mkLscr+XMN2/XdVm3t9WvV/52qL5T+da5ynT28Py3/+Qrfhy9s2/cVjw5A1vouNnz36tMLYc2+NYcPhrw7O1eZeTTxAVpnkF1vlMbFa41P0tnmuXrJGC9Ygq/r0ssme+4hya7T5JHt5DvNcbnNVw1+oVuCWt2kFmwjA8dCu/DLo5T4z3wrnckQbX7rPyoEy8bnLyuGnFrxNvdwCBhOM0jikNvSI4qtawl6DXm5HrEQdVQevx8MqxF99Wr6yl11fqE+OG2tsEGTzJ1nliOZWIdE7YsNwzCtSc8RerUHqsiK2o85+r3GuSr/hVbwnG1Y6hw5xXrGJ+0vrMbWGCea63wgCjE5oxAhD7Iw2rFtW3PDY2EWv4gaLqJaswfKrL15uML/UX6xWanfivRuNeZt+YzxFKyvvHNS7Az8oRlkZRWM/X8EoR1FWYRXRFNl2e3mvppxoZ40RhzE2dggQY54hgGdI7HtJXW4LslV6UeZlZzUmVtlb3uTLKJMyyasRGxx7HbkJ8/UvtFlbOG7EzohaXq1BoteWWsmw1zsGGvMR3yudg8e6Yi/pN0y8zLvlyC/3e9nR5AtZHEbbUewdeKE25L2NRi/nRO3I1Zz22Fz7agmjWDU3QZsaGx2xwWPeAl5QFNWuK0bvzl9Zt6kjAMVe50KcV2adjXbmqhvyWqk9De1FLWUlY4g2z2NfYJTbkng5c1iDKnHWvqgiHRk9iw23PO9Seoh1qh8qRlWiN2qwrGfL+UW5Q19ig7Psmg7QZuYrK+WW93NVVKwuVZ3v5dpeLb/sqWhDMMr5Mu3MPRspy37Hbli/ofyrF/tDtzyrDpHrsR4gM3oWURbyi3O9MeMYVYLPiRyxGc7nCR1TYKI+T/2l3T+vRE2QmlreO71hFVa/VpbNZwGxju1XuYZSqSkeE7w6rLpotcJGRfrzXk1ymKJNS5ZncZgZPbV85CkeUcSGNeZroSrQqmcB36kCk3WbjvDQ/aW9AEXRyDzIqqiK1Kp5TUv5JpezpsdWRUSrTPazNTgCRFtWMIrj4bB4TTP3XK6x7IyHDNliB8s08zw3Z/mVFRjWEcXuv6It11l2ZLzVGwuKomxqpqoInfis3KFWKysz+jjxoYidsZdUvYwAlAVEhshUxyaVqII2WSOi82WNQ6bO9RRRVX9VqoNO9v2eVAVt6rgRn/tMsWRDep/t/dSMdnqVGwtxUkyVQEeZOA0kPXacdewtHxUYqrS7xessW5GtoopU5w7vezZWiSoTOkv5RZX2PLupdXqOvUxLyblcZ9k8oqIexbIyTpco/4q4wZRbveNYm+zX74uu+iGb3cTqUFM4Xc1i58r8qzKhU02Fx7xjMMMNf9ufFA+thIfrrUXaY8dOj1S9dSpN1Z54f4PO9b6796VTGF7N47mospSnt7WbuvW7qRrz/C6xBSQgmfJNNXc/VbDXJ+CRIe76Q1Wk+W0W7635jCMqnPxcyujpzDfPsllsZP5VmROtairpzGOHXrWGz7JJp+fsht6pyKv4dKnGK5vkcO3+RuwPK7hR64i0m6ywm/V2Or+rrzobYxxZdaxNiutxaEsc7mJDuTmbLuUpJ5+n6Iye9vP2BQLEyRyNjbyqyqRUseBZmfUoigBcq1wzpTI3V0WQ/z+OuCfZK/a9lHFoXeZKRV1NXafSDA+dIdbUHp1J7dno8x86Kk0K')).decode())

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
