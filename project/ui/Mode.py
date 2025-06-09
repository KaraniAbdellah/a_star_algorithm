import customtkinter as customtkinter
from helper_func.helper import current_mode, mode_label

class Mode(customtkinter.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        global mode_label

        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        mode_label = customtkinter.CTkLabel(master=self, text=f"Mode: {current_mode}",
            fg_color="transparent", text_color="black", anchor="w", font=("Arial", 16))

        mode_label.grid(row=0, column=0, sticky="sw", padx=5)