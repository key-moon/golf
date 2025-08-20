
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJylnF2OG0cMhK+TAHroYCDoMIbuf404zmqbrPqKPU5evNAKFqf5UywWW/vjjx8/Xo/XYz3+ejx//rvejx//vKqvV3n9bK9//ub98xe/fnP9euf6/vn5n9f7/ecDrHw+ZX1b1ff/+Q1Zub6trO+f68vK/l/byuuXlefXs7/Ks9f3V7GyfllZ5Qz/Wl3fZ1nl2eqzdyvrQR6sVqq17bltZX09e31Wj8u/Vl/FY0+LS7XWPdatvJrf+7P37PhY2c/++fQL4rLKs22Pre+c6nHbZ9e4+M+r5NjCT13hLPXsH49dEv3rK/qrxOXVcuol0X5Jjr3a2fUsKZO3Ffd7/9T19RT1bGzlMo/tTH1KbS/JOXr/E32PusZlW+k5plb2Wbj266d7JnMV7pzSuFVsSHE51Ytb2YjyLGdbzWMXxIURpqNhffbuUc8xzWTOsdlDrxgXRRiqzu4xz9SMli/J5I5fhJY5+ttDPdPr2U/RV4R5Wg6dqvRpVq4xLtXv3SOK9A/BimQlZ3JHw201dbGN/JdkMJ2lI4p6KCF/9Rj1e47Lkk9dD+0vHbN79DfSs5Vayx35n/LsK8Tlsqg7jiX+5YhDOVg9Rp1ZO3L1kFZpR/6ak3qWnGPM6hwdlUktQZhPXC60ov2j987sMUXL01k669v145+qPOBUlY4wGv1dH/1sjjCf6Dsb17g4h/E4KE9+St/v3eySHEsIcpo0liCMTxiX9Er30FPQ0znMKfqXRZ8QhXKsVq17TLuZ9n1FFGew5xyb0PL1YLTs/IzYBlcl1YtPSVwfikALz+L933NMuxYzpRqnimMTU0o8ueKY9s5XO8vGr6vkFkdfMXefRXkBzciOkolduEcSh8mzmFen9xfNKeL8y6x4f9k8+ZKzaLSVjVOvVM7v80tisCnHyIP32Th14IVxoo59qn3v+0+0onFznszKiDIl5ls1G1Ltz2e5Ht1jmmPKLXUm6PMLxyNPScxZvGq5XrQqCccmTUn7PmOyWlOEoSmoxoERSONCZ5mQX9mGIlBHy4T8C62sZsV1ypxjHYsTJifOQooJz2Kuv/AsxmybGW2a+HJceof1SVz7vlvxiSJXZWVCxM+4y/Uc87lfq9I7cuovCS27msCzGD27s2+2on2FMDnV9mn+Vzau7ILqpZ7lpPWxpsRn0rj0Gdk/Nc3I7ql8FuYoJ8R5j32fMrl7qMalW3HlqsflamdydjFxlppzypM5x2p/cV1SO7TiXI1jj/62ktUe7vvOnKbo+4TBHMbRkzvDNItRjqWJz7NB5xvO5Aus+LPz/mVb0fmFrJz3Ysr5PU4dYSjqFH3m/MxouwenHOvauCqGSS3V2k/bN679XZWkWieuOWtKvkty/Sv1+blX1ppPvdKnU69KzzntlbVnXm3iy5oS8TFHy1yVl52lPivNkbyPeY98zPcvtAnRWteznHKMNrycyRMfm9lF52OuWid1lBGGlN4TwnSP+NQ0Ta8+KyelVxntzlzPuY4wO4NXyQKOvn6qZkNGy0mHUZxKVaiYzbNYVUdT7fdPpQlv2ozQmWgv5s+qvVGrtlphDMhsXGevjNm9XibWN+VQVq03WvpO/AK01KpUXpxyzqsy7/hc6WX2zb2T0XKy0uNQ46QI5P2FduI9x7L62T2mcUlMaaoX18Zn9PSzTGqP9sY0JekOYz0cLXtV9v2L7yhSF+vsI3uMo5/nxo4wdxlsRkuuB0acVJVqxW+qUAcmpkRTEkWdpyRV4UhDUky+r/QSU1LVmmYCymTXx5LOr8rVnHPvwC48+sqDs4bkGP270U/6mOrJ1F/u3Ifh7YHmVM3BHv1856rnmKrUKfpnhcT7DN+7UCtLzsZ6st6CoimJ+rp6sCKQZjL3ygtYH/V1x2DuYvsM9ed6cBejaOsWaLWz/Q4m86SdM9mVqzMfU2T3aKcuxyoccUt9du3Ang06Jd1Ve0gN3dF35E8e6xPGHBft+95L3WMJYaZbalMnWDfiQjs+14sT6+sToVqZbqr4DKxnS/1l2VlyJtNZ0px5zuQ0Ja0H98rTNq5mcv90Uns0uh3ZHQumyWLZWaiL9SqknR5xy1of5201eYSqUucX8th5+zZr5TU7WOfnHHNkJ7WUOc1khbdvCcd8zjydhVQ49VjGZM2OpJDMqjWrCL5NOLPxjDBelat5TLVyx7GMyQkdCT399SeTuw5TWYbrY9RftP8QJt/b8kyzGE2ErCd7fK7oMfdQ5vzdY/P2zT9FlV22uucXPYvfIqCtDlmp7zPr632F0dInB+6d9Sly9PUsVNszb/bJQu+N015Mq7J/KilXPPERJnuOKf9y9FRGm+ZKnpGZjasVZePK+uiu4mn75jlFXY2jP2/eZ0TpVcmaUr6fPOdU7j+ayXOvdP1r0i3n6Ps3IXIXo5xTppR3SSn6nMlpMj+pcCkuGafyBDgpJN73VR3NqhvxAEXLfjudESZlMr+mudLVa85k31k4u0hVeUftSZpSissHLWkbus90Povilk9NauVOf3E0JE3WdxZ3FMXkd80x6jdcL2TFmdGkKHaMnq34tvo8vSp67uj3mp+3osrGqc8z67uvwmltk0Ky7PX9uCQtr3ex+n979PM3ufLER7x5QSZXj/kZ7n4bvf3fGDe14np/in7Sw3zX5FV5vmvNVZkzO+tj3pGdw/A2QT36X2s/T94UJ+rI1AHy9q33To2+I3/F4Kz1EXfUfuKZrJisOswJ+XuvTOopIYxqS0nnp/0L4Rxl8vydkZOVkwJ/tqK1n+rDe6dnMlWn45h23IkpdRzzb6Npf2G/086iIozrMI5nXJUrWCEOc6+/+F04RcfcKzvyX+CxXZ1pl8SaEsUp41hW4VgRcf3MVQXPMWd9uZ/4fM/sgicLvaN4Yn2a2cotc/RP9y4cUZQpnRRFUhUoDqSWkgJ/5smJW1araUrKqrV/W1A5/YmNK4ch7TVzGJpPfCe+zGMeF9L6PC6z7q9qj2sWdyZxxwJW4Sry3/mbKj2HeM50tPS4UK7dVxVIb55qf7Kymscct/b7Pr/0v0UwcUuKruLWzC62Fb+f/EKP+GTumX5S4H9PuUozMlvhTaJn6p3euaxetGey2kM45bj2eb2RXzdVVJV5Emd20efMub9c6DFldcrPfNL4eIzrpU/ikwqX5pvVEIbj4vsXQvrO8Snn1GMp+qoZaa9cctaX5didTFY9zLvahHO19u9seRyTk3aRMbnmFnN+V6m1XtK8z3cUkhXFZN4udKvvwpPVYyn6k4ZUZ+askPQzUSZTL1SWp0+RrOS7CktyqL9WHKsI47fSp8lC60E7wX2ePH1fjKxQ/agVmijOHIZVhLR/yTp/zzFS3KsHVen1HKOb9knr06r0mynTxMe8zM/CKnXXA/rZT9HXGZk68Goec87PW9GOZ2nLsx7UX3wGyH1/yjFiQnkGmDCZzjJzyYoF3rF79HUDv6Dv72dPU5P3n44wE46l2tacSpz/zmRB3FHVUWW49ya+FP0eF9X5nUfrXQWqm7QZqbXN88uJjc9noenVdRnlYymT04ysVcj8jDj/pxoz51cerIijOJeVqyWTn+eY4lbGgoTJ/DMxJY0+K/Adx05VmaqOtgudOU1MiTTYtG1z9q39p59lUhXydo31slfwGOtkfhPyzvySu1j9qcg/cXrlX47Zb2FKd7dvzpycBTKH4QnDb9ozBieM9nqZkZ9wyxGlV6Ujf0cWjn5Fdo2DMiXl/H6GM09WrSLzNd68d0abduKqlnbMdhwj3TLtkiinFNeUXaS/N84eO9V+mpI0k89sPHVkj/5/m5ISE2JdhhRFxmRFGM6hdYjTgkz2PcyswGtHVg/mjtxfp0ncVTlW6PMk7jvx1D90znQrK1hZYKX7mc6S+NrExuksrLPs6CvXdLTkeqm177ok65T/T7VOVroOo1YpLj5X+ndFHfl1M+IT4N3aX+XZeUpyxEn95T6HSRhNT+F9/3xXgbUK0mE0+n4Wv93hCJKq8l7fp1s3lEPcX3yeyTl2us+vVjNGEyafrFTk52mWtPL3g75j5VtRj4vXOvWXswJP2zevSveg19OcY6SO3tGPFQvqWdRjC86StAvnmu4xZ3vUKzVTWdnt2dCVK/7bHfP8kiZzV0tTJhPnJ4ShSSKx8RU9NrFxrkrK9N89i1Zd2pNR9B2/sgbLXYsm9axdeAdIs1ia+FztmSe+D8K8/waOFkJ0')).decode())

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
