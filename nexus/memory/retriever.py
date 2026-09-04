"""Memory retrieval interfaces."""


class MemoryRetriever:
    def __init__(self, store=None):
        self.store = store

    def retrieve(self, query: str, limit: int = 5):
        if self.store is None:
            return []
        return self.store.search(query, limit=limit)
