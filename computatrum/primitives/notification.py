from dataclasses import dataclass

from computatrum.services.notification_service import NotificationService


@dataclass
class Notification:
    subject: str
    message: str
    id: str | None = None
    importance: int = 0  # 0-3, 0 = least important, 3 = most important

    def broadcast(self):
        NotificationService.Singleton().broadcast(self)

    def reschedule(self, value):
        NotificationService.Singleton().reschedule(self, value)

    @property
    def scheduled_for(self):
        return NotificationService.Singleton().scheduled_for(self)

    scheduled_for.setter(reschedule)
