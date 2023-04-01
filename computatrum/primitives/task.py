from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    title: str
    details: str
    impetus: str
    subtasks: list[Task]
    dependencies: list[Task]
    dependants: list[Task]
    importance: int  # 0-10
    created: datetime
    completed: datetime | None
