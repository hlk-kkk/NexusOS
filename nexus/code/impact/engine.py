"""Blast radius analysis engine."""

from dataclasses import dataclass


@dataclass
class BlastRadiusResult:
    target: str
    affected: list
    risk_score: int


class BlastRadiusEngine:
    def __init__(self, dependency_analyzer=None, scorer=None):
        self.dependency_analyzer = dependency_analyzer
        self.scorer = scorer

    def analyze(self, target: str):
        affected = []
        if self.dependency_analyzer:
            affected = self.dependency_analyzer.affected_by(target)
        score = 0
        if self.scorer:
            score = self.scorer.score(affected)
        return BlastRadiusResult(target, affected, score)
