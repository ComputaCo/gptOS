from computatrum.apps.app import App
from gptos.api.lmi.windows.window import Window


class SinglePageApp(Window, App):
    @property
    def windows(self):
        return [self]
