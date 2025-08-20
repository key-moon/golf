
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJztWkluwzAM/E4D5KBLgPwl8P+/0aJNZZEirRFFbUXhQ4IpIXo44Wb39fF6hXt2HfcL9JFcKfpr543++KHesPv9gt3YPd+XN/r4/ovE7ine74ket7tBvXZUVsRL6TPyVL1SNLxQWREvpRN2JvXIGVk8a1B+rmwrecPuty33KJpEE0TfV8G2gZ0x96TawqIPovxc2Vby1ks9nV2eDSU0VU+3NbNrzL11OtwOfc/e4fr3vRU1teXeLpqe6u0zR1rU22eO7J17LBIRJSqBaABsx04tGjuiEoimfU+znTG1SGi/LUBGkW5/uG0M/bYAZDfYWT2vmXNN9f7OzKmrN25q2adHtqi3Vo30y70Va6R/7q1VI3dQz53d9MoZAFuv3GtjZ1FPelI2O/eYzwRNol9AQ4Wt7K2Xejq7JPoqyrYF6AQzO/PMmfgkaPxWREOFreytl3o6uxh9FeXqXdk2s5v0jiFU2Mre+qmnsct3bQlleQec0MBuUt8LFbZ79b2sbi43c7ajo6ZWy8zZjo6aWv/fzuLsaqrh1cw5rnJ67gZo5vCMrIl8nXqeuwGaOX3e7/XTyVsRi3r9dPJWxKZer3iO6nBI7u3b4bymFnZuREmEQTQAtpI3/H5r+57Gju0AEJr2Pc22kd20vjemns7qe2Pqadu7dYomGoEoP1e2HZl7Ors8c0oonTk12565d4VGzwx9fwJoqLCVvfmrV2KXP+eiaFY3wRNM7Kb9P2eosEU6uKd6Gru8Ruao/qxFP8HMzuEpNUXjZxENFbayt17q6exi9FU0yzzoBCO7jTcGGaW/5GPbjQHZI1o2BoomkQRRfq5sK3nD77c29zR2bOIAUHljcGZ3Oz4Bs5DQRA==')).decode())

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
