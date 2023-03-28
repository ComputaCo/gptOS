from abc import abstractmethod
import datetime
from typing import Callable
from computatrum.primitives.notification import Notification

from computatrum.services.base_service import Service
from computatrum.utils.singleton import Singleton


class NotificationService(Service, Singleton):
    def schedule(self, time: datetime, notification: Notification):
        pass

    def scheduled_time(self, notification: Notification) -> datetime:
        pass

    def reschedule(self, time: datetime, notification: Notification):
        pass

    def cancel(self, notification: Notification):
        pass

    def broadcast(self, notification: Notification):
        pass

    def add_listener(self, listener: Callable[[Notification], None], min_level=0):
        pass

    @abstractmethod
    def poll(self):
        pass
