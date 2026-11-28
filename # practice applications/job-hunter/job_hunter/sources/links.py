"""Generic sources.

links       - every job on the page is an <a> whose absolute URL matches `link_regex`.
page_watch  - unstructured careers pages: report links that look like vacancies
              (PDF adverts, "vacancy"/"career opportunity" posts, ICT job titles).
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .. import http
from ..models import Job

VACANCY_HINT = re.compile(
    r"vacanc|career[- ]opportunit|position|job|recruit|hiring|apply|\.pdf$|"
    r"analyst|developer|engineer|officer|specialist|manager|technician|administrator",
    re.I,
)
NAV_JUNK = re.compile(
    r"^(home|about|contact|login|log in|sign in|register|privacy|terms|search|apply now|"
    r"read more|learn more|view all|more|careers?|jobs?|next|previous|\d+)$",
    re.I,
)


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _caribbeanjobs_title(a) -> str:
    # Result cards put the title in the link; company/location sit nearby.
    return _clean(a.get("title") or a.get_text(" "))


def _context(a) -> str:
    """Text of the nearest card-like parent (used to find company/location)."""
    node = a
    for _ in range(4):
        node = node.parent
        if node is None:
            return ""
        text = _clean(node.get_text(" "))
        if len(text) > len(_clean(a.get_text(" "))) + 20:
            return text[:400]
    return ""


def parse_links(html: str, page_url: str, cfg: dict) -> list[Job]:
    soup = BeautifulSoup(html, "html.parser")
    pattern = re.compile(cfg["link_regex"], re.I)
    jobs: dict[str, Job] = {}
    for a in soup.find_all("a", href=True):
        url = urljoin(page_url, a["href"]).split("#")[0]
        if not pattern.search(url):
            continue
        title = _caribbeanjobs_title(a) if cfg.get("title_from") == "caribbeanjobs" else _clean(a.get_text(" "))
        if not title or NAV_JUNK.match(title):
            continue
        job = Job(title=title, url=url, company=cfg.get("company", ""), source=cfg["name"],
                  location=_context(a))
        # Keep the longest title seen for the same URL (cards often repeat links).
        if job.id not in jobs or len(title) > len(jobs[job.id].title):
            jobs[job.id] = job
    return list(jobs.values())


def parse_page_watch(html: str, page_url: str, cfg: dict) -> list[Job]:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select("nav, header, footer, script, style"):
        tag.decompose()
    jobs: dict[str, Job] = {}
    for a in soup.find_all("a", href=True):
        url = urljoin(page_url, a["href"]).split("#")[0]
        title = _clean(a.get_text(" ")) or url.rsplit("/", 1)[-1]
        if url.rstrip("/") == page_url.rstrip("/") or url.startswith(("mailto:", "tel:", "javascript:")):
            continue
        if NAV_JUNK.match(title) or len(title) < 4:
            continue
        if not (VACANCY_HINT.search(title) or VACANCY_HINT.search(url)):
            continue
        job = Job(title=title, url=url, company=cfg.get("company", ""), source=cfg["name"],
                  location=_context(a))
        jobs.setdefault(job.id, job)
    return list(jobs.values())


def fetch_links(cfg: dict) -> list[Job]:
    out: dict[str, Job] = {}
    for url in cfg["urls"]:
        for j in parse_links(http.get(url).text, url, cfg):
            out.setdefault(j.id, j)
    return list(out.values())


def fetch_page_watch(cfg: dict) -> list[Job]:
    out: dict[str, Job] = {}
    for url in cfg["urls"]:
        for j in parse_page_watch(http.get(url).text, url, cfg):
            out.setdefault(j.id, j)
    return list(out.values())
