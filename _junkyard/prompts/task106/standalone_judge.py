
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJyVXFmu47gO3c5rQD+W5WktBe9/Gy8ReQbaKTQaF1WxLEp2JA6Hg/Lnf3/+nG2/25+9nffn49tq3+t5p7Evr9B7/9M+I492TEp8fqlilnnn8/f5RD9bkyr+Xq2/j4sn7u1q13yj0QY/v0+cPfPtdtyff9erdbG1v1pzfMyUT1w+Pcun5zN2PvFqy2eW7xNnz/eu+qMNKvZ9Kb+tZT5/zCvMF1fxlHji2dbP/bVtuR/r5++MO5+/tVyhFyNjRXuO1Br3z9/zKncrv2X/3Ovfd5jf7Eu1xJ3GvrxCL0Yu802u75vM3ovr8+mZ67Cgv33/X0DVMCZ6rqRckm6dqzXHz3m0PvscBT79Uu7k3dlK/v3y7ZocEffnndkKTl45U95JHscs4PP9sxvJHZMvt9yd2dO+/x/kns2pZus7dn7OP1BuTfN9xs82+PxKTj3mU2Jt8s7n73kVvTESuxsj+9zlHncopbhCb4wcKVPrZ3fH7B3JSSEf/bMm7J9tUsWdydto9dkC5TpbGDnyidv89lvuXq5QrtVu8hj3YiXxLcGLy+SZtYF3Z8/kF/a37lQPjl7y7UhHvg/qziceQZVPOcoTQlv56IMjl9y7hfy9UM5CKyyUiaWJGn9X6pOFlBcpOV9KD2Vy3j8ph7zz+XteLSZbKzVMyOk2P7+zzJ75j/1TSjZQNWgCXrMvaXNczkONvoMLxM2p0UMXb+oPDS+en3q6pe6HjFCDp8xutAvQH1vov9QZW7FE8c5unTbqgZHaY2Tvl5fXlJCvphmUgu+4QjX1CzTPGrQ5f1In5ZiUQ1w3eQsSdYQtTA78/vXk5a+UHZ//YTejL1qgjdaYPSPHcR7KZNzfUia/FFvcaezLK/S6zjpMZx24U3TWkVfSWTv15zHX6Jif4IFj6tcd/dEG1fyL75XXnClooUUwS7Wx58vGnrZP5w8b6zo7EAs4KfhVb5eoKVtAOcJTE9nQTp22Bkfh14PrHt9tM+vz3YEt9zl28muNoC+nteHYvDP7gu5Inuo5z0EtcGhNU2rX1AJY19XWPHZgLS31/aLEPq5CkkFF9Ghv8Lo6CiKU3jhSF+zcjyv+ob9ojNgt8OVOytAeB7VJzsH92FLmlvzcqM9THj7t7SZOciq2Oi3RxhYw1xxfJGudY7QH3fcl51vtXue6xn4PSvPWBu6QF+bdeTWCs1KaO9em5/r1lOzeKiLprVDNv+jL69nqc017RS2TkmggNfaSGn/juu6GpGb/XGVSxZ20EnNVSRl3YEEqitjnO+/5lE+LeqZiBOiQbvpjJIIC3oIfAn3e1U+sdKanIduS7RtY6Uz+mOPDNvBd4aEAWwGdzZ75j/1miUbuQfT1B1YLWny/nEd2kgjhnJ+b2czg3hP9xvVpPQ1nYKbg7DPRyAkJMJy90guERoE/GXbzMA0ALRS29TR0e4aNLZoG43IeStZaJGstkvX7SmgZuxicAjswch9PWvhOC99zPeSNnUTo5Jvkh5zDsIDZ+kmxp6bDrjoW2J1q8i70TrSB3feCBZJbKJHJJymFg9pjFB6C9himPVzvXFPvXH/RO9fUO5fQ8rx3OkKOO5+/q1xV1Lsl4rzyM9BpvHmgzkv9ZVe3x1ttZce39ES3hpH6lsL7WEHoyNT1qflgCxZQUdsvbMGbSGtA/Rk+APg1Yg3A5MtEoPMOMf73L/y0MRE5VgfoIfDBxAq5Okcih4oNIDHyWnltUuh4I+88fNjl5cNWr+btw8rPAZctyYP57cgTY35HRGCW1KeIuWRvthZGgDJqY37PZpGs9+qcrdz/sTohzb9XB6se82wPxNNfiKcbbu8/EM/Gu8KFQuuB9jf0t0LVNpvb0eG8yl3ecg7hD+7RSya1p7iqMnmZboFuGskPsEwXZcJjCsP0Gds37CTmA8IY5B3oiCMt1fdtzvt35AS9ivTBjx/8vDPSF3uw4D6l7CDXwbsKrjsolWgtOYcifT3ng0e3EJHjWQv5AhEHvGvELHq+30rp7xnPWE3DLOHFJ44I3YYolbyJvUEXAi1FjGo1vbjn3IhlbWztTf52aNedlnKT1bjDu97SUqYVMFtypo2ZVMSriU3pnw9gpxwHa+JWfc/di1he3kl9Gb76nm8vq95zH3tyYnBk7M6Ye9cftpJULx5QX3+MOwK7FV23JsXKiAuiKKv6IyYFqohY5a4vjLEsSYe4FmjFARnlpJfksX1F3ZADcE+0kz8DpZ7UX4F0pfuiRarWbQU6UU6fWrHbuDO1HnZypCQdadMOYrUx0Rzs35EySqq22n6sRItJRcoxewY54Eq8r8899d68U6zYHt4GqBidUgQKkbyglKbczaYDUy2UCVm9Jfkd2iZ4fVDXrUW7pueXEY3ggvN2xAHNEF4ixsJnBJdhvjPnUPSDyMpigoaUbsT7LNYn3jFdd5Q9V4zC+Uex8MRY3AWhKsc8sAe+slhJ7P2az0fOx/qDD0AVvPWjVSk1i/xC2Dn4hfCZxuR67IhrMPiM5kk0eJjSivILY3aszpp8FZ8zd5IrFXmUS/2WcUE+BjyZ2Zlb2ZjV+qIlHUnfcr4vkAHzAvJQGzAcYgbSitlOyqt1UjJv8Ihn76949pSrx5XrOvpg7pvfiPUqVit/XLFet83Thqe9f9vm0RIrPHZkZGas7og0yJhto2qr7ab2Z53rs7bhWMt25Cr47Bcqe19BnndFBu6W7ZDtyIrBcobn2Gkzd7Z2+pQrW90ocyY+8UoZZ7w413j2hKyhvxWq2cJYIWZF9hBbDMr1wQPjxQPVi/3FA7KMYQ2BXkfmDzH3vHKqhrE7ozyYKcbCx8csWJ30JHJFFIOuXobHqt2qb5Y7AY6rWRJgNFl1RrBeGUOtCq5qxnDudK4avisiEsEHp/pL9Dv5Z86YaMMrDYgOzpynl28J+5McSvsTM8D+JOdRRsILOFNGTspDrUSAjJyUEWUfLP7M7O83hozIPSwFshPxh8yFOPZJGXMo+0sr+PIN/34l3Vz9LUQk6DUVFAZ/q//sg7/17pNu3tK3kbesOKBHDRD/kwcs3xzxQEnXMqXE+sPjktQSD8H7QiRSkZAx45LDNDP8admPTt8r/Ktn1hhx/qnz6R0GPmHkh0+Mq0DJsFwpqWm5TqL5ynVA6qflcOFtyus8cha8A/ujbW8nXORv7pTs4RNhfTciJHAHInWDmb+00BwZfIzd22krVVcD72hMXh+F0xFXzojJjQxsvDWysoimYH0yUp9rAvsfsfu9XKFXkXS+Xb7RwUj6fE98n/TVSGUtttnCN9wbPMCdTwxJ7/yElQ0dBWvZYSsnP0Azuk8GrbmSMjIYYZ3lc0PP7FxXr1A5Uut49clh77rmXfj6etfAvhgFyy5EIOS/P/rWZjneEh+glLH2yGMZ0jrg6O6erGVEUZ8Dy3CYDcy8T1lJaSdfZdbpsOV5Y9DJkl6MnqBegf3F8m6MrCB2UqxyyTbWaoXQLECwCz2ImmOBd7CYr4bMqHEQsV14rCv6f/DZ9S99KzOjhrQyoo8cBjAptDat8LS/QOCBSYXHo60W7PLZLmp7avTgD8uDmJ36eeWZUayIZxcRyVIVEiqTiLYzlxG6TXmYfO821D/x3gWqH+uKDEhQojUKSh+UCFX8yFIq4q8KIlK1YbbAW07ps1AL3LJbO9HVr/qIvUgztQMR0vHQN66DjoJ6FF2CVCta0H9E1vvteQeLIaT89vaO1nt0qWc0A9yzNWTa5/NuVLisqZs3cs9K6d0lxfRi3BvaIWuU9WeUCBqDsm/61L0YeWrKO96q2G3wPhKjp7+RFZ9E14q9PSmByyVbG1d45KdWyquAEJ1FHggIUdWBJefH3dlyHvkT6f87Yr2ZD7iZs74ZgbVIGNftdk/kpKU8ua6qIIUn4trt5Ewn99FngUwGmoEcHuUNLQ58Ex888MdOOkSqd6APYqajCa2gF2gk9MtBTXM0ZfKBvCBZqK5WhgcVRJGdP2gLQ0pOUDVkxk62onoOlJKsQGy1YlYez24+02ZaIXVAqdNCRhG98KD2Iss5D1HERtQQ3CVEsbWKKqJNqrhzh8+i7Os2r7aKPCYlvuPgygBP4juOFnUIB/q5c4xT07POeLTtKnKRMcewzN9hunXjSsF79Cv00tqVyH1n1gfyqvxm5y73RCqyn5tJPfKLyhl2s5JCOwdxn9taWFl5xmjtxg/e2kip/JTbZdUZXRkLXhmXROwR8cr+iouqYukZ+8R83WKWFQkA78TnrRhcjTG08z+3NAtWNSoReq7kRc3am9dcQdtelm9OT4hSiKxk1X/wNYtk3fLwQ5ogLa7XISWSEMR3V3o0KyOh8Z6IWePvAlV7VLZl62ILZw5yVyzXGNw5+KlcozzZrSHG7NnFyufqC1rVzXXLwSAiiarXGXukZquxGvTWdV1e61rzPu91PcszVc//65no9ag2chIZPbkRBZc3AaslRCh/EDWcu/FSrQJN3/AWjkGl1lGw0drSG7xVISq+Y26T2fF6/sSv0OvY/jANp4oI51jaQkoJ5e5VPfCOpNfqgd18G0gyfNGMNibOc4/mSoxxpTW4EoFYnVO29vSRLrPqWX9Am6MYkKJjiv0Ms85eY6XY+a8aK/TqWzKec8O3xLdEnSziPfB9gIgVC3JPaCSyESbe7VsKST69WNS5dfXTo5KnWvvor1lfzCEsyVNiKSPwReXZuY8XvYovwvPr2SvP9Gq6j8wYqR76u+czZ2VL88xYUj9yGzgrptxGjdm9cxsdPgCj/qiG7U3ViYhL7Rb1R+wDFSQXfR9EMmCl3PeBJZNv7TIF3yfq8zZGRDwyKU0uXF2/pVck1njNbvlzYO3kSPVPfbdrjuaxSzyzUnIOixDlN6JUyL9z318yrTgYKqhUHecVV5fZglpD99JOrdTXlXGzlzxwmJ7s9KIPakddoZcVNukj6NyEamjPhnNEs7+pGjfPUpAfk/pWFS8qDLacZ31o5v2lmd/r+qzryp16RYofnt/9jBRDsyyUYd5pz1ORNbrEegyO9MiC6IGKPC51sJ+nd4j3UZeHkzuF6hUFKXWE+VyvEcReeiUizmX8rkSspzbwTY7X+tQ3ea+Pnw1CJaEQVGZ00T9byvQext2R6QXlxeyGz+KxHkUKt7IPwtBCgL1IdDeJllZ0zoP2LBZaNST8vNNaK1IQNSazYokt5RbiWn0rWz4LMzGMMY/Us8rKhMc80N8UH99/6DvV8+0TH8N2bmllWTU578PXnrrxZt1buUIvJDq93JRoVPAfj9wYUOzp53FvZYEDbeoEUs0CHwVTIqqsGlTFakexH7LyrEQL/mf1mU4Y+E5Blw2XEtYU1oqHnlIrrrtaiYK23xUPMe6ycZiFK6sqI+wAVzkrkdDfClXrtvadO4fqJVUhoW7GLbQwk07L13UFZpKFhmaUtpLWXJvbpD75vnNXU6ullgkde9yobzu46rE2q61ORLCwIjr/WTXB+/wnY1qpCbamk4glZnVH7GKjJmAtF6tH3pUnvlJnQTD6pYPEq0QwgYAltTjNE6h2txl3ImWdENK5plEQDLKmC/00nJBCJSP7GyqP97gy+VPrSalZsCMZR84d6YxAItrU6bmdU3PrFw96cuTCrNjCWZyb88QzK+zi1NKvFiirFAhNRBWCzlafuFM86DOvVIuGb68qNschqmIDDlleOOR62VlEWPzK7aw8y51o6aQdC++yRv9hz86HFj6LrVO24Xx4pYEvMzp0I1N6p3ewEJtG9Ai+QngOiiIhQxp9GedKpJBzWBxFlY/EubnG8x5rLoCHcd6/ImUh7Cdl/IqF19CHRKIKSVbXbfjazEOgHvDzZoP0v86boddjGh61LSeWfl55VmVQq8oLfVvoWneJE1Vbonn97kWcqDrsefpNEpyJUT2woi1rI+2N3J2fqGL261XfVbH6u75rL9Eir/14R4vQSwt0y7J3xhpXs+e4Qm+tYCqnjCyypuhazb3iXIiibDjDpCytReAsCqeKAuVV5HsrqoJT5EfzX0RQVF1ZyKshryIvdTfpUrQLHhiywvA1T/VPn41UTTV2V/p2iC2tzWPmzxi3WeG7ekC9cF1v0oXwgDT2MAyAP+c6nW9C/kU1V4jKIlujEzxRQYWTP4tF2Lw1SMnarRKBo25gPYbni6tPWutn99QNqsmxKgSrtwFmWI3PeyLzwbo6+afBeYhODbYi79XJn6ErUO/G+ju2loJD13JKemX8/0zv3k9J6wzC+iNKAO04TyPQ6vecRzUviHrrJPFpfu3R9JsO58STOndSK850lmWNUYxzHMUHxpohNqXq+IpdWDFvtb65R/Qo/JSS0CF4QB7FYTKnWuo787lXU+bxnLIOT+syzxoe8kXKqylPjHHym9L/dh/9Rrzp0Ow367E5MjI18O6Vd6va1c4ayPrcnutai9zrtIpZoEcdgceJFQcelJZfdQSBapBZEc5BjuWkrkSdckX4yKwI4Vcc9Ub4G/MaqiKFlcVp4A39rVA1jK2tSumz0Gfneuuc7Z3+O2KE2f/05QwxPX06/6WjqIRSrjw8X1QdXJSujQhQMcfwen1HFOHWar4r4tHr+aP6u1CK2dVzQ8j6QzITuaRkAtnE2aatXKEX3J4R7OR2x7COzYR5rwe+u174TvF2XTm+k+eiSgXVG2eFMr8j6geXh0eE1nKjjhDrlZXQTbXJkERV2gMX5vnRgmWBBFH3+MSFO1uOgffHuhpH3k/ck+fyyLH6lcD9FTf3X5DaybHeUvWkVxQtxARreq+rWdvFqdiKHnAb6fgd0ape3vny8s52vq7cy4NEHC8ZqVrrLSNnw0lo5gSZ+zwS3WH8RZvomE05B+QLaYNoV6LFSFHDmabQKqjSQNUjPKIx0YtRTY2C/BtsRWjTpL7Da7pKhAn5u8H3HcY7g7MOPKE8w8ba89E7SDmqRzp5YaUXCg6sXt77dPaR+L5UEVBn1vqnV60BfYN6Ooq0pNxNvzr21dmIm9gXiFbnBXQmY7FZxeej1fMJiZitiqlnftD8e+L7jARI3zVU82w/eG5rqPip2nFGQx5eJc5PeAQLtnzn+0KWMTJ1ZY4822JyjsiS4lqnjbRfFM1PVfm9cH5T3npYPMFbylv7uPp7PfnLdhlPk9UMTeuRXZyqwDl7+U1Bqd/B84hwzmOxSVSQ83c03XNvyn1WD/4V76jefVN+tHr5J7JQ1FHA5bXyBRj/ME3nNUh5kpa+SPgU500P36naae96kpJ09EXqL8VBI8l3UNwHvwg40P+MBLX6a4EeEcJ8A6Oo6RB/RGQbPPorBoJeIULXkYORDKA8/crtRUSI2IV0pMc1XEf6LDUrcjHuf1h8M3QWTnQrR5L5vqIF0VIeBDqhZkUYC2C22zOAynMqp6JspWFUaq6bCK+ivKq/fOz10FEPJJho8P4/EW9Hlw==')).decode())

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
