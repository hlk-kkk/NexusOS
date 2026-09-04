from typing import Dict


class ToolRegistry:
    """Registry for MCP tools."""

    def __init__(self):
        self._tools: Dict[str, object] = {}

    def register(self, tool):
        self._tools[tool.name] = tool

    def get(self, name):
        return self._tools.get(name)

    def list_tools(self):
        return list(self._tools.values())
