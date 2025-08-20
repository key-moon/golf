
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzVWu1qwzAMfJ0N/KPsA/Yuwe//GvOWGcfyRT5JNnQE1tKDRDudTrLa4+U4PtN5PdLwLqcOfVz+llcTKu9c4OMtlau8+UrlKq/vqVw5v6ZpVH/PIND6V/+PrlGdUaTjI5WrvJ5RMlEN9yPQ389uuTrRn6gqR5WzMzouKmt+ea76aGxc1c+GbHVc6SjWVY2mZvLkzsrV86j92TNofa6dq6iuGop0NaKcrnzOgJSjozpXlaOYrlCOxqhmNdj8qnJVo+L9yuPtyEUlirzd4qKccjDKZdCjK3t+Wa6kM6zrOHof5HTl6YPP2Z1ZNtgMjrrqa3GXt7NcSW/36KpVGXJRHR3vjLzd4qLcrILR+zsjZ+AziH2SQ2dR9dFY/Ao9t+VIR61RRfsgW4Ocrvou7XdRxif5qPpa/L9zO9Zzfa6OWnW1zkWRrhDK6GrdzMBGhTpOPyt4nYFF2Y7Tz1XRWdTjV4grOYvG/Or6XPaswejK0wc9utK5kpPMXl2hqBBXUlfRTRHr7XpUchbd0XHYLjnqyj6LthwN2bpFrc7Q16KXK73K7DVYMxjbFOmOxPuVPA96okIZZFHMVc9RfH+ln63YGpRnnGgNNtReg03tsgb3np3ZDEq/iu36kJ51lNNV7DyIat8TlTwPRnfIjE/yXK3qOHEURbXjexybb6BJxjOLIuXo6Iwr2QdjUx/fB/WopDNEvx+0nweZuX2v2tlJRqo9pivEFUKturJwNfrkDGW5ki4a20DOUGsG10elc3V/1shgJ+ObGdCJj3VRLYNrdsjouR61ywz69lc6ipgUDN3UYOwbXsGLC0Vcxbx9ZIP3dqQrueuLTchXNka1Y65QBuXMsKMPjugsg3L7sW7PgNhgu7M8pcZqsOVIR61crfvth/dclsGeYZ0z6Gq/7wsZnFJ9syhSjr3jtKhkx9m7v2Kyj+ar2C9SeNTGVY0qfwNOjF/n')).decode())

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
