import dearpygui.dearpygui as dpg
import os

# Initialize Dear PyGui
dpg.create_context()

# Create a theme that mimics Discord's dark theme
def create_discord_theme():
    with dpg.theme() as theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (54, 57, 63))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (220, 221, 222))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (114, 137, 218))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (128, 151, 232))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (104, 127, 208))
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 5)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
    return theme

# Custom font setup
def setup_fonts():
    with dpg.font_registry():
        # Try to load system fonts first
        font_paths = [
            "C:/Windows/Fonts/arial.ttf",  # Windows
            "/usr/share/fonts/truetype/arial.ttf",  # Linux
            "/Library/Fonts/Arial.ttf"  # MacOS
        ]
        
        for path in font_paths:
            if os.path.exists(path):
                return dpg.add_font(path, 20)
        
        # Fallback to Dear PyGui's default font
        return dpg.add_font(":default:", 20)

# Create resources
default_font = setup_fonts()
discord_theme = create_discord_theme()

# Main window creation
with dpg.window(tag="main_window", label="Discord Font Display"):
    dpg.bind_theme(discord_theme)
    
    if default_font:
        dpg.bind_font(default_font)
    
    # Header
    dpg.add_text("Custom Discord Font Display", color=(114, 137, 218))
    dpg.add_separator()
    
    # Text examples
    dpg.add_text("This is regular text")
    dpg.add_text("This is colored text", color=(114, 137, 218))
    
    # Formatting examples
    with dpg.group(horizontal=True):
        dpg.add_text("This is ")
        dpg.add_text("bold", color=(255, 255, 255))
    
    with dpg.group(horizontal=True):
        dpg.add_text("This is ")
        dpg.add_text("italic", color=(200, 200, 200))
    
    # Input and button
    dpg.add_spacer(height=10)
    dpg.add_input_text(label="Type something", tag="user_input", width=400)
    dpg.add_button(label="Send", callback=lambda: send_message("main_window"))

def send_message(parent):
    user_input = dpg.get_value("user_input")
    if user_input.strip():
        with dpg.group(parent=parent):
            dpg.add_text(f"You: {user_input}", color=(220, 221, 222))
        dpg.set_value("user_input", "")

# Create viewport
dpg.create_viewport(title='Discord Font Display', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

# This is the critical fix - we need to set the primary window AFTER showing the viewport
dpg.set_primary_window("main_window", True)

# Start the app
dpg.start_dearpygui()
dpg.destroy_context()