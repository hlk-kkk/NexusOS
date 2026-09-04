"""Embedding abstraction for NexusOS memory layer."""

from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        raise NotImplementedError


class SimpleEmbeddingProvider(EmbeddingProvider):
    """Placeholder deterministic embedding provider.

    Real vector providers can implement the same interface later.
    """

    def embed(self, text: str) -> list[float]:
        return [float(len(text))]
