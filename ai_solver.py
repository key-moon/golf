#!/usr/bin/env python3
import os
import json
import argparse
import re
import sys
import openai
from tqdm import tqdm

from checker import check
from concurrent.futures import ThreadPoolExecutor
import time

from utils import get_task


def strip_code_fences(text: str) -> str:
    match = re.search(r"```(?:py|python)?\n(.*?)```", text, re.DOTALL)
    if match: return match.group(1)
    match = re.search(r"(?s)(def\s+p\(g\):.*?return\s+.*?)(?:\n|$)", text)
    if match: return match.group(1)
    return match
    

def generate_prompt(task):
    prompt = "Find the common rule that maps an input grid to an output grid, given the examples below."
    examples = task["train"] + task["test"] + task["arc-gen"]
    for i, example in enumerate(examples[:8]):
        inp = example.get('input')
        out = example.get('output')
        inp_s = "\n".join([" ".join(map(str, row)) for row in inp])
        out_s = "\n".join([" ".join(map(str, row)) for row in out])
        prompt += f"\n\nExample 1:\n\nInput:\n{inp_s}\nOutput:\n{out_s}"
    prompt += "\n\n\nWrite the **short** Python code in code golf manners that performs the transformation according to the rule in following format: `def p(g): ...`. Note that input and output are passed by 2D arrays. Use `val_` as a prefix for all variables except `_`. Avoid line breaks as much as possible.\n"
    return prompt

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not set", file=sys.stderr)
    sys.exit(1)
client = openai.OpenAI(api_key=api_key)

run = time.strftime("%Y%m%d%H%M%S")
log_dir = f"logs/{run}"
os.mkdir(log_dir)

def process_task(i):
    if os.path.exists("ABORT"): return
    try:
        task = get_task(i)
        print(f"[+] generating {i}...")
        prompt = generate_prompt(task)
        open(f"prompts/task{i:03}.txt", "w").write(prompt)

        if os.path.exists(f"dist/task{i:03}.py"):
            print(f"[-] skip {i}")
            return

        if os.path.exists("SKIP_PREDICTION"): return
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

with ThreadPoolExecutor(max_workers=15) as executor:
    executor.map(process_task, range(1, 401))
