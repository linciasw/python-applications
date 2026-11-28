"""iCIMS career sites (careers-<company>.icims.com)."""
from __future__ import annotations

import re
from urllib.parse import quote_plus, urljoin

from bs4 import BeautifulSoup

from .. import http
from ..models import Job

MAX_PAGES = 5
JOB_LINK = re.compile(r"/jobs/\d+/[^/]+/job")


def parse(html: str, cfg: dict) -> list[Job]:
    soup = BeautifulSoup(html, "html.parser")
    base = cfg["base_url"].rstrip("/") + "/"
    jobs, seen = [], set()
    for a in soup.find_all("a", href=JOB_LINK):
        url = urljoin(base, a["href"]).split("?")[0]
        if url in seen:
            continue
        title = a.get_text(" ", strip=True)
        title = re.sub(r"^(Job )?Title\s*", "", title).strip()
        if not title:
            continue
        seen.add(url)
        row = a.find_parent(class_=re.compile(r"iCIMS_JobsTable|row|listing", re.I)) or a.parent
        row_text = row.get_text(" ", strip=True) if row else ""
        m = re.search(r"\b([A-Z]{2}-[A-Za-z .'-]+)", row_text)
        jobs.append(Job(title=title, url=url, company=cfg["company"], source=cfg["name"],
                        location=m.group(1).strip() if m else row_text[:120]))
    return jobs


def fetch(cfg: dict) -> list[Job]:
    base = cfg["base_url"].rstrip("/")
    out: dict[str, Job] = {}
    for term in cfg.get("search_terms") or [""]:
        for page in range(MAX_PAGES):
            url = (f"{base}/jobs/search?ss=1&searchKeyword={quote_plus(term)}"
                   f"&pr={page}")
            jobs = parse(http.get(url).text, cfg)
            new = [j for j in jobs if j.id not in out]
            for j in new:
                # The keyword search already matched e.g. "Trinidad".
                if term and term.lower() not in j.location.lower():
                    j.location = f"{j.location} ({term})".strip()
                out[j.id] = j
            if not new:
                break
    return list(out.values())
