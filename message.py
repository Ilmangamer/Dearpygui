from re import X
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
    de_font = dpg.add_font("C:/Users/nathand/Downloads/Maven_Pro/static/MavenPro-Regular.ttf",20)
    sec_font = dpg.add_font("C:/Users/nathand/Downloads/Maven_Pro/static/MavenPro-Regular.ttf", 13)
    dpg.bind_font(de_font)
    dpg.bind_theme(global_theme)


# image for image button
def btn():
    print("press me")

width, height, channels, data = dpg.load_image("C:/map for pic/green menu_icon.jpg")

with dpg.texture_registry(show=False):
    dpg.add_static_texture(width, height, data, tag="texture_tag")



def animate_window():
    i = 0
    if dpg.get_item_configuration("c_win")['width'] < 280:
        while i <= 1:
            x_pos = int((1 - math.pow((i-1), 8)) * 50)
            i += 0.03
            width = 280+x_pos
            dpg.configure_item("c_win",  width=width)
            sleep(0.001)
    else:
        while i <= 1:
            x_pos = int((1 - math.pow((1 - i), 8)) * 50)
            i += 0.03
            width = 50 - x_pos
            dpg.configure_item("c_win",  width=width)
            sleep(0.001)
        dpg.configure_item("c_win", width=50)


with dpg.window(label="about us", modal=True, no_resize= True, no_move=True, no_background=False, show=False, id="modal_id", no_title_bar=True):
    dpg.add_text("We are a group of minor teens, that sell Pc services (Salg på pc-komponenter)")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", width=90, height=30, callback=lambda: dpg.configure_item("modal_id", show=False))
        with dpg.child_window(width=50, border=True, tag="c_win", callback=animate_window):
            dpg.add_image_button("texture_tag")
            dpg.add_button(pos=[100,180], width=1350, height=30, callback=lambda: dpg.configure_item("modal_id", show=False))
            dpg.add_text("About us", pos=[120, 180])
            
    
with dpg.window(label="window", tag="main_window", horizontal_scrollbar=True):
    dpg.add_text("Lenovo", color= (0,0,0), pos=[1000, 80])

    #dpg.add_child_window(pos=[400, 110], label="child_window", tag= "big child window", parent="main_window", width=1450, height=850, horizontal_scrollbar=True)

"""
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
            dpg.add_text("Nyhed", pos=[70, 10])
            smaller_text = dpg.add_text("Trykk på bildet for å se närmere.", pos=[10, 130])
            dpg.bind_item_font(smaller_text, sec_font)
             
            
        
 
# Function for clicking small windows
    #def on_click(self):
       # if dpg.is_mouse_button_clicked(button=dpg.mvMouseButton_Left):
            #with dpg.popup(mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
              #  dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))
#dpg.show_documentation()

    dpg.show_style_editor()
# Placing child_windows in (i, y) coordinates, for every small child_windows.
for i in range(150, 1850, 220):
    for y in [70, 320, 570, 820]:
        s_window = Small_Child_windows([i, y], "big child window", width, height)
   """     
# Adjusting for each monitors
MonitorInfo = []
for m in get_monitors():
    if m.is_primary:
        MonitorInfo = str(m)
        MonitorHeight = m.height
        MonitorWidth = m.width

# creating viewport + showing window
dpg.create_viewport(title='title', x_pos=0, y_pos=0, width=MonitorWidth, height=MonitorHeight)
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.get_total_time()
dpg.destroy_context()