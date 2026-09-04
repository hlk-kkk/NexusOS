from .model import CodeRelation, CodeSymbol


class CodeGraph:
    """Lightweight code dependency graph for Nexus analysis."""

    def __init__(self):
        self.symbols = {}
        self.relations = []

    def add_symbol(self, symbol: CodeSymbol):
        self.symbols[symbol.name] = symbol

    def add_relation(self, relation: CodeRelation):
        self.relations.append(relation)

    def impact(self, symbol_name: str):
        return [
            r
            for r in self.relations
            if r.source == symbol_name or r.target == symbol_name
        ]
