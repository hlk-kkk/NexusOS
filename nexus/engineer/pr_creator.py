from dataclasses import dataclass


@dataclass
class PullRequestDraft:
    title: str
    body: str
    branch: str


class PRCreator:
    """Create pull request drafts after automated fixes."""

    def create(self, title: str, body: str, branch: str) -> PullRequestDraft:
        return PullRequestDraft(
            title=title,
            body=body,
            branch=branch,
        )
