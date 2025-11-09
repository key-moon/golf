#!/usr/bin/env python3
"""Simple concurrent exporter: fetch a fixed set of GET URLs and save raw responses.

Saves responses as:
 - / -> index.html
 - /tasks -> tasks.html
 - /tasks/<n> -> tasks/taskNNN.html

Does not parse or rewrite HTML. Meant for quickly snapshotting a running webapp.

Usage:
    python3 scripts/export_static_simple.py --base http://127.0.0.1:5000 --out out_static --concurrency 16
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request as _urllib
_requests = None
try:
        import requests as _requests
        HAS_REQUESTS = True
except Exception:
        HAS_REQUESTS = False


def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def url_to_path(path: str, outdir: Path) -> Path:
    # path begins with /
    if path == '/' or path == '':
        return outdir / 'index.html'
    if path == '/tasks' or path == 'tasks':
        return outdir / 'tasks.html'
    parts = path.strip('/').split('/')
    if parts[0] == 'tasks' and len(parts) == 2 and parts[1].isdigit():
        idx = int(parts[1])
        return outdir / 'tasks' / f'task{idx:03}.html'
    # fallback
    safe = path.strip('/').replace('/', '_') or 'index'
    return outdir / f"{safe}.html"


def write_out(p: Path, status: int | None, text: str) -> None:
    meta = f"<!-- status: {status} -->\n"
    p.write_text(meta + text, encoding='utf-8')


def fetch_requests(session, url: str, timeout: float):
    try:
        r = session.get(url, timeout=timeout)
        return r.status_code, r.text
    except Exception as e:
        return None, str(e)


def fetch_urllib(url: str, timeout: float):
    try:
        req = _urllib.Request(url, headers={"User-Agent": "export_static_simple/1.0"})
        with _urllib.urlopen(req, timeout=timeout) as r:
            data = r.read()
            try:
                text = data.decode('utf-8')
            except Exception:
                text = data.decode('latin1', errors='replace')
            status = getattr(r, 'status', 200)
            return status, text
    except Exception as e:
        return None, str(e)


def worker(base: str, path: str, outdir: Path, session=None, timeout: float = 8.0, retries: int = 2):
    full = base.rstrip('/') + path
    outpath = url_to_path(path, outdir)
    safe_mkdir(outpath.parent)
    last_err = None
    for attempt in range(retries + 1):
        if HAS_REQUESTS:
            status, text = fetch_requests(session, full, timeout)
        else:
            status, text = fetch_urllib(full, timeout)
        if status is None:
            last_err = text
            time.sleep(0.2)
            continue
        try:
            write_out(outpath, status, text)
            return True, status
        except Exception as e:
            last_err = str(e)
            time.sleep(0.1)
    # failed
    (outpath.parent / (outpath.name + '.error.txt')).write_text(f'failed to fetch {full}: {last_err}\n', encoding='utf-8')
    return False, last_err


def make_targets():
    paths = [
        '/', '/tasks', '/judge',
        '/api/tasks/thumbs',
        '/api/tasks/thumbs_with_out',
        '/api/teams', '/api/team_lengths',
        '/api/recent_our_updates', '/api/recent_best_updates',
        '/api/team_last_time', '/api/judge/outputs', '/api/summary', '/api/tags'
      ]
    for i in range(1, 401):
        paths.append(f'/tasks/{i}')
        paths.append(f'/tasks/{i}/cases')
        paths.append(f'/dist/task{i:03}.py')
        paths.append(f'/api/tags/{i}')
        paths.append(f'/api/task/{i}/data')
        paths.append(f'/api/task/{i}/progress')
        paths.append(f'/api/task/{i}/code_summary')
    return paths


def main(argv: list[str] | None = None):
    p = argparse.ArgumentParser()
    p.add_argument('--base', '-b', default='http://127.0.0.1:5000', help='Base URL for the running webapp')
    p.add_argument('--out', '-o', default='static_export', help='Output directory')
    p.add_argument('--concurrency', '-c', type=int, default=12, help='Concurrent workers')
    p.add_argument('--retries', type=int, default=2, help='Retries per URL')
    p.add_argument('--timeout', type=float, default=8.0, help='Request timeout (s)')
    args = p.parse_args(argv)

    base = args.base
    outdir = Path(args.out)
    safe_mkdir(outdir)

    targets = make_targets()
    total = len(targets)
    print(f'Exporting {total} pages from {base} -> {outdir} (concurrency={args.concurrency})')

    session = None
    if HAS_REQUESTS and _requests is not None:
        session = _requests.Session()
        session.headers.update({'User-Agent': 'export_static_simple/1.0'})

    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {ex.submit(worker, base, t, outdir, session, args.timeout, args.retries): t for t in targets}
        done = 0
        for fut in as_completed(futures):
            path = futures[fut]
            try:
                ok, status = fut.result()
                done += 1
                print(f'[{done}/{total}] {path} -> {"OK" if ok else "FAIL"} ({status})')
            except Exception as e:
                done += 1
                print(f'[{done}/{total}] {path} -> EXCEPTION ({e})')

    if HAS_REQUESTS and session:
        session.close()
    print('Done')


if __name__ == '__main__':
    main()
