import re
from pathlib import Path

from .model import JavaClass


class JavaParser:
    """Lightweight Java source parser foundation.

    The first version extracts classes and methods using regex.
    It will later be replaced/extended with Java AST parsing.
    """

    CLASS_PATTERN = re.compile(r"class\s+(\w+)")
    METHOD_PATTERN = re.compile(r"(?:public|private|protected)?\s*\w+\s+(\w+)\s*\(")

    def parse_file(self, path: str) -> JavaClass | None:
        content = Path(path).read_text(encoding="utf-8")
        match = self.CLASS_PATTERN.search(content)
        if not match:
            return None

        methods = self.METHOD_PATTERN.findall(content)
        return JavaClass(name=match.group(1), methods=methods)

    def parse_repository(self, root: str):
        result = []
        for file in Path(root).rglob("*.java"):
            parsed = self.parse_file(str(file))
            if parsed:
                result.append(parsed)
        return result
