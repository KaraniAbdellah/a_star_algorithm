import customtkinter as ctk
from helper_func.helper import set_mode

class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid The Buttons Frame
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        def add_node():
            set_mode("Add Node")

        def add_arcs():
            set_mode("Add Arcs")

        def define_start():
            set_mode("Define Start")

        def define_end():
            set_mode("Define End")

        def launch():
            set_mode("Launch")

        def clear():
            set_mode("Clear")
 
        def save_logs():
            set_mode("Save")

        btns_values = [
            {"value": "Add Nodes", "column": 0, "row": 0, "color": "#328E6E", "function": add_node},
            {"value": "Add Arcs", "column": 1, "row": 0, "color": "#1B56FD", "function": add_arcs},
            {"value": "Define Start", "column": 0, "row": 1, "color": "#FF9B17", "function": define_start},
            {"value": "Define End", "column": 1, "row": 1, "color": "#F7374F", "function": define_end},
            {"value": "Launch", "column": 0, "row": 2, "color": "#8B44AD", "function": launch},
            {"value": "Clear", "column": 1, "row": 2, "color": "#5F7A76", "function": clear},
            {"value": "Save Graph", "column": 0, "row": 3, "color": "#8B4513", "function": save_logs},
        ]

        for btn_value in btns_values:
            self.btn = ctk.CTkButton(master=self, fg_color=btn_value["color"], 
                text=btn_value["value"], corner_radius=2, command=btn_value['function'])
            self.btn.grid(column=btn_value["column"], row=btn_value["row"], padx=4, pady=4, sticky="nsew")