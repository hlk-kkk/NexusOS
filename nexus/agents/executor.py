from .base import Agent


class ExecutorAgent(Agent):
    def __init__(self):
        super().__init__("executor")

    def execute(self, task):
        return {
            "status": "completed",
            "result": task.goal,
        }
