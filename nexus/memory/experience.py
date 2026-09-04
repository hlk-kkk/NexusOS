from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class Experience:
    """A reusable memory record produced by an agent execution."""

    task: str
    steps: list[str] = field(default_factory=list)
    result: Any = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class ExperienceStore:
    def __init__(self):
        self.items: list[Experience] = []

    def save(self, experience: Experience):
        self.items.append(experience)

    def all(self):
        return self.items
