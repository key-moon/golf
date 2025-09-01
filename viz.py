import argparse
import numpy as np
import tqdm
from matplotlib import colors
import matplotlib.pyplot as plt

from utils import parse_range_str, get_task

hex_palette = [
  '#8B00FF',  # 0 Violet
  '#4B0082',  # 1 Indigo
  '#0000FF',  # 2 Blue
  '#FFFF00',  # 3 Yellow
  '#00FF00',  # 4 Green
  '#FF7F00',  # 5 Orange
  '#FF0000',  # 6 Red
  '#964B00',  # 7 Golden
  '#000000',  # 8 Black
  '#FFFFFF',  # 9 White
]
cmap = colors.ListedColormap(hex_palette)
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

SYMBOL = 1
LITERAL = 2
def printmat(matrix, char_type=SYMBOL, pad=2, gap=0):
  # exact hex palette (same as matplotlib cmap)
  def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

  palette_rgb = [hex_to_rgb(h) for h in hex_palette]

  reset = '\033[0m'

  for row in matrix:
    line = []
    for v in row:
      try:
        idx = int(v)
      except Exception:
        line.append((str(v) if char_type == LITERAL else "?"*pad).ljust(pad))
        continue

      if idx < 0 or idx >= len(palette_rgb):
        line.append((str(v) if char_type == LITERAL else "?"*pad).ljust(pad))
        continue

      r, g, b = palette_rgb[idx]
      # choose contrasting foreground (black or white) based on luminance
      luminance = 0.299 * r + 0.587 * g + 0.114 * b
      if luminance > 186:
        fr, fg, fb = (0, 0, 0)   # dark text for light background
      else:
        fr, fg, fb = (255, 255, 255)  # light text for dark background

      #            0123456789
      content = (str(idx) if char_type==LITERAL else " .@+*%$`#~"[idx]*pad).ljust(pad)

      seq = f'\033[48;2;{r};{g};{b}m\033[38;2;{fr};{fg};{fb}m'
      line.append(f"{seq}{content}{reset}")
    print((" "*gap).join(line))

  def visualize_challenges_console(task, num_visualize):
    tasks  = []
    tasks += [(f"train_{i}", t) for i, t in enumerate(task['train'])]
    tasks += [(f"test_{i}", t) for i, t in enumerate(task['test'])]
    tasks += [(f"arcgen_{i}", t) for i, t in enumerate(task['arc-gen'])]
    for idx, (name, task) in enumerate(tasks[:num_visualize]):
      mat_inp = np.array(task['input'])
      mat_out = np.array(task['output'])
      print(f"{name} INPUT MATRIX ({mat_inp.shape}):")
      printmat(mat_inp)
      print(f"{name} OUTPUT MATRIX ({mat_out.shape}):")
      printmat(mat_out)

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
