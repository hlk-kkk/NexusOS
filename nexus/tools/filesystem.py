from pathlib import Path


class FileSystemTool:
    """Read and inspect files for Nexus agents."""

    name = "filesystem.read"

    def schema(self):
        return {
            "name": self.name,
            "description": "Read text file content",
            "parameters": {
                "path": "string"
            }
        }

    def execute(self, path: str):
        return Path(path).read_text(encoding="utf-8")
