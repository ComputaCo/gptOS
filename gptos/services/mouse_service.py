import attr
from gptos.lmi.handlers.click_event_handler import ClickEventHandler
from gptos.lmi.handlers.drag_event_handler import DragEventHandler
from gptos.lmi.handlers.drop_event_handler import DropEventHandler
from gptos.lmi.handlers.focus_event_handler import FocusEventHandler
from gptos.lmi.handlers.mouse_event_handler import MouseEventHandler
from gptos.lmi.handlers.scroll_event_handler import ScrollEventHandler
from gptos.services.focus_service import FocusService
from gptos.services.service import Service
from gptos.tools.tool import Tool


class MouseService(Service):

    scroll_event_handlers: set[ScrollEventHandler] = attr.ib(set())

    @Tool.wrap
    def click(
        self,
        target: ClickEventHandler,
        button: MouseEventHandler.MouseEvent.Buttons = MouseEventHandler.MouseEvent.Buttons.LEFT,
        click_type: ClickEventHandler.ClickEvent.ClickType = ClickEventHandler.ClickEvent.ClickType.SINGLE,
    ):
        """Click `clickable` with `button` and `click_type`

        Args:
            clickable (ClickEventHandler): The object to click
            button (MouseEventHandler.MouseEvent.Buttons, optional): The button to click with. Defaults to 'left'.
            click_type (ClickEventHandler.ClickEvent.ClickType, optional): The type of click. Defaults to 'single'.
        """
        # set focus if the target supports it
        if isinstance(target, FocusEventHandler):
            FocusService.current.set_focus(target)
        # invoke the click event on the target
        event = ClickEventHandler.ClickEvent(button=button, click_type=click_type)
        target.click(event)

    @Tool.wrap
    def drag_and_drop(
        self,
        drag_from: DragEventHandler,
        drop_to: DropEventHandler,
        button: MouseEventHandler.MouseEvent.Buttons = MouseEventHandler.MouseEvent.Buttons.LEFT,
    ):
        """Drag from `dragable` to `dropable` while holding `button`

        Args:
            dragable (DragEventHandler): The object to drag from
            dropable (DropEventHandler): The object to drop on
            button (MouseEventHandler.MouseEvent.Buttons, optional): The button to drag with. Defaults to 'left'.
        """
        # start drag
        drag_event = DragEventHandler.DragEvent(button=button)
        for handler in {drag_from} + self.drag_event_handlers:
            handler.start_drag(drag_event)
        # drop
        drop_event = DropEventHandler.DropEvent(button=button, obj=drag_event.obj)
        drop_to.drop(drop_event)
        # end drag
        drag_from.end_drag(drag_event)

    @Tool.wrap
    def scroll(
        self,
        direction: ScrollEventHandler.ScrollEvent.Direction,
        target: ScrollEventHandler = None,
        speed: ScrollEventHandler.ScrollEvent.Speed = ScrollEventHandler.ScrollEvent.Speed.MEDIUM,
    ):
        """Scroll `scrollable` in `direction` at `speed`

        Args:
            direction (ScrollEventHandler.ScrollEvent.Direction): The direction to scroll
            scrollable (ScrollEventHandler, optional): The object to scroll. Defaults to whatever component is in focus.
            speed (ScrollEventHandler.ScrollEvent.Speed, optional): The speed to scroll. Defaults to 'medium'.
        """
        # invoke the scroll event on the target and all scroll event handlers
        event = ScrollEventHandler.ScrollEvent(direction=direction, speed=speed)
        for handler in self.scroll_event_handlers + (
            {target} if target is not None else {}
        ):
            handler.scroll(event)

    @property
    def tools(self) -> list[Tool]:
        return [
            self.click,
            self.drag_and_drop,
            self.scroll,
        ]
