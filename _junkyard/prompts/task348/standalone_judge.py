
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzdXVmSHCkMvc44oj7467lLB/e/ht2uJUF6YpWE0tExE4lMgRBanoAkv//7/k6Pn7+vv/9P+bFYfv3lP4Tv///86+e/vzWu8vsXz/JQi78eLy6/CupDlZKalJ8xFSN6jaKkJEK5Wvr8+07/HwnIkjpFE7lGuvDSB0RLkJYgDenTVXeba0Vp96TjOZqvos7IM2uzeq5sotT9UuvnW53itt3WKOfr3PZHgdrrleFcQj+bSt351KhHs9EDtgOsjxtUkYMF6lsqtYcpY0zhoZGt+XNcSHk3BmvG7NmyVoyvpM61eIs6MBt/9YdoT+EZeHyvxqnFhYMX9PWIDR9f1fBAb89a9lhNd+5s5gjMBR23UBZlAL0L97vc4270sDwKvVG2R00w0mvebKXSi+eSN45AFcbQpDKJF7EJU6WcQ8o6JKQuYXXV0aEIyWONC0XkFM0B0XuJgmWO5I1kPcWjUUbU8taRPLedT+z5vF5Z3ycCdF3UOkup5UY8VGarJEuUZ28o60EZT5NHZ0xqj32WrKzWQNUSHC31lsMlYjvtHnH2xf2rKQ3OgCQV7E+IfnwxPeF2IOX+Cxyqr5c0+2vioHeraLw+qx17a2A6a2Yj8SixsuaaGsx1eRwzpHUkwqLupS1VHUYreynqzHGDojOKR4Y0Kh2UKVBa4nEWRVoUa2e4odKpf7lQAn2B2CPiiXqE9djWewyZlZbyiJo97qwcw7lQKD/lxcfJR+jGkTKCg/10bUofs61YWETUuo5TP/WQ1SjSACcKtEz37wDeqGkIl1x1D47EZe9mn0qlzzIHtDIlUku9pShAwgE7O0X7ViyMXc0aucatUS4uL4nVWo/sAFmB2LZ7vtuc3W0/wrQT6SbSTKSX50biuBMu8DGEb5rZASj74qEI5wk0pGYrxbXcCrQFfKtHjiT5thkqlMwCNT/qKIAwioRSzHlTxia63K1IWR9ZOI/DfUa8Jbe+vzjyzHpu7jWOPM/tpggrmhQr3obKZk8lM6DUBKgJUBOg1hxX9eZHFxAdxEcLMnrgPmKE0pwnfl4Kzfxq24q7uNTvaJz6ttO6Ea3a05qVDB3O1HKJaE6tNR794/0cLrsNalqmMg0oajNvS2ffmrcgb/jIsuIWctGs39I5cQqjZVkeZzIky6Ia2isLLQ7G4couaBTS71HxZB6NThqIF411hCKOWIz/eJ2Oy16hN4dspTUXOhmKfVaCZukUckc+Q4vS0BR4tvcO53bXNXJG88hc8lEepTZl26CCWedRrklNXEuqueGZTqUttqMzOh0wjhdmMEG081IzyBFpBdYJrBFYH5Y4NI3nltFb/0QY82edEpndTM+H1aVESpo7IbM42AoXx3iTC0rSnQq5XaBm+BY32P+vqNKpGa6FdX330SkgObEHNUrmuyY8Np/mUT13ucZumaPIEtNYu5mJ1Nds1vhdb+1mPirrz9lC/lj7bFiCo1Eq5cMruQO4s4FhtCgCP8OUzLFo9nxnTsWr8RlXK4tcTL/JqY+B7pJXr+ajTMIoU1yglpI/l2173IC0W2YIh0rjPIcuJ/fH45DHTkcn8tR+17R0SWA849XPhn1ir6iDprH3dKTtxt5Sbw2fL4nNZh36mQm10V5ZkKXgbXlWwTOK5R6M3kcQVgM27AKvYHAKXrng0UmdxwAn8Zn/oN4DlHX1S3O/SXoetfmYZ6t2fMHZuW35DoR5d2iNfrE0PjUxWsdYfalnBXQFWm+WMsNTa7hookfn8xsrUSCh2fXlSMkCmr1s0oDUDKxii0M1i9KyE69bfH2popzEXGOFmgSq3/3CEddRcrh1E48b/UZRm+1t4ndY9dDxU6L2mFGZ5LvUtyXgfO4aOaXivA5JSp1jg9WkWh7IM2rgnPPZPUUfMBrwSMCjwGr/TgjNB2XpvYFN+J3wOS0PhHRRm9afB4w/MPrA2AMjjwVugknnnlJck3bR27EIV8nmYNTy0T0dvZV0b4dmr7f3OO3BsUa8sx2emFacT3U/EA3TrnmSL1Bbm8ZlWFv0s2aln4xWtlihr5mej1v0aWv1+IZgEwVveDkSBVhcADrENYjrjyXXLjfX5s4ahW5O4Kk3+3MyojfxNEkP5zV6KaLZgYyJt7hN2ZT54bc6V3AUan+U1pqxWf3BErE8JW+lZ7LsscZIY9fXht0ba/Jj55YajxtNZqgdaX1GTJDVa7yUmgD1ahljUIs7Uc7uUY7IMzF5eu8Ejkgu5qociDDBVuAifkuLlpkUKXrrlBmSozhun8Pb3gxI/qbezaCYGeHmEjszX8tnpuCN+NrZcQS7VWrGYyDpMy+MfDDywC7YzPeLR7PlS7I7XsT+C0p++7wjFGG2h9ezEqD47xePIOdxRD2KtKVnnRMyutYGZbgUo22/J6YSk3kMUaZQmfTiKIiLPCbyeDjW/4HTU3Upd9YpWyWuO1RzBvp3WlWTIvmztXOYvtWqfU6ZQ2SPp7D5wEypULmXedf2xNtmo3PS5VqeP0/++vmpvRHN12Ip06FCI3yiuec9t62SIJHamlRKxOra3ATQkXg6M4T4sB+bpDX7naJRqb1rMq+MfLIPh8dWBHtlWYoauTz19tzPcw/f4ND5vYzyOTeyUf13NKqeg1lgLGs78c4pj2r6WdZE/w53WLI537Zl2bYLCZF6O7RyJNeMXBji/csaSTz/KJ4Y6MX5rAbz3aanLvxvR8dU6ImwL8LeSIcLtztewKizvC468ux7E/7KrLrPn8MIrajekjMbh+IdI6VsuDfkvpB7QrFFtS8oz2ENjdx3BV28/1BeuUO7RvZ85tnu85ecJr0L0Ogl1G7gCOWSTqW9Q+fdT+8h+ty5mRapme6uEbup/ChHSra8Gd1EPfK8gi/M9mC3NKM/J946YBHZdsv6kXGbo4NfFd3BE9rl0/jED7t43P0q4RpLCbTGrDUuq3M5o3Hg5An4NEDN6P4Jbk96/QX4qlInEg1/Vencl5bufs9YR9b/xt1hrL4HbreiZnS2SAX1RaD6+90Ts+fn5U/NniV6G0do69jl5Hc4BuQM39QoR+uRJQ5bMNVjsSy03C0zq6L2pN9jwNt1OQV4G+5pTvOocm6g04sTLaOdjdoH3WUkB94zyO7vEejuGkxK+FHKl44Qj1Kp5yCnonkUe9cmEYxR65aJbc1ysXwuRWyZ+wHK53yLB06Bsvmh+ELdPu138fbtG2IvgLyYdICEqM3r+IEY9waKszwt2RFpQ5RL9dGGa6dvaGSX72Wc+CIo8Za1r7Tp8Z95Z380soJMuZA3pSZATYCaALXmbS82a0dsOd5SibExTUfwiG/qnkfcuwid96pFgf1DSg73LbNY54UuKfG4jSK5lySjnAfepzJv9ant6YcVxuF8V0P5nE32jYd6Nsg4LSKDbgZrGRnqObEvAY6OfzFXQrjvP78MeYeW2e6mV9a8xXXAd3TbFg2y6I9Fn8J+3jd6SsiuyqipFGz7d//+RX7UuBFZkuZd9oJfwnZ6mNqXHM6x2UogeKetpEpv+WE9LOZDZxym38bCNkZWG+qYV/yO443p3tTWs7LSKlWsXG03ewuWz9XzsFyWZp1kB49460Q22KInBfv7EWewA7VC7XIpFeq5e2Xk07k3F3sMsnM7GhHftSuLAdS65aqeFm8mb7qLfaI3dhgG0MOW/84Xl/ooFeeAHtjVbHQHbyrcoWWeLSGdjsa1+61y1laB0HQS50X7Ln5t/S94MfBetl6RIYLCI2GqdGpEWgHz8X8RMWk8DBrlnvlG1i/6baalFKsCvFqiGEST1isQulngWv1O52aPixSqpQkh3UIzj/B4i7PrEqZGUQ1FtDBc3/Q0nuQ5UBzDsQ3jkhhoMeJX6oB0uRy5FLkM9Tgy3mMF/U7uo/J4zlFwt0fTyGIZESLdQCHMX6gbJmSJWlGTKhX630p7vphckKZV8jsxDvUc3J7n2Xl6c4uiXbwcfG32tPzlPlrHsZPbiR82j/0mew78Hvodzwhgzxz5NIAXAp5BoCNW7IuJ/W7Eb0iByoD6MerFqA/r93jDu2VrKdW1if+KwvEN9nly+D0drxvYNaSIPTn249iLm3F4i1NIOEKQeJqjnUsawII1oloogZ6apdxZVdFYR2n2r2i1opw71uhveXv7aLDd6TLz6NSb23Ng9mWYbj4i6gPJDAmG8vxaTJw7Dy7pRL3LoJAyamGLWo+fjMslD6vrtUppulTrPNFirT5C7HS10Si3fZBfNWj2u1pedxLlRzlXGrY6GAGRLCYpYo8Ie7mexGxjv6I1jDaOUhuj+EiSWARG2xhxY9RNMCayIu3V8vM6eQe9ndVtu9ylF9esc5exmDcevXfjbCuye9xJ34r6YvuKCG3WZz2ffdDcuh/6tL0Y6efi8g4NyhRJVB1NbHGtsuIltC/6b0kee+tJPZShFdPs414Ot+OzFPdorGmUhVYN7jC2WuNVliVfKy9Gam85c/NNEedsWexlu0wtKeXdXUF1Dp1ues5oZ5COfr8XZ+vytRPvr8PQkdKM8qcmyRpfvyYzTb3mXM+3yAwl3YgUIa2j6E6UpXLicrOJwlz7RijTUuXej/s+vd5c93asYsTlPSktMVpitMRoZc/xYo44l4YZy4lzVLOIyf6c1bivqCTMakZaYZmhZroXTVZj4q3RTI3O6JRHNjm7cW7FYAYzAT/NvfQgxQoh3eE28QG5viTAIiCOgTgK4jiII+Esx6a7y83ep1DFXd57XEOj2vjU/w3p86ti+fCK173u2xBGUUgS4XgiXyxjKGdKxXMizcviOFTuwZaeWc/Vc2WPpSUOPq/fj+315ZQZ741in+4a07ynLlpVxVX2eEiTc/sVKoCJCv3WlpIa17/ybzQM9Ss=')).decode())

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
