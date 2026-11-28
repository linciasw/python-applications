"""Decide whether a job fits Lincia's profile and how well."""
from __future__ import annotations

import re
from dataclasses import dataclass

from .models import Job


@dataclass
class Rule:
    regex: re.Pattern
    weight: int
    track: str = ""


class Scorer:
    def __init__(self, profile: dict):
        c = lambda p: re.compile(p, re.I)  # noqa: E731
        self.title_rules = [Rule(c(r["pattern"]), r["weight"], r.get("track", ""))
                            for r in profile["title_keywords"]]
        self.exclude = [c(p) for p in profile.get("exclude_title", [])]
        self.adjust = [Rule(c(r["pattern"]), r["weight"]) for r in profile.get("title_adjust", [])]
        self.skills = [c(rf"\b(?:{s})\b") for s in profile.get("skills", [])]
        self.max_skill_bonus = profile.get("max_skill_bonus", 6)
        loc = profile.get("locations", {})
        self.tt = c("|".join(loc.get("tt_terms", ["trinidad"])))
        self.remote_re = c(r"\bremote\b|work from home|anywhere")
        self.allow_remote = loc.get("allow_remote", True)
        self.remote_penalty = loc.get("remote_penalty", -1)
        self.min_score = profile.get("min_score", 5)

    def location_ok(self, job: Job, mode: str) -> bool:
        """mode 'tt': source is local, keep everything. mode 'filter': must be TT or remote."""
        text = f"{job.location} {job.title}"
        job.remote = bool(self.remote_re.search(text))
        if mode == "tt" or self.tt.search(text):
            return True
        return self.allow_remote and job.remote

    def score(self, job: Job) -> int:
        """Sets job.score / job.track / job.reasons. Returns the score (0 = not ICT)."""
        title = job.title
        hits = [r for r in self.title_rules if r.regex.search(title)]
        if not hits:
            job.score, job.reasons = 0, ["not an ICT title"]
            return 0
        best = max(hits, key=lambda r: r.weight)
        if any(x.search(title) for x in self.exclude) and best.weight < 8:
            job.score, job.reasons = 0, ["non-ICT role"]
            return 0

        score = best.weight
        reasons = [f"title: {best.regex.search(title).group(0)}"]
        # Small bonus for each extra, different ICT keyword in the title.
        extra = {r.track for r in hits if r is not best}
        if extra:
            score += 1
        for r in self.adjust:
            if r.regex.search(title):
                score += r.weight
                reasons.append(f"{'+' if r.weight > 0 else ''}{r.weight} {r.regex.search(title).group(0)}")
        if job.description:
            found = [s.pattern for s in self.skills if s.search(job.description)]
            bonus = min(len(found), self.max_skill_bonus)
            if bonus:
                score += bonus
                reasons.append(f"+{bonus} skills")
        if job.remote and not self.tt.search(f"{job.location} {job.title}"):
            score += self.remote_penalty
            reasons.append("remote")
        job.score, job.track, job.reasons = score, best.track, reasons
        return score

    def keep(self, job: Job, mode: str) -> bool:
        return self.location_ok(job, mode) and self.score(job) >= self.min_score
