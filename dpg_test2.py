import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Example window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="save")
    dpg.add_input_text(label="string", default_value="Quick Brown fox")

    dpg.create_viewport(title="Custom title", width=600, height=200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
