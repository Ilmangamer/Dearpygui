import dearpygui.dearpygui as dpg
import math
from screeninfo import get_monitors
from screeninfo import get_monitors
from time import sleep
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
    bigger_font = dpg.add_font("C:/Users/kodjo/Downloads/Maven_Pro/static/MavenPro-Regular.ttf", 29)
    dpg.bind_font(de_font)
    dpg.bind_theme(global_theme)

# File path for menuicon. In additon setting the image
width, height, channels, data = dpg.load_image("C:/Python data/menu/Meny_ikon_hvit_utgave_2.png")
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width, height, data, tag="tag_for_menu")

# File path for main icon. In additon setting the image
width, height, channels, data = dpg.load_image("C:/Users/kodjo/Downloads/MicrosoftTeams-image.png")
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width, height, data, tag="tag_for_main_icon")

# animating menu window
def animate_window():
    i = 0
    if dpg.get_item_configuration("c_win")['width'] < 250:
        while i <= 1:
            x_pos = int((1 - math.pow((1 - i), 8)) * 50)
            i += 0.03
            WIDTH = 280+x_pos
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


# Creating main window and a child window(in other words menu window) 
# Adding a menu window + other widgets, on the main window
with dpg.window(label="window", tag="main_window", horizontal_scrollbar=True):
    dpg.add_image("tag_for_main_icon")
    with dpg.group(horizontal=True):
        with dpg.child_window(width=50, border=True, tag="c_win"):
              dpg.add_image_button("tag_for_menu", callback=animate_window)
              dpg.add_button(pos=[100,180], width=1350, height=30, callback=lambda: dpg.configure_item("modal_id", show=True))
              dpg.add_button(pos=[100,300], width=1350, height=30, callback=lambda: dpg.configure_item("modal_id2", show=True))
              dpg.add_text("About us", pos=[120, 180])
              dpg.add_text("Contact us", pos=[120, 300])
              

# Creating information windows        
with dpg.window(no_move=True, modal=True, width=750, height=600, show=False, tag="modal_id", no_title_bar=True):
    dpg.add_text("Vi er en mindreåriggruppe profesjonelle IT konsulenter, som selger omfattende Pc tjenester. \n For mer informasjon, besøk nettsiden")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", pos=[34, 500], width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
     
with dpg.window(no_move=True, modal=True, width=750, height=600, show=False, tag="modal_id2", no_title_bar=True):
    dpg.add_text("Kontakt utvikleren? \n Tlf: 45917534")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", pos=[34, 500], width=75, callback=lambda: dpg.configure_item("modal_id2", show=False))
   

# Creating big child window which holds the product information
dpg.add_child_window(pos=[400, 110], label="child_window", tag= "big child window", parent="main_window", width=1450, height=850, horizontal_scrollbar=True)
# loading images to big child window
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

# Small child windows width and height
w = 180
h = 190


image_names = ["laptopLen", "len2", "lenm", "lenm2", "dock", "dock2", "dock3", "len3", "len4", "mon", "mon2", "mus", "MicrosoftTeams-image (1)", "MicrosoftTeams-image (2)", "MicrosoftTeams-image (3)", "MicrosoftTeams-image (4)", "MicrosoftTeams-image (5)", "MicrosoftTeams-image (6)", "MicrosoftTeams-image (7)", "MicrosoftTeams-image (8)", "MicrosoftTeams-image (9)"]
load_images(image_paths=create_paths(image_names))


# Filelist for the windows that appear from the image_button


filelist = ["C:/Users/kodjo/Downloads/laptopLen.png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (1).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (2).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (3).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (4).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (5).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (6).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (7).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (8).png", "C:/Users/kodjo/Downloads/MicrosoftTeams-image (9).png","C:/Users/kodjo/Downloads/len2.png", "C:/Users/kodjo/Downloads/len3.png", "C:/Users/kodjo/Downloads/len4.png", 
"C:/Users/kodjo/Downloads/lenm.png", "C:/Users/kodjo/Downloads/lenm2.png", "C:/Users/kodjo/Downloads/mon.png", "C:/Users/kodjo/Downloads/mon2.png", "C:/Users/kodjo/Downloads/dock2.png", "C:/Users/kodjo/Downloads/dock3.png", "C:/Users/kodjo/Downloads/mus.png"
]


for img in filelist:
    width, height, channels, data = dpg.load_image(img)
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, data, tag=img)

with dpg.window(pos=[480, 125], no_move=True, modal=True, width=850, height=600, show=False, tag="ex_win", no_title_bar=True):
    dpg.group()
    dpg.add_separator()
    big_text = dpg.add_text("Sjekk disse rå PC tjenestene! Gå å handle dem på nettsiden.")
    dpg.bind_item_font(big_text, bigger_font)
    for img in filelist:
        dpg.add_image(img, width=200, height=200)
    dpg.add_button(label="Close", callback=lambda: dpg.configure_item("ex_win", show=False))


class Small_Child_windows():
    def __init__(self, pos, parent, image_key, width=w, height=h):
        self.pos = pos
        self.parent = parent
        self.width = width
        self.height = height
        self.image_key = image_key
        with dpg.child_window(pos=pos, parent=parent, width=w, height=h, horizontal_scrollbar=True):
            dpg.add_text("Nyhet", pos=[70, 10])
            dpg.add_image_button(image_key, pos=[15,33], width=145, height=110, callback=lambda: dpg.configure_item("ex_win", show=True))
            smaller_text = dpg.add_text("Trykk på bildet for å se nærmere.", pos=[10, 150])
            dpg.bind_item_font(smaller_text, sec_font)


# Function for clicking small windows
# Placing child_windows in (i, y) coordinates, for every small child_windows.
x = 0
for i in range(150, 2050, 380):
    for y in [70, 320, 570, 820]:
        try:
            s_window = Small_Child_windows([i, y], "big child window", f'text{x}',  w, h)
            print(f'text{x}')
            x = x + 1
        except Exception as exception:
            print(exception)
            x = 0


# Adjusting for each monitors
MonitorInfo = []
for m in get_monitors():
    if m.is_primary:
        MonitorInfo = str(m)
        MonitorHeight = m.height
        MonitorWidth = m.width

# creating viewport + showing window
dpg.create_viewport(title='title', x_pos=0, y_pos=0, width=MonitorWidth, height=MonitorHeight)
dpg.set_viewport_small_icon("C:/Users/kodjo/Downloads/MicrosoftTeams-image.ico")
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.toggle_viewport_fullscreen()
dpg.destroy_context()