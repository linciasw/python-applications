"""Write the results files and the daily digest (GitHub Issue body)."""
from __future__ import annotations

import csv
from pathlib import Path

from .models import SourceResult

TRACK_LABEL = {"software": "Software", "data": "Data", "automation": "Automation / IT"}
MAX_IN_DIGEST = 40


def _line(j: dict, resumes: dict, new: bool) -> str:
    badge = "🆕 " if new else ""
    bits = [j["company"] or j["source"]]
    if j.get("location") and len(j["location"]) < 60:
        bits.append(j["location"])
    if j.get("posted"):
        bits.append(j["posted"])
    if j.get("remote"):
        bits.append("remote")
    resume = resumes.get(j.get("track", ""), "")
    resume_txt = f" · resume: *{TRACK_LABEL.get(j.get('track'), j.get('track'))}*" if resume else ""
    return (f"- {badge}**[{j['title']}]({j['url']})** — {' · '.join(bits)}  \n"
            f"  score {j['score']}{resume_txt}")


def write_latest(path: Path, open_jobs: list[dict], today: str, resumes: dict) -> None:
    lines = [f"# Open ICT jobs — {today}", "",
             f"{len(open_jobs)} matching jobs open right now, best first. 🆕 = first seen today.", ""]
    for track in ("software", "data", "automation"):
        group = [j for j in open_jobs if j.get("track") == track]
        if not group:
            continue
        lines += [f"## {TRACK_LABEL[track]} ({len(group)})", ""]
        lines += [_line(j, resumes, j["first_seen"] == today) for j in group]
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(path: Path, state: dict) -> None:
    cols = ["first_seen", "last_seen", "score", "track", "title", "company", "location",
            "posted", "remote", "source", "url", "id"]
    rows = sorted(state.values(), key=lambda j: (j["last_seen"], j["score"]), reverse=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_sources(path: Path, results: list[SourceResult], manual: list[dict], today: str) -> None:
    lines = [f"# Source status — {today}", "",
             "| Source | Type | Jobs read | Matches | Status |", "|---|---|---|---|---|"]
    for r in results:
        status = f"❌ {r.error[:120]}" if r.error else "✅"
        lines.append(f"| {r.name} | {r.type} | {len(r.jobs)} | {r.note or 0} | {status} |")
    if manual:
        lines += ["", "## Check these by hand", ""]
        lines += [f"- [{m['name']}]({m['url']}) — {m.get('why', '')}" for m in manual]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def digest(new_jobs: list[dict], results: list[SourceResult], manual: list[dict],
           resumes: dict, today: str, repo_url: str = "") -> str:
    lines = [f"**{len(new_jobs)} new ICT job(s) found** on {today}.", ""]
    for j in new_jobs[:MAX_IN_DIGEST]:
        lines.append(_line(j, resumes, new=False))
    if len(new_jobs) > MAX_IN_DIGEST:
        lines.append(f"\n…and {len(new_jobs) - MAX_IN_DIGEST} more in `results/latest.md`.")
    broken = [r for r in results if r.error]
    if broken:
        lines += ["", "<details><summary>⚠️ Sources that failed today</summary>", ""]
        lines += [f"- {r.name}: {r.error[:150]}" for r in broken]
        lines += ["", "</details>"]
    if manual:
        lines += ["", "<details><summary>Check these by hand</summary>", ""]
        lines += [f"- [{m['name']}]({m['url']})" for m in manual]
        lines += ["", "</details>"]
    if repo_url:
        lines += ["", f"Full list: {repo_url}"]
    return "\n".join(lines) + "\n"
