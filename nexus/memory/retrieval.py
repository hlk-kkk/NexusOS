from .repository_memory import RepositoryMemory


class MemoryRetriever:
    """Simple retrieval interface for agent context."""

    def __init__(self, memory: RepositoryMemory):
        self.memory = memory

    def search(self, keyword: str):
        result = []
        for fact in self.memory.facts:
            if keyword.lower() in fact.lower():
                result.append(fact)
        return result
