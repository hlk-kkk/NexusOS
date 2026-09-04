class ToolExecutor:
    """Execute tools registered in MCP runtime."""

    def __init__(self, registry):
        self.registry = registry

    def execute(self, name, **kwargs):
        tool = self.registry.get(name)
        if tool is None:
            raise ValueError(f"Tool not found: {name}")
        return tool.execute(**kwargs)
