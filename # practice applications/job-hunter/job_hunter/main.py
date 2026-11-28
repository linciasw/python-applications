"""Run every source, score the jobs, update state and write the reports.

Usage (from the job-hunter folder):
    python -m job_hunter.main                 # full run
    python -m job_hunter.main --only Shell    # just one source (name contains "Shell")
    python -m job_hunter.main --dry-run       # don't save state
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import traceback
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml

from .models import SourceResult
from .report import digest, write_csv, write_latest, write_sources
from .scoring import Scorer
from .sources import FETCHERS

ROOT = Path(__file__).resolve().parent.parent
TT_TZ = timezone(timedelta(hours=-4))  # Trinidad & Tobago, no DST


def load_yaml(name: str) -> dict:
    return yaml.safe_load((ROOT / "config" / name).read_text(encoding="utf-8"))


def run(only: str = "", dry_run: bool = False) -> int:
    profile = load_yaml("profile.yaml")
    sources = [s for s in load_yaml("sources.yaml")["sources"] if s.get("enabled", True)]
    if only:
        sources = [s for s in sources if only.lower() in s["name"].lower()]
    scorer = Scorer(profile)
    today = datetime.now(TT_TZ).date().isoformat()

    state_path = ROOT / "data" / "state.json"
    state: dict = json.loads(state_path.read_text()) if state_path.exists() else {}

    results: list[SourceResult] = []
    manual = [s for s in sources if s["type"] == "manual"]
    matched: dict[str, dict] = {}

    for src in sources:
        if src["type"] == "manual":
            continue
        res = SourceResult(name=src["name"], type=src["type"])
        try:
            res.jobs = FETCHERS[src["type"]](src)
        except Exception as e:  # one broken site must not stop the run
            res.error = f"{type(e).__name__}: {e}"
            traceback.print_exc()
        kept = [j for j in res.jobs if scorer.keep(j, src.get("location", "filter"))]
        res.note = str(len(kept))
        for j in kept:
            matched.setdefault(j.id, j.to_dict())
        results.append(res)
        print(f"[{'ERR' if res.error else ' ok'}] {src['name']}: {len(res.jobs)} read, {len(kept)} matched"
              + (f" — {res.error}" if res.error else ""), flush=True)

    # Sources that failed today shouldn't make their jobs look closed.
    failed = {r.name for r in results if r.error}
    ran = {r.name for r in results}
    new_jobs = []
    for jid, j in matched.items():
        if jid in state:
            j["first_seen"] = state[jid]["first_seen"]
        else:
            j["first_seen"] = today
            new_jobs.append(j)
        j["last_seen"] = today
        state[jid] = j
    for j in state.values():
        if (j["source"] in failed or j["source"] not in ran) and j["last_seen"] != today:
            j["last_seen"] = today  # carry forward

    open_jobs = sorted((j for j in state.values() if j["last_seen"] == today),
                       key=lambda j: -j["score"])
    new_jobs.sort(key=lambda j: -j["score"])

    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    resumes = profile.get("resumes", {})
    write_latest(out / "latest.md", open_jobs, today, resumes)
    write_csv(out / "jobs.csv", state)
    write_sources(out / "sources.md", results, manual, today)
    repo = os.environ.get("GITHUB_REPOSITORY")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    link = (f"https://github.com/{repo}/blob/{branch}/%23%20practice%20applications/job-hunter/results/latest.md"
            if repo else "")
    (out / "digest.md").write_text(digest(new_jobs, results, manual, resumes, today, link), encoding="utf-8")
    (out / "new_count.txt").write_text(str(len(new_jobs)))

    if not dry_run:
        state_path.parent.mkdir(exist_ok=True)
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
    print(f"\n{len(open_jobs)} open matches, {len(new_jobs)} new, {len(failed)} source(s) failed.")
    return 0


def cli() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--only", default="", help="run only sources whose name contains this text")
    p.add_argument("--dry-run", action="store_true", help="don't save data/state.json")
    a = p.parse_args()
    sys.exit(run(a.only, a.dry_run))


if __name__ == "__main__":
    cli()
