# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = guess_terminal()

keys = [

    #Recorrer ventanas con IJKL
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),

    # Desplazar ventanas 
    Key([mod, "control"], "k", lazy.layout.shuffle_up()), 
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    
    #Shotcuts de Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    #Change window sizes (MonadTall)
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),

    #Shortcuts personalizados 
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod], "q", lazy.spawn("firefox")),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "p", lazy.spawn("redshift -O 3500")),
    Key([mod, "shift"], "p", lazy.spawn("redshift -x")),

    #Volumen
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),

]

groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i +1)
    keys.extend([
        #Ir al Grupo N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        #Enviar Pestaña al grupo N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
     ])

layouts = [
   
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),

      layout.MonadTall(
          border_focus = "#FF8552",
          border_normal= "#BAC5CF",
          margin = 10,
      ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
      layout.Max(),
]

widget_defaults = dict(
    font='Ubuntu Mono Nerd Font',
    fontsize=16,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding= 10,
                    linewidth= 0,
                ),

                widget.TextBox (
                    text = "ﭳ",
                    foreground = "#626971",
                    padding = 0,
                    fontsize = 50,
                    width = 14,
                ),
                widget.GroupBox(
                    background = "#626971",
                    highlight_method = 'block',
                    fontsize = 19,
                    this_current_screen_border = "#FF8552",
                ),

                widget.TextBox (
                    text = "ﭳ",
                    foreground = "#626971",
                    padding = -31,
                    width = 14,
                    fontsize = 53,
                ),

                widget.WindowName(
                    foreground = "#626971",
                ),
                widget.TextBox (
                    text = "ﭳ",
                    foreground = "#FF8552",
                    padding = 0,
                    fontsize = 50,
                    width = 14,
                ),

                widget.TextBox (
                    text = "",
                    background = "#FF8552",
                ),
                widget.ThermalSensor (
                    treshhold = 60,
                    background = "#FF8552",
                    
                ),
                widget.TextBox (
                    text = "ﭳ",
                    background = "#FF8552",
                    foreground = "#A9B4CF",
                    padding = 0,
                    fontsize = 50,
                    width = 14,
                ),

                widget.CurrentLayoutIcon(
                    scale = 0.65,
                    background = "#A9B4CF",
                    padding = 4,
                ),
                
                widget.CurrentLayout(
                    #background = "#aec2ff",
                    background = "#A9B4CF",
                    padding = 10,

                ),

                widget.TextBox (
                    text = "ﭳ",
                    foreground = "#A9B4CF",
                    background = "#626971",
                    padding = -31,
                    width = 13,
                    fontsize = 53,
                ),

                widget.TextBox (
                    text = "",
                    background = "#626971",
                    padding = 5,
                ),

                widget.Clock(
                    format='%d-%m-%Y %H:%M',
                    padding = 10,
                    background = "#626971",
                ),
                
                widget.Systray(
                    background = "#626971",
                ),

                widget.TextBox (
                    text = "ﭳ",
                    foreground = "#626971",
                    padding = -31,
                    width = 13,
                    fontsize = 53,
                ),
                widget.Sep(
                    padding= 10,
                    linewidth= 0,
                ),
            ],
            24,
            background = "#BAC5CF",
            opacity = 0.9,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
