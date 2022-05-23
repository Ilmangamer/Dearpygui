import dearpygui.dearpygui as dpg

dpg.create_context()


def buttn_cb():
    print('i got pressed')

width, height, channels, data = dpg.load_image("C:/Python data/menu/menu3.png")

with dpg.texture_registry(show=True):
    dpg.add_static_texture(width, height, data, tag="texture_tag")

with dpg.window(label="Tutorial"):
    dpg.add_image_button("texture_tag", callback=buttn_cb)


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()