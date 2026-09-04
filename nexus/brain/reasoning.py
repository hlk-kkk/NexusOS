class ReasoningLoop:
    """Basic think-act workflow orchestration."""

    def __init__(self, planner, executor=None):
        self.planner = planner
        self.executor = executor

    def run(self, goal):
        plan = self.planner.create_plan(goal)

        if self.executor:
            return self.executor.execute(plan)

        return plan
