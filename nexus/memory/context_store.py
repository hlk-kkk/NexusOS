from typing import Any, Dict


class ContextStore:
    """Lightweight persistent context abstraction for agents."""

    def __init__(self):
        self._contexts: Dict[str, Any] = {}

    def put(self, key: str, value: Any):
        self._contexts[key] = value

    def get(self, key: str, default=None):
        return self._contexts.get(key, default)

    def clear(self):
        self._contexts.clear()
