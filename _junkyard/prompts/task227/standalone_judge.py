
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJydnVmS5EYMQ69jR9RHSjpOh+5/DfemSgJ4TKkd82FF9UxR3EAQKbU//vn4GK/vP+fr8+r4/PNzdX12fF8d78+2z6vt67+/V9vv1dcnXz/9vPzYX19/9Hv06uun57+vT+vHt80jrP98dti/3+xq+/3p9vvZl/VpaYer8XtvP9arzaP4efz6ft3b9HMrNrf3d35fm/XLz+uO9xIF9336eRTfrzvafr//sqQ5uD5L69Nj/Wz6Pt6Wat7zs+0d+S0i/3P1k/e0vkcULuua4+nxMOvT9/G2OYr1DazX+ttL5Pd35EexRBV6vC1tEAXK+245fv32wf6uvx3zPqt/QB9ojq941xz0eb8i31nXSh9WAdN3r/mt/JSs72L9qr9adYQxE4EO8T37bP40q06zPTt/+k61NiIH1fdqs2LRynetfvedulzz4kibfXD5rlEmzJ0dV607ulffuc/qfZxvnN/f1tP3GnlFVcXcQyyNqHmvxFXNay1Q3jPyjieJ+NtD6ztYnz1FV7MWtNJnDhR3Luuzt7MCuONmDrTzj3e/D5hxW7mjzax7zdOMqxWWee+wTmf+Jr5ffu5vm92U0Vo7ogLGK9GmZlOn7rOqo47zvPtninAeBZ2wu+AaRSEjP2ut1oLj/JDqH2HdI5+Y69YVX73zndFsEpk1t3F+qWgzXkNynLPF53vNuyOQ+j6xLvml+15zTGjDVUfzvVrPzne0meher6bvx5mR77kN8bqshUSbZHOHfH/1U61fkTltxhHuKNblXNXIO9pseLUV6/1czX5nZpUcq04U6r0u8oS0yWm1ArzqMscdsxrBX6kCcpuotebYr4y6ovuKVWb1q+8DfPcsJdaNuCPvd/fdO79ym1lrXumzqrnjKuausK5yLNpha81rPKbvzip96qb1q8u53z3bE2kV5727dMro/q4dlzWv6kHFGJ1xaj0ZdccqWbuY1nfMe79TbVBruVl2kU9u3fN511B4niXiE9J2FdDvccPi4bjGs1b3ON8mVlXnea/Yn9aZ2WvkHeH8ivd3rbWq25BmcFVi13EVY3awPsTPFdpkvH27SnbhbO65euDsQrmNKnfK59V3Qr27ms/PlEcro65I22lW3HHsp3Ms31fT+qrfe+uJtMRunckq/o3XgLzPvWLF62hryp1e6y953ZV31esqxiS3UeuUA+84VSzuNavqsVedThTm1j7jasdtt9aJWaV6QGxOVeL5nayc5P6eW83109zjqnXG+SeMmvudNWraW2jS12ynaqk1P7PdMXua7/VvpHamMy6rboV13dmE7+/a5RVzVS/pJ6z6vjfTLpG2m7CuXdRvUo5/vj4EY6gCHG28y51lz5r3jhtNv3c6GVl3PsXsgmac445jXX+VaFN7z++Ip4x3/hnchvXiHaqOdcPkNoqvd1OGEJ8in/VXI+a6JPHcU1glsdv7XYZUtBpl55IrZuVX/dkE+z5V4uTRfd4nsqz2d5rqjjbKX3mPq1Om2+Mqw+Nz2Hnl2kVVTvyzdx81p0Jaf6zPp1I1K4CnzEDfNcf76TnYLfLOonSPS+vJqO/29w5tLu8OiwKdDNNsqRVw5b1GmaynVqn9Pl5af1UnIx2BsM7ne3f+rja7Xab2mbMLVQ86xYI0avZYOz9nuffBJpHnU7h+xjHHmjWfvZc7Pfme3IbQxiuMcJ52iBWr1I7jCZsbNG0YpJfQlFHrnYZCp4GrLVLRxk/mhlUdcdpUyDXyxOcdOXx/H2dWXfresQvus1F8X7EkrrpULFQ/2oNV1oky72MyK55s223e1yfgqUsOiwLx+TuFPLkNKSfUcYf5fpjNLaxflZh59wqgE7HV6ev0PT12DDiNz2etXE+grU+FUikdluO8mk8+pE29Su2CGPUBviujSd/VEm017rsyGuo4jbd3fs/r9hukHRLlTj2o893VmlXNj/BdI8++k2bl7MJroebddbI7rJv1XXvv+qz2WeUUm+Qga17PwTzvyl/dpionPNnW1rvOJ+2CZ8vcpBRfXbl7uklpzXu262cV61w5GVL9c4ucqrzq82udVvl8nr8Twj1TDxxtOq0ymX1qVsQqK87PCvNsE7OqnCL7zP1wfllZn1eda8Pke29TmdW8D9+p7nyvTzezSuwzzmc+KWZeAWdwm64CVupBzfsRaDPi6p3NiHy30dEZtG8wzvVYqVKc/6tiVqOcLMd9r8ze7+iE/X1lfXa0sgvvQo98ok2qBzMHHdoc4jGpGHW+O6tU3YaYVU6ZnyueMr7RKascEQVF37PZYVf9Pv+Ge+zd5bjj6Hsau1C06fKuPNorPfk8X+UJOPV7p5SqdWVbqVMQ43DfuwrIqqt+5lZDUz37IGveq/+6Wp3DdnyePfb53nX5aoPWCkiWoxO2dvnfTgOz4+hMKq2PV62wjEc+S8ycdm+s84TVeUa4k4qZznd/f2jHbWKUyM9pR6jKV6fNd8Wd+hm/rdOfExCzUt9Xp/871ryrB8rmlM+7VjTEd666OmUo8orkyW49x6Sh3PmeCEQTNmdLcr2c6lrz6/09fafI11pI/ur3kZtUdyble1zVDJLhdUj7rOPcZlZdhzbaezXyFetyxrlSwG+P0OkAzdp+0m92R7nHjWKzV4kVX0kx83gnyxkNu1hN2Oo78bpZ/cpjsv5WjDoZR89tZhTcT++4NbtQtKlRoCdecqea98EaodcfVV1Wf/U9PXb86zGmfntFWp+wNQeqUVPk9Y4SbdK6qwfd/t6dSdXZUrOR8935lHdc2kwtJ58p1Q3ad+mMd+70Xc2v8u7zjLZqne9eC7XfHWPyCQzW6/g+SEMhxNea7zap64o16vstUnvvjtusT8R0V+89nhV2+Znqwd1bmfzOSG4w+u91k3LcqYh/PtqgO33ec3CI9US47YHvq5r3rT3Pxo5gF/qdvXKiNu/QpmJM/ntnkMo0td+JWZFe1zHI9Yz7e9XVc5kObWirGSXH9GSZ9FGjWalq5O+IebZnDgbmfYsc3O1xHbPijssNY0gUGHfOJausFUDPmHEUVjivvXe2E9bV6v6pjzrZkmcMi7zjvD/LuVLI67fSjHu2x9UNOnd1Rz16X4aUqpl3j3JO+jrjCG2sO8K6cizll7m3UB+49f50qt9luP6y47L+zlc+P3/3DHn6rhsGzVqtP7W+g/Wu5lM90HlzFD/zBHyFNrxBV+vMrLLjcmN0nqs77NPnrOrn/TarKsn2yr1ie5F6cFnval4xxncInTw0VyvmnsZtqALU98wxIX7ldbo3e9Vld71KPJLX9TqtKhs5YbUfvebvT4U43nw1LXn9edVV6/dnE+57vapaZa0w4peENon46jvrZN3+vkK9U+Z7fx+dWuj3UXfpUSxl1c09rkd3Zhe9SkyM2vUSn3FuSWs+q272mXIsV410tgyLPJ2A1xx01mmD8ZqnPqu1kFtkxXneJqi+6Y5ok0rU69Hmvuqoz3KDTp2s6/euAqr11CWHRcEnbK10QhtS6Z4wq+tvdKyydpfPfGZW3S7NvM7znqpRr5muIz9eVHXpp/PLOWWUWTHauM1kVjtEXuPt005rnib9+AOzerrDzntLbsN73EQWrbp7fX7YfcyfancNq4VEWtXrulOh6qdOlNQqUyV2JemETcpr3nUbn6Za6UepOtUMlNlnzdNesYf1w6yzUjrrW7EuI3+PdbnL1Cu2nvHWyfNsvrtOSxM22YVbqhjwruSm41I1Z4VcGXVVC4dYp95j1Yh7L0+Ba817/WmUfYe97oOsr5B2gHWftcSeefIQ0mrNq+8+z4jhUd6nx/XqfHUnI+y7R77Pe26uXnV3vyWVfc9+HyUek9fV3tPPFOumTVfpCOd7JjHMd/rp3dmEPnNydWHy+exyn++0RXrHdbujspzVc5XXv6rxoGzfV12ejPxc0Tmsc4rZ78opcp9U3ztO4SehirRe/Vp1PuNSR1jVPE8Z8lh3qu48WPfJtUrcK+S0tddtdmLdkHgrn1ff+URilXetNUd8xXTt/LpNZJRXrLLadEZzt79zzfe/7SCtHxHlWunZcbS/V7TptSJ+0mmYTcKdlWKRE7YyyOeRv65ywlIUfY/bIPLr3zjhu4xyLOU21OWZd+W0611Go0x5d0atNonTcrbvqu7yU5WkfpdxvvN/30hVjOk36PHAd3pPKuPBviujYaRljjWWE5bnO/F5ne+p11H1j7f1LvKs2wyx6VO9flNa953+jF2GTinUd4+3Rp7yXnEnmZWzZ4881TzpZLzHTeuMNpntZ/0+0SYRqMOYnl10/e7PUXfZrv2erDIr4Gw3aJ97/Rtq3gcjLA24j7R+fzIyoNKJ24yosPpZzy7ydKq3npjLGMNbZK8S71b9+fuoeYucaJN9xqzyb2iTO8SshRoP12QT55nbrGdcVxndaUnlNr1ixr9bZWLAar6njpDIQjO/z3vtPdaoWT1YW9da6Kwr5nreO3Yxo6BoQ73Huo1rVp1CXnFHs63KSZ0tWgv9b5DzjqNNinBHt0hHd5qws9L7il49ve97Radd+DbBb6xw7/XP0zqjpvneYx3tsBV9K9Z1Vec1X+u7q4D1JrW/K4BqvsP5yuep9ySbD97CVuvq3RCPdeZT5GmDVmbF7yj66UDtvdXe7FGgquvPJn4qIJUT36XpPohR+2ngXeS941gnS5x35WSFdfxEISOt9vaQbHtvT1bpO/1T67zLTN9HRD5z7JWYvl85XjMr3x31jo4FzhOj9mma0047zj3WHVbRjDQDV8z21uMrB6v/m9VEG0cgt+59cL7y+TqfcVnzHnnaInnGzZpk9UA9przXv9vNd+I2zuscbfiMJN+PS48ddxTraN5sYb1DPfe9U2toi3RWWXvvlF0muST9ZqHxtpTTTq0P89j1y2l9xW1cPcgNhrJBm6v+9LQd1tUamnG+uXaTPlm8K7Zp/c733CKpEju9JPO+qrXJ8OiNVPe4op7vbDpvqOOqTY8Hd5yrV7P6PceUg6e+r54t1CjMDdrRPXcqzXtyitWTD8xk3ffKM+o2cYe0eh+k28wKGGZd53vtd+e0aWnWWr6ZSL2t/NL5VHa+dlyPMT5h67bS7RUe+dlxzrFm1eXv9uF+Jx6T3Hpraq1TD/wp7q7ms+N88mTeXbXsO+5OKb0+V2Y1Ih4z3swqa8cx2nS/bWOcPmVyw/Ao58x/gvOkUXufVQ2vsgvv977mu7d1Mu+kWTnadDpZx+dHa50ZtXa+Z4N8n3nPLXL1RipNWO/3K/K1wvzce1gX9mjDG7R2ucfb806ngU8in2rKE5yvLCd5tCt3/KzR+u28RJZesyK1sNbC2UyZte9us3Jr53XUcaoeaJffnUFfUc6NTnndFvG+8C9ZZb6b1c24ijZ0QkOcdoj16+q85TYrXueoNz9zpWqtnDjOd1U3SmaT19U7ckyneJzNJpUsh/U62ujWOm2vGvFzvawW8taeqo5iHfX7qup0i6z9Pit99oGyC+dTNQq5y6iKoW+prp76qF3uWKfsIn33Wsun+7TmPfJ0xfN9Mww4H813PpvICnCtcnUWSVNmF5s032e/K8fSzl9j3buLb8+kVCXmrf2ILuz3p/oZRX41ZXqEI5U4bY4Sj/45ao9H9/8Vyur3CVt3Kmd4lHet/sR53mX8s3r3pFXSLqPWCesSbSgHrpeQctK/qbTKe06ZIXk/IMrMM85mxmU2zn/P/wAqmPzR')).decode())

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
