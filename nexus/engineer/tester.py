from dataclasses import dataclass


@dataclass
class TestResult:
    command: str
    success: bool
    output: str = ""


class TestAgent:
    """Runs and records validation results."""

    def validate(self, command: str) -> TestResult:
        return TestResult(
            command=command,
            success=False,
            output="not executed"
        )
