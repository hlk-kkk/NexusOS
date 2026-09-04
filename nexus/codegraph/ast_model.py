from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class CodeNode:
    name: str
    kind: str
    file: str = ""
    metadata: Dict = field(default_factory=dict)


@dataclass
class CodeEdge:
    source: str
    target: str
    relation: str


@dataclass
class ASTRepository:
    nodes: List[CodeNode] = field(default_factory=list)
    edges: List[CodeEdge] = field(default_factory=list)
