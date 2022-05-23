import dearpygui.dearpygui as dpg

filelist = ["C:/Python data/menu/menu3.png", "C:/Most used/Tverrfaglig x64 pictures/MicrosoftTeams-image.png"]

dpg.create_context()
for img in filelist:
    width, height, channels, data = dpg.load_image(img)
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, data, tag=img)


wins = [dpg.add_window(label="Tutorial"), dpg.add_window(label="2")]
for i in wins:
    for img in filelist:
        dpg.add_image(img)


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()