import subprocess
from pathlib import Path
import warnings
import argparse
from typing import Optional

from compress import get_uncompressed_content
from generator import RunResult
from public_data import get_scores_per_task
from utils import signed_str

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

GITHUB_REPO_URL = "https://github.com/key-moon/golf/"

def create_github_link(commit: str, file_path: Optional[Path | str] = None, text: Optional[str] = None):
  """Create a GitHub link for a commit or file at a specific commit."""
  if file_path:
    url = f"{GITHUB_REPO_URL}blob/{commit}/{file_path}"
  else:
    url = f"{GITHUB_REPO_URL}commit/{commit}"
  
  display_text = text if text else (str(file_path) if file_path else f"`{commit[:7]}`")
  return f"[{display_text}]({url})"

def get_commits_between(commit1: str, commit2: str):
  """Get the list of commits between two commits, including author, excluding those with [skip ci]."""
  result = subprocess.run(
    ["git", "log", "--pretty=format:%H||||%s||||%an", f"{commit1}..{commit2}"],
    stdout=subprocess.PIPE,
    text=True,
    check=True
  )

  commits = []
  for line in result.stdout.strip().split("\n"):
    if line.strip():
      parts = line.split("||||", 2)
      if len(parts) == 3:
        commit_hash, message, author = parts
        # if "[skip ci]" not in message:
        commits.append((commit_hash, message, author))
  
  return commits

def get_changed_dist(commit1: str, commit2: str):
  """Get the list of files changed in the dist/ directory between two commits."""
  result = subprocess.run(
    ["git", "diff", "--name-only", commit1, commit2, "--", "dist/"],
    stdout=subprocess.PIPE,
    text=True,
    check=True
  )
  return [Path(path) for path in result.stdout.strip().split("\n") if path.strip() and "results.json" not in path]

def get_file_content(commit: str, file_path: Path):
  """Get the content of a file at a specific commit."""
  result = subprocess.run(
    ["git", "show", f"{commit}:{file_path}"],
    stdout=subprocess.PIPE,
    check=True
  )
  return result.stdout

def generate_release_note(commit1: str, commit2: str, output_dir: str):
  """Generate a release note in markdown format for files changed in dist/."""
  public_scores_per_task = get_scores_per_task()
  changed_files = get_changed_dist(commit1, commit2)
  commits = get_commits_between(commit1, commit2)

  old_results = RunResult.from_json(get_file_content(commit1, Path("dist/results.json")))
  new_results = RunResult.from_json(get_file_content(commit2, Path("dist/results.json")))
  assert isinstance(old_results, RunResult) and isinstance(new_results, RunResult)

  improvement = new_results.score - old_results.score

  notes = [""]
  
  note_buffer = ""
  def _add_note(note: str):
    nonlocal note_buffer
    note_buffer += note

  def _flush():
    nonlocal note_buffer
    if len((notes[-1] + note_buffer).encode()) <= 1950:
      notes[-1] += note_buffer
    else:
      notes.append(note_buffer)
    note_buffer = ""

  _add_note(f" - score: {signed_str(improvement)} ({old_results.score} → {new_results.score})\n")
  _add_note(f" - changed: {len(changed_files)}\n")
  _add_note(f" - commits: {len(commits)}\n" if commits else "")
  _flush()

  
  if commits:
    _add_note("## commits\n")
    for commit_hash, message, author in commits:
      commit_link = create_github_link(commit_hash[:7])
      _add_note(f" - {commit_link} by {author}: {message}\n")
      _flush()
    _flush()


  if len(changed_files) <= 10:
    for file_path in changed_files:
      if file_path.suffix != ".py":
        continue
      task = int(file_path.stem[-3:])
      old_result, new_result = old_results.results[task - 1], new_results.results[task - 1]

      old_content, _ = get_uncompressed_content(get_file_content(commit1, file_path))
      new_content, _ = get_uncompressed_content(get_file_content(commit2, file_path))
      
      improvement = signed_str(new_result.length - old_result.length) if old_result.length and new_result.length else "-"

      public_scores = public_scores_per_task[task - 1]
      community_best = public_scores[0]["score"]

      best_delta = signed_str(new_result.length - community_best) if new_result.length else "-"

      _add_note(f"### {file_path} ({improvement}, best{best_delta}, {create_github_link('main', f'vis_many/task{task:03d}.png', 'vis_many')})\n")
      
      # Create GitHub links for old and new versions
      old_link = create_github_link(commit1, file_path, "old")
      new_link = create_github_link(commit2, file_path, "new")

      best_names = [score["name"] for score in public_scores if score["score"] == community_best]
      others = ', '.join([f'{score["score"]}({score["name"]})' for score in public_scores if score['score'] != community_best][:5])
      _add_note(f"best: {community_best}({', '.join(best_names)}) / others: {others}\n\n")

      _add_note(f"**{old_link}** ({old_result.length} bytes, {create_github_link(commit1, str(old_result.base_path), str(old_result.base_path))}, {old_result.compressor}, {old_result.message})\n")
      _add_note("```\n")
      _add_note(old_content if len(old_content) < 700 else f"<too long (len: {len(old_content)})>")
      _add_note("\n```\n")
      _add_note(f"**{new_link}** ({new_result.length} bytes, {create_github_link(commit2, str(new_result.base_path), str(new_result.base_path))}, {new_result.compressor}, {new_result.message})\n")
      _add_note("```\n")
      _add_note(new_content if len(new_content) < 700 else f"<too long (len: {len(new_content)})>")
      _add_note("\n```\n\n")
      _flush()

  output_dir_path = Path(output_dir)
  with open(output_dir_path / "release_note.md", "w") as f:
    f.write("".join(notes))
  for i, note in enumerate(notes):
    with open(output_dir_path / f"release_note_{i}.md", "w") as f:
      f.write(note)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate release notes for changes between two commits.')
  parser.add_argument('commit1', help='First commit (older)')
  parser.add_argument('commit2', help='Second commit (newer)')
  parser.add_argument('-o', '--output', default='tmp', help='Output file (default: release_note.md)')
  
  args = parser.parse_args()
  
  try:
    generate_release_note(args.commit1, args.commit2, args.output)
    print(f"Release note generated under {args.output}") 
  except Exception as e:
    print(e)
