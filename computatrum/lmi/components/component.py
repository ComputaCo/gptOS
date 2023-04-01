from __future__ import annotations

from enum import Enum
import attr
from abc import abstractmethod

from computatrum.primitives.alignment import Alignment


@attr.s(auto_attribs=True)
class Component:
    preferred_size: int = None
    parent: Component = None

    @property
    def max_size(self) -> int:
        return self.preferred_size

    @property
    def min_size(self) -> int:
        return self.preferred_size

    @abstractmethod
    def render(self, size) -> str:
        pass

    @classmethod
    def saferender(cls, component, size) -> str:
        try:
            return component.render(size)
        except Exception as _:
            return component

    @property
    def component_name(self) -> str:
        return self.__class__.__name__

    @property
    def component_path(self) -> str:
        if self.parent is None:
            return ""
        else:
            return self.parent.component_path + "/" + self.component_name
