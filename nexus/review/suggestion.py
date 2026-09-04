from dataclasses import dataclass


@dataclass
class ReviewSuggestion:
    issue: str
    suggestion: str
    confidence: float = 0.0


class SuggestionGenerator:
    """Generate remediation suggestions from detected issues."""

    def generate(self, issue):
        return ReviewSuggestion(
            issue=issue.title,
            suggestion=f"Review {issue.title} and validate the affected execution path.",
            confidence=0.5,
        )
