class DependencyIndex:
    """Track repository dependency relationships."""

    def __init__(self):
        self.graph = {}

    def add_dependency(self, source: str, target: str):
        self.graph.setdefault(source, []).append(target)

    def impact(self, module: str):
        return self.graph.get(module, [])
