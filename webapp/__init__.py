from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Optional
import subprocess

from flask import Flask, jsonify, render_template, request, send_from_directory, abort

# 内部モジュール
from public_data import get_scores_per_task, loads_task_scores_progressions
from utils import WORKSPACE_DIR
from compress import get_content_summary

import json
import re

DIST_RESULTS_PATH = Path(WORKSPACE_DIR) / "dist" / "results.json"
TASKS_DIR = Path(WORKSPACE_DIR) / "tasks"
TAGS_DIR = Path(WORKSPACE_DIR) / "data" / "tags"
TAGS_FILE = TAGS_DIR / "tags.json"
TMP_OUTPUTS_PATH = Path(WORKSPACE_DIR) / "tmp" / "outputs.json"

# --- Banner helpers --------------------------------------------------------

def build_banner_lines_for_task(task_id: int) -> list[str]:
    """Return banner lines for a task: [best_line, eq_line?].
    best_line like: "# best: 12(name1, name2) / others: ..."
    eq_line like:   "# ===== ... =====" (only when best is small)
    """
    if not (1 <= task_id <= 400):
        return []
    try:
        scores_per_task = get_scores_per_task()
        scores = scores_per_task[task_id - 1] if scores_per_task and len(scores_per_task) >= task_id else []
    except Exception:
        scores = []
    lines: list[str] = []
    if scores:
        try:
            best = scores[0].get("score")
            names = [s.get("name") for s in scores if s.get("score") == best]
            others = ", ".join([f"{s.get('score')}({s.get('name')})" for s in scores if s.get('score') != best][:5])
            lines.append(f"# best: {best}({', '.join(names)}) / others: {others}")
            if isinstance(best, int) and best <= 150:
                lines.append("# " + f" {best} ".center(best - 2, "="))
        except Exception:
            pass
    return lines

_PAT_BEST = re.compile(r"^\s*#\s*best:\s*", re.IGNORECASE)
_PAT_EQ = re.compile(r"^\s*#\s*=+")

def apply_banner_update(text: str, header_lines: list[str]) -> tuple[str, bool]:
    """Replace all banner lines in text and optionally prepend header if missing.
    Returns (new_text, updated_flag).
    """
    lines = text.splitlines()
    out_lines: list[str] = []
    new_best = header_lines[0] if header_lines else None
    new_eq = header_lines[1] if len(header_lines) > 1 else None
    updated = False
    replaced_best_any = False
    for ln in lines:
        if _PAT_BEST.match(ln):
            if new_best is not None:
                out_lines.append(new_best)
            updated = True
            replaced_best_any = True
            continue
        if _PAT_EQ.match(ln):
            if new_eq is not None:
                out_lines.append(new_eq)
            updated = True
            continue
        out_lines.append(ln)
    if not replaced_best_any and header_lines:
        out_lines = header_lines + out_lines
        updated = True
    return "\n".join(out_lines) + "\n", updated

def _load_tags_store() -> dict:
    if TAGS_FILE.exists():
        try:
            data = json.loads(TAGS_FILE.read_text())
            if not isinstance(data, dict):
                data = {}
        except Exception:
            data = {}
    else:
        data = {}
    # normalize structure
    data.setdefault("all", [])
    data.setdefault("tasks", {})
    # ensure types
    if not isinstance(data["all"], list):
        data["all"] = []
    if not isinstance(data["tasks"], dict):
        data["tasks"] = {}
    return data

def _save_tags_store(data: dict) -> None:
    TAGS_DIR.mkdir(parents=True, exist_ok=True)
    data["tasks"] = { k: v for k, v in sorted(data["tasks"].items(), key=lambda x:int(x[0])) }
    TAGS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def _load_our_results() -> dict:
    if DIST_RESULTS_PATH.exists():
        try:
            return json.loads(DIST_RESULTS_PATH.read_text())
        except Exception:
            return {"score": 0, "results": []}
    return {"score": 0, "results": []}


