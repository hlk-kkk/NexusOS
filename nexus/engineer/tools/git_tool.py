from dataclasses import dataclass


@dataclass
class GitTool:
    """Git operation abstraction for autonomous agents."""

    workspace: str

    def status(self):
        from subprocess import run
        result = run(
            ["git", "status", "--short"],
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )
        return result.stdout

    def diff(self):
        from subprocess import run
        result = run(
            ["git", "diff"],
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )
        return result.stdout
