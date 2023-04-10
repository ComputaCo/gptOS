from abc import abstractmethod
from dataclasses import dataclass

import attr
from gptos.api.lmi.components.component import Component
from gptos.api.lmi.windows.window import Window
from computatrum.primitives.screen import Screen

from computatrum.services.base_service import Service
from computatrum.utils.singleton import Singleton


@attr.s(auto_attribs=True, slots=True)
class WindowService(Service, Singleton):

    screen_stack: list[Screen] = []

    @property
    def top_screen(self) -> Screen:
        if len(self.screen_stack) == 0:
            self.screen_stack.append(Screen())
        return self.screen_stack[-1]

    @property
    def visible_windows(self) -> list[Window]:
        return self.top_screen.windows

    def show(self, window):
        self.top_screen.windows.append(window)

    def show_fullscreen(self, window):
        self.hide(window)
        self.screen_stack.append(Screen([window]))

    def hide(self, window):
        for screen in self.screen_stack[:]:
            screen.windows.remove(window)
            if len(screen.windows) == 0:
                self.screen_stack.remove(screen)
