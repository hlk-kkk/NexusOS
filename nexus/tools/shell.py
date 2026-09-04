import subprocess


class ShellTool:
    """Execute shell commands through Nexus tool runtime."""

    name = "shell.execute"

    def schema(self):
        return {
            "name": self.name,
            "description": "Execute shell command",
            "parameters": {
                "command": "string"
            }
        }

    def execute(self, command: str):
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "code": result.returncode,
        }
