
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJylmlFuHEEIRK+TSPsx7HVWvv81vLITTzfQUA8rH0k8atNAURTMvP68Xtfj/efj8bJ/f3////2P13P7yc+Tv4+vU3Y89SxOvc8tz0w8ZT8/s7EtzS9bbMUbPttoWBKN06nMlrlTz9ZWdsN4as3Td1QM2Lpvbyhf9mVLu+EVsnLbqnDo/dKyHLHho5H7ZS6GxK9zNDS/TIq8NTjMsGHHStFu6HGoRP7GiB5D2zKgnLojntuqavkC6LUiGn2+LmRrx7pelTuiDEXjKtgmt7VGnmP+CjfU/VJq2ZxfKuY9H2pV6TGvYqPrDrVfsVdWDJDcQ2abc31V/Svr5me/Vht6LXu9QU8RveEVkWrrhMOrsBWfmXTK41BDVNcrFY4iflXapsIGqcqdm9Ro+HzpiPK2Jhpb0WzeL6Yqeb7+9xKdbXyWWS3TiWOmlr3SI37tdabecI+KHg3q1+X80rBx1htVVXYaoO4OvCrzUxUDeESxaOj9a4+4XpVrDdOeknciBYfc1ooNPfJ7TavMNtNRu03FFtc2XlXOZofVr/TJYeKY6Hk1hj7yCqKiX0zPn2e9vr4ob6yqmeSL7aNWHGoMYOGGhDfy+uoZ4KxtKqXHZvPbBplTfJYn2wO6j1p3KrqtaVWSG/bKvKoUgvn9N3n0dvowx6G++4o37OtLi4Yl3UFnbDbDZhO9xht8Z57to/QNJ9Vse32p0fCVonLUORqKX7/Ziqi613dYBYd9/6q5l0Qjzub6btk9a3EY9byerzXyk8mX9a91otIxP9EAe/dTbeVZ7nmDVGXGbLpavtJokH2v3r+YItrzpKPXI0pFL2eAeGqi59lcWZ0626r2NlXkfzcTadiI3YFFQ598vV8aDrMs8w0M5SiCDT/dqDH02wONo6oOW1Ul1wCZX7xXapWSYYPpQ/aOfoLDndlofZFaviPOeCMqBzJXMmz0G05lytZUij06HCrvslUc7sxGOWq2MZtN9BPNRublbG8zeVNMbzjnXjZxWHFKq5TZF0GT2Zx+fUQYO+7nuQag+SLzV6xKpqMm+crnr3Nf3mtZ5Sj/PYCWr7Xy1RtGPa9VSo/emntJvvpoKFpUy1fUAGT+ypRDFfkd8yp619+oT76Gbe02CB9287L2RpUw9kQRMQbwM6zOACtj08mXzA6+f3FFRFSKZwBt8vV6nkyI7GvMSziVM1vHAP0WS61lj0OiN6r6yv3q9LzyjRnhKBb5bPKdvHmkc+XkbQX9Sscrc75Z4vrwxGx9DPVONNktR+5lSo9pNv5dSjY78PfLbJLa/eNZnu03mN6gbNNtlvo3CFNVSRHFe2WF+Txf/hsYvVIqbNTfAzAF699XTvYbtOtNTp15XkMU0/OMASZTm1d6qjLf80VrWceh31Sw7RzVbF6l0JmIxDDecDIF0PlLw/zHJ8LLHmI=')).decode())

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
