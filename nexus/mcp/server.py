class MCPServer:
    """Minimal MCP style tool runtime."""

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def list_tools(self):
        return list(self.tools.keys())

    def execute(self, name, **kwargs):
        tool = self.tools[name]
        return tool.execute(**kwargs)
