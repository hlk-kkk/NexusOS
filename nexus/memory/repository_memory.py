from typing import Dict, List


class RepositoryMemory:
    """Stores learned repository facts for SWE agents."""

    def __init__(self):
        self.modules: Dict[str, str] = {}
        self.facts: List[str] = []

    def remember_module(self, name: str, description: str):
        self.modules[name] = description

    def remember_fact(self, fact: str):
        self.facts.append(fact)

    def summary(self):
        return {
            "modules": self.modules,
            "facts": self.facts,
        }
