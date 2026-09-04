from dataclasses import dataclass


@dataclass
class ImpactReport:
    target: str
    risk_score: int
    affected: list

    def to_dict(self):
        return {
            "target": self.target,
            "risk_score": self.risk_score,
            "affected": self.affected,
        }
