from gptos.lmi.components.scroll_view import ScrollView
from gptos.lmi.components.stack import Stack
from gptos.lmi.components.text import Text
from computatrum.services.registry_service import RegistryService


class Home(App):
    def render(self, size):
        return ScrollView(Stack(children=[
            Text(content=f"{i+1}. {app.name}")
            for i, app in enumerate(RegistryService.apps)
        ])
            
            