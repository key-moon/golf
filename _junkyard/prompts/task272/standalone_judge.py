
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJydXF2S7KwO2879qvKA2c6p7H8b9/w0WJJlkp6ah+4JFgFjyzYw8+t/v36Na17zvvbnvMY17t9fSkv8a/nv+o2af579/u1f6/h8+/Mz4dmfXnrJ+PtNex0i++/Z3KjV+mdMq3+PCY/JN31mu0ec/X1a9ghpfLPMJRH4DMcXBRN/v0XFfN4ETz8zmvv3P/3GWeJvL2vOF2kp++jbA8fBM8XR5hv3fOM7xB7nkHFM0OHYOjTtnx5wHS/6PbXzry9c11ZS9MdjV3vzOvWYuFo902riqNx6B0vsXvLd0A4aG9C6+u0xAZiA8Y7SF89ySE9b89RXxQRi0ALBQ7B/tIdig+8xtAaVG2C9Pz5dJYMkkzPUXqYZVeoHraSRxF6Rd0CLYEPaO7IOIeLznPkY9CQcs99cNOIkg8buIs7S920iD0qIBRKfKOdMkPmsNWgDV+2EDkajp4GeYd7kD2gz7xAcb9A3c7UnxFZuD+KVz3tAS7zqqqU1ZuKyI3rZjKBtlgBWSSyj8Rwxyy5bTGEJWb/t8cgCyhIBmOgwoNFB1sIxDT0ytXhGpEfSysNIkE8nrQLwLOVcjI4GHYwubx/w9nmh/jqpuFhjmJ9hjK65VzSSGS2YV2kmEgOWJ9l2yhkqm4OXUs7wIAmWSBEX/ZZ8aSZ3bqtjW0REWJ2C1ZcR3pI3ZGwqkqJTtji0XdXu4hvNbaZ6DHhSZs3gH8l/OV9kWxhzxgVk1+glsLoQbk4Pgfz/wuwkVKpYT77popVJXT1JxjETplkdc+Ii2Vh6b9kcYSV7Ig5yTPeMqEyH+krtEOMXS45eEvSIrIUeyZEXmGHPI636S7SNRpp/ouWRn5rsr8W0OStb30kiJJsBH6X5wnu5aniFIHsCP2A2WVyiNY1GVc0hmNuRUSrGxwPO6QbK2Pxo9T22/NJIGHQ8o9FiwXe5dlNeSA44Y5AhfOzgKIa2o7GjkWxXl5mYWOLGqM6SXCtQK8QmyKbAzzbfCoYrQq5CPQ+hB3OsUR5qJEsGTAx3jZLtEq8ZLpmX2E7hBc4o3mKC4qPfLao5usYeI9nG7vy8m9gNEtILzGF/ci9WIn0M1tjFw6C1dXHRs+I5p3Cs+Jxf1LGi/6wxltoa8jYXRdw+lUquXaHKjJ/5lhkvPuP6dq/MF+hIdGHGwf2I3aXGCxc/YYp9KHclJ6idKHeBZKl/fPzLsWZO3cRBymhQ1xh3avX+hFAWpNXeVnhfZwm3O4gachGsRuXRxK2xPcTlGZNX/iSFmTbWOJLRpk/Wmu0naKzfxrZxzgpyne6rl4qUkqrBZwzsZVo/+IyhYMquG9sU6gCj2pT5xM/QdBqB+XfiMZ70UlxV4tqy/tCT4oWkVE1gvZyFKpdtRjfnGz7GUj1LHgg2JGdZLFH2eMsokasG+M8o+UWOknYWGCOnEymB3M4zp8j5iAnSzGI1yIyJ7QBLK/CE4Ld0q4pxz62geBNEBh6PnlIpc0F/aLESW5MTXyNIh1Mwy6MYjzrUPfUGUTwaR6M8mn2tftMvf4TG7ByzoKKjxU2D+l3ehRz6BfrFnjXHBMoU0Brvujvu8zfNiWsMvyW6a/4LkpQtpQYxa8GcoeY1VrLsgPG8agRbFaQ/H1BP49qi/j4lu9YMDysDzRdRE/dVW7jSRJsjnjE3BqS9aB75fZpxuN1eltSzosoMi+nu6yS1omSNg9LT9gXkDbRatW6pvWD8aoM587Tgo2ST1SBbKwfekMns+ksQzIEcr5EPJsXpAXN21sJ8POjbkksLeovRux6YnWGk5Nrhhkwr90lxZwV9U7RQctUBfVbrX/7tx4m2PcGLeGxGqrGoUT47i6qSQZEls1uNhXyC1knFIU5h3luruhVb7usnaM2mRHfFf7t25clZNEZcvnypSsgOY8fZ2KKnGGBnFKXRiryfU/QyaLfDW0+J3JjVmsJklhSpSragvhjvMfaMh+0E1mJbkyIypodDlNt2ycXIfNmitx+Yj9jn1bpVSneSkfcUU9cb87tkt273gLh199ZLaQ2G+FrJ4wrhCcwXGNmPxiiO60I6lj3qM4ZZmqNGzRlqPr0QcUDYexLFvzijrRLpdz2zPDOMywbRqpgTcJarpTIH24TzTGZqtN1oEP6sjqIxeS2umFru3Kt6Z6z+Gu3ims5LmYj7Rc+P79G0q635zgRMrtbi2LhqvtMgim/LCOGbevRB0lRJ9RuyfVpefIcpt/Uwf04mUgm/e40exRUKt+guKfI56kd8EzgopbR2SKtcKwa5TONp4/K52hM6fZuz1sqBq6/0YZQ63D4hpuZ6mbXzJKl3KpGb03OwxzhL2XMbjFBpjzgKaJdZokcgY6Ztd5J4y/hNJqDzuh+zAkaIte0RYTYH9kTtbn9xkMXXsbHFZA4WZTxo2ZO0OOktrBnch32DDkWXbOAzXxNPlpTeVdS4UTwuI0CxBmIlsc2OC3NFBujgzJ8GY28/Zn9627FkhGvmS5+bJXcs6iVa7vZ5+LOk3Mbb7fPCmSlDYp05KIZ+h+bMe9LIVL8al3xNuSXL/iCvkrboaXuNahort+2AJFVNN+/4aK/DrBbfUhhmlTSOIWN2mX5aeBwxLtNXb0QLmYTPN+FNzwdM4TBlcR4v2xTf0IqX6Lpz5WwEfdJ7NFcJxDtkK0s3FF2qRKk1cC6LNXGvts4YpGhMxJoyAqg6jSTPvL+Dqd49itdLdvATtOw/IzPT2hmGP2HwFLiwgORVuDpT53Tv3YnkN5RsbwKzB1EEMN4yDuxaotpJqrkjCtaPDEv+1iEk89PYQnpfq5J9Nu3oGXuNtYqieInRD7OmJ4y5dTGsXU3zJm2PE8acFE6SvS8+FSztxpqUo9W7nIW9wJR7oMyOq8WxIq3lssT9+31VCWJy2s3QNRvy7L68pGrR5TvLp5hFsTq9L70L7BFZqfrbTfl9lu/1jXrr6YR2+5kLo/m5crjEZZjv6tmh+RyI0IZb8I3MoxR1Gp75Co1WI20LPx80j1p9QneaV8vfmLSmXqIwBM7fecM0rJGj836BuQKNWDJMtvVBOnqD4RoIZ4q9zvKs+rViwmOKBWTc2yMjy4K+d742SX9v0f4+gPL4LLPT/yVQJM3tNvRs2i327WZvuFgGjpjH1yKCEXIHCrQjzK/2TxJ2tl09sWaUGoj3mPbEDFdb89Kxn99Xj3ZniILGW1nkNc5n15rmO13W6TDu76vVEnx00XnmTjlbRYfWWw88k1Mk5/H3kZwylqVdyi6wxZ8g6yj6Vdad2xZhbhPyyt7lNqG0l1tenENN7EMk6v84EZ/fmncMopLoUybCp3UTc2GsiHeSTYWT8SzHiRWOO8PXEzeIk43Nkj5fIfhUm33mxLAYX94g3F2eZXVDvmesuh9yOIOw+wZiG7WFzmzRr+vv27ehJUQSz4p4LarG3N9aWylTh5IeMcP37fb0Q3OStCKthhvJ5s5lZTLcUbx+Ddor7PbRXORZvgXzfUBopqhxbIqu0Z7B998iJCJipEC/GNeQOJiWbiTNeUWu5fIAZBzc0cQ64IgoNrv0nXzLmJp31rNORnc333QnEn0gP/eq9xKo/2IN+WbQfZFKPqaTHWEb1ijy3tIg/73MW3TemNAbmrN4V3rd5uSDJOcyqmf2YV5RzXSNZNkvwDjIz5ln3iL8PSeOPUPwarm3jbwOnZZbzyyFjYQ5u/ZQeyIJZX3HEzS2glmMyrvA5CVlrNnOPFH2YNJGoa/0d59vudpcc6dpe/0OI3fFRYdkt5gvwS4reP0R4/8D3SR59nWOFe4+xVdouzPl2c3tbTl2Y8sgbmorUrWRYvNYw5t8D2PUT9FsX+gvzq/Sqpwk1md8loX8oZFTR5VvekJ3//dI3i5Wz6tDp2kkqecF7i8yUcuTeAGqJDp9fYk5Vlakt2NlJZImq5q00nfJpZAP/d8AUwQBluX2mj9mbqvVRea0XF2wvaWHIwv5dndbnd+blUN9L3PDKBrz7XrujxI1grDV1WiX0Vej+om5knM8wrEY1naDejMtdNcT1qOMcxoe4rueJ3R49GF3hXXl/mqzSmLNSRa8P9FSpMXssChLoq1ildlJnv6HD1gbc0CRipSyp3jEZvv5ZoKDpO7oyzygXiOWMeu+ENEjTHWbcmxDo+oZvCBaBMXCbeOoEW2pWaKvUTGXUqbsqlWLERabtD7MJ15Cd6s0AxbtCk9l3H3GlMwG+rpIW7yKyqmKCY8pJw7IVk5DXjKsplJ2vxM+cz1dlWck7T3fKVohLI6a4ukDhnblKrvj8631gyTvyql9qveDxWRsRf1eJUISr2Geitn8pOf3xej4Dv3f/X+KVql7')).decode())

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
