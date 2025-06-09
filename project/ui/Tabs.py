import customtkinter as ctk

class Tabs(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        # Create tab buttons
        self.logs_btn = ctk.CTkLabel(master=self, text="Results", fg_color="#4682B4")
        self.logs_btn.grid(column=0, row=0, sticky="nswe", columnspan=2)