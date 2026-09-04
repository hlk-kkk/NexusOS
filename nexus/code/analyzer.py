from pathlib import Path

from .model import CodeSymbol


class RepositoryAnalyzer:
    """Initial repository analyzer abstraction."""

    def scan(self, path):
        symbols = []
        for file in Path(path).rglob("*.py"):
            symbols.append(
                CodeSymbol(
                    name=file.stem,
                    kind="file",
                    file=str(file),
                )
            )
        return symbols
