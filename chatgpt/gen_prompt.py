from utils import get_task


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

for i in range(1, 401):

    """
    Find the common rule that maps an input grid to an output grid, given the examples below.



    Write Python code that performs the transformation according to the rule in following format: `def p(g): ...`. Note that input and output are passed by 2D arrays
    """
