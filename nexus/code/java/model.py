from dataclasses import dataclass, field
from typing import List


@dataclass
class JavaClass:
    name: str
    package: str = ""
    methods: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)


@dataclass
class JavaMethod:
    class_name: str
    name: str
    calls: List[str] = field(default_factory=list)
