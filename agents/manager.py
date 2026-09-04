from .base import BaseAgent

class ManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__('manager','planner')

    def execute(self, state):
        state.status='PLANNING'
        state.plan=['analyze','research','review']
        return state
