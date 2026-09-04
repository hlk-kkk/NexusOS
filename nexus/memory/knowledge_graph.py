"""Minimal knowledge graph primitives for NexusOS."""

from dataclasses import dataclass


@dataclass
class KnowledgeNode:
    id: str
    kind: str
    name: str


@dataclass
class KnowledgeEdge:
    source: str
    target: str
    relation: str


class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: KnowledgeNode):
        self.nodes[node.id] = node

    def add_edge(self, edge: KnowledgeEdge):
        self.edges.append(edge)

    def neighbors(self, node_id: str):
        return [
            edge
            for edge in self.edges
            if edge.source == node_id
        ]
