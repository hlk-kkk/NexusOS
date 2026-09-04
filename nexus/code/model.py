from dataclasses import dataclass, field


@dataclass
class CodeSymbol:
    name: str
    kind: str
    file: str
    metadata: dict = field(default_factory=dict)


@dataclass
class CodeRelation:
    source: str
    target: str
    relation: str

