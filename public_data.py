import datetime
import json
import re
from typing import Any, Callable, Iterable, TypedDict
import hashlib
import os
from functools import wraps
from utils import WORKSPACE_DIR

# watched_cache デコレータ版: 指定パス群/動的パス列挙の (path, mtime_ns, size) 変化で自動失効
def watched_cache(*paths: str, dynamic_paths: Callable[[], Iterable[str]] | None = None):
  def decorator(func: Callable[[], Any]):
    _MISSING = object()
    value: Any = _MISSING
    sig: tuple | None = None

    @wraps(func)
    def wrapper():
      nonlocal value, sig
      watch: list[str] = list(paths)
      if dynamic_paths is not None:
        try:
          watch.extend(list(dynamic_paths()))
        except Exception:
          pass
      parts: list[tuple[str, int | None, int | None]] = []
      for p in watch:
        try:
          st = os.stat(p)
          parts.append((p, int(st.st_mtime_ns), st.st_size))
        except (FileNotFoundError, NotADirectoryError):
          parts.append((p, None, None))
      new_sig = tuple(parts)
      if value is _MISSING or new_sig != sig:
        print("[+] cached file updated")
        value = func()
        sig = new_sig
      return value

    def cache_clear():  # 明示的クリア
      nonlocal value, sig
      value = _MISSING
      sig = None

    wrapper.cache_clear = cache_clear  # type: ignore[attr-defined]
    return wrapper
  return decorator


def _datetime_parser(dct):
  for key, value in dct.items():
    if key == "date" and isinstance(value, int):
      dct[key] = datetime.datetime.fromtimestamp(value)
  return dct


def _datetime_serializer(obj):
  if isinstance(obj, datetime.datetime):
    return int(obj.timestamp())
  raise TypeError("Type not serializable")


def _loads(path: str, default: Any):
  try:
    with open(path) as f:
      return json.load(f, object_hook=_datetime_parser)
  except FileNotFoundError:
    return default


def _dumps(path, data: Any):
  with open(path, "w") as f:
    json.dump(data, f, default=_datetime_serializer)


class Submission(TypedDict):
  date: datetime.datetime
  score: float


class TeamData(TypedDict):
  name: str
  submissions: list[Submission]


SCOREBOARD_PROGRESSIONS_PATH = "data/kaggle_scoreboard_progressions.json"

@watched_cache(SCOREBOARD_PROGRESSIONS_PATH)
def loads_scoreboard_progressions() -> dict[int, TeamData]:
  return { int(k): v for k, v in _loads(SCOREBOARD_PROGRESSIONS_PATH, {}).items() }


def dumps_scoreboard_progressions(data: dict[int, TeamData]) -> None:
  _dumps(SCOREBOARD_PROGRESSIONS_PATH, data)


class TaskSubmission(TypedDict):
  date: datetime.datetime
  score: int | None


TASK_SCORE_PROGRESSIONS_PATH = os.path.join(WORKSPACE_DIR, "data/task_score_progressions")


def _dynamic_task_progression_paths() -> Iterable[str]:
  if not os.path.isdir(TASK_SCORE_PROGRESSIONS_PATH):
    return []
  for f in os.listdir(TASK_SCORE_PROGRESSIONS_PATH):
    if f.endswith('.json'):
      yield os.path.join(TASK_SCORE_PROGRESSIONS_PATH, f)

@watched_cache(TASK_SCORE_PROGRESSIONS_PATH, dynamic_paths=_dynamic_task_progression_paths)
def loads_task_scores_progressions() -> dict[str, list[list[TaskSubmission]]]:
  task_scores: dict[str, list[list[TaskSubmission]]] = {}
  if not os.path.isdir(TASK_SCORE_PROGRESSIONS_PATH):
    return task_scores
  for filename in os.listdir(TASK_SCORE_PROGRESSIONS_PATH):
    if filename.endswith('.json'):
      f = _loads(f"{TASK_SCORE_PROGRESSIONS_PATH}/{filename}", None)
      if f is None:
        print(f"[!] invalid file ({filename})")
        continue
      name = f.get("name")
      data = f.get("data")
      if isinstance(name, str) and isinstance(data, list):
        task_scores[name] = data  # type: ignore[assignment]
  return task_scores
def dumps_task_scores_progressions(data: dict[str, list[list[TaskSubmission]]]) -> None:
  for name, scores in data.items():
    filename = get_user_filename(name)
    path = f"{TASK_SCORE_PROGRESSIONS_PATH}/{filename}"
    print(f"[+] dumping to {path}")
    _dumps(path, { "name": name, "data": scores })
  loads_task_scores_progressions.cache_clear()  # type: ignore[attr-defined]


class TaskSubmissionWithName(TypedDict):
  name: str
  score: int
  date: datetime.datetime


def get_scores_per_task():
  task_scores = loads_task_scores_progressions()
  res: list[list[TaskSubmissionWithName]] = [[] for _ in range(400)]
  for name, subs_per_task in task_scores.items():
    for i, subs in enumerate(subs_per_task):
      if len(subs) == 0 or subs[-1]["score"] is None:
        continue
      sub = subs[-1]
      if sub["score"] is None:
        continue
      res[i].append(
        TaskSubmissionWithName(
          name=name,
          date=sub["date"],
          score=sub["score"],
        )
      )
  for i in range(400):
    res[i].sort(key=lambda x: x["score"])
  return res


def delete_user_progressions(name: str) -> None:
  filename = get_user_filename(name)
  path = f"{TASK_SCORE_PROGRESSIONS_PATH}/{filename}"
  if os.path.exists(path):
    os.remove(path)
    print(f"[+] deleted {path}")
  loads_task_scores_progressions.cache_clear()  # type: ignore[attr-defined]


