import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self)
        self.label.pack()
        self.label.configure(fg_color="red")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Title Here")
        self.button = ctk.CTkButton(master=self, text="Test")
        self.button.pack(side="top", fill="both", expand=False)
        
        self.frame = MyFrame(master=self)
        self.frame.pack(side="top", expand=True, fill="both")


app = App()
app.mainloop()
        
