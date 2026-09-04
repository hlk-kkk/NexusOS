"""Select tools for agent tasks."""


class ToolSelector:
    def __init__(self, registry):
        self.registry = registry

    def select(self, intent: str):
        tools = []
        for name in self.registry.list_tools():
            if any(keyword in intent.lower() for keyword in name.lower().split('_')):
                tools.append(name)
        return tools
