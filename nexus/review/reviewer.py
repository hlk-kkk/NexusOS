from .issue_detector import IssueDetector
from .suggestion import SuggestionGenerator


class ReviewPipeline:
    """Connect code intelligence results with review generation."""

    def __init__(self):
        self.detector = IssueDetector()
        self.suggestion = SuggestionGenerator()

    def review(self, context: dict):
        issues = self.detector.detect(context)
        return {
            "issues": [
                {
                    "severity": issue.severity,
                    "title": issue.title,
                    "message": issue.message,
                    "suggestion": self.suggestion.generate(issue).__dict__,
                }
                for issue in issues
            ]
        }
