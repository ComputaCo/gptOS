from abc import abstractmethod
from dataclasses import dataclass
from gptOS.lmi.components.component import Component

from gptOS.tools.tool import Tool
from gptOS.services.screen_service import ScreenService


@dataclass
class screen(Component):

    title: str

    @abstractmethod
    def render(self, size) -> str:
        pass

    @abstractmethod
    @property
    def tools(self) -> list[Tool]:
        pass

    @property
    def is_visible(self) -> bool:
        return self in ScreenService.current.visible_windows

    @property
    def is_active(self) -> bool:
        return any(
            self in screen.windows for screen in ScreenService.Singleton().screen_stack
        )

    @property
    def component_name(self) -> str:
        return self.title
