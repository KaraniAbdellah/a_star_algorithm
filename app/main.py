import customtkinter as ctk 


class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid The Buttons Frame
        self.columnconfigure([0, 1], weight=1)
        self.rowconfigure([0, 1, 2, 3], weight=1)

        btns_values = [
            {"value": "Add Node", "column": 0, "row": 0},
            {"value": "Add Arcs", "column": 1, "row": 0},
            {"value": "Define Start", "column": 0, "row": 1},
            {"value": "Define End", "column": 1, "row": 1},
            {"value": "Launch", "column": 0, "row": 2},
            {"value": "Clear", "column": 1, "row": 2},
            {"value": "Save Graph", "column": 0, "row": 3},
            {"value": "Load Graph", "column": 1, "row": 3}
        ]

        for btn_value in btns_values:
            self.btn = ctk.CTkButton(master=self, text=btn_value["value"])
            self.btn.grid(column=btn_value["column"], row=btn_value["row"])


class Logs_Adj(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.logs = ctk.CTkLabel(master=self, text="Logs")
        self.adj = ctk.CTkLabel(master=self, text="Adjcency matrix")
        self.logs.pack()
        self.adj.pack()
        


class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Grid For Menu
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)
        
        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        
        # Frame Contain Logs and Adj
        self.logs_adj = Logs_Adj(self)
        self.logs_adj.grid(row=1, column=0, columnspan=2, sticky="nswe")
        
        # Mode Element
        self.mode_ele = ctk.CTkLabel(master=self, text="Loading Mode...")
        self.mode_ele.grid(row=2, column=1, columnspan=2, sticky="nswe")
        



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title("A* Pathfinding Algorithm")

        # Grid The Window
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        
        # Make Left And Right Frames
        self.menu_frame = Menu(self, fg_color="grey")
        self.menu_frame.grid(column=0, row=0, sticky="nswe", pady=10, padx=10)
        
        
        

app= App()
app.mainloop()

