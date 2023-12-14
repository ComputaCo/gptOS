from computatrum.apps.app import App
from gptos.lmi.windows.window import Window


class SinglePageApp(Window, App):
    @property
    def windows(self):
        return [self]
