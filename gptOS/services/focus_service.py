from typing import Optional
from gptOS.lmi.components.component import Component
from gptOS.lmi.handlers.focus_event_handler import FocusEventHandler
from gptOS.lmi.handlers.keyboard_event_handler import KeyboardEventHandler
from gptOS.lmi.handlers.click_event_handler import ClickEventHandler
from gptOS.lmi.handlers.drag_event_handler import DragEventHandler
from gptOS.lmi.handlers.drop_event_handler import DropEventHandle
from gptOS.lmi.handlers.scroll_event_handler import ScrollEventHandler
from gptOS.services.keyboard_service import KeyboardService
from gptOS.services.mouse_service import MouseService


from gptOS.services.service import Service


class FocusService(Service):
    """Tracks which component is in focus"""

    __focus: Optional[Component] = None

    @property
    def focus(self) -> Optional[Component]:
        return self.__focus

    def set_focus(self, component: Component):
        # update the focus
        if self.__focus is not None:
            self.unfocus()
        self.__focus = component

        # register with the 'omniscent' event handlers
        if isinstance(self.__focus, KeyboardEventHandler):
            KeyboardService.keyboard_event_handlers.add(self.__focus)
        if isinstance(self.__focus, ScrollEventHandler):
            MouseService.scroll_event_handlers.add(self.__focus)

        # invoke the focus event on the target
        self.__focus.on_focus()

    def unfocus(self):
        # if there is no focus, do nothing
        if self.__focus is None:
            return

        # invoke the unfocus event on the target
        event = FocusEventHandler.FocusEvent()
        self.__focus.on_unfocus(event)

        # deregister from the 'omniscent' event handlers
        if isinstance(self.__focus, KeyboardEventHandler):
            KeyboardService.keyboard_event_handlers.remove(self.__focus)
        if isinstance(self.__focus, ScrollEventHandler):
            MouseService.scroll_event_handlers.remove(self.__focus)

        # update the focus
        self.__focus = None
