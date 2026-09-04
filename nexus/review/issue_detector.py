from dataclasses import dataclass
from typing import List


@dataclass
class ReviewIssue:
    severity: str
    title: str
    message: str
    file: str | None = None
    line: int | None = None


class IssueDetector:
    """First-stage rule based issue detector.

    Designed to be extended with LLM and static analysis providers.
    """

    def detect(self, context: dict) -> List[ReviewIssue]:
        issues = []
        for finding in context.get("findings", []):
            issues.append(
                ReviewIssue(
                    severity=finding.get("severity", "medium"),
                    title=finding.get("title", "Code risk"),
                    message=finding.get("message", "Potential issue detected"),
                    file=finding.get("file"),
                    line=finding.get("line"),
                )
            )
        return issues
