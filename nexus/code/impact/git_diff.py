"""Git diff analysis primitives for NexusOS blast radius engine."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ChangedFile:
    path: str
    additions: int = 0
    deletions: int = 0


class GitDiffAnalyzer:
    def analyze(self, files: List[ChangedFile]):
        return {
            "files": files,
            "changed_count": len(files),
            "lines_changed": sum(f.additions + f.deletions for f in files),
        }
