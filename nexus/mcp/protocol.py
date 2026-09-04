from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ToolRequest:
    name: str
    arguments: Dict[str, Any]


@dataclass
class ToolResponse:
    success: bool
    result: Any = None
    error: str | None = None
