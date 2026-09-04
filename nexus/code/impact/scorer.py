from dataclasses import dataclass


@dataclass
class RiskScorer:
    """Simple risk scoring foundation for blast radius analysis."""

    def score(self, changed_files: int, affected_nodes: int) -> int:
        score = changed_files * 10 + affected_nodes * 5
        return min(score, 100)
