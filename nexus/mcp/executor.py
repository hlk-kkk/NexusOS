from .protocol import ToolRequest, ToolResponse
from .registry import ToolRegistry


class MCPExecutor:
    """Execute tools discovered from MCP registry."""

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, request: ToolRequest) -> ToolResponse:
        tool = self.registry.get(request.name)
        if not tool:
            return ToolResponse(False, error=f"Tool not found: {request.name}")

        try:
            return ToolResponse(True, result=tool(**request.arguments))
        except Exception as exc:
            return ToolResponse(False, error=str(exc))
