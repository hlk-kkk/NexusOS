from dataclasses import dataclass
from typing import List


@dataclass
class EngineeringPlan:
    goal: str
    steps: List[str]


class EngineerPlanner:
    """Creates implementation plans for software engineering tasks."""

    def create_plan(self, issue: str) -> EngineeringPlan:
        return EngineeringPlan(
            goal=issue,
            steps=[
                "understand repository context",
                "identify impacted modules",
                "prepare code changes",
                "run validation"
            ]
        )
