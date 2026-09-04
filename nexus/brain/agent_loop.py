"""Minimal agent execution loop."""


class AgentLoop:
    def __init__(self, planner, binding):
        self.planner = planner
        self.binding = binding

    def run(self, task: str):
        plan = self.planner.plan(task)
        results = []
        for step in plan:
            results.append(self.binding.invoke(step['tool'], **step.get('args', {})))
        return results
