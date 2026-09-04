from typing import Dict, Callable


class ToolRegistry:
    """Dynamic MCP tool registry."""

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, tool: Callable):
        self._tools[name] = tool

    def get(self, name: str):
        return self._tools.get(name)

    def list_tools(self):
        return list(self._tools.keys())
