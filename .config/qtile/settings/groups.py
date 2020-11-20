# Workspaces

from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from settings.keys import mod, keys

# Get the Icons from https://www.nerdfonts.com/cheat-sheet
# Icons:
# nf-fa-firefox
# nf-custom-vim
# nf-mdi-console
# nf-mdi-music_circle

groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i +1)
    keys.extend([
        #Ir al Grupo N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        #Enviar Pestaña al grupo N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
     ])


