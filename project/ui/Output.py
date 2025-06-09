import customtkinter as ctk
from helper_func.helper import content, output_instance

class Output(ctk.CTkFrame): 
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        global output_instance

        # Create text box
        output_instance = ctk.CTkTextbox(self, text_color="black", corner_radius=5, font=("JetBrains Mono", 16))
        output_instance.pack(side="top", fill="both", expand=True)
        output_instance.insert("0.0", content)