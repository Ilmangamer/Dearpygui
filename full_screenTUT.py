from pickle import TRUE
import dearpygui.dearpygui as dpg
from sqlalchemy import false

dpg.create_context()
dpg.create_viewport(title='Custom Title', decorated=False, width=600, height=200)
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")

dpg.show_viewport()

# below replaces, start_dearpygui()
dpg.maximize_viewport()

start = True
while dpg.is_dearpygui_running():
    if start:
        dpg.toggle_viewport_fullscreen()
        start = False
    dpg.render_dearpygui_frame()


    

dpg.destroy_context()