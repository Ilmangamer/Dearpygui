import dearpygui.dearpygui as dpg
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

# theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255,255,224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255,255,224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (100, 175, 227), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 100)
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 14)

# Font + Theme for all widgets
with dpg.font_registry():
    de_font = dpg.add_font("C:/Users/kodjo/Downloads/Maven_Pro/static/MavenPro-Regular.ttf",20)
    sec_font = dpg.add_font("C:/Users/kodjo/Downloads/Maven_Pro/static/MavenPro-Regular.ttf", 13)
    dpg.bind_font(de_font)
    dpg.bind_theme(global_theme)

# main window
with dpg.window(label="window", tag="main_window", horizontal_scrollbar=True):
    dpg.add_text("Lenovo", color= (0,0,0), pos=[1000, 80])
dpg.add_child_window(pos=[400, 110], label="child_window", tag= "big child window", parent="main_window", width=1450, height=850, horizontal_scrollbar=True)


images =["C:/Python data/menu/menu3.png", "C:/Most used/Tverrfaglig x64 pictures/MicrosoftTeams-image.png"]


                        
for b in images:
    width, height, channels, data = dpg.load_image(b)
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, data, tag=b)



# Small child windows
w=180
h=190
class Small_Child_windows():
    def __init__(self, pos, parent, width=w, height=h):
        self.pos = pos
        self.parent = parent
        self.width = width
        self.height = height
        
        with dpg.child_window(pos=pos, parent=parent, width=w, height=h, horizontal_scrollbar=True):
             # dpg.add_image_button("eq")
                 smaller_text = dpg.add_text("Trykk på bildet for å se nærmere.", pos=[10, 130])
                 dpg.add_text("Nyhet", pos=[70, 10])
                 dpg.bind_item_font(smaller_text, sec_font)
       
    def image_func(b):
            dpg.add_image_button(b)

for i in range(150, 1850, 220):
        for y in [70, 320, 570, 820]:
            for b in images:
                s_window = Small_Child_windows([i, y], "big child window", width=width, height=h)
                s_window.dpg.add_image_button(b)
dpg.create_viewport(title='title', x_pos=0, y_pos=0, width=333, height=333)
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.toggle_viewport_fullscreen()
dpg.destroy_context()