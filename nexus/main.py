from nexus.runtime.engine import NexusRuntime
from nexus.runtime.task import Task
from nexus.agents.executor import ExecutorAgent


def run(goal="Hello Nexus"):
    runtime = NexusRuntime()
    runtime.register_agent(ExecutorAgent())
    return runtime.execute(Task("executor", goal))


if __name__ == "__main__":
    print(run())
