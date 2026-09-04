from dataclasses import dataclass


@dataclass
class EngineeringTask:
    issue: str
    status: str = "created"


class AutonomousFixLoop:
    """Coordinate issue analysis, patching and validation."""

    def run(self, task: EngineeringTask):
        task.status = "planning"
        return task
