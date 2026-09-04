class AgentRuntime:
    def __init__(self, agents):
        self.agents = agents

    def run(self, state):
        for agent in self.agents:
            print('Running ' + agent.name)
            state = agent.execute(state)
        return state
