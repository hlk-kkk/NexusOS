"""Brain and MCP binding layer."""

from typing import Any


class MCPBinding:
    def __init__(self, executor):
        self.executor = executor

    def invoke(self, tool_name: str, **kwargs) -> Any:
        return self.executor.execute(tool_name, kwargs)
