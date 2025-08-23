import datetime
from functools import cache
import json
from typing import Any, TypedDict
import hashlib
import os

from utils import WORKSPACE_DIR


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


@cache
def loads_scoreboard_progressions() -> dict[int, TeamData]:
  return { int(k): v for k, v in _loads(SCOREBOARD_PROGRESSIONS_PATH, {}).items() }


def dumps_scoreboard_progressions(data: dict[int, TeamData]) -> None:
  _dumps(SCOREBOARD_PROGRESSIONS_PATH, data)


class TaskSubmission(TypedDict):
  date: datetime.datetime
  score: int | None


TASK_SCORE_PROGRESSIONS_PATH = os.path.join(WORKSPACE_DIR, "data/task_score_progressions")


@cache
def loads_task_scores_progressions() -> dict[str, list[list[TaskSubmission]]]:
  task_scores: dict[str, list[list[TaskSubmission]]] = {}
  if not os.path.isdir(TASK_SCORE_PROGRESSIONS_PATH):
    return task_scores
  for filename in os.listdir(TASK_SCORE_PROGRESSIONS_PATH):
    if filename.endswith(".json"):
      f = _loads(f"{TASK_SCORE_PROGRESSIONS_PATH}/{filename}", None)
      if f is None:
        print(f"[!] invalid file ({filename})")
        continue
      name = f["name"]
      data = f["data"]
      task_scores[name] = data
  return task_scores


def dumps_task_scores_progressions(data: dict[str, list[list[TaskSubmission]]]) -> None:
  for name, scores in data.items():
    alphanumeric_name = ''.join(c for c in name if c.isalnum())
    sanitized_name = f"{alphanumeric_name}-{hashlib.md5(name.encode()).hexdigest()}"
    path = f"{TASK_SCORE_PROGRESSIONS_PATH}/{sanitized_name}.json"
    print(f"[+] dumping to {path}")
    _dumps(path, { "name": name, "data": scores })


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
