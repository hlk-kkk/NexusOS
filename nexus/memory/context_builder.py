class ContextBuilder:
    """Build context from previous Nexus memories."""

    def __init__(self, memory_manager):
        self.memory_manager = memory_manager

    def build(self, query=None):
        memories = self.memory_manager.history()

        context = []
        for item in memories:
            if query is None or query.lower() in item.task.lower():
                context.append(
                    {
                        "task": item.task,
                        "steps": item.steps,
                        "result": item.result,
                    }
                )

        return context
