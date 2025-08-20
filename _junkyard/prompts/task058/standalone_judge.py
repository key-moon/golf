
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztWltuwkAMvE4r7QdSj4O4/zVaqkLZeF5LKSrUyg+JvU7WHs84EfuX/X43zsdh3OTs43T/Ns7HZD2enSyns93mrHoeoxxex/y09c53v7LZadkt2EfdZ83D5gpahSLTLLl9tP2h7AB1BoPzAXAj8LlZOyo2p7WTHazd2MvaYt+sBfZkvb+/f36/f58/n/+gi1V923aFTXaUWMkryVHAEcTRx5Ebdo3qONWtqtMVSyiEc3TjTD/cVYIm6I0yBbUeVAPXllWV1ZNVktQwmTBUdtqrve7qZacly/Lfh1Vuy4xfcYbi1oSdL+KMygEgTvGCcYAXiAO9dqFXfsf06dNMpFlNK5RWO0UOYdctMm9+Xjpk4zE/+7zjmqeakbL3fpev+l7xkSmt5632eGKPQN1sFMdNjuMcVzrOddztNMBpybK+eZ30eut12+u/nyO8quTz+ogQ157t+W89w3eJiHVPRzgZjoQPPuMNzy0pT53jDc15KX9O8YAniQc9YTziCeIJz5W7r+xoJUsrmV+p5gpCVlC3guRIlXT/tPVOVsN4crXCg8KVwqfCueqXeELUE6aeUPWEqydkPWHrzuov6iZXKL+oJrjKrLqsqqya8Rf1eV9Xnx3u9z8MdGQTUHu11696hTN7FK2//7vZOZ2b05k5nZfTWTmdk9MZOZ2Pf/D9//JQKG3bFTbJDmIlrydHBMcURyXHte4M3Q+6CzT2NeIlztPZIeHi9mkf6hNpfhDJs7bnf68kXpO8unmd9IqbaXem3JluZ6qdaXam2JleR2rd/7X+B3bLJCaCRpLR0qEQHWj4YJ0Vzg7Avsw2jrEc6znmdOzrOpl1Marrn7oGkQk8awZq1mqmcXVwRXAVYOY1Z/JeaovmIrqK4Z91Dus51q2szzUDqN5XXa/6XXS6Qh3L3NNepygiK3BeSc8PVDvBJQPhg6ODY4Mjg+Ji5Z8xyVtH+7Xfw/hFb8hSWeYj+74Zvn0NrgBekUCsgVgGxCp+JBbwg7GgH4hF/Fbi5c+X7zfPX16PvL45XnL8Ada/xHf0e+qcC8v3E8xPPT3Zx90P7xRdUic=')).decode())

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
