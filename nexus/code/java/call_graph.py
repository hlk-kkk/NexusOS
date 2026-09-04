from collections import defaultdict


class JavaCallGraph:
    """Directed call graph used for impact analysis."""

    def __init__(self):
        self.edges = defaultdict(set)

    def add_call(self, caller: str, callee: str):
        self.edges[caller].add(callee)

    def impact(self, symbol: str):
        visited = set()
        queue = [symbol]

        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            queue.extend(self.edges.get(current, []))

        return visited
