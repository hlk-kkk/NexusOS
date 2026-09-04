import subprocess
from dataclasses import dataclass


@dataclass
class ShellTool:
    """Command execution tool used by SWE agents."""

    workspace: str

    def run(self, command: str):
        result = subprocess.run(
            command,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )
        return {
            "code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
