import dearpygui.dearpygui as dpg
from itertools import cycle
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

# theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (100, 175, 227), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 100)
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 14)

# Font + Theme for all widgets
with dpg.font_registry():
    de_font = dpg.add_font("C:/Users/kodjo/Downloads/Maven_Pro/static/MavenPro-Regular.ttf", 20)
    sec_font = dpg.add_font("C:/Users/kodjo/Downloads/Maven_Pro/static/MavenPro-Regular.ttf", 13)
    dpg.bind_font(de_font)
    dpg.bind_theme(global_theme)

# main window
with dpg.window(label="window", tag="main_window", horizontal_scrollbar=True):
    dpg.add_text("Lenovo", color=(0, 0, 0), pos=[1000, 80])
dpg.add_child_window(pos=[400, 110], label="child_window", tag="big child window", parent="main_window", width=1450,
                     height=850, horizontal_scrollbar=True)


def load_images(image_paths: list):
    for image_path in image_paths:
        width_image, height_image, channels, data = dpg.load_image(image_path)
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width_image, height_image, data, tag=f"text{image_paths.index(image_path)}")
            print(f"text{image_paths.index(image_path)}")

def create_paths(image_names_list: list):
    image_paths = []
    for image in image_names_list:
        image_paths.append(f'C:/Users/kodjo/Downloads/{image}.png')
    return image_paths


# Small child windows
w = 180
h = 190

image_names = ["laptopLen"]
load_images(image_paths=create_paths(image_names))

class Small_Child_windows():
    def __init__(self, pos, parent, image_key, width=w, height=h):
        self.pos = pos
        self.parent = parent
        self.width = width
        self.height = height
        self.image_key = image_key
        with dpg.child_window(pos=pos, parent=parent, width=w, height=h, horizontal_scrollbar=True):
            dpg.add_text("Nyhet", pos=[70, 10])
            dpg.add_image_button(image_key, pos=[15,33], width=145, height=110)
            smaller_text = dpg.add_text("Trykk på bildet for å se nærmere.", pos=[10, 130])
            dpg.bind_item_font(smaller_text, sec_font)


# Function for clicking small windows
# Placing child_windows in (i, y) coordinates, for every small child_windows.
x = 0
for i in range(150, 1850, 220):
    for y in [70, 320, 570, 820]:
        try:
            s_window = Small_Child_windows([i, y], "big child window", f'text{x}',  w, h)
            print(f'text{x}')
            x = x + 1
        except Exception as exception:
            print(exception)
            x = 0

dpg.create_viewport(title='title', x_pos=0, y_pos=0, width=333, height=333)
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.toggle_viewport_fullscreen()
dpg.destroy_context()
