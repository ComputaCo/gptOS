from computatrum.lmi.components.scrollable import Scrollable
from computatrum.lmi.components.stack import Stack
from computatrum.lmi.components.text import Text
from computatrum.services.registry_service import RegistryService


class Home(App):
    def render(self, size):
        return Scrollable(Stack(children=[
            Text(content=f"{i+1}. {app.name}")
            for i, app in enumerate(RegistryService.apps)
        ])
            
            