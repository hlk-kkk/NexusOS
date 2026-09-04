class ToolLoader:
    """Load builtin tools into MCP registry."""

    def __init__(self, registry):
        self.registry = registry

    def load(self, tools):
        for tool in tools:
            self.registry.register(tool)

        return self.registry
