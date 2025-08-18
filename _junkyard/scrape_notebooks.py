#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime as dt
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, cast
from kagglesdk.kernels.types.kernels_api_service import ApiListKernelSessionOutputRequest
import requests

# ========== Kaggle API ==========
# どちらの import 形でも動くようにフォールバック
try:
    import kaggle  # noqa: F401
    from kaggle import api as kaggle_api_singleton
    _HAVE_SINGLETON = True
except Exception:
    _HAVE_SINGLETON = False

try:
    from kaggle.api.kaggle_api_extended import KaggleApi
    _HAVE_CLASS = True
except Exception:
    _HAVE_CLASS = False

DEFAULT_COMP = "google-code-golf-2025"
DEFAULT_OUT = "notebooks"
PAGE_SIZE_DEFAULT = 100
MAX_PAGES_DEFAULT = 1000
SLEEP_BETWEEN_PULLS = 0.4  # API 負荷軽減

def die(msg: str, code: int = 1) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
    sys.exit(code)

def ensure_kaggle_api():
    """
    kaggle.api のシングルトンを優先して使う。
    無ければ KaggleApi() を生成して authenticate()。
    """
    api = None
    if _HAVE_SINGLETON:
        api = kaggle_api_singleton
        # authenticate() がある場合は呼ぶ（古い版だと無い）
        try:
            api.authenticate()
        except Exception:
            pass
    elif _HAVE_CLASS:
        api = KaggleApi()
        api.authenticate()
    else:
        die("kaggle API の import に失敗しました。`pip install kaggle` と API token 設定(~/.kaggle/kaggle.json)を行ってください。")
    return api

