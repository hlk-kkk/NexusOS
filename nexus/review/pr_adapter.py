from dataclasses import dataclass


@dataclass
class PullRequestContext:
    number: int
    title: str
    changed_files: list


class PRAdapter:
    def build_context(self, number, title, changed_files):
        return PullRequestContext(
            number=number,
            title=title,
            changed_files=changed_files,
        )
