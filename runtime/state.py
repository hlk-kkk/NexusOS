from dataclasses import dataclass, field


@dataclass
class AgentState:
    goal: str
    plan: list = field(default_factory=list)
    messages: list = field(default_factory=list)
    artifacts: list = field(default_factory=list)
    status: str = "CREATED"

    def add_message(self, message: str):
        self.messages.append(message)

    def add_artifact(self, path: str):
        self.artifacts.append(path)
