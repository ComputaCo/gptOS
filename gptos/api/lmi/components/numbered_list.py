import attr
from abc import abstractmethod

from gptos.api.lmi.components.component import Component
from gptos.api.lmi.components.scrollable import Scrollable
from gptos.api.lmi.components.stack import Stack


@attr.s(auto_attribs=True)
class NumberedList(Component):

    children: list[Component]

    def render(self, size) -> str:
        return Scrollable(
            child=Stack(
                children=[
                    f"{i + 1}. {Component.saferender(child, size // len(self.children))}"
                    for i, child in enumerate(self.children)
                ]
            )
        )
