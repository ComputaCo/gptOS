from computatrum.apps.app import App
from computatrum.apps.single_page_app import SinglePageApp


class Introspection(SinglePageApp):
    """Useful for introspecting and modifying yourself."""

    def render(self, size):
        # view API health checks
        # view API usage + costs
        # view card balance
        # view python memory profile
        # option to send python commands to be executed in this process
        # view network usage
        # view disk usage
        # view CPU usage