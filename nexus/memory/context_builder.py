class ContextBuilder:
    """Build context from previous Nexus memories."""

    def __init__(self, memory_manager):
        self.memory_manager = memory_manager

    def build(self, query=None):
        memories = (
            self.memory_manager.recall(query)
            if query
            else self.memory_manager.history()
        )

        return [
            {
                "task": item.task,
                "steps": item.steps,
                "result": item.result,
                "metadata": getattr(item, "metadata", {}),
            }
            for item in memories
        ]