def get_user_filename(name: str) -> str:
  alphanumeric_name = ''.join(c for c in name if c.isalnum())
  return f"{alphanumeric_name}-{hashlib.md5(name.encode()).hexdigest()}.json"


MERGED_USERS_PATH = os.path.join(WORKSPACE_DIR, "data/merged_users.json")


@watched_cache(MERGED_USERS_PATH)
def loads_merged_users() -> set[str]:
  return set(_loads(MERGED_USERS_PATH, []))


def dumps_merged_users(data: set[str]) -> None:
  _dumps(MERGED_USERS_PATH, list(data))


# ---- ours score progressions helpers ----

def _ensure_task_progressions_dir() -> None:
  os.makedirs(TASK_SCORE_PROGRESSIONS_PATH, exist_ok=True)


def init_empty_progressions() -> list[list[TaskSubmission]]:
  """Create an empty 400-length list of per-task submission lists."""
  return [[] for _ in range(400)]


def load_user_progressions(name: str) -> list[list[TaskSubmission]]:
  """Load an individual user's progressions by name or return empty if missing."""
  _ensure_task_progressions_dir()
  filename = get_user_filename(name)
  path = os.path.join(TASK_SCORE_PROGRESSIONS_PATH, filename)
  if not os.path.exists(path):
    return init_empty_progressions()
  f = _loads(path, None)
  if f is None or "data" not in f:
    return init_empty_progressions()
  return f["data"]


def save_user_progressions(name: str, data: list[list[TaskSubmission]]) -> None:
  """Persist a single user's progression file."""
  _ensure_task_progressions_dir()
  filename = get_user_filename(name)
  path = os.path.join(TASK_SCORE_PROGRESSIONS_PATH, filename)
  _dumps(path, {"name": name, "data": data})
  loads_task_scores_progressions.cache_clear()  # type: ignore[attr-defined]


def record_ours_task_score_progression(current_scores: dict[int, int | None], name: str = "ours", when: datetime.datetime | None = None) -> None:
  """Append current scores to ours' progression file (per task) only when changed."""
  if when is None:
    when = datetime.datetime.utcnow()
  data = load_user_progressions(name)
  if len(data) < 400:
    data.extend([[] for _ in range(400 - len(data))])
  for task_id, score in current_scores.items():
    idx = task_id - 1
    if not (0 <= idx < 400):
      continue
    history = data[idx]
    last_score = history[-1]["score"] if history else None
    if last_score != score:
      history.append({"date": when, "score": score})
    data[idx] = history
  save_user_progressions(name, data)


def compute_current_scores_from_dist(dist_dir: str = os.path.join(WORKSPACE_DIR, "dist")) -> dict[int, int | None]:
  """Return {task_id: file_size or None} for dist/taskNNN.py."""
  scores: dict[int, int | None] = {}
  for i in range(1, 401):
    path = os.path.join(dist_dir, f"task{i:03}.py")
    if os.path.exists(path):
      try:
        scores[i] = os.path.getsize(path)
      except OSError:
        scores[i] = None
    else:
      scores[i] = None
  return scores


# --- Banner helpers --------------------------------------------------------

def build_banner_lines_for_task(task_id: int) -> list[str]:
    """Return banner lines for a task: [best_line, eq_line?].
    best_line like: "# best: 12(name1, name2) / others: ..."
    eq_line like:   "# ===== ... =====" (only when best is small)
    """
    if not (1 <= task_id <= 400):
        return []
    lines: list[str] = []
    try:
        # progression から各チームの直近スコアを使って best を決定（"ours" 除外）
        prog = loads_task_scores_progressions()  # dict[name] -> list[list[{date, score}]]
        items: list[tuple[int, str]] = []  # (last_score, name)
        for name, per_task in prog.items():
            if name == "ours":
                continue
            if task_id - 1 >= len(per_task):
                continue
            series = per_task[task_id - 1] or [{ "score": None }]
            last_sc = series[-1].get("score")
            if last_sc is not None:
                items.append((last_sc, name))
        if items:
            items.sort(key=lambda x: x[0])
            best = items[0][0]
            names = [n for sc, n in items if sc == best]
            others_items = [(sc, n) for sc, n in items if sc != best][:5]
            others = ", ".join([f"{sc}({n})" for sc, n in others_items])
            lines.append(f"# best: {best}({', '.join(names)}) / others: {others}")
            if isinstance(best, int) and best <= 200:
                lines.append("# " + f" {best} ".center(best - 2, "="))
    except Exception:
        pass
    return lines

_PAT_BEST = re.compile(r"^\s*#\s*best:\s*", re.IGNORECASE)
_PAT_EQ = re.compile(r"^\s*#\s*=+ \d+ =+")

def apply_banner_update(text: str, header_lines: list[str]) -> tuple[str, bool]:
    """Replace all banner lines in text and optionally prepend header if missing.
    Returns (new_text, updated_flag).
    """
    lines = text.split('\n')
    out_lines: list[str] = []
    new_best = header_lines[0] if header_lines else None
    new_eq = header_lines[1] if len(header_lines) > 1 else None
    content_changed = False
    banner_found = False
    for ln in lines:
        if _PAT_BEST.match(ln):
            banner_found = True
            if new_best is not None:
                out_lines.append(new_best)
                if ln != new_best:
                   content_changed = True
            else:
               content_changed = True
            continue
        if _PAT_EQ.match(ln):
            banner_found = True
            if new_eq is not None:
                out_lines.append(new_eq)
                if ln != new_eq:
                    content_changed = True
            else:
               content_changed = True
            continue
        out_lines.append(ln)
    if not banner_found and header_lines:
        out_lines = header_lines + out_lines
        content_changed = True
    return "\n".join(out_lines), content_changed

