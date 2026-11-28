"""One polite HTTP session shared by every source."""
from __future__ import annotations

import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36 job-hunter/0.1 (personal use)"
)
TIMEOUT = 30
DELAY_SECONDS = 1.0  # pause between requests to the same site

_session: requests.Session | None = None


def session() -> requests.Session:
    global _session
    if _session is None:
        s = requests.Session()
        s.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})
        retry = Retry(total=2, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504],
                      allowed_methods=["GET", "POST"], raise_on_status=False)
        s.mount("https://", HTTPAdapter(max_retries=retry))
        s.mount("http://", HTTPAdapter(max_retries=retry))
        _session = s
    return _session


def get(url: str, **kw) -> requests.Response:
    time.sleep(DELAY_SECONDS)
    r = session().get(url, timeout=TIMEOUT, **kw)
    r.raise_for_status()
    return r


def post_json(url: str, payload: dict, **kw) -> requests.Response:
    time.sleep(DELAY_SECONDS)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    headers.update(kw.pop("headers", {}))
    r = session().post(url, json=payload, headers=headers, timeout=TIMEOUT, **kw)
    r.raise_for_status()
    return r
