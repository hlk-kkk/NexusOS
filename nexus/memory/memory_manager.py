from .experience import Experience, ExperienceStore


class MemoryManager:
    """Unified memory entry point for Nexus agents."""

    def __init__(self):
        self.experiences = ExperienceStore()

    def remember(self, task, steps, result, metadata=None):
        experience = Experience(
            task=task,
            steps=steps,
            result=result,
            metadata=metadata or {},
        )
        self.experiences.save(experience)
        return experience

    def history(self):
        return self.experiences.all()
