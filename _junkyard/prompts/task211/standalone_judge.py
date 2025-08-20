
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJy9XVmu4zgMvM4M4A+/JW85S8P3v8bECy1SVSrS7mDQQMJnmlZEUdzl/vPPnz/z9LNMz895+/xZnl9/fqbn33Z92nHt2n3s8u/0HPF9u/Y+vW+f8zbiPD3/tuvTjmvX7mP3EW12j+fn4xzxMT2264/t1z3CL26QxxqFot1H/Jg+ntc+tntWeB3x+T3t1+cNOnCT3XsX6+f4OX1unzbH5992fdpxbI4eaxSKdh/x157y/PydfrcRn9/rv26c9VoPGbZRKNrIVePtPkfFLc1BRbuPaPw8Zn+MiHzTkOa5QbaOv24/9iN6vq3Qb4DYfYrWc3U+eRtl9WO7d8zVa1ib4+c5R5RVz6MV+gyQnw/KKtJGDZCNmEFqxLg7vrZr9vm1jfj8Xv9t967QnEKNQtF6WZ1PiV1H9FLWeMlk9Ro2cvWdyur7Br0PeHkVayN+n+v4fY74PX139N8b9B0gP06jGNPuI573HZ/riPzp+Ex2n6KNOueQs2Mdm/yjXmb6m++dnta46n2Asc7RVl5D0Qc47QEd0Ws0tB1a3yGtl9Vv43wnOd8b1EtJk4iGZavc00bJybiqpTGDvOSce2dhnpWH2JPYfWNapsl7ndOerjW5tplMk/8cUmj+6vZvv3JAXAbxPkVrI+6e6kjLmc/ZdJaHmkeKvwdpve2oSA6zHVXJ8bbDdO3IJ2czQ4j75P195nUcftey+x7L5nWsd1zz1hrFmDau48H5bUQWT+iZ+TUb0+4j/jhZxXX08rZCc4CqkmwU0Zcz3i5d3GH03C++hkWLrGQ1s8gKiha57f3NqhwjIt+yPa54bhCzHeYDmNav2g4NRZ3TxmJcvfpM/XvQQ0au1rUKchXvQ53D9GpV5+CvGOmcc++k+1HvuArWRqxGrBU9pnWgjx8torYRm+/Uou2VqodaBM78rp7W78dz/UUGSVnpLIOE+3Ee+nJKv1Q99riOZ6y3ZPGjjhArWGYfe1mtygbjwMg+tliVjahjV4/FEZGWxVao5a6tlF5l1HLMB9C6rekX5gP099mIx7wHXF2hrxTiXO3vQz9nPuc4T+jJ2LX7WIvmqjkrnetTkFH4HHKzIHGOVz1SPVu/jl/DObadwFZPe+c9rdc5ee6xlrOdJC3LIGEOeaXPc0T89/S0XgPkfk4t7uZ+Tq8BWmYe4w6vQ+3afSxWH9bPdcRWN6hWHzQUdU7LAOhIR0M60om7o/GT+znIo/tYz1W7G/djexLbcdew+4hv09vz2tuGWeF1xOf3tF+fN+jATXbvXSxaK4w7qpqzFhmglvs6ucrsvdZyOqfttVysBvayWq33aSjK6m/wkPu61WuhuI4jTd40J9PV17Doy2H1oerLaSj6ci0/pj0r7TvVsOhZoazWPauKdDM/xyRnvSN6MtrP0ZW7KDk+g6SznZVshs6ExEgnqyLVrLz2EPzuyPcjk//qfuy13KF/N4xp8vWOqJf9tbtYtFZoH+v2SEN+jiYDI/vI8jSV3A27L2bJ7HPpanO6tsHuG9NitpPN0SCdz9RQzHaeNZCFV1gava66VLC4H3GO1f2Y2Q6/H9/cHBVXm9fioRpXjQLzq6zGWs1nNoox7T7iw7zm7bP3ydvTH1unzyNAHmsUijbax7zCwjwZw2bxrLePPi+HtqP9ziwvV8FG+zjKPc5Tn2dk+Uhd8+09q1YrZ/XHa9VwXUk3z8rnAcyzWu+I3oT2trQnYhSMq2gfa1ytYb3tsBVWtQBtMSpYlkNWHQhKGjXEcsjWxWcaoO3x1uvHntn6/5h+6Gmj13Hov87r8DGgXbuPRZ2DXK3rHOTASOecv4eOyD0mNh8cEe9jmUDVg6Q0p55jHz8eGmkgq6zbkUFMrvr7WMSqajraB2Z6lUesb+cKclltq8KyGWq9kTZmV0aSg+PosRWt1wCVGBmfWY+RvQaI/irmHu3pWf3dKBQt8wHGmjzTq0qTR73qM4G4jvVcH/JcZwIrkQ7bcdewXq++D0esZlDZiD0txlboIVdjq6xv0c9xp809Kz5izbNiI5o/3Vvkep4cLfIoT95y8mwdr+beR79nh1BWmU9ek8YsA8S4alZy6aqBbByEap0XrJv0/zhR0joB9O7Q8l/DWvzYuMq8x8YZPDPipURFl0aBnSSqX053ktSw2IesYysdPVWwUVYt3llCfrXa96shtjvOszzdyaBqFJBBuDvOPdvtDr+zUf6vYjFG1v3kdu0+lmV0x/4qX8eavxq5+luWHJ1b0JLjffLIVfQBanzjcqW4Oh++0Li3U0O1XCizHeN6h4ZqO9jr1dNqw0k9FmPfxTLPCtexmrWuYGONNeuz4nWralSyU7DutXGXfnaiSnXpj3PIb+ccWZZY55ArWIzmFFc132rYaDtG3iOz6Hex0evIO0nUSdXMm8Xdcfoo4JPXZqGhnqvV7u6VamQBs3roToHdMqpfLuuWMQpF63dHXn9k8l+tP8bdEU8jjvs6XgHFimfW+cwk52p3K4vmxrvjFRDrXcGaTq135cpJ9tjXgT0P1R7dCjZWyrKoXMfdNWzMr458uWo+s1GMaWN+deQDqExrNaPb162afVS1OQ3VqiHoWWlrpX0nba2YZ5X3duIzr2JjN+nhfYksmYJqp3vZ6Sccsf1i9sxrWKwFqN2RQWp39LJqe5/rVbaf72JZZxdm5td7KxDLzPf3seqD6gjSkLLIffXBc3W8HzXf9H7sudrmiP2rV2ehOYC91ixirXZTs4hV91rn3WvIt3r3mtc53rNS/QC1nljdmRg95JHtaP7u+qQ+g1rLIY89ZH2u/O+huI5WMV9C/FitFHP/uadFi4w6h43DoFr9kOUBesmp5gFqWDxRwnZH7USJhlhv53x6dMs0ekeQgrjfxbkaT8302c76HBvFmDZ2BGV15FdArBYwPhuYnSpFTo9qAbGbFGs6tW5SrZFYN2l798LSnQtY6evdKbqzxWty28cYI7dxmCa/ho0Vlmw/vgLyZwONS6pLv3EQOZ116e8U0ZfL9Ko+9aj1an+ipPqeB1Wdr2Gx/qg6n6vvDVK0LDM/jjs0VHsng8VW7Y0E6h0Ir4Bit0zWScL8w2onSeyW8Z1dzFrVOrtqvVfeduQ6J/MrlM7pbUfTAKofINMAFWzcHfm7LFAar/Z+Y2ylstZZTKqhncLvx1b1iHPM+uOvYbHPCmOrap9Vtnd8n5XPkmFV96r8673DKp54aqam5WrnbHy2M68/ZhUNlUOL2c74FpTxSfZXQGiRWcTa9IZdu49lZ8qMq1ghz86wVLDor7K+x1dCrO8R+3Oq+1FBcT/Gt0uNO0lqtTBdRzPJqZ5E0FAlH8nOIo37kHWlOOsx95WyWA0c93ZmENNDPNfx4eaotZzWYxWsH7FyGvHvoWiRD50I561Ulfoq1nc+t89l4idnXwExn3ysVzVUe/sLeo9ak1eiJx15RT8nr1zjzOqVaz/H2fyCQ/Msw2ogjlivBvoRm0blehW1ZKZNx7SxVm4WZJn4O0m45NSy6HGO/t2k6j262fndCpadmsFesqp/iOs4iq38OjINUF3HChZ75pntqHX91bB4NhBHrJ+4ZHunp8Xzjyyfg/0E97Gxn3zUEVTbcbV8JDvfod6gpXNERqFoWUfQ+PST7gjSWpf3y41kleUu72JjfjV7E5quj7ERkZadtlBRAJtFNQrwc4xxhzrfofPkqjYXffLvkHvEdwTh27LuY9m5gD6aq5/9UVCftfY9D6jlrll57SGgRVaVay45tcp1lBzPVWU7Mq4q29FztbqO65Pyt78oWta/Oj5vVfufViZJ6zW53a2ynZWKhq6GRIts3s7SZcmY5DEJZV5QT4udlupkEOPb1VphPG0x8uWqs8DdirQxthrVymvWIXsTlJ9jPKfTy2o9f4K/B2mx75FlV1Qulft3Y9rodRz+BGRXWE5FdVQoWq/l8rfZ1DpwJkkbNUCeX1WV4gwandVVFpnr6ppF7mW1WkXSO0ZXkXYKVvFUXsdKNT5Tqb2OnQLPsKDkeIjZI3bfmJbJKnaS1GQ1g1BWm82Kc+QSquyWomXdayoK0BDjJe9e87ZD2cfsnRkVbOxgzySneq5F0WLEqjNIfw9FzyrfHehZ1XcHdndXOoLYk6odQXPQcn6O43d2ZStlFIoWvQ71hkk2ztV4No6YV3VxxKsdEegDsJN6r4RiRnekAdh+1vt+TIt1K3U6+BWQn2PlDcxsjrX8Ur+OvrsbO2ar78/RJ85iB7uvBvbrePVU9SRpfXbl1CGgc1C/8PfVMJ3T07J6h8rL4TpexbLq/FiTV6MfRRuzK9l+rK6eol3+Xf4DFGzrfw==')).decode())

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
