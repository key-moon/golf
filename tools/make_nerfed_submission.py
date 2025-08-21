import os
import zipfile
import sys

from utils import parse_range_str

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python nerfed_submission.py <byte_count>")
    sys.exit(1)

  byte_count = int(sys.argv[1])
  range_str = sys.argv[2] if 3 <= len(sys.argv) else "1-400"
  
  score = 0
  dist_dir = "dist"
  with zipfile.ZipFile("submission.zip", 'w') as zipf:
    for i in parse_range_str(range_str):
      filename = f"task{i:03}.py"
      filepath = os.path.join(dist_dir, filename)

      if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
          content = f.read()
      
        pad = b"\n" + b"1" * (byte_count - 1)
        modified_content = content + pad
        score += 2500 - len(modified_content)

        # Write the modified content to the ZIP file
        zipf.writestr(filename, modified_content)
      else:
        print(f"File not found: {filepath}")
  print(f"expected score: {score}")
