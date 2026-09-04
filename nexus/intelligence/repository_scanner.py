from pathlib import Path


class RepositoryScanner:
    """Scan repository structure and collect source metadata."""

    def scan(self, root: str):
        path = Path(root)
        files = [str(p) for p in path.rglob('*') if p.is_file()]
        return {
            "root": str(path),
            "file_count": len(files),
            "files": files,
        }
