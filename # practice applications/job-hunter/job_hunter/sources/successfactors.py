"""SAP SuccessFactors Career Site Builder sites.

These are the careers.<company>.com sites with /go/<Category>/<id>/ and
/search/ pages. The search page is plain HTML with one <tr class="data-row">
per job.
"""
from __future__ import annotations

import re
from urllib.parse import quote_plus, urljoin

from bs4 import BeautifulSoup

from .. import http
from ..models import Job

PAGE_SIZE = 25
MAX_PAGES = 12


def parse(html: str, cfg: dict) -> tuple[list[Job], int]:
    soup = BeautifulSoup(html, "html.parser")
    base = cfg["base_url"].rstrip("/") + "/"
    jobs, seen = [], set()
    rows = soup.select("tr.data-row") or soup.select("li.job-tile, div.job-tile")
    for row in rows:
        a = row.select_one("a.jobTitle-link") or row.find("a", href=re.compile(r"/job/"))
        if not a or not a.get("href"):
            continue
        url = urljoin(base, a["href"])
        if url in seen:
            continue
        seen.add(url)
        loc = row.select_one(".jobLocation, [class*=location]")
        date = row.select_one(".jobDate, [class*=date]")
        jobs.append(Job(
            title=a.get_text(" ", strip=True),
            url=url,
            company=cfg["company"],
            source=cfg["name"],
            location=loc.get_text(" ", strip=True) if loc else "",
            posted=date.get_text(" ", strip=True) if date else "",
        ))
    # Fallback for page templates without table rows: any /job/ link.
    if not jobs:
        for a in soup.find_all("a", href=re.compile(r"/job/[^/]+/\d+/?")):
            url = urljoin(base, a["href"])
            title = a.get_text(" ", strip=True)
            if url not in seen and title:
                seen.add(url)
                jobs.append(Job(title=title, url=url, company=cfg["company"], source=cfg["name"]))
    total = 0
    label = soup.select_one(".paginationLabel")
    if label:
        m = re.search(r"of\s+([\d,]+)", label.get_text(" ", strip=True))
        if m:
            total = int(m.group(1).replace(",", ""))
    return jobs, total


def fetch(cfg: dict) -> list[Job]:
    base = cfg["base_url"].rstrip("/")
    loc = quote_plus(cfg.get("location_search", ""))
    q = quote_plus(cfg.get("query", ""))
    out: dict[str, Job] = {}
    for page in range(MAX_PAGES):
        url = (f"{base}/search/?q={q}&locationsearch={loc}&sortColumn=referencedate"
               f"&sortDirection=desc&startrow={page * PAGE_SIZE}")
        jobs, total = parse(http.get(url).text, cfg)
        new = [j for j in jobs if j.id not in out]
        for j in new:
            out[j.id] = j
        if not new or len(jobs) < PAGE_SIZE or (total and len(out) >= total):
            break
    return list(out.values())
