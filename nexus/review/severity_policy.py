class SeverityPolicy:

    LEVELS = [
        "critical",
        "high",
        "medium",
        "low",
    ]

    def normalize(self, severity):
        if severity in self.LEVELS:
            return severity
        return "medium"

    def should_block(self, severity):
        return self.normalize(severity) == "critical"
