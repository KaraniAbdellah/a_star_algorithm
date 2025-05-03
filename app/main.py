import customtkinter as ctk 


class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        btns_values = ["Add Node", "Add Arcs", "Define Start", "Define End", 
            "Launch", "Clear", "Save Graph", "Load Graph"]
        
        for btn_value in btns_values:
            self.btn = ctk.CTkButton(master=self, text=btn_value)
            self.btn.pack()


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

        # Frame Contain Buttons
        self.menu_frame = Buttons(self)
        self.menu_frame.pack()
        
        # Frame Contain Logs and Adj
        self.logs_adj = Logs_Adj(self)
        self.logs_adj.pack()
        
        
                



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title("A* Pathfinding Algorithm")

        # Grid The Window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        
        # Make Left And Right Frames
        self.menu_frame = Menu(self, fg_color="red")
        self.menu_frame.grid(column=0, sticky="nswe")

app= App()
app.mainloop()

