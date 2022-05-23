import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(tag="winapi"):
    dpg.add_text("some data")
    dpg.add_button(label="B")

dpg.create_viewport(title="data_obj", width=500, height=250)

dpg.setup_dearpygui()
dpg.show_viewport()

# fills the viewport. Draws always behind other windows.
dpg.set_primary_window("winapi", True)

# instead of start dearpygui
# This renders in a loop throught every frame
while dpg.is_dearpygui_running():
    print("1")


    dpg.render_dearpygui_frame()


dpg.destroy_context()




