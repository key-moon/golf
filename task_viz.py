import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import tqdm

from checker import get_task
from utils import parse_range_str

cmap = colors.ListedColormap([
    '#8B00FF',  # Violet
    '#4B0082',  # Indigo
    '#0000FF',  # Blue
    '#FFFF00',  # Yellow
    '#00FF00',  # Green
    '#FF7F00',  # Orange
    '#FF0000',  # Red
    '#964B00',  # Golden
    '#000000',  # Black
    '#FFFFFF',  # White
])
norm = colors.Normalize(vmin=0, vmax=9)

def visualize_challenges(task, num_visualize, path):
    tasks  = []
    tasks += [(f"train_{i}", t) for i, t in enumerate(task['train'])]
    tasks += [(f"test_{i}", t) for i, t in enumerate(task['test'])]
    tasks += [(f"arcgen_{i}", t) for i, t in enumerate(task['arc-gen'])]
    fig, axes = plt.subplots(num_visualize, 2, figsize=(5, 5 * num_visualize))
    for idx, (name, task) in enumerate(tasks[:num_visualize]):
      mat_inp = np.array(task['input']) 
      shape_i = mat_inp.shape
      mat_out = np.array(task['output'])
      shape_o = mat_out.shape
      axes[idx, 0].set_title(f"INPUT MATRIX : {shape_i}")
      axes[idx, 0].imshow(mat_inp, cmap=cmap, norm=norm)
      axes[idx, 1].set_title(f"OUTPUT MATRIX : {shape_o}")
      axes[idx, 1].imshow(mat_out, cmap=cmap, norm=norm)
      axes[idx, 1].axis('off')
    plt.tight_layout()
    plt.savefig(path)

if __name__ == "__main__":
  p = argparse.ArgumentParser()
  p.add_argument("range", nargs="?", default="1-400")
  p.add_argument("--count", default=5)
  p.add_argument("--directory", default="vis")
  
  args = p.parse_args()

  directory = args.directory
  count = int(args.count)

  for i in tqdm.tqdm(parse_range_str(args.range)):
    visualize_challenges(get_task(i), count, f"{directory}/task{i:03}.png")
