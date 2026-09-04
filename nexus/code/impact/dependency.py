"""Dependency impact calculation primitives."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class DependencyNode:
    name: str
    dependents: List[str] = field(default_factory=list)


class DependencyAnalyzer:
    def __init__(self):
        self.nodes: Dict[str, DependencyNode] = {}

    def add_dependency(self, source: str, target: str):
        node = self.nodes.setdefault(target, DependencyNode(target))
        node.dependents.append(source)

    def affected_by(self, symbol: str):
        return self.nodes.get(symbol, DependencyNode(symbol)).dependents
