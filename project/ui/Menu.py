import customtkinter as ctk
from ui.Buttons import Buttons
from ui.Output import Output
from ui.Mode import Mode
from ui.Tabs import Tabs

class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Grid For Menu
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=2)
        self.rowconfigure((2), weight=5)
        self.rowconfigure((1, 3), weight=0)

        # Mode Element [It Like Status Which Is {add node, add arcs, ...}]
        self.mode_ele = Mode(self)
        self.mode_ele.grid(row=3, column=0, sticky="nsew", pady=(10, 10))

        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")

        # Frame Contain Logs and Adjacency Matrix
        self.tabs_frame = Tabs(self, fg_color="#eee")
        self.tabs_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))

        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Output(self)
        self.output_frame.grid(row=2, column=0, sticky="nsew")

