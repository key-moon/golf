#!/usr/bin/env python3
from dataclasses import dataclass
from datetime import datetime
import kaggle
import csv
import zipfile
import tempfile

import requests
from tqdm import tqdm

from public_data import Submission, TaskSubmission, TeamData, dumps_task_scores_progressions, loads_scoreboard_progressions, dumps_scoreboard_progressions, loads_task_scores_progressions, loads_merged_users

@dataclass
class KaggleRawScoreboardEntry:
  rank: int
  teamid: int
  teamname: str
  lastsubmissiondate: datetime
  score: float
  submissioncount: int
  teammemberusernames: list[str]

def update_new_submissions():
  submissions = loads_scoreboard_progressions()

  with tempfile.TemporaryDirectory() as tmpdir:
    kaggle.api.competition_leaderboard_download("google-code-golf-2025", path=tmpdir)
    csv_path = f"{tmpdir}/google-code-golf-2025.zip"

    # ZIPファイルを開く
    with zipfile.ZipFile(csv_path, 'r') as zip_ref:
      file_list = zip_ref.namelist()
      if len(file_list) != 1 or not file_list[0].endswith('.csv'):
        print(f"Warning: Invalid file in the ZIP archive. {file_list=}")
        return
      else:
        csv_file_name = file_list[0]
        with zip_ref.open(csv_file_name) as csv_file:
          csv_content = csv_file.read().decode()

  csv_reader = csv.reader(csv_content.splitlines()[1:])
  scoreboard_entries: list[KaggleRawScoreboardEntry] = []
  for row in csv_reader:
    try:
      entry = KaggleRawScoreboardEntry(
        rank=int(row[0]),
        teamid=int(row[1]),
        teamname=row[2],
        lastsubmissiondate=datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S"),
        score=float(row[4]),
        submissioncount=int(row[5]),
        teammemberusernames=row[6].split(",")
      )
      scoreboard_entries.append(entry)
    except (ValueError, IndexError) as e:
      print(f"Error parsing row: {row}, error: {e}")

  for entry in scoreboard_entries:
    # チート検知
    if (2500 - 75) * 400 <= entry.score: continue
    if entry.teamid not in submissions:
      submissions[entry.teamid] = TeamData(
        name=entry.teamname,
        submissions=[
          Submission(
            date=entry.lastsubmissiondate,
            score=entry.score
          )
        ]
      )
    elif submissions[entry.teamid]["submissions"][-1]["score"] != entry.score:
      submissions[entry.teamid]["submissions"].append(
        Submission(
          date=entry.lastsubmissiondate,
          score=entry.score
        )
      )
  dumps_scoreboard_progressions(submissions)

def update_task_scores_progressions():
  task_scores = loads_task_scores_progressions()
  merged_users = loads_merged_users()
  ts = datetime.now()

  csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=0&single=true&output=csv"
  csv_content = requests.get(csv_url).text
  csv_reader = csv.reader(csv_content.splitlines())

  updated = set()
  name_row = []
  for row in tqdm(csv_reader):
    if not name_row:
      name_row = [*map(str.strip, row)]
      for name in name_row:
        if not name:
          continue
        if name in merged_users:
          print(f"[!] skipping merged user: {name}")
          continue
        if name not in task_scores:
          task_scores[name] = [[] for _ in range(400)]
          updated.add(name)
      continue
    try:
      task_num = int(row[0].lstrip("0")) - 1
    except ValueError:
      continue
    for name, score in zip(name_row, row):
      if not name:
        continue
      if name in merged_users:
        continue
      if score.strip() == "":
        score = None
      else:
        try:
            score = int(score)
            if score <= 0:
              score = None
        except ValueError:
          continue
      scores = task_scores[name][task_num]
      if len(scores) == 0 or scores[-1]["score"] != score:
        updated.add(name)
        task_scores[name][task_num].append(TaskSubmission(date=ts, score=score))

  filtered_task_scores = {name: task_scores[name] for name in updated}
  dumps_task_scores_progressions(filtered_task_scores)

if __name__ == "__main__":
  print("[+] updating task scores...")
  update_task_scores_progressions()
  print("[+] updating submissions...")
  update_new_submissions()
