class Task:
    def __init__(self, agent: str, goal: str, context=None):
        self.agent = agent
        self.goal = goal
        self.context = context or {}
