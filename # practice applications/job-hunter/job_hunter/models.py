"""Shared data types."""
from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field


@dataclass
class Job:
    title: str
    url: str
    company: str
    source: str
    location: str = ""
    posted: str = ""
    description: str = ""
    # Filled in by scoring
    score: int = 0
    track: str = ""
    reasons: list[str] = field(default_factory=list)
    remote: bool = False

    @property
    def id(self) -> str:
        """Stable ID: the job URL without query noise (falls back to title+company)."""
        key = self.url.split("?")[0].rstrip("/").lower() or f"{self.company}|{self.title}".lower()
        return hashlib.sha1(key.encode()).hexdigest()[:12]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["id"] = self.id
        d.pop("description", None)  # keep state files small
        return d


@dataclass
class SourceResult:
    name: str
    type: str
    jobs: list[Job] = field(default_factory=list)
    error: str = ""
    note: str = ""
