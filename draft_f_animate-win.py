

import math
from time import sleep

import dearpygui.dearpygui as dpg




dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

def animate_window():
    i = 0
    if dpg.get_item_configuration("c_win")['width'] < 380:
        while i <= 1:
            x_pos = int((1 - math.pow((1 - i), 8)) * 50)
            i += 0.03
            WIDTH = 380+x_pos
            dpg.configure_item("c_win",  width=WIDTH)
            sleep(0.001)
    else:
        while i <= 1:
            x_pos = int((1 - math.pow((1 - i), 8)) * 50)
            i += 0.03
            WIDTH = 50 - x_pos
            dpg.configure_item("c_win",  width=WIDTH)
            sleep(0.001)
        dpg.configure_item("c_win", width=50)
with dpg.window(label="Example Window") as main:
    dpg.add_text("Title")
    with dpg.group(horizontal=True):
        with dpg.child_window(width=50, border=True, tag="c_win"):
            dpg.add_button(label='S', callback=animate_window)
        with dpg.child_window(border=True):
            dpg.add_button(label='content')

dpg.set_primary_window(main, True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




