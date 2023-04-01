from computatrum.lmi.components.component import Component
from computatrum.lmi.components.stack import Stack
from computatrum.lmi.windows.window import Window


class Screen(Component):
    windows: list[Window] = []

    @property
    def children(self):
        return self.windows

    def render(self, size) -> str:
        return Stack.render(self, size)
