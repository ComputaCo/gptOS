from notifypy import Notify
from langchain.agents import tool

from computatrum.utils.constants import APP_DIR

help_notification = Notify(
    default_notification_title="Help Requested",
    default_application_name="Computatrum",
    default_notification_icon=APP_DIR / "imgs" / "icon.png",
    default_notification_audio=APP_DIR / "audio" / "help_requested.wav",
)


@tool
def request_help(input: str) -> str:
    help_notification.message = input
    help_notification.send()
    return "Help request sent."
