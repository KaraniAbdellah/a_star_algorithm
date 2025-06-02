import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality



class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.title = ctk.CTkLabel(master=self)
        
        # Widgets
        self.menu = Menu(self)
        self.menu.pack()
        
        self.mainloop()
        

class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button1 = ctk.CTkButton(master=self, text="Button1")
        self.button1.pack()
        

App("Classes", (600, 600))





