from typing import Dict, List

from .ast_model import CodeEdge, CodeNode


class GraphStore:
    def __init__(self):
        self.nodes: Dict[str, CodeNode] = {}
        self.edges: List[CodeEdge] = []

    def add_node(self, node: CodeNode):
        self.nodes[node.name] = node

    def add_edge(self, edge: CodeEdge):
        self.edges.append(edge)

    def neighbors(self, name: str):
        return [
            edge.target
            for edge in self.edges
            if edge.source == name
        ]

    def impact(self, name: str):
        visited = set()
        queue = [name]
        while queue:
            current = queue.pop(0)
            for item in self.neighbors(current):
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
        return list(visited)
