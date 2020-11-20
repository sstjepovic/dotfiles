# Qtile Layouts

from libqtile import layout

layout.conf = {
    'border_focus': "#FF8552",  
    'border_width': 1,
    'margin': 10,
}

layouts = [
   
      layout.MonadTall(**layout.conf),
      layout.Max(),

]

floating_layout = layout.Floating(
        float_rules=[

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

        ],
        border_focus="#FF8552" 
)
