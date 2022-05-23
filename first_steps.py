import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport(title="First dpg app", width=500, height= 500)

with dpg.window(label= "My window"):
    dpg.add_text("Hello world!" )
    dpg.add_button(label="Save")
# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
