import attr
from gptos.api.lmi.components.component import Component
from computatrum.primitives.alignment import Alignment
from computatrum.utils.truncation import truncate


@attr.s(auto_attribs=True)
class Stack(Component):
    children: list[Component] = []
    separator: str = "\n"
    truncation_alignment: Alignment = Alignment.LEFT

    def render(self, size) -> str:
        output = ""
        for i, child in enumerate(self.children):
            output += self.separator
            remaining = size - len(output)
            ideal_length = remaining // (len(self.children) - i)
            output += Component.saferender(child.render, ideal_length)
        return truncate(output, self.truncation_alignment, size)
