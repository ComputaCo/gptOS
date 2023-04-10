# Computatrum

- Computatrum is an operating system for humans to instruct AI's to interact with tools.
- Computatrum is an AI system that can interact with tools, humans, and long term memory.

- This is the agent's mind. There is no separate agent. At least not right now...
- Apps have tools and/or views
- The layout manager is responsible for the layout of the windows, tool listings, ltm, monologue, and notifications. Its entire state is stored in a stack that can be pushed and popped by apps (eg, temporarily go into full screen for a dialog or disable notifications in meditation)
- When there is more than one window displayed, the tools are prefixed with `context.`. For example, `mailbox.all_messages()`

```
Apps:
  mailboxes:
    email.py
    messages.py
  terminal.py
  python_shell.py
  file browser.py
  text editor.py
  web browser.py
  gui.py
  meditation.py
LMI:
  layout manager.py
  window.py
computatrum.py
```

## Apps:

- Mailbox (email, sms, messaging server, etc):
  - functions:
    - all_messages(from='*', to='*', subject='*', before='*', after='*', limit=20): lists all messages from `from` to `to` with `subject` before `before` after `after` with a limit of `limit` in a numbered list. Unspecified parameters are wildcards.
    - read_message(id): reads message `id`
    - send_message(to, subject, body): sends a message to `to` with `subject` and `body`
- Terminal:
  - shows the terminal window
  - functions:
    - scroll(lines): scrolls the terminal window `lines` lines
    - input(text): inputs `text` into the terminal window
- GUI: ppix2struct --> browser agent
- Meditation:
  - disables notifications
  - show monologue
  - show small window of STM
  - show small window of LTM
- base context for all of the above:
  - show notifications (if any)
  - show monologue
  - show small window of STM
  - show small window of LTM
  - functions:
    - launch(app): launches `app`
    - side_by_side(left_windows, right_window): displays `left_windows` on the left and `right_window` on the right
    - minimize(window=None): minimizes `window`. Defaults to the current window
    - maximize(window=None): maximizes `window`. Defaults to the current window
    - close(window=None): closes `window`. Defaults to the current window
    - help(): provides help information for manipulating windows


------------

applications
windows
components
tools

------------


PROMPT

WINDOWS

TOOLBAR

