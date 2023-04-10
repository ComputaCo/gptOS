from abc import abstractmethod

from computatrum.services.base_service import Service
from computatrum.utils.singleton import Singleton


class MemoryService(Service, Singleton):
    @abstractmethod
    def remember(self, text, application, context=None, time=None):
        pass

    @abstractmethod
    def recall(self, application, context=None, time=None):
        pass
