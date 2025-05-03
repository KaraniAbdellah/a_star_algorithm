import customtkinter as ctk 


class Buttons(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.add_node = ctk.CTkButton(master=self, text="Add Node")
        self.add_arcs = ctk.CTkButton(master=self, text="Add Arcs")
        self.define_start = ctk.CTkButton(master=self, text="Define Start")
        self.define_end = ctk.CTkButton(master=self, text="Define End")
        self.launch = ctk.CTkButton(master=self, text="Launch")
        self.clear = ctk.CTkButton(master=self, text="Clear")
        self.save_graph = ctk.CTkButton(master=self, text="Save Graph")
        self.load_graph = ctk.CTkButton(master=self, text="Load Graph")

        self.add_node.pack()
        self.add_arcs.pack()
        self.define_start.pack()
        self.define_end.pack()
        self.launch.pack()
        self.clear.pack()
        self.save_graph.pack()
        self.load_graph.pack()


class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.menu_frame = Buttons(self)
        self.menu_frame.pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title("A* Pathfinding Algorithm")

        # Make Left And Right Frames
        self.menu_frame = Menu(self)
        self.menu_frame.pack()

app= App()
app.mainloop()

