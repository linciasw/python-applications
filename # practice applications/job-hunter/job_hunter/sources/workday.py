"""Workday career sites (*.myworkdayjobs.com).

Workday sites are JavaScript apps, but they load jobs from a public JSON
endpoint: POST {base}/wday/cxs/{tenant}/{site}/jobs
"""
from __future__ import annotations

from .. import http
from ..models import Job

PAGE_SIZE = 20  # Workday's maximum
MAX_PAGES = 10


def parse(data: dict, cfg: dict) -> list[Job]:
    base, site = cfg["base_url"].rstrip("/"), cfg["site"]
    jobs = []
    for p in data.get("jobPostings", []):
        path = p.get("externalPath", "")
        jobs.append(Job(
            title=p.get("title", "").strip(),
            url=f"{base}/en-US/{site}{path}",
            company=cfg["company"],
            source=cfg["name"],
            location=p.get("locationsText", ""),
            posted=p.get("postedOn", ""),
        ))
    return jobs


def fetch(cfg: dict) -> list[Job]:
    base = cfg["base_url"].rstrip("/")
    endpoint = f"{base}/wday/cxs/{cfg['tenant']}/{cfg['site']}/jobs"
    jobs: dict[str, Job] = {}
    # Open the careers page first, like a browser, so the site sets its cookies.
    try:
        http.get(f"{base}/en-US/{cfg['site']}")
    except Exception:
        pass
    for term in cfg.get("search_terms") or [""]:
        for page in range(MAX_PAGES):
            payload = {"appliedFacets": {}, "limit": PAGE_SIZE,
                       "offset": page * PAGE_SIZE, "searchText": term}
            data = http.post_json(endpoint, payload,
                                  headers={"Referer": f"{base}/en-US/{cfg['site']}", "Origin": base}).json()
            batch = parse(data, cfg)
            for j in batch:
                # Workday's search already matched the location term, so an
                # unhelpful "2 Locations" label still counts as a TT match.
                if term and "location" in j.location.lower():
                    j.location = f"{j.location} ({term})"
                jobs.setdefault(j.id, j)
            if len(batch) < PAGE_SIZE or (page + 1) * PAGE_SIZE >= data.get("total", 0):
                break
    return list(jobs.values())
