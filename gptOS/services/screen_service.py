from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

import attr
from gptOS.lmi.abstractions.abstract_component import AbstractComponent
from gptOS.lmi.components.component import Component
from gptOS.lmi.components.flexbox import Flexbox
from gptOS.lmi.misc.alignment import Alignment
from gptOS.lmi.screens.screen import screen
from gptOS.services.service import Service
from gptOS.tools.pyobj_tool import PyObjectTool


@attr.s(auto_attribs=True)
class ScreenService(Service, AbstractComponent):

    preferred_size: int = 6000  # change this to suit your needs

    __screen_stack: Flexbox
    __menu_bar: PyObjectTool
    __composite_flexbox: Flexbox

    def __attr_post_init__(self):
        self.__screen_stack = Flexbox(
            separator="\n---\n",
            truncation_alignment=Alignment.RIGHT,
            truncation_mode="block",
        )
        self.__menu_bar = PyObjectTool()

    @property
    def children(self) -> list[Component]:
        return self.screen_stack

    def push(self, screen: screen):
        self.screen_stack.children.append(screen)

    def pop(self, screen: screen):
        self.screen_stack.children.remove(screen)

    def top(self) -> screen:
        return self.screen_stack.children[-1]

    def render(self, size=None) -> str:
        size = size or self.screen_size
        menu_bar_rendering = self.__menu_bar.render()
        divider = "\n---\n"
        screen_stack_rendering = self.__screen_stack.render(
            size=size - len(divider + menu_bar_rendering)
        )
        return screen_stack_rendering + divider + menu_bar_rendering

    @property
    def visible_components(self) -> list[Component]:
        return self.__screen_stack.visible_components()
