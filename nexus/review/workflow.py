class ReviewWorkflow:
    """Review execution workflow.

    Flow:
    diff -> analysis -> risk -> comments
    """

    def __init__(self, review_agent, formatter=None):
        self.review_agent = review_agent
        self.formatter = formatter

    def run(self, context):
        result = self.review_agent.review(context)

        if self.formatter:
            return self.formatter.format(result)

        return result
