import subprocess


class GitTool:
    """Git operations exposed to Nexus agents."""

    name = "git.execute"

    def schema(self):
        return {
            "name": self.name,
            "description": "Execute git command",
            "parameters": {
                "command": "string"
            }
        }

    def execute(self, command: str):
        result = subprocess.run(
            ["git"] + command.split(),
            capture_output=True,
            text=True,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "code": result.returncode,
        }
