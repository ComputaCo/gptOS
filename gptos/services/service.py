from abc import abstractmethod

from gptos.tools.tool import Toolbox


class Service(Toolbox):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
