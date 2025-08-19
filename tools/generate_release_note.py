from ast import literal_eval
import subprocess
from pathlib import Path
import warnings
import argparse
from typing import Optional

from generator import RunResult
from utils import signed_str

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

GITHUB_REPO_URL = "https://github.com/key-moon/golf/"

def create_github_link(commit: str, file_path: Optional[Path] = None, text: Optional[str] = None):
  """Create a GitHub link for a commit or file at a specific commit."""
  if file_path:
    url = f"{GITHUB_REPO_URL}blob/{commit}/{file_path}"
  else:
    url = f"{GITHUB_REPO_URL}commit/{commit}"
  
  display_text = text if text else (str(file_path) if file_path else commit[:7])
  return f"[{display_text}]({url})"

def get_commits_between(commit1: str, commit2: str):
  """Get the list of commits between two commits, excluding those with [skip ci]."""
  result = subprocess.run(
    ["git", "log", "--pretty=format:%H %s", f"{commit1}..{commit2}"],
    stdout=subprocess.PIPE,
    text=True,
    check=True
  )
  
  commits = []
  for line in result.stdout.strip().split("\n"):
    if line.strip():
      parts = line.split(" ", 1)
      if len(parts) == 2:
        commit_hash, message = parts
        if "[skip ci]" not in message:
          commits.append((commit_hash, message))
  
  return commits

def get_changed_dist(commit1: str, commit2: str):
  """Get the list of files changed in the dist/ directory between two commits."""
  result = subprocess.run(
    ["git", "diff", "--name-only", commit1, commit2, "--", "dist/"],
    stdout=subprocess.PIPE,
    text=True,
    check=True
  )
  return [Path(path) for path in result.stdout.strip().split("\n") if path.strip()]

def get_file_content(commit: str, file_path: Path):
  """Get the content of a file at a specific commit."""
  result = subprocess.run(
    ["git", "show", f"{commit}:{file_path}"],
    stdout=subprocess.PIPE,
    check=True
  )
  return result.stdout

def get_uncompressed_content(content: bytes):
  if b"zlib.decompress" in content:
    try:
      start_idx = content.index(b"bytes(") + len(b"bytes(")
      end_idx = content.index(b",'L1'")
      return literal_eval(content[start_idx:end_idx].decode("L1")), True
    except Exception:
      return "# failed to decompress", True
  else:
    try:
      return content.decode(), False
    except Exception:
      return "# failed to decode", False

def generate_release_note(commit1: str, commit2: str, output_file: str):
  """Generate a release note in markdown format for files changed in dist/."""
  changed_files = get_changed_dist(commit1, commit2)
  commits = get_commits_between(commit1, commit2)

  with open(output_file, "w") as f:
    old_results = RunResult.from_json(get_file_content(commit1, Path("dist/results.json")))
    new_results = RunResult.from_json(get_file_content(commit2, Path("dist/results.json")))
    assert isinstance(old_results, RunResult) and isinstance(new_results, RunResult)

    improvement = new_results.score - old_results.score

    f.write("### overview\n\n")
    f.write(f" - score: {signed_str(improvement)} ({old_results.score} → {new_results.score})\n")
    f.write(f" - changed {len(changed_files)} files\n")
    if commits:
      f.write(f" - commits: {len(commits)}\n")
    f.write("\n")
    
    if commits:
      f.write("### commits\n\n")
      for commit_hash, message in commits:
        commit_link = create_github_link(commit_hash)
        f.write(f" - {commit_link} {message}\n")
      f.write("\n")

    f.write("\n")
    if len(changed_files) <= 10:
      for file_path in changed_files:
        task = int(file_path.stem[-3:])
        old_result, new_result = old_results.results[task - 1], new_results.results[task - 1]

        old_content, _ = get_uncompressed_content(get_file_content(commit1, file_path))
        new_content, _ = get_uncompressed_content(get_file_content(commit2, file_path))
        
        improvement = signed_str(new_result.length - old_result.length) if old_result.length and new_result.length else "-"

        f.write(f"#### {file_path} ({improvement})\n\n")
        
        # Create GitHub links for old and new versions
        old_link = create_github_link(commit1, file_path, "old")
        new_link = create_github_link(commit2, file_path, "new")
        
        f.write(f"**{old_link}**({old_result.length} bytes, {old_result.compressor}, {old_result.message})\n")
        f.write("```\n")
        f.write(old_content)
        f.write("\n```\n\n")
        f.write(f"**{new_link}**({new_result.length} bytes, {new_result.compressor}, {new_result.message})\n")
        f.write("```\n")
        f.write(new_content)
        f.write("\n```\n\n")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate release notes for changes between two commits.')
  parser.add_argument('commit1', help='First commit (older)')
  parser.add_argument('commit2', help='Second commit (newer)')
  parser.add_argument('-o', '--output', default='release_note.md', help='Output file (default: release_note.md)')
  
  args = parser.parse_args()
  
  try:
    generate_release_note(args.commit1, args.commit2, args.output)
    print(f"Release note generated: {args.output}")
  except Exception as e:
    print(f"Error: {e}")
    exit(1)
  
  exit(0)
