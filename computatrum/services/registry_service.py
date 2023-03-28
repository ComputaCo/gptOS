import attr
from computatrum.apps.app import App
from computatrum.services.base_service import Service
from computatrum.utils.singleton import Singleton


@attr.s
class RegistryService(Service, Singleton):

    agent_name: str = "Agent"
    apps: list[App] = []
