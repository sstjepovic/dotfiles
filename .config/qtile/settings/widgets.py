# Qtile Widgets

from libqtile import widget

# Get the Icons at http://www.nerdfonts.com/cheat-sheet
# Separator: nf-mdi-bandcamp
# ThermalSensor: nf-fa-thermometer_0
# Clock: nf-mdi-clock

primary_widgets =  [

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

]

secondary_widgets = [

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

     widget.Sep(
        padding= 10,
        linewidth= 0,
     ),
 
] 

widget_defaults = {
    'font': 'Ubuntu Mono Nerd Font',
    'fontsize': 16,
    'padding': 6,
}

extension_defaults = widget_defaults.copy()


