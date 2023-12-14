import codecs
import re
import attr
from gptOS.lmi.handlers.keyboard_event_handler import KeyboardEventHandler
from gptOS.services.focus_service import FocusService
from gptOS.services.service import Service


class KeyboardService(Service):

    SPECIAL_KEYS = {
        "[shift]": "\x1b[2~",
        "[ctrl]": "\x1b[5~",
        "[alt]": "\x1b[3~",
        "[super]": "\x1b[6~",
        "[enter]": "\n",
        "[tab]": "\t",
        "[backspace]": "\b",
        "[del]": "\x7f",
        "[esc]": "\x1b",
        "[left]": "\x1b[D",
        "[right]": "\x1b[C",
        "[up]": "\x1b[A",
        "[down]": "\x1b[B",
        "[home]": "\x1b[1~",
        "[end]": "\x1b[4~",
        "[pageup]": "\x1b[5~",
        "[pagedown]": "\x1b[6~",
        "[f1]": "\x1bOP",
        "[f2]": "\x1bOQ",
        "[f3]": "\x1bOR",
        "[f4]": "\x1bOS",
        "[f5]": "\x1b[15~",
        "[f6]": "\x1b[17~",
        "[f7]": "\x1b[18~",
        "[f8]": "\x1b[19~",
        "[f9]": "\x1b[20~",
        "[f10]": "\x1b[21~",
        "[f11]": "\x1b[23~",
        "[f12]": "\x1b[24~",
    }

    keyboard_event_handlers: set[KeyboardEventHandler] = attr.ib(set())

    @property
    def tools(self):
        return [
            self.type,
        ]

    def type(self, text: str):
        """Type a string of text. The text may include escape sequences.

        You may optionally use these following symbols in place of their corresponding keys: [shift] [ctrl] [alt] [super] [enter] [tab] [backspace] [del] [esc] [left] [right] [up] [down] [home] [end] [pageup] [pagedown] [f1]-[f12]. Combine them with +, e.g. [ctrl+shift+C].
        """
        text = codecs.decode(text, "unicode-escape")
        for keys in self._tokenize(text):
            event = listener.KeyboardEvent(keys)
            for listener in self.keyboard_event_handlers:
                listener.key_input(event)

    def _tokenize(self, char_stream) -> list[list[str]]:
        """Convert a stream of characters into a list of tokens.

        Tokens are either a single character or a list of special keys.

        Examples:
            >>> _tokenize("hello")
            [['h'], ['e'], ['l'], ['l'], ['o']]
            >>> _tokenize("[ctrl+C]")
            [['ctrl', 'C']]
            >>> _tokenize("[ctrl+C]hello")
            [['ctrl', 'C'], ['h'], ['e'], ['l'], ['l'], ['o']]
        """
        for match in re.finditer(r"\[.+?\]|[\[\]]|.", char_stream):
            keys = match.group(0)
            if keys.startswith("[") and keys.endswith("]"):
                # makes [ctrl+shift+C] into ['ctrl', 'shift', 'C']
                keys = keys.lower().strip("[]").split("+-, ")
                keys = [self.SPECIAL_KEYS.get(key, key) for key in keys]
                yield keys
            else:
                for key in keys:
                    yield [key]
