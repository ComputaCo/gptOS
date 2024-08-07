from gptos.api.abc.task import Task
from computatrum.services.base_service import Service
from gptos.api.misc.singleton import Singleton


class TaskService(Service, Singleton):

    focus: list[Task]  # sorted by priority
    tasks: list[Task]  # all tasks

    def extract_tasks(self, data):
        """Extracts tasks from data"""
        ...

    def evaluate_focus(self):
        """Determine which tasks to focus on."""
        ...