# ---------- 文字列ユーティリティ ----------
def normalize_slug(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "unknown"

def parse_ref_from_meta(meta: Any) -> Optional[str]:
    """
    ApiKernelMetadata から owner/slug を取り出す。
    meta.id または meta.ref に "owner/slug" 形式が入っていることが多いので優先的に使う。
    """
    for attr in ("id", "ref"):
        v = getattr(meta, attr, None)
        if isinstance(v, str) and "/" in v:
            return v.strip()
    # フィールドが分離している可能性にも一応備える
    owner = getattr(meta, "owner_slug", None) or getattr(meta, "author", None) or getattr(meta, "user_name", None)
    slug  = getattr(meta, "slug", None) or getattr(meta, "kernel_slug", None)
    if owner and slug:
        return f"{owner}/{slug}"
    return None

def parse_owner_slug(ref: str) -> Tuple[str, str]:
    if "/" not in ref:
        raise ValueError(f"ref 形式が不正です: {ref} (期待: owner/slug)")
    owner, slug = ref.split("/", 1)
    return owner.strip(), slug.strip()

def extract_owner(meta: Any, fallback_ref: Optional[str]) -> str:
    # まずはメタの属性から
    for attr in ("authorUsername", "owner_slug", "author", "user_name", "owner"):
        v = getattr(meta, attr, None)
        if isinstance(v, str) and v.strip():
            return normalize_slug(v)
    # ダメなら ref から
    if fallback_ref:
        return normalize_slug(fallback_ref.split("/", 1)[0])
    return "unknown"

def extract_slug(meta: Any, fallback_ref: Optional[str]) -> str:
    for attr in ("slug", "kernel_slug"):
        v = getattr(meta, attr, None)
        if isinstance(v, str) and v.strip():
            return normalize_slug(v)
    if fallback_ref:
        return normalize_slug(fallback_ref.split("/", 1)[1])
    return "unknown"

def extract_last_run_ts(meta: Any) -> str:
    """
    CSV行から時刻カラムを探して、YYYYMMDD-HHMMSSZ 文字列を返す。
    見つからなければ 'unknown' を返す。
    """
    try:
        ts = meta.last_run_time
        return ts.strftime("%Y%m%d-%H%M%SZ")
    except Exception as e:
        print(e)
        return "unknown"

def build_versioned_dir(base: Path, slug: str, author: str, ver_ts: str) -> Path:
    return base / f"{ver_ts}-{slug}-{author}"

# ---------- Kaggle API 呼び出し ----------
def list_kernels_for_competition_api(api, comp_slug: str,
                                     page_size: int = 100,
                                     max_pages: int = 1000) -> List[Any]:
    """
    Kaggle API の kernels_list をページングして全件取得。
    """
    if page_size > 100:
        page_size = 100
    page = 1
    out: List[Any] = []
    while page <= max_pages:
        kernels = api.kernels_list(
            page=page,
            page_size=page_size,
            competition=comp_slug,
            # search=None, user=None, language=None, kernel_type=None, output_type=None, sort_by=None ...
        )
        if not kernels:
            break
        # None が混ざる可能性に備える
        items = [k for k in kernels if k is not None]
        out.extend(items)
        print(f"[INFO] fetched page {page}: {len(items)} kernels")
        if len(items) < page_size:
            break
        page += 1
        time.sleep(0.25)
    # ref 重複除去
    seen: set[str] = set()
    uniq: List[Any] = []
    for meta in out:
        ref = parse_ref_from_meta(meta)
        if not ref:
            continue
        if ref not in seen:
            uniq.append(meta)
            seen.add(ref)
    return uniq

def pull_kernel_with_api(api, ref: str, dest_dir: Path, with_metadata: bool = True) -> None:
    """
    api.kernels_pull(kernel=ref, path=dest_dir, metadata=with_metadata, quiet=True)
    既に dest_dir が存在する場合はスキップ。
    """
    if dest_dir.exists():
        print(f"[SKIP] already exists: {dest_dir}")
        return
    dest_dir.mkdir(parents=True, exist_ok=True)
    # KaggleApi.kernels_pull の引数名は metadata / quiet がある版が多い
    api.kernels_pull(kernel=ref, path=str(dest_dir), metadata=with_metadata, quiet=True)

def download_submission_zip_with_api(api, ref: str, dest_dir: Path, skip_if_exists: bool = True) -> bool:
    """
    api.kernels_output を使って出力を一時フォルダに取得し、
    submission.zip があれば dest_dir/submission.zip に移動。
    既存が同サイズならスキップ。サイズ違いは更新。
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / "submission.zip"
    if skip_if_exists and target.exists():
        print(f"[SKIP] submission.zip already exists: {target}")
        return False

    try:
        # outfiles, _token = api.kernels_output(kernel=ref, path=str(tmp_dir), force=False, quiet=True)
        kernel=ref
        path=str(dest_dir)
        force=False
        quiet=False
        if kernel is None:
            raise ValueError("A kernel must be specified")
        api.validate_kernel_string(kernel)
        kernel_url_list = kernel.split("/")
        owner_slug = kernel_url_list[0]
        kernel_slug = kernel_url_list[1]

        target_dir = path

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if not os.path.isdir(target_dir):
            raise ValueError("You must specify a directory for the kernels output")

        token = None
        with api.build_kaggle_client() as kaggle:
            request = ApiListKernelSessionOutputRequest()
            request.user_name = owner_slug
            request.kernel_slug = kernel_slug
            response = kaggle.kernels.kernels_api_client.list_kernel_session_output(request)
            token = response.next_page_token

        for item in response.files:
            if item.file_name != "submission.zip":
                continue
            download_response = requests.get(item.url, stream=True)
            if force or api.download_needed(download_response, target, quiet):
                target.parent.mkdir(exist_ok=True)
                with open(target, "wb") as out:
                    out.write(download_response.content)
                if not quiet:
                    print(f"[SAVE] submission.zip -> {target}")
    except Exception as e:
        print(f"[INFO] kernels_output failed or has no outputs for {ref}: {e}")
        return False
    return True

# ---------- メイン ----------
def main():
    ap = argparse.ArgumentParser(description="Kaggle コンペのノートブック（API版） + submission.zip を取得（既存はスキップ）")
    ap.add_argument("-c", "--competition", default=DEFAULT_COMP, help="コンペ slug（例: titanic）")
    ap.add_argument("-o", "--out", default=DEFAULT_OUT, help="保存先ルート（既定: notebooks）")
    ap.add_argument("--page-size", type=int, default=PAGE_SIZE_DEFAULT, help="kernels_list の1ページ件数（最大100）")
    ap.add_argument("--max-pages", type=int, default=MAX_PAGES_DEFAULT, help="最大ページ数（保険）")
    ap.add_argument("--also-submission", action="store_true",
                    help="各Notebookの outputs から submission.zip を取得し Notebook ディレクトリ直下へ配置（既存はスキップ）")
    ap.add_argument("--sleep", type=float, default=SLEEP_BETWEEN_PULLS, help="pull 間スリープ秒（API負荷軽減）")
    args = ap.parse_args()

    api = ensure_kaggle_api()

    root = Path(args.out).resolve()
    root.mkdir(parents=True, exist_ok=True)

    metas = list_kernels_for_competition_api(api, args.competition, page_size=args.page_size, max_pages=args.max_pages)
    if not metas:
        die(f"コンペ '{args.competition}' の公開 Notebook が見つかりませんでした。")

    print(f"[INFO] total kernels: {len(metas)}")

    saved_src = skipped_src = saved_sub = skipped_sub = failed = 0

    for i, meta in enumerate(metas, 1):
        ref = parse_ref_from_meta(meta)
        if not ref:
            print(f"[WARN] meta に ref がありません。スキップ: {meta}")
            continue

        owner = extract_owner(meta, ref)
        slug = extract_slug(meta, ref)
        ver_ts = extract_last_run_ts(meta)

        dest = build_versioned_dir(root, slug, owner, ver_ts)

        if dest.exists():
            print(f"[SKIP] same version exists: {dest}")
            skipped_src += 1
            if args.also_submission:
                try:
                    changed = download_submission_zip_with_api(api, ref, dest, skip_if_exists=True)
                    if changed:
                        saved_sub += 1
                    else:
                        skipped_sub += 1
                except Exception as e:
                    print(f"[ERROR] submission.zip fetch failed for {ref}: {e}", file=sys.stderr)
                    failed += 1
            continue

        print(f"[{i}/{len(metas)}] pull {ref} -> {dest.name}")
        try:
            pull_kernel_with_api(api, ref, dest, with_metadata=True)
            saved_src += 1
            if args.also_submission:
                try:
                    changed = download_submission_zip_with_api(api, ref, dest, skip_if_exists=True)
                    if changed:
                        saved_sub += 1
                    else:
                        skipped_sub += 1
                except Exception as e:
                    print(f"[ERROR] submission.zip fetch failed for {ref}: {e}", file=sys.stderr)
                    failed += 1
        except Exception as e:
            print(f"[ERROR] kernels_pull failed for {ref}: {e}", file=sys.stderr)
            failed += 1

        time.sleep(max(0.0, args.sleep))

    print("\n=== Summary ===")
    print(f"Saved notebooks : {saved_src}")
    print(f"Skipped src     : {skipped_src}")
    if args.also_submission:
        print(f"Saved submission: {saved_sub}")
        print(f"Skipped submit  : {skipped_sub}")
    print(f"Failures        : {failed}")
    print(f"Root directory  : {root}")

if __name__ == "__main__":
    main()
