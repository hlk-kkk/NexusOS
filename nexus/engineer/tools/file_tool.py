from dataclasses import dataclass


@dataclass
class FileTool:
    """Repository file access abstraction for SWE agents."""

    workspace: str

    def read(self, path: str) -> str:
        with open(f"{self.workspace}/{path}", "r", encoding="utf-8") as f:
            return f.read()

    def write(self, path: str, content: str):
        with open(f"{self.workspace}/{path}", "w", encoding="utf-8") as f:
            f.write(content)
