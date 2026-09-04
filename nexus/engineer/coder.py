from dataclasses import dataclass


@dataclass
class CodePatch:
    file: str
    content: str
    reason: str


class CodeAgent:
    """Generates code patch proposals.

    Actual LLM based generation will be connected through Brain providers.
    """

    def generate_patch(self, file: str, instruction: str) -> CodePatch:
        return CodePatch(
            file=file,
            content="",
            reason=instruction
        )
