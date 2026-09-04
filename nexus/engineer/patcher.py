from dataclasses import dataclass
from typing import List


@dataclass
class Patch:
    file: str
    changes: str
    confidence: float = 0.0


class PatchGenerator:
    """Generate code patch proposals from engineering plans."""

    def generate(self, plan: dict) -> List[Patch]:
        files = plan.get("files", [])
        return [
            Patch(
                file=f,
                changes="Generated patch proposal pending execution",
                confidence=0.5,
            )
            for f in files
        ]
