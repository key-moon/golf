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


def strip_code_fences(text: str) -> str:
    """
    Remove markdown code fences from the model response.
    """
    return re.sub(r"^```(?:python)?\n|```$", "", text.strip(), flags=re.MULTILINE)


def format_examples(train_examples):
    """
    Convert train examples to Python literal for prompt.
    """
    formatted = []
    for i, ex in enumerate(train_examples):
        inp = ex.get('input')
        out = ex.get('output')
        formatted.append(f"# Example {i}\ninput_grid = {inp}\noutput_grid = {out}")
    # print(formatted)
    return "\n\n".join(formatted)
    
def generate_solver_from_grids(grid_examples: list, model: str) -> str:
    system_msg = {
        "role": "system",
        "content": (
             "You are a Python code-golf champion. Generate the shortest valid Python function of the form def p(g):...return g based only on examples. Use the short variable names. Avoid redundant comments, and unnecessary imports."
         )
    }
    examples_text = format_examples(grid_examples)
    prompt = "Here are input/output examples:\n" + examples_text
    user_msg = {
        "role": "user",
        "content": (
            prompt
        )
    }
    try:
      resp = client.chat.completions.create(
          model=model,
          messages=[system_msg, user_msg],
      )
    except Exception as e:
        raise RuntimeError(f"OpenAI API request failed: {e}")
    return resp.choices[0].message.content


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not set", file=sys.stderr)
    sys.exit(1)
client = openai.OpenAI(api_key=api_key)

run = time.strftime("%Y%m%d%H%M%S")
log_dir = f"logs/{run}"
os.mkdir(log_dir)

def process_task(i):
    if os.path.exists("SKIP"): return
    try:
        task = json.load(open(f"tasks/task{i:03}.json", "r"))
        print(f"[+] generating {i}...")
        # msg = generate_solver_from_grids(task["train"], "o4-mini")
        msg = generate_solver_from_grids(task["train"], "o3")
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
        print(f"{code_path} -> {res}")
    except Exception as e:
        print(e)

with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(process_task, range(4, 400)[::-1])
