
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzNXW2O5LYOvM4LkB+zP/o0C9//GnnYHbdIiZ9F0tMYJAgU2ZJLVLFYcnf//t/v31//bn/Xv0bbK9hPb3s5/V7u/f7faFz9a93hu+3X9z9ev3t+f/4Pa/u+w5+2+0raj42w9XvP+p9/DbRfZHwU2RyK0VX5i/Z6mj//tT31n//annr1k0be0fFQ9FZlXz0L7ZfQpqMjR4nWZq9eLLY3bP703LD50/a3H+n9viPpTXbuu/c2sr16PxnbuZXKt1VjO7dSbbM20dbb9iiJX3s/dQfa1ii/Dh56o2n2k2L775Vr9bR+VbTvdcXR8TJiDW3GoFtGpOhI/RjeYe6djW2dj/2xc1z+Jayyhzbjxi0WObKv7xYvPnUup22Y7unLkplrexRghXvta1ccr37zCtBueyXQ8eM4xzgeb78x2556xfaGraoA2Q7Y4pgzjtRvm3UB7ROxLl3OVhBG+0Sswu/nE2cUJYp2X4VSZRL56ukKBRnjPetW3u5G1q4l87zdjazUD60ls3HsafDOiufaqpsTCT4yqybJHakG36I9lXWDs25Ee2/D3asXvb4N7XMU1L2SVo/lTaVfV5aMtFEMp2tJpI1ic2dJiuGdTaV+wVmHYrtWD3YpxRNtS/d6+pjOr0cpVtGutuFxHK8lKzPEPZH+WrIjFjH36hneZmgomVPu95m8jcZ2FO3qDNHYnkW77mt07wGOtqejUV+jugeOWRc8wDXHykphK3AFPMC7TTq7iTtQ+ormVyBSS2Lcm23j845kSasa8aoWZO0p2sS/3bKk1O896+BpAoJY7llyK3Vtpwm0p64N8JODp5jkWRSjeSDH290oTrpSXUzS6XJNMMm8y5VVgC9yh44V0Nvs7KwpQAmJhdhCwkYsMsM5f5sii6u97tim/Wzn03JIpZVabc/FdhYdvtIVDR7j7Sw6EvdyjmaqwuDoCd5mGIKIzWdJZEcvJPL14Czafpu+B9CV8q/VeFtq0/cAX4Et2h2OnuPtCLI5xF7Q/Xy0c+yiI3Z7IrTf7Z3Q+/F+7qxbXKk8R/to98U2svMlFDna3KmK7YvKmTuim6S2XL3qoX0iRpFd3p7UT3tixMtGY3vSJ2G5FES7p6q2OF9ytHznC0MbR/GNJJx1tf2TYxINRbIGV7wKojF87wsa6/z8kvbrfldK6pdnHOYZtKBtsQFlElYbbffbTxN4dbN5BmK/znelprQ1yturTa9a5hwohEmQDFZBMcpCF+S4xlbFQxFnIb9yf/97JEsyXJOxTTMT50/y76vy/oedYedOyqbR5m0Z3pZQ5Gjr/dAZPsXbXjXSuSqmlkrXkno1gq5KPt573pavIGvxe02TSIjZWkO6n8XvntO74T1+doNcG/FOrqazG4SP8z74e9aDsV3R4K6WaohttgqbnvE0uHUtnQvXQrO15Gc4rlJbvSJ/wnHdsHh4BeJo4wzR5YlgCvCNUDv3+m3RLEmz1YatmK26PnmdHXf6U06VLIkowGyNWMmS+ezcFdt4RuzwSfwYY9imMqLtl9urfMx69KQMbWMMn4rtHobwUTj3ReQEeS5L5p/llbi2niV1xCRk3/fc2tYeWNdK/b5KaPP5PLsqEbRpmxXvEh9XV8WYdTOTvLYIy6IY5XyUSbhPQtyS9yjEVSFZSVN7OXegE+1Kha+N0Ym2H8cbtoG9wp1ejvbZ72lXyttr1djm1+ZdqezpxGxsMxxgPravjbpS9gw9VWh51La3t+XNhO5B9HYuPvN1aKTtMvQ29a55fEr98nVoYdbJty679TaaBy7lrUuG9Hfbdgac0tu9eQBjEkxr5PSMfT+bSRB/LqtnyF0D+eILQjviYeTa/LoR0SSVE4b9ibG6sQPttX4nYhjaVlvUAzyv5k+98QtBTOqXQaHbA6xXKLF5r7acJsFYIztDj6MtLiezBmIb9/v0Z8nez4ptSzPbfh8d16sl9ZpzopbsUna9PomthW3NrD1xxi93Zj32Zhq7Hkbbi+1s7bePUvUKbV+QPocX2zZ/4rHdoWcu9zNlK2Y3HNxM56+A3s+ZdQjtmXqwwlYc7S7WiLXh4z5ZS+rX5nWPpkkqtaS+V/wxpLkIsx5zpapt76onrUnYk7O2Tv+D8PmmUzhv037d3wZT36fbqMnYZqh+t9E8l/OjrdyOZOef+A6H7izZVaX3V/3HrGEFOMckkVXxFaDvwt6jZJkEX5XpU2Ct7RVaUR/tDDq0zXP/vZrTqk2NWRcq9y6OPlfAry8ttFlMbehQxKR+1gztSsaueDJoe55kD9pfMNq2/rD18RolesKAV/M/7QGieiajSfR+/gwldsH1zOw3i+ZWKo921THKrZSE4uzZjd3GGafiaHm5IZMlNxxMnaLrGX4/LDfMv7+NKcV4dXOi+PfPVntVj6W/urFRzK9KVSnqaK+rK74gkk1z7II5rraHMaNTTrQ9F+lGgjIGz2p6NW+tXmHWP6RJXsUxpjUJj1myXtsYUj8M7Xp85hytLNpIjeivgO5oYWNE0e5oQxyoiAbHNMnZJjlL3jkNrsGfeFfKYo1KbOs9KzqaswblfI6sdMLgzjqI9pQn0oV2vfKQ+1EU7/vROJb6VdDOxSK2Kn1ZklUs3226TomuSlcmfv4d157MiaLN+0mjTGbOiiZB4rhSze9oe5oEiWOsRuzR2xYTYRX53vZa90qjbbtStNJm5wGHajqr/nU/PY79eM+iXYlF5pS0ZtiFdiUWtzqdrRTdA1I/eNbj33VZ2QP6tVSTIJqZjpF1tPBrp98D5G06M2VXtB7b0ig6M/GV2nKxu6LvWY99t3wOba3NqiWzlbu/Bzb23dhFWpU+DzDehmfTmVryHAXNpogLa8z6I3+FmY2TRNtCVuqH8jZS8cz9CnPFFQ5ESflXmCVVaMV7ZUXfs076JPVa0h8jcu0e2zO+hsS9UY7GmKTi9/nPUqtu3s+29ew7N3+2uomjmEesqkkkdHQUJbS7z3i81cujXeHjdXW1vtTRXmitp97OgVXu3XLnxfU7RVHqF5j1A7+bkEeW8YuLdq2WRPhY1+W2fv/EN4qjmoQhSHqy6o/FYt6VktsmNElVf1Sqfo9xMAXIR6lU/RjjPOuTsDu2KMB+P1rXONJ5TrcCzCPhx2ydhfKaxEOCrgpnF8bIRr/ArD+gckf2z4726tlfuesrIK1UL9q97LLulYt3He1edrFdKdu96kFbej6yCu36I4v22YYqtor+wNHucpskHMgIMNpdbtM5suSNM+1h9MuhPeNAvfdBaYwOBSiPwit8qtO5yyX1c2c9rgBx/RGpJescjfrbSA07F9v2Slu6KTJuPbZtPrZ8F3rl3S82bu9v8HVW846Wgn6Dr1NHd5/d9GTEmQx7tXymjKAxkGGFWTejvTMbiqyrpUC0/epbr9I5Mki+mPqmI4Tzsz6JzdsrFjfm3dqkqmXdT+JoOpNOn8SKbYyju+pQP7Y9hmDYFGO2h0libXRNEPdKXwGjTgC/w0HSEJbWsFcg66F/yve4dvkkvbUf3RcU2e2Oar9j1g3fK9Vdc0b1tn1Hm7dtfrdniOv86c+Ufa8LjKwaJU2fKXvjrWQ/j4Wkyl3PnL28jWROPZoilXtklJprqmdiySvEK3cb2b0frq3lMbBaUt/lXDNv2LCcfdaI0hi83+bfKv16q5vOyt2+n68A+frpGSzmQMkzzN5v8jevu7S1Hdvc+aRPzPnz7DerrSuahKpKHDHcF9TRJlhuPLvQtr29NQruC8pzyaGNZbCKssuh3ZnBnvj9vsqnU7Ps0o82w+vIflyxcQdKUnafgPYbcRixPOf7z3Ip55JIJZN3m1Cnd/Y3+OL3yzJTXgFyxGLVyJOnwJk2S3/YKwDuSejshrcxt3Drt1ZA8sazJxZRtHEVV9EfcSbBVVxFf6Ar8Jm/VOvPxYttaUdzTbJVegHEZk8TahqC1d+w/rBcqZqG0NH2V8VGtu5KIbUk7p0wnysU21jcSZ5IxDuxmURnnN7PAqM+ib4qPY5r9URAXxVp9SqxnUeir5LxXCkcCc+3vu9nVzK9rlSfr5HLulFNMu1raFlXcgJ0x4DMuuVbcytOFXa/S33H9f7zGALVzL561PtN/nJWxXF164SGX85iauPKaHVU58/+SgXG+VG0ozPUV8V3tO7Z7NmP7ZZGtOsqLnItxtvb84AqbrXpbPAEb1tPjaq9/VnsfrYCtBCjDMHcj4CuWPfrdbnwz5T1oI2uns4kVW2tjZxVe+KsH/zOtB4NfqLteyJ6Py+bet54ctYPOK7ZVckrQH8U3Cs8V0VmJovBsmjnK5m5al5CO++TzFXzvI326/YA+Xxy155tduWOeIB0VViEbvEu9Ttn2Fu5S20VZRcbI7LKfpakbVFlx/BSOR93eqe+V6ozI3bqbUuxecquYdYP/ponu1sD2hujshjLn9BW+Lhbk1T4uNMrpGjzMXA+zmdYeNZDvy4UbwOVa/HXhQh+Doqo34fHNt9/da1ht+WzJNcGzMVgsS31y89wKkvm447Hew9H62jn487z9qxzn4ZZj73hILXpq5fON+U3HKR++ur5HqA+bhZt3IHiHmfuWq+6of1Qx0jS0RTFrR7fGKK/uulmA/1+max7lf1tbRT9fj4Lkf/TyiRemxXH3jPXaslYm5XpvHi3dL49Ro/jWqnmcQW47udxtFSlT5/TVPT2RIWyxsiz1bXp7Xv3UgzvXa65UpEZbviTOOZsJfXLoU3/Kv7Hk7Uk4n98Ri2J7vJq5ozsqavt22AibTxmKbfwPcUz57mivd++iCtF3uavspUlpRpRryXzJ8P4KuOfBOlCFrufhrakhRcOC1lbM0sj45q+A+29H6rL2fo1or3aNgVxsAEfZc90UtW/rZ/abw7t7mvt1cuj7ffLXYtUVX0KMBfbVZ2SV4CSu+qf8dBR6zqlx5XCtQu6V6wsuTBbo6AVSmWvTKGNIWbvH4xJZLT//uU9O+uteknteW7t/Hfv5LVLXG93zDCvNfAa9hO+M01qezn3y6A9UeEzZ+qimp7zO+/3CW+mWdd2xbZe8fj9rGsp2swvFLPp7Nvyclu3B+hdnc10P+MB5tp8BdhZGeV529fHut+HVkZ9aNPsN+de4UxCs992JkDiU+6XQSGjy3/62xen9LasIRbaKzJlrXHf7zP09jfeMLt417oMGGASP+70+lLSzLrWiGbdye9MQ1DMx7aOmI/sOUpFuwRm/UG15FdwX3wFYnuilrzb8Mw59bmbPB/nsu6VOgU+++X5uCPrdn0SpIshELTfWBgcjfGsHktTZzfoKUF2BXJ+ys7bvGdMC+c4+pmzGz6fJ9WeWScEvg/wbtN5lo9cqzm3dRYZ7Imzm9co2jXE3mhsbZG3I3rR7qy0J3i7Vy/kdukMb1ezH32WCgtJaG94Bbj3vKOkU2h8bkpD3T/BWT94CpwbA9PbvZW2pcEl98pzuXrPbnK6wmcN/X4a2nYboiss1vA0+H6/Z9/f1pHNsmeHAjxH0ZH1Pe9tlBYmsdv4ODXOt/2ZjthmmDHOl/rt90P8mc/8xUPG3C1oSxUK41qj33m/jZHJHuDxvvebesfVzqb1VbmK77ja2dT2xulz2KtyzBqKbZ3LMWc2fz87tnUu93xrhmP7/bpOE3pdKf9+ESahSDDFwJhE7ufNENP5nVlyopLpzJITlYznPfJ+leoGY41YGxrbkv9BY+5GQuqXmeFUbPdydJd2uQJ6G+HoXu1yzPqHToG9+3Xz9v0XPQXm9zv7YXlg+pPXftvCNRUlTZ+89me48FoorhVZaEv9jlk3VO5eRrTrBGylIkxyt+kuErnDJfvbXh7gY7izHvqGusoK5NDmSNA2i6M9r9BaAW/cebS79XbWcfXQZuctYQ1hP3HeDfskf/uVGCOiAO+2Ln/bindvX0TQzvsk9h7AvGwd7bxPYu8BKyNmvWyUSbLec/Va5gAGYlvylKPeM3KtnnUnz25e23wy155t1Kv3r9WYhN/Rq270Kui8n+0L2v7he9Zjv+UUQ1brF6lu5jja1+96zcnvN+FKVfk9vy8isb3aqvxe3Re9aGttbwZu3wM5tLU2vXL3K3yCrrEHeL9P9QC9MSIKcNID/DKurTmuvq7IM8mXsAcy1+Y0yaYOAkzCR0YqmQ4myWfOnNaIrkAktu82O3OiWuOJWjKCRL2NKW6At7ti0c660l6pnLljSHS1YWijSCD8l62Mps4lkft1nybU0dEzYv9pQqSC7uP3nMa53tUNUkHX3vOmM8m5sLM+CV+pTs87p0m0ftIK8JUiNcwbRdzz/hSfhK7oJ/okpyvFVzT2dsTTn07d29Bq6dpOyvB60J5hb7XU62/nszvKLhfkb2cr7Z/+DT4bHVRL5XODxiQ2OnYlI6G9tcB65nvWP/z7klJbnLet2O44a/HZ5VxRq9/k75RJ/TwdnVeAuaf2VBzjnIvraDobrqPDs37wO4o7WQjjbXuGUywURZthUdr53epx520rZj1dIaH9/GkCguLexsfO7RXPJ8H5U8tqW31D9orUb8InQfV2H7IzejvHQk9oEoYFiOyMdrlSb11Kenteu6BoV9p8tPX8ZUTJg98syqKb6RTexnhIHAP/nPuc3l7j+mhLSgxDIsuT2gpYK4XVkrgD1am3pZ4VF9ZePQnt9Kw/6DNlqOOq9ay7//r97r/nHNcvstLdyHqrl+PtfBU0U3N2Z8kOz7vL35baOqqWGZ+kuy1XLdk6v0+TWOj4v1KR0/lPfkcx/bOZxGemPNpSVa2/9WAzicQ4EX9m0pWyuLcH7ZorZekPO8NOoG3t/GylbWl1RM9cjk9CK+itQtx2pFRp+1pd1/TmrEezpH+tx+XdvJ1VcR6XS/36TsqiaFf8wyc0iYSOh+J9v+c0iY4EXl9qbZ7jKl2tIyGpOD1LRmY44bjG2pYL36seu5jEqka8qsUaI8dMPb+bcParnUR0KEDb29tURYINNI1TV4AE15aY7avwr5Y30+ooPhXbnati141dWRJfFfR86Jj18K8wV1cgijaqNaorwGfoZd3YaULl5MC/Fq1u1rNkXf04v9tj8BlOVjf1etC/Vl+pbJas1IN950NRnySv7LIZMbd/rs0nkfwK29fIZkR/D0irvM268X2SPu3ir8AFvE/Sp10sZCunwPEV6KslK5X7E7XkbOXOx665sOSO0P6R0OaxuOFIGELqpz3xHbOr14rZhazUz5x1w9s7tbpRbvO00JV4e6dWN8ozxLRQ3y+MY23oGDtv39mPonhnSalfdIa9Y8x/t/zMvri29wB5zwwfP7kvOj553c8khEeSWVJCVsqIeuaMzJDxA8sNPF/s/T7pM2Vnvwhvd3kYiP6wsyl9jpwCzKKdi/e6K5Xz4p54m6HCJFOxTdHOjFtFOzdDPTfw+xHOEset1JL+CvRVPBLaXnxaviBFR4pZH21o1unY7qhuVludtzmyFJmF7Ma0Wz9rhk/ydsWVyiJ7tvmapOJKZZE9++V9l+ffJ/E5uuKTeG0+v+vswpmJc7THYN+z/uf6D1Eu5rI=')).decode())

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
