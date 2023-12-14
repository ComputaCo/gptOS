from __future__ import annotations

from enum import Enum
from typing import Literal
import attr
from abc import abstractmethod
from gptOS.lmi.components.component import Component
from gptOS.tools.tool import Tool
from gptOS.tools.toolbox import Toolbox

from gptOS.lmi.utils import normalize
from gptOS.lmi.misc.alignment import Alignment
from gptOS.lmi.handlers.display_event_handler import DisplayEventHandler
from gptOS.lmi.handlers.drag_event_handler import DragEventHandler
from gptOS.lmi.handlers.drop_event_handler import DropEventHandler
from gptOS.lmi.handlers.focus_event_handler import FocusEventHandler
from gptOS.lmi.handlers.keyboard_event_handler import KeyboardEventHandler
from gptOS.lmi.handlers.mouse_event_handler import MouseEventHandler
from gptOS.lmi.handlers.scroll_event_handler import ScrollEventHandler
from gptOS.services.keyboard_service import KeyboardService


@attr.s(auto_attribs=True)
class AbstractComponent(Toolbox, DisplayEventHandler):
    tools: list[Tool] = attr.ib([])
    preferred_size: int = None
    flex_factor: float = 1.0  # 0 = fixed, 1 = normal, inf = absorb all difference

    @property
    def max_size(self) -> int:
        return self.preferred_size

    @property
    def min_size(self) -> int:
        return self.preferred_size

    @abstractmethod
    def render(self, size) -> str:
        pass

    @property
    @abstractmethod
    def visible_components(self) -> list[Component]:
        pass