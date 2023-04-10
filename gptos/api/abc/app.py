from abc import abstractmethod

import attr

from gptos.api.lmi.windows.window import Window
from gptos.api.abc.tool import Tool, Toolbox


@attr.s(auto_attribs=True)
class App(Toolbox):
    windows: list[Window] = []
    top_level_tools: list[Tool] = []

    @property
    def tools(self):
        return self.top_level_tools + self.windows
