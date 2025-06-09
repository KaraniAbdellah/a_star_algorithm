# ui/App.py
import customtkinter as ctk
from ui.Menu import Menu
from ui.Grid import Grid

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title("A* Pathfinding Algorithm")

        # Grid configuration
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        
        # Create frames
        self.menu_frame = Menu(self, fg_color="#EEEEEE")
        self.menu_frame.grid(column=0, row=0, sticky="nsew", pady=10, padx=10)

        self.grid = Grid(self, fg_color="#FFFFFF")
        self.grid.grid(column=1, row=0, sticky="nsew", pady=10, padx=10)