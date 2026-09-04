from dataclasses import dataclass, field


@dataclass
class ReviewResult:
    issues: list = field(default_factory=list)
    risk_score: int = 0


class ReviewAgent:
    """Coordinates code intelligence and review generation."""

    def __init__(self, analyzer=None, memory=None):
        self.analyzer = analyzer
        self.memory = memory

    def review(self, context):
        issues = []

        if self.analyzer:
            issues = self.analyzer.analyze(context)

        return ReviewResult(
            issues=issues,
            risk_score=min(100, len(issues) * 20),
        )
