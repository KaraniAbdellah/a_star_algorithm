import customtkinter as ctk
from tkinter import simpledialog, messagebox

# Define Global Variable For Mode
current_mode = "null"

# Define Global Variable For Logs
content = ""

# Global references for UI elements
output_instance = None
mode_label = None

def set_mode(new_mode):
    global current_mode
    current_mode = new_mode

    if 'mode_label' in globals() and mode_label is not None:
        mode_label.configure(text=f"Mode: {new_mode}")

def set_content(new_content):
    global content
    content = new_content

    if 'output_instance' in globals() and output_instance is not None:
        output_instance.delete("1.0", "end") # delete first the content
        output_instance.insert("1.0", new_content)  # Insert New Content