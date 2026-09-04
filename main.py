from runtime.state import AgentState
from runtime.runtime import AgentRuntime
from agents.manager import ManagerAgent


def main():
    state = AgentState(goal='demo task')
    runtime = AgentRuntime([ManagerAgent()])
    result = runtime.run(state)
    print(result)


if __name__ == '__main__':
    main()
