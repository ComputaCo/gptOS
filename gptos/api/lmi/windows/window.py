from abc import abstractmethod
from dataclasses import dataclass
from gptos.api.lmi.components.component import Component

from computatrum.primitives.tool import Tool
from computatrum.services.window_service import WindowService


@dataclass
class Window(Component):

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
        return self in WindowService.Singleton().visible_windows

    @property
    def is_active(self) -> bool:
        return any(
            self in screen.windows for screen in WindowService.Singleton().screen_stack
        )

    @property
    def component_name(self) -> str:
        return self.title
