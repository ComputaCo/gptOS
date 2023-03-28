import attr
from abc import abstractmethod

from computatrum.lmi.components.component import Component


@attr.s(auto_attribs=True)
class Text(Component):

    content: str

    @property
    def preferred_size(self) -> int:
        return len(self.content)

    @abstractmethod
    def render(self, size) -> str:
        if size < self.preferred_size:
            return "..." + self.content[: size - 3]
