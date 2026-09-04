"""Java-specific impact analysis adapter."""


class JavaImpactAnalyzer:
    def __init__(self, call_graph=None, dependency_graph=None):
        self.call_graph = call_graph
        self.dependency_graph = dependency_graph

    def analyze_symbol(self, symbol: str):
        result = set()
        if self.call_graph and hasattr(self.call_graph, "callers"):
            result.update(self.call_graph.callers(symbol))
        if self.dependency_graph:
            result.update(self.dependency_graph.affected_by(symbol))
        return list(result)
