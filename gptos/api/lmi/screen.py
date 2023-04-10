from gptos.api.lmi.components.component import Component
from gptos.api.lmi.components.stack import Stack
from gptos.api.lmi.windows.window import Window


class Screen(Component):
    windows: list[Window] = []

    @property
    def children(self):
        return self.windows

    def render(self, size) -> str:
        return Stack.render(self, size)
