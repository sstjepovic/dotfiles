# Allows the mouse to interact with windows as if it where a FWM (Floating Window Manager)

from libqtile.config import Drag, Click
from libqtile.lazy import lazy
from settings.keys import mod

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())

]
