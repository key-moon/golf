
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJyFW1u25CAO287MOfzwCrCWOtn/NqYqWJZM3er56VQHCGCMLAvu6z+vV0kl5Tu9nzmV5znf/3//eOX3ryIl73/fz/u/6d1qvX+3p6zZc33K0st+pdf7vT3fb6zVfH9xvt/11J/nfD/70yq+SVZzt6rPF9K7z/U8S6qpPq3ez6cPlHxGVa3VZSO70vU82/s5nlZD3lw20stH2N9f+PRfZaSfVhzZLqm7xFoVt920J6yxbTjdlsVbRbuiDlpNq8212a3ye6756T/bc/l6rWfs7/f2fEpshNfz7rIvX8//tw23FT69X8/3Lh/hsDm/LfeU9afup9WnfSzpH+ua5df7d3qee1Wujwekl/3a6/VpNZ4nrEELladsuDXG870iVi7eqtlawg+Ltyruh6iBVt3mfNlzPbPZfrhHeEmN7n1tb6Plq/dVg+V3TawXVxlrCT/8LsmyylU8uwafjyVLWhX74l7lHDwq2ypn9yxYY68yvvyZH6yR7c0u2TWjDbt5wnqXYZX7M7LuPkIbfvofts8nv5g4CpQMQYD2/l1t9O1PazSbcX1qwHuBQMM86oNZn1YfTNoeNRzFhsyrPKPuNr/iPl9sPrukyLyy+ejHa5d5AqyxvWVJjew75bI9N2x3Vu+rHiWXYFR9Rg1rzMfD97zaYwVYoz1YBWsMszw8e3pf03192giHtCr+blsD3rutMXx3stVnVYatE+aM9YIV9rrtJ/uaNuc90uHYO3xk1Uo4wr0PhmOKYhRwaNiO4SqXsPd68PkedmXxVUYkKo5sy+fFNzsiMRK9I8rzxY+Hw3uxXvDebjWq98Voxy8S2WLJ8gj76SObj6LPuL+6eW+WvXzZXLNzgBNFi3lx3rshIHYzP2xhfzUpUcRuzxd2Hzs+6/667DvFSprPC4iWbRbT5zXtTXaE6+4b1fGLXgfcUD/c/6cf7j03zIuHj3CY1w7fncN3ZfMo3nx+sAbsNA1tyAGiNf6yIa3B+LVjGp5zfzG97NeOdt2fbLWRmk/ixrLv4Uk/zMbMsnn49L6mvdEa2Cnd+lgeORgddrRZ1lf3nZLNo8lFl7f6LmHUa8/KN/OAzxPzyo99sj+btxpmhSG4DI/im2HWGG4N+OEyVFf2taRkW4fzWrYayyyPefFN4/fMo4aNsNs4umNvP0qGeJTi8X6iL2K5MCzHw/7U7jZ3xQ28KXeymnFe2dEvuzWy42E+5lWOOZdgjXLYiRnHcP9bNyIt5jWkZNck+xrPCHedtj0gba9pN+JxetgYPWpYdBg/ORtKhsyrOPurhpVAmyKMMT3/L4691Rk0OemdXsJBwcKrY281DoDnFfbyRlHEFkZYxJlmkWg+z92qG250Q5bu2Is+mnOS5iNszlva0dcIPB5ca/fFN+D1wy1frYyWog2rlHyeyqPmrVFPuY1GvSk8ahgLHLanjfck5UrTanCETTxpr4BymyolY8/Y5nVZ/MR+0FVW3Ng10VczLkI05yojAuQbkYD8cEeiYjY82fLOQrcNpyA2ysRHk/o1SojY1W1Yf7aqbsPqe7kEtlQCihL5k9WkNYbbdfN6ehTe7BpqDeaB4MZopfw55ubAr+y8pzraVOdKmZgXVJFm8zPtI7Ek1oh9LfeE7L6R3VvW0dcM8/krpuj8piAbI6GjXlKkRDQlsn1i9e4DuadaA/np7nPJKi/nAIh+0XuXcwAy2Or7uzgeRqXick5axQ+ZFe9YoLsS+YFk0p6NNsMLoB/VHuRY/QZ3Yzaqlm8BbZT3TslG66F9fTNY1b5oQ/Coyy2FvtZR0oPORjb5l+WVoSsXjVqVYlTUt2L8Ulyugc/Hkiq5w16N6UjwzSo3Rm2MIM6Dmf+KlWDmivPZMBJMRqM52U6yPUBrKP8um4ukl/1KRw3mDhsdhu0m7Svf6ajBvbw5I/kqdyU47bTdOSV+IScbt+uziZpurAEEmJbxTMEx7SvWONWDf83rVA+acUZ6XfcR9kO3I98AyiAyfiPAct2khuigeu8V9N7NiKj3UiPqQY8aT8TfreZR0sWGl2fZ5G7bD8HVkGUzml/GzKhMK4+iEu0lhhuXZYj/irCFdvL1osIK9ek2brOtCpU26jbgc78y3+qWrxIdkBWDCzA6aCZVJToAS+B1MyDAWUIEQE5E9fFUpC/PiS7BDaAnVofZ6CUlS3ADasj0fZHd8nyz8TBLrKxBW76C+h1LNBI1w8NlqHfm5loyfV7FVx6sKZ7CFPce6jbd0Y7jAQLom6j3asyWU5OkJy0hzocMcYVM/LbcHMjGTDHmRNV5/XQEmM7jRTF1tUc1nSt4L7wWNVQJRAwY91+K2fC4oUpg93x56xvKsbe+gXyZbDmu/J4ffQM6lEQ2P7uBYrt1Fo2w8+bZzSVnNxg9cogSsHePDDmErnKxdcL53vd5SrF1ozo3Zb0w0rhel6wXRzi8/9+W33MYouk1/+LOw85zveGjoG4zhHUB1amlAPk7S7yVsorvEZKJaHTIZnFozKotZynpghuMkeCOmt1Evsn9dTkOKi4CD4eUqEfB54ucjHCVzxI98WHEwJdvU8ygpUGDV80cKvX2cNX0+CZZPCOKKurt5/1EB32DnCQy2G6s8lt1XK5zKWcDg7l89MTDIb6m/FBP7X4p7Xq+FzNfqBkrWCOWaOZLda7drsEl6nYtUZ0jt4EuxlnESDQsLp6cjSrqngURu0tJFs6GE5oZfTRFv563n+pYK7DaqfpsUk13OjOmUkEsqX/6fBU8Us0BrB16C2NlvtNR41sXLTf0UeBGkRLVRZv7KGLmmd1AjZhPZh1xfskTrciE8dRzvWxfhPaBEfLNtq5mHEtWw9XqRIWbJUv4RvP+95ouX+UV7lQsYbCXRw7icuS9+J6ylCYnar/0Da0R41cLt1DuxJsCxUdapBX0telRguuFnJwnLsyywb42Jyneqvgti82+mGUvjxxg5ue5OUo0o+++84Omk6IOBCTosl45rJcim65XlvUCRuE8rgTcKFISMQpaVfu5Xs31LZ7r8ZSi336KnHjy3OW04mRfWJ0a1qv6Ckb2RTyE3+gNE71hpHgIVguN+TtP4b7lbZZqDFozKvLDS0pywCiy5W2p4utVXG3kSBH1mBn+5mznvRTiV/lp+aKY530hM/ylzzNT5C2d4q2YKaKvWKJ3zKDcZbfKebqUXe1b0le/04u8/rxHNKRGEYyC6lRsDzI6IINCDc04MB88ydkwL96EYISFHgGlIqpYLGGEjYz8r5PiyNBjXB6GSCN47zDUktsWYV4Y/beWghnrvJarGMtxnghwmVUbS2ynNLNQ8/Mq9IUzrmbWbcL0hnuveEBSr4H38pSTZ/SwmJ4FwHbnGT0QdibV1dEKWIca551AqrpndIASrOcOqhpsX1XL482ZIWIc1e9JKdpMKWmiSPNeAnX1eBND4zL9MAdky6GvWKKnFbzdReS+0ysgtdy4dJ/nrUkoMUAA5MKowb7g2dPPfnmPKPsuiHfMrufUJfmZy7fls9RgrKwJd1JxG4+4gbOScvuZifXFyDFvRPzbVP1LSnZmTy1lx4AuZ1OwRiyhloJV4dnNeWMBuVaWTAqaDvUIvbOkGobenm0WHZrvXMX5KiV7b8eoRw3u+yahniTF/QXf+MbDWCPyDWgOJUSHzTO657LMfHFnhU/4PPQfPrvs5XVY/sz1qp/88WQkWwTKus/DGUe2iJQlmtcQR785QJW4zGiO3Cz7kx4VS/QmRrwj+71T9F4tcX4l5VgzqMTzVl5GlRixWnUJag7ULvxmYmB64KTfqiPmp0yvipqPVaaqX6XkOlhlVLjOWElVjH3pbdffNzHkhmzYldyd500M3v5oghuIdjnhvg2z7GJ2OpkDIgdus8zA9ObN2yzzOIclS/azzMTzT5bEeyk4BULWhlVuR4neSwFLqsKatg2/S5Rja367Qua7pGQK2pBVrPTr1Gylk4sO299Av+9TGDCsFRRpMnM8aflYQt8o6c+/agj6PGuQESESUmnn+RciEaLpyYj6P+9U9Pu8ewA9lKetURfF7VWN5s0tDh3gjF+xBldZ7x6MEFM0C+whpvAuKdnKnV7CTnj/lGyZOh/4BmOKnsMW0Q974p16ZAjxls5wHNJbwbw9Ce0UI+QbuXFpfcEaReec1E5FIi3xkDcjdybOOxV4g7OT+rXK/+8ucTnQBui5v3ye63VH0yp7+fL4uXWOk0dlqcH7NjhryVbnZLCX/90DT2+pDs6f82KJepSylL/+Moitub94oxFYRdygXodTd3JRvVVTgzqnfzPShIvyLhbuXJ73zLVE7yyBVZLzq/dmZ5XMArAq4AkrxMolJZdoKbhrmYWtnCyl+Z0KvY0JNrEZhO6U4rvAZ+ycDQzmF86T9egJXb7xNxXJ/n+bzjalJItye/l8mPVT742IHf9CTeNoD+vVb42wzKSAClSQTz2Kdyo2+7r/BxZRZZI=')).decode())

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
