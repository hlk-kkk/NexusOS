class GraphQueryEngine:
    """High level queries for AI agents."""

    def __init__(self, graph):
        self.graph = graph

    def find_impact(self, symbol):
        return self.graph.impact(symbol)

    def explain(self, symbol):
        return {
            "symbol": symbol,
            "affected": self.find_impact(symbol),
        }
