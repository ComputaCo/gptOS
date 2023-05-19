from abc import abstractmethod

import attr

from gptos.lmi.windows.window import Window
from gptos.tools.tool import Tool
from gptos.services.service import Service


@attr.s(auto_attribs=True)
class App(Service):
    windows: list[Window]
    top_level_tools: list[Tool]

    @property
    def tools(self):
        return self.top_level_tools + self.windows
