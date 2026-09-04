from dataclasses import dataclass
from typing import List


@dataclass
class CommandResult:
    command: str
    success: bool
    output: str = ""


class CommandExecutor:
    """Command execution boundary for future sandbox integration."""

    def run(self, command: str) -> CommandResult:
        return CommandResult(
            command=command,
            success=False,
            output="execution backend not configured",
        )
