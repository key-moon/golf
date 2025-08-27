#!/usr/bin/env python3
import base64
import os
import json
import argparse
import re
import sys
import zlib
import openai
from tqdm import tqdm

from concurrent.futures import ThreadPoolExecutor
import time

from strip import strip_for_zlib_space
from utils import Case, get_cases, get_code_paths, get_task
from checker import check


def strip_code_fences(text: str) -> str:
    match = re.search(r"```(?:py|python)?\n(.*?)```", text, re.DOTALL)
    if match: return match.group(1)
    match = re.search(r"(?s)(def\s+p\(g\):.*?return\s+.*?)(?:\n|$)", text)
    if match: return match.group(1)
    return match

JUDGE = """
import ast
import zlib

def get_cases(case_path: str) -> list[list[list[int]]]:
  return ast.literal_eval(zlib.decompress(open(case_path, "rb").read()).decode())

if __name__ == "__main__":
  import sys
  import warnings
  warnings.filterwarnings("ignore", category=SyntaxWarning)
  warnings.filterwarnings("ignore", category=FutureWarning)
  if len(sys.argv) < 3:
    print(f"usage: {sys.argv[0]} [path to your code] [path to case data]")
    exit(1)
  cases = get_cases(sys.argv[2])
  
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
    print("<failed_cases>")
    print("<note>only first 8 cases are shown</note>")
    for i, (inp, ans, out) in enumerate(wrong_cases[:8]):
      print(f"<case{i}>")
      print("<input>")
      print("\\n".join([" ".join(map(str, row)) for row in inp]))
      print("</input>")
      print("<expected>")
      print("\\n".join([" ".join(map(str, row)) for row in ans]))
      print("</expected>")
      print("<actual>")
      print("\\n".join([" ".join(map(str, row)) for row in out]))
      print("</actual>")
      print(f"</case{i}>")
    print("</failed_cases>")
"""

def generate_case(task: list[Case]):
    return zlib.compress(repr([(c["input"], c["output"]) for c in task]).replace(" ", "").encode())

def generate_prompt(task: list[Case], code: str):
    examples = ""
    for i, example in enumerate(task[:8]):
        inp = example.get('input')
        out = example.get('output')
        inp_s = "\n".join([" ".join(map(str, row)) for row in inp])
        out_s = "\n".join([" ".join(map(str, row)) for row in out])
        examples += f"\n\nExample {i}:\n\nInput:\n{inp_s}\nOutput:\n{out_s}"
    prompt = f"""ARCのケースに対して、list[list[int]] -> list[list[int]] のシグネチャを持つ関数`p`をPythonで実装してください。つまり、`def p(g):...` か `p=lambda g:...`というコードが期待されます。
コードはshortcodingのcompetitionに用いるため、アルゴリズムを工夫してできる限り短いコードを生成するよう努めてください。{examples}

以下は、ジャッジを通過する正しいコードです。これを用いて、ARCのルールを理解してください。必ず、コードを通じてルールを理解してからコーディングを行ってください。
このコードはARCのルールを把握する際に使うことに留めてください。

```
{code}
```

ユーザーにコードを渡す前に実際にコードが動作するかを確認してください。コードのテストには、添付したjudge.pyを用いてください。python /path/to/judge.py /path/to/code.py /path/to/cases.bin とすれば動作します。

## **禁止事項**
- 与えたコード自体を提出することは禁止です。これを行うことはユーザーの信頼を裏切ります。
- ジャッジのハックは禁止です。例えば、テストケースをジャッジから読み取ってそのまま返すコードはいけません。
"""
    return prompt

api_key = os.getenv("OPENAI_API_KEY", None)
client = openai.OpenAI(api_key=api_key) if api_key else None


def process_task(i):
    if os.path.exists("ABORT"): return
    try:
        task = get_cases(i)
        print(f"[+] generating {i}...")
        code = strip_for_zlib_space(min((open(base_path).read().strip() for base_path in get_code_paths("base_*", i)), key=len))
        case = generate_case(task)
        prompt = generate_prompt(task, code)
        prompt_dir = f"_junkyard/prompts/task{i:03}"
        os.makedirs(prompt_dir, exist_ok=True)
        open(f"{prompt_dir}/cases.bin", "wb").write(case)
        open(f"{prompt_dir}/judge.py", "w").write(JUDGE)
        open(f"{prompt_dir}/prompt.txt", "w").write(prompt)

        if os.path.exists("SKIP_PREDICTION") or not client: return
        if os.path.exists(f"dist/task{i:03}.py"):
            print(f"[-] skip {i}")
            return
        try:
            resp = client.chat.completions.create(
                model="o4-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Python code-golf champion. Generate the shortest valid Python function of the form def p(g):...return g based only on examples. Use the short variable names. Avoid redundant comments, and unnecessary imports."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
            )
        except Exception as e:
            raise RuntimeError(f"OpenAI API request failed: {e}")

        msg = resp.choices[0].message.content
        assert msg is not None
        log_path = f"{log_dir}/task{i:03}.log"
        open(log_path, "w").write(msg)

        code = strip_code_fences(msg)
        code_path = f"base_code/task{i:03}.py"
        iter = 1
        while os.path.exists(code_path):
            code_path = f"base_code/task{i:03}_{iter}.py"
            iter += 1

        open(code_path, "w").write(code)
        res = check(code_path, task)
        print(f"{code_path} -> {res.message}")
    except Exception as e:
        print(e)
    return

for i in tqdm(range(1, 401)):
    process_task(i)
# with ThreadPoolExecutor(max_workers=15) as executor:
#     executor.map(process_task, range(1, 401))
