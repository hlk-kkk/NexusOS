from dataclasses import dataclass, field
from typing import List


@dataclass
class ImpactRadius:
    target: str
    affected_nodes: List[str] = field(default_factory=list)

    def add(self, node: str):
        if node not in self.affected_nodes:
            self.affected_nodes.append(node)

    @property
    def size(self) -> int:
        return len(self.affected_nodes)
