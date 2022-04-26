


# Hover
import dearpygui.dearpygui as dpg

dpg.create_context(
)

with dpg.window(label="H"):
    dpg.add_text("Some label", tag= "tooltip_parent")
    dpg.add_button(label="Button", tag="tooltip_parent2")

with dpg.tooltip("tooltip_parent2"):
    dpg.add_text("Hover")


with dpg.tooltip("tooltip_parent"):
    dpg.add_text("Hover")

dpg.show_style_editor()

# Theme

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, ("0077C899"), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


dpg.create_viewport(title="win32", width=600, height=250)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


