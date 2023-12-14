from abc import abstractmethod

from gptOS.tools.tool import Toolbox


class Service(Toolbox):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
