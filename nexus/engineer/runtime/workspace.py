from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Workspace:
    """Repository workspace abstraction for agent execution."""

    root: str
    metadata: Dict[str, str] = field(default_factory=dict)

    def describe(self):
        return {
            "root": self.root,
            "metadata": self.metadata,
        }
