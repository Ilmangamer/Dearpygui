import dearpygui.dearpygui as dpg

# create context otherwise the program will never run
dpg.create_context()

# add for instance text, button, input_text, slider_float
with dpg.window(label="win32"):
    dpg.add_text(label="Some_text")
    dpg.add_button(label="click")
    dpg.add_input_text(label="", default_value="")
    dpg.add_slider_float(label="", default_value=0, max_value=1)

# create viewport
dpg.create_viewport(title="Data_obj created by my pc", width=600, height=250)

# run the app with setup_dpg, show_viewport, start_dpg and destroy_context
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
    