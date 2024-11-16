import subprocess
import tkinter as tk
from tkinter import messagebox, colorchooser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import itertools

# -----------------------------
# Global Configuration
# -----------------------------
RAINBOW_COLORS = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"]
color_offset = 0  # Color offset for the rainbow title animation


# -----------------------------
# General Helpers
# -----------------------------
def execute_command(command):
    """Executes a shell command and handles errors."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing the command:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")


def clear_window():
    """Removes all widgets from the main window."""
    for widget in root.winfo_children():
        widget.destroy()


# -----------------------------
# Rainbow Title Functions
# -----------------------------
def create_rainbow_title(container, text):
    """Creates an animated rainbow-colored title."""
    # Clear previous widgets from the container
    for widget in container.winfo_children():
        widget.destroy()

    # Create labels for each character
    labels = []
    for char in text:
        label = ttk.Label(container, text=char, font=('Arial', 24, 'bold'))
        label.pack(side="left")
        labels.append(label)

    # Start the rainbow animation
    update_rainbow_colors(labels)


def update_rainbow_colors(labels):
    """Dynamically updates the colors of the rainbow title."""
    global color_offset
    num_colors = len(RAINBOW_COLORS)

    # Assign shifted colors to the letters
    for i, label in enumerate(labels):
        label.config(foreground=RAINBOW_COLORS[(i + color_offset) % num_colors])

    # Increment the offset
    color_offset = (color_offset - 1) % num_colors

    # Repeat the animation every 500 ms
    labels[0].after(500, lambda: update_rainbow_colors(labels))


# -----------------------------
# Interface Functions
# -----------------------------
def show_main_menu():
    """Displays the main menu with the title and buttons."""
    clear_window()

    # Create a frame for the main menu
    menu_frame = ttk.Frame(root)
    menu_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Create the rainbow title
    title_container = ttk.Frame(menu_frame)
    title_container.grid(row=0, column=0, pady=20)
    create_rainbow_title(title_container, "Aura for Linux")

    # Create main buttons
    for row, (label, command) in enumerate(main_commands.items()):
        button = ttk.Button(menu_frame, text=label, command=command, bootstyle="success-outline")
        button.grid(row=row + 1, column=0, padx=5, pady=5, sticky="ew")

    # Display version text at the bottom
    version_label = ttk.Label(
        menu_frame, text="v0.0.1", font=("Arial", 10), foreground="#00ff00", bootstyle="secondary"
    )
    version_label.grid(row=len(main_commands) + 2, column=0, padx=5, pady=10, sticky="se")

    # Configure column expansion in the main menu
    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.grid_rowconfigure(len(main_commands) + 2, weight=1)


def show_color_buttons(mode):
    """Displays buttons to control colors in the selected mode."""
    clear_window()

    # Create a frame for color buttons
    color_frame = ttk.Frame(root)
    color_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Commands and labels dynamically adapted to the mode
    commands = {
        "White": f"asusctl led-mode {mode} -c ffffff",
        "Green": f"asusctl led-mode {mode} -c 00ff00",
        "Blue": f"asusctl led-mode {mode} -c 0000ff",
        "Yellow": f"asusctl led-mode {mode} -c ffff00",
    }

    # Create buttons for each command
    for row, (label, command) in enumerate(commands.items()):
        button = ttk.Button(color_frame, text=label, command=lambda cmd=command: execute_command(cmd), bootstyle="success-outline")
        button.grid(row=row, column=0, padx=5, pady=5, sticky="ew")

    # Button for custom color
    custom_button = ttk.Button(color_frame, text="Custom Color", command=lambda: set_custom_color(mode), bootstyle="success-outline")
    custom_button.grid(row=len(commands), column=0, padx=5, pady=5, sticky="ew")

    # Button to return to the main menu
    back_button = ttk.Button(color_frame, text="Back", command=show_main_menu, bootstyle="danger-outline")
    back_button.grid(row=len(commands) + 1, column=0, padx=5, pady=5, sticky="ew")

    # Configure column expansion in the color frame
    color_frame.grid_columnconfigure(0, weight=1)


def set_custom_color(mode):
    """Allows the user to select a custom color."""
    color_code = colorchooser.askcolor(title="Select a Color")
    if color_code and color_code[1]:
        color_hex = color_code[1][1:]  # Remove the '#' at the beginning
        command = f"asusctl led-mode {mode} -c {color_hex}"
        execute_command(command)


# -----------------------------
# Application Configuration
# -----------------------------
root = ttk.Window(themename="cyborg")
root.title("Aura for Linux")
root.geometry("800x600")

# Global expansion configuration
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Dictionary of main commands
main_commands = {
    "STATIC": lambda: show_color_buttons("static"),
    "BREATHE": lambda: show_color_buttons("breathe"),
    "PULSE": lambda: show_color_buttons("pulse"),
    "RAINBOW-CYCLE": lambda: execute_command("asusctl led-mode rainbow-cycle"),
    "RAINBOW-WAVE": lambda: execute_command("asusctl led-mode rainbow-wave"),
    "OFF": lambda: execute_command("asusctl -k off"),
}

# Show the main menu at the start
show_main_menu()

# Run the application
root.mainloop()
