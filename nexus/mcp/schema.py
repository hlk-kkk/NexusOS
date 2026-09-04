from dataclasses import dataclass


@dataclass
class ToolSchema:
    name: str
    description: str
    parameters: dict
