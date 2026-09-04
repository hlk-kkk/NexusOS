class SymbolIndex:
    """Index code symbols for agent retrieval."""

    def __init__(self):
        self.symbols = {}

    def add(self, name: str, location: str):
        self.symbols[name] = location

    def search(self, keyword: str):
        return {
            k: v for k, v in self.symbols.items()
            if keyword.lower() in k.lower()
        }
