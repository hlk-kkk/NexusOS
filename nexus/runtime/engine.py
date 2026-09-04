class NexusRuntime:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.name] = agent

    def execute(self, task):
        agent = self.agents.get(task.agent)
        if agent is None:
            raise ValueError(f"Agent not found: {task.agent}")
        return agent.execute(task)
