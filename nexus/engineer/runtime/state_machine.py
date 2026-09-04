from enum import Enum


class AgentState(str, Enum):
    CREATED = "created"
    ANALYZING = "analyzing"
    PATCHING = "patching"
    TESTING = "testing"
    CREATING_PR = "creating_pr"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentStateMachine:
    def __init__(self):
        self.state = AgentState.CREATED

    def transition(self, state: AgentState):
        self.state = state
        return self.state
