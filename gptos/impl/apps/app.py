from abc import abstractmethod

import attr

from gptos.api.lmi.windows.window import Window
from computatrum.primitives.tool import Tool


@attr.s(auto_attribs=True)
class App:
    windows: list[Window] = []
    top_level_tools: list[Tool] = []
