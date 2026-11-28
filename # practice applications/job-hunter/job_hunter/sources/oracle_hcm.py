"""Oracle Recruiting Cloud sites (fa-*.oraclecloud.com/hcmUI/CandidateExperience/...).

The candidate site reads from a public REST endpoint:
GET {base}/hcmRestApi/resources/latest/recruitingCEJobRequisitions?finder=findReqs;siteNumber=...
"""
from __future__ import annotations

from .. import http
from ..models import Job

PAGE_SIZE = 25
MAX_PAGES = 10


def parse(data: dict, cfg: dict) -> tuple[list[Job], int]:
    base, site = cfg["base_url"].rstrip("/"), cfg["site_number"]
    items = data.get("items") or [{}]
    block = items[0]
    jobs = []
    for r in block.get("requisitionList", []) or []:
        loc = r.get("PrimaryLocation", "") or ""
        extra = [s.get("Name", "") for s in (r.get("secondaryLocations") or [])]
        if extra:
            loc = "; ".join([loc, *extra])
        jobs.append(Job(
            title=(r.get("Title") or "").strip(),
            url=f"{base}/hcmUI/CandidateExperience/en/sites/{site}/job/{r.get('Id')}",
            company=cfg["company"],
            source=cfg["name"],
            location=loc,
            posted=(r.get("PostedDate") or "")[:10],
            description=r.get("ShortDescriptionStr") or "",
        ))
    return jobs, int(block.get("TotalJobsCount") or 0)


def fetch(cfg: dict) -> list[Job]:
    base, site = cfg["base_url"].rstrip("/"), cfg["site_number"]
    out: list[Job] = []
    for page in range(MAX_PAGES):
        finder = (f"findReqs;siteNumber={site},limit={PAGE_SIZE},offset={page * PAGE_SIZE},"
                  "sortBy=POSTING_DATES_DESC")
        url = (f"{base}/hcmRestApi/resources/latest/recruitingCEJobRequisitions"
               f"?onlyData=true&expand=requisitionList.secondaryLocations&finder={finder}")
        jobs, total = parse(http.get(url, headers={"Accept": "application/json"}).json(), cfg)
        out.extend(jobs)
        if not jobs or len(out) >= total:
            break
    return out
