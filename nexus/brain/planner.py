class Planner:
    """Create execution plans from user goals."""

    def __init__(self, llm=None):
        self.llm = llm

    def create_plan(self, goal, tools=None):
        if self.llm:
            return self.llm.chat([
                {
                    "role": "user",
                    "content": f"Plan execution for: {goal}"
                }
            ])

        return {
            "goal": goal,
            "steps": [],
            "tools": tools or []
        }
