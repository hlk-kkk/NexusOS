class CommentFormatter:

    def format(self, issue):
        return {
            "severity": issue.get("severity", "unknown"),
            "body": self._build_body(issue),
        }

    def _build_body(self, issue):
        return (
            f"### {issue.get('severity', 'Issue')}\n\n"
            f"{issue.get('message', '')}\n"
        )
