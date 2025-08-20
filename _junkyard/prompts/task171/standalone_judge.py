
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzVWEuOwzAIvc5UyqLL3iXy/a8xHlXTxNj8wXaVRQxSDHl5PHDOn/N8HvUqB7jXxfk66lUXr+p53//s8jjQp+inkV2u59jVZ9/Pjk9iNYjU7qe0btGbDNrYmHU9F5dRXrbGN4FZDGyQF4jQxRAyTsY8LY9tu6M8b9FIWTfo3pCNXRPfv//igZ6OOx17IGN1HpR3G3yXDMw9eJJY4TER3yCTQeRhbKeianUy7p1zsJH6CAzFemjTRUIfMRSmerJVRuKJ4/fu0wRlzUYg7y1j6sxXb/752zqJAxxMc6PW7qoYVJrNZvR/k6zZLrWpVpKZ36O71iV0Rh5ma6gof22BnFaesRPqeU29czbKVyW2li7Hd6v8Wppz9iS1bPl0zegWFjvRE6vKEk8UAvLMBRETzmL7neM8PgLF/zcw34trRvX+Q5NrUZRC2tRPgzyNqL5/5J2END1RN3msr/Z5VfyNGvcduqdGm2HuvMke5Lvkz5BPG+QWyXzINNbuWAiYYDhJb4hnLn9zmAyyJ3vhuAdGcWTPMyfbA3rVXewZKH6nu/M9e3fTtV1SgE56Ne1RbZxNoHTPuFkX8mxw7VZ+ATZpjsQ=')).decode())

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