# 一括サムネイル用の簡易キャッシュ
_TASK_THUMBS_CACHE: dict[str, list[dict]] = {}


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    # ルート: ダッシュボード
    @app.get("/")
    def index():
        return render_template("index.html")

    # タスク一覧
    @app.get("/tasks")
    def tasks_page():
        view = request.args.get("view", "thumb")  # thumb | list
        sort = request.args.get("sort", "problem")  # problem|best|length|diff
        order = request.args.get("order", "asc")    # asc|desc
        return render_template("tasks.html", view=view, sort=sort, order=order)

    # タスク詳細
    @app.get("/tasks/<int:task_id>")
    def task_detail(task_id: int):
        if not (1 <= task_id <= 400):
            abort(404)
        return render_template("task_detail.html", task_id=task_id)

    # タスクのケース一覧
    @app.get("/tasks/<int:task_id>/cases")
    def task_cases(task_id: int):
        if not (1 <= task_id <= 400):
            abort(404)
        return render_template("task_cases.html", task_id=task_id)

    # API: タグ 取得・更新
    @app.get("/api/tags")
    def api_get_tags():
        return jsonify(_load_tags_store())

    @app.get("/api/tags/<int:task_id>")
    def api_get_tags_for_task(task_id: int):
        data = _load_tags_store()
        tags = data.get("tasks", {}).get(str(task_id), [])
        return jsonify({"task_id": task_id, "tags": tags})

    @app.post("/api/tags/add_type")
    def api_add_tag_type():
        body = request.get_json(silent=True) or {}
        name = (body.get("name") or "").strip()
        if not name:
            return jsonify({"ok": False, "error": "name required"}), 400
        data = _load_tags_store()
        if name not in data["all"]:
            data["all"].append(name)
            data["all"].sort(key=lambda x: x.lower())
            _save_tags_store(data)
        return jsonify({"ok": True, "all": data["all"]})

    @app.post("/api/tags/set_for_task")
    def api_set_tags_for_task():
        body = request.get_json(silent=True) or {}
        task_id_raw = body.get("task_id", None)
        if task_id_raw is None:
            return jsonify({"ok": False, "error": "task_id required"}), 400
        try:
            task_id = int(task_id_raw)
        except Exception:
            return jsonify({"ok": False, "error": "invalid task_id"}), 400
        tags = body.get("tags") or []
        if not isinstance(tags, list):
            return jsonify({"ok": False, "error": "tags must be list"}), 400
        # normalize
        tags = [str(t).strip() for t in tags if str(t).strip()]
        data = _load_tags_store()
        # add unknown tags into all
        for t in tags:
            if t not in data["all"]:
                data["all"].append(t)
        data["all"].sort(key=lambda x: x.lower())
        data.setdefault("tasks", {})
        data["tasks"][str(task_id)] = sorted(set(tags), key=lambda x: x.lower())
        _save_tags_store(data)
        return jsonify({"ok": True, "task_id": task_id, "tags": data["tasks"][str(task_id)], "all": data["all"]})

    # API: サマリー (ダッシュボード・一覧用)
    @app.get("/api/summary")
    def api_summary():
        ours = _load_our_results()
        others = get_scores_per_task()  # list[list[{name, score, date}]]

        # 我々の長さ配列・best 配列
        our_lengths: list[Optional[int]] = [None] * 400
        base_path: list[Optional[str]] = [None] * 400
        base_short: list[Optional[str]] = [None] * 400
        compressor: list[Optional[str]] = [None] * 400
        message: list[str] = [""] * 400

        for item in (ours.get("results") or []):
            idx = int(item.get("task", 0)) - 1
            if 0 <= idx < 400:
                our_lengths[idx] = item.get("length")
                # results.json は basePath を使用。後方互換のため両方を見る
                bp = item.get("base_path") or item.get("basePath")
                base_path[idx] = bp
                # base_xxx のディレクトリ名だけを抽出
                if isinstance(bp, str):
                    parts = bp.replace("\\", "/").split("/")
                    short = next((p for p in parts if p.startswith("base_")), None)
                    base_short[idx] = short
                compressor[idx] = item.get("compressor")
                message[idx] = item.get("message") or ""

        bests: list[Optional[int]] = []
        best_names: list[list[str]] = []
        for arr in others:
            if arr:
                best_score = arr[0]["score"]
                bests.append(best_score)
                best_names.append([x["name"] for x in arr if x["score"] == best_score])
            else:
                bests.append(None)
                best_names.append([])

        return jsonify({
            "our_score": ours.get("score", 0),
            "our_lengths": our_lengths,
            "bests": bests,
            "best_names": best_names,
            "base_path": base_path,
            "base_short": base_short,
            "compressor": compressor,
            "message": message,
        })

    # API: チーム一覧
    @app.get("/api/teams")
    def api_teams():
        data = loads_task_scores_progressions()  # dict[name] -> list[list[{date, score}]]
        names = sorted(list(data.keys()), key=lambda x: sum(min([log["score"] or 200 for log in entry])for entry in data[x]))
        return jsonify({"names": names})

    # API: 指定チームの各タスク最終スコア（400長配列）
    @app.get("/api/team_lengths")
    def api_team_lengths():
        name = request.args.get("name")
        if not name:
            return jsonify({"error": "name required"}), 400
        data = loads_task_scores_progressions()
        if name not in data:
            return jsonify({"name": name, "lengths": [None] * 400})
        per_task = data[name]
        out: list[Optional[int]] = [None] * 400
        for i in range(min(len(per_task), 400)):
            subs = per_task[i] or []
            # 最終提出のスコア（Noneはスキップ）
            if subs:
                last = subs[-1].get("score")
                out[i] = last if isinstance(last, int) else 2500
        return jsonify({"name": name, "lengths": out})

    # API: タスクJSONを返す（クライアント側でレンダリング）
    @app.get("/api/task/<int:task_id>/data")
    def api_task_data(task_id: int):
        path = TASKS_DIR / f"task{task_id:03}.json"
        if not path.exists():
            abort(404)
        try:
            return jsonify(json.loads(path.read_text()))
        except Exception:
            abort(500)

    # API: タスクの一括サムネイルデータ
    @app.get("/api/tasks/thumbs")
    def api_tasks_thumbs():
        include_output = request.args.get("include_output", "0") in ("1", "true", "True")
        cache_key = "with_out" if include_output else "no_out"
        if cache_key in _TASK_THUMBS_CACHE:
            return jsonify(_TASK_THUMBS_CACHE[cache_key])
        out: list[dict] = []
        for task_id in range(1, 401):
            path = TASKS_DIR / f"task{task_id:03}.json"
            if not path.exists():
                item = {"id": task_id, "input": None}
                if include_output:
                    item["output"] = None
                item.update({"train_n":0, "test_n":0, "arcgen_n":0, "in_h":None, "in_w":None, "out_h":None, "out_w":None})
                out.append(item)
                continue
            try:
                data = json.loads(path.read_text())
                # Use the first test example if available, otherwise fall back to train/arc-gen
                ex = None
                if (data.get("test") or []):
                    ex = (data.get("test") or [None])[0]
                elif (data.get("train") or []):
                    ex = (data.get("train") or [None])[0]
                elif (data.get("arc-gen") or []):
                    ex = (data.get("arc-gen") or [None])[0]
                train_n = len(data.get("train") or [])
                test_n = len(data.get("test") or [])
                arcgen_n = len(data.get("arc-gen") or [])
                in_h = in_w = out_h = out_w = None
                if ex and ex.get("input"):
                    in_h = len(ex["input"]) or None
                    in_w = len(ex["input"][0]) if in_h else None
                if ex and ex.get("output"):
                    out_h = len(ex["output"]) or None
                    out_w = len(ex["output"][0]) if out_h else None
                item = {"id": task_id, "input": ex.get("input") if ex else None, "train_n":train_n, "test_n":test_n, "arcgen_n":arcgen_n, "in_h":in_h, "in_w":in_w, "out_h":out_h, "out_w":out_w}
                if include_output:
                    item["output"] = ex.get("output") if ex else None
                out.append(item)
            except Exception:
                item = {"id": task_id, "input": None}
                if include_output:
                    item["output"] = None
                item.update({"train_n":0, "test_n":0, "arcgen_n":0, "in_h":None, "in_w":None, "out_h":None, "out_w":None})
                out.append(item)
        _TASK_THUMBS_CACHE[cache_key] = out
        return jsonify(out)

    # API: タスクごとのスコア推移（トップ10チーム）
    @app.get("/api/task/<int:task_id>/progress")
    def api_task_progress(task_id: int):
        # ランクは最終スコアで算出し、上位10チームの推移を返す
        scores_per_task = get_scores_per_task()
        if not (1 <= task_id <= 400) or task_id - 1 >= len(scores_per_task):
            return jsonify({"teams": []})

        ranked = scores_per_task[task_id - 1] if scores_per_task else []
        top = ranked[:10]

        all_progress = loads_task_scores_progressions()
        teams_out = []
        for entry in top:
            name = entry.get("name")
            series = []
            if name in all_progress:
                per_task = all_progress[name]
                if 0 <= task_id - 1 < len(per_task):
                    raw = per_task[task_id - 1]
                    series = [{
                        "t": int(x.get("date").timestamp()) if isinstance(x.get("date"), datetime) else x.get("date"),
                        "score": x.get("score")
                    } for x in raw]
            teams_out.append({"name": name, "series": series})

        return jsonify({"teams": teams_out})

    # API: VS Code でファイルを開く
    @app.post("/api/open_file")
    def api_open_file():
        data = request.get_json(silent=True) or {}
        path = request.args.get("path") or data.get("path")
        if not path:
            return jsonify({"ok": False, "error": "path required"}), 400
        try:
            abs_path = (Path(WORKSPACE_DIR) / path).resolve()
            # ワークスペース外は拒否
            Path(abs_path).relative_to(Path(WORKSPACE_DIR))
        except Exception:
            return jsonify({"ok": False, "error": "invalid path"}), 400
        try:
            subprocess.run(["code", str(abs_path)], check=False)
            return jsonify({"ok": True})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500

    # API: 指定ファイルを開きつつ、そのファイル内のバナー（# best: と = ライン）を更新
    @app.post("/api/open_and_update_banner")
    def api_open_and_update_banner():
        data = request.get_json(silent=True) or {}
        path = request.args.get("path") or data.get("path")
        if not path:
            return jsonify({"ok": False, "error": "path required"}), 400
        try:
            abs_path = (Path(WORKSPACE_DIR) / path).resolve()
            Path(abs_path).relative_to(Path(WORKSPACE_DIR))
        except Exception:
            return jsonify({"ok": False, "error": "invalid path"}), 400

        # task id をファイル名から推定
        m = re.search(r"task(\d{3})\.py$", str(abs_path))
        task_id = int(m.group(1)) if m else None

        # ヘッダ生成（task_id が特定できた場合のみ）
        header_lines: list[str] = build_banner_lines_for_task(task_id) if task_id is not None else []

        # 置換（best/== ラインを全行で）
        try:
            text = Path(abs_path).read_text(encoding="utf-8")
        except Exception:
            text = ""
        new_text, updated = apply_banner_update(text, header_lines)
        if updated:
            try:
                Path(abs_path).write_text(new_text, encoding="utf-8")
            except Exception as e:
                return jsonify({"ok": False, "error": f"write failed: {e}"}), 500

        # 開く
        try:
            subprocess.run(["code", str(abs_path)], check=False)
        except Exception:
            pass
        return jsonify({"ok": True, "path": str(abs_path), "updated": updated, "task_id": task_id})

    # dist の静的配信（存在すれば）
    @app.get("/dist/<path:filename>")
    def serve_dist(filename: str):
        dist_dir = Path(WORKSPACE_DIR) / "dist"
        if not dist_dir.exists():
            abort(404)
        return send_from_directory(dist_dir, filename)

    # API: dist/taskNNN.py のコード要約（圧縮解除またはそのまま表示）
    @app.get("/api/task/<int:task_id>/code_summary")
    def api_task_code_summary(task_id: int):
        if not (1 <= task_id <= 400):
            return jsonify({"ok": False, "error": "invalid task_id"}), 400
        path = Path(WORKSPACE_DIR) / "dist" / f"task{task_id:03}.py"
        if not path.exists():
            return jsonify({"ok": False, "error": "not found"}), 404
        try:
            content = path.read_bytes()
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
        try:
            summary = get_content_summary(content)
        except Exception:
            # フォールバック: バイナリをL1でデコード（壊れる可能性あり）
            try:
                summary = content.decode("L1", errors="replace")
            except Exception as e:
                return jsonify({"ok": False, "error": str(e)}), 500
        return jsonify({"ok": True, "task_id": task_id, "path": f"dist/task{task_id:03}.py", "summary": summary})

    # API: 最近のベスト更新を返す
    @app.get("/api/recent_best_updates")
    def api_recent_best_updates():
        all_progress = loads_task_scores_progressions()  # dict[name] -> list[list[{date, score}]]
        events: list[dict] = []
        # 400 タスクを走査
        for t_idx in range(400):
            # 全チームの提出を集約
            submissions: list[tuple[datetime, int, str]] = []  # (date, score, name)
            for name, per_task in all_progress.items():
                if t_idx < len(per_task):
                    for sub in per_task[t_idx] or []:
                        sc = sub.get("score")
                        if sc is None:
                            continue
                        dt = sub.get("date")
                        if isinstance(dt, (int, float)):
                            dt = datetime.fromtimestamp(dt)
                        if not isinstance(dt, datetime):
                            continue
                        submissions.append((dt, int(sc), name))
            if not submissions:
                continue
            submissions.sort(key=lambda x: x[0])
            current_best: int | None = None
            for dt, sc, name in submissions:
                if current_best is None or sc < current_best:
                    events.append({
                        "task_id": t_idx + 1,
                        "from": current_best,
                        "to": sc,
                        "name": name,
                        "t": int(dt.timestamp()),
                    })
                    current_best = sc
        events.sort(key=lambda e: e["t"], reverse=True)
        return jsonify({"events": events[:50]})

    # タスク初期化/オープン（tools/init.py の動作を模倣）
    @app.post("/api/task/<int:task_id>/init")
    def api_init_task(task_id: int):
        if not (1 <= task_id <= 400):
            return jsonify({"ok": False, "error": "invalid task_id"}), 400
        try:
            user = os.getlogin()
        except Exception:
            user = os.environ.get("USER") or os.environ.get("USERNAME") or ""
        base_map = {"keymoon": "base_keymoon", "yu212": "base_yu"}
        base_dir_name = base_map.get(user, "base_keymoon")
        padded = f"{task_id:03d}"
        base_dir = Path(WORKSPACE_DIR) / base_dir_name
        base_dir.mkdir(parents=True, exist_ok=True)
        file_path = base_dir / f"task{padded}.py"

        # ヘッダ情報生成
        def build_header():
            lines = []
            try:
                scores_per_task = get_scores_per_task()
                scores = scores_per_task[task_id - 1] if scores_per_task and len(scores_per_task) >= task_id else []
            except Exception:
                scores = []
            if scores:
                best = scores[0].get("score")
                names = [s.get("name") for s in scores if s.get("score") == best]
                others = ", ".join([f"{s.get('score')}({s.get('name')})" for s in scores if s.get('score') != best][:5])
                lines.append(f"# best: {best}({', '.join(names)}) / others: {others}")
                try:
                    if isinstance(best, int) and best <= 150:
                        lines.append("# " + f" {best} ".center(best - 2, "="))
                except Exception:
                    pass
            return lines

        created = False
        if not file_path.exists():
            src_lines = build_header()
            src_lines.append("def p(g):")
            src_lines.append(" return g")
            file_path.write_text("\n".join(src_lines) + "\n", encoding="utf-8")
            created = True
        else:
            # 既存: ファイル全体を走査して、バナー関連行を「すべて」置換する（共通ロジック使用）
            header_lines = build_banner_lines_for_task(task_id)
            try:
                original = file_path.read_text(encoding="utf-8")
            except Exception:
                original = ""
            new_text, updated = apply_banner_update(original, header_lines)
            if updated:
                file_path.write_text(new_text, encoding="utf-8")

        # VS Code でファイルを開く
        try:
            subprocess.run(["code", str(file_path)], check=False)
        except Exception:
            pass
        if user == "yu212":
            vis = Path(WORKSPACE_DIR) / "vis_output" / f"task{padded}.png"
            try:
                subprocess.run(["code", str(vis)], check=False)
            except Exception:
                pass
        return jsonify({"ok": True, "created": created, "path": str(file_path), "user": user})

    # ジャッジ結果出力ページ
    @app.get("/judge")
    def judge_page():
        # default: show only incorrect; client reads query param
        return render_template("judge.html")

    @app.get("/api/judge/outputs")
    def api_judge_outputs():
        try:
            mtime = int(TMP_OUTPUTS_PATH.stat().st_mtime)
        except Exception:
            mtime = 0
        task_id: Optional[int] = None
        outputs = []
        if TMP_OUTPUTS_PATH.exists():
            try:
                raw = json.loads(TMP_OUTPUTS_PATH.read_text())
                # New schema: { "task": id, "outputs": [...] }
                if isinstance(raw, dict) and "outputs" in raw:
                    task_id = raw.get("task")
                    outputs = raw.get("outputs") or []
                # Legacy: list
                elif isinstance(raw, list):
                    outputs = raw
                else:
                    outputs = []
            except Exception:
                outputs = []
        # Backward compatibility: also include 'items' as alias of outputs
        return jsonify({"mtime": mtime, "task": task_id, "outputs": outputs, "items": outputs})

    return app


# ローカル起動用
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
