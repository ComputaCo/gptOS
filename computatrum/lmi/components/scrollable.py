import attr
from abc import abstractmethod

from computatrum.lmi.components.component import Component
from computatrum.primitives.tool import Tool


@attr.s(auto_attribs=True)
class Scrollable(Component):

    child: Component
    position: int = 0

    @abstractmethod
    def render(self, size) -> str:
        content = Component.saferender(self.child, size)
        self.position = min(self.position, len(content))
        self.position = max(self.position, 0)
        start = min(self.position, len(content) - size)
        end = start + size
        return content[start:end]

    def scroll(self, lines):
        self.position += lines

    @property
    def scroll_tool(self) -> Tool:
        return Tool(
            name="Scroll",
            description="Scroll up or down",
            func=lambda lines: self.scroll(int(lines)),
        )
