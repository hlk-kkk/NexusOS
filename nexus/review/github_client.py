class GitHubReviewClient:
    """GitHub review integration abstraction.

    The implementation keeps provider details isolated so GitHub API,
    GitHub Enterprise and internal SCM adapters can share the review flow.
    """

    def create_review_payload(self, pr_context, comments):
        return {
            "pr": pr_context,
            "comments": comments,
        }

    def publish(self, payload):
        return {
            "published": False,
            "payload": payload,
            "message": "Adapter ready for GitHub API integration",
        }
