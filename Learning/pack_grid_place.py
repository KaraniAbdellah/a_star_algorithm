import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Grid")

        self.frame_left = ctk.CTkFrame(master=self, fg_color="grey")
        self.frame_left.pack(side="left", expand=True, fill="both")

        self.frame_right = ctk.CTkFrame(master=self)
        self.frame_right.pack(side="right", expand=True, fill="both")

        # grid for left frame
        self.frame_left.columnconfigure(0, weight=0)
        self.frame_left.columnconfigure(1, weight=0)
        self.frame_left.columnconfigure(2, weight=0)
        
        self.button1 = ctk.CTkButton(master=self.frame_left, text="Button1")
        self.button2 = ctk.CTkButton(master=self.frame_left, text="Button2")
        self.button3 = ctk.CTkButton(master=self.frame_left, text="Button3")

        self.button1.grid(row=0, column=0, columnspan=1,sticky="nswe")
        self.button2.grid(row=0, column=1, columnspan=1,sticky="nswe")
        self.button3.grid(row=1, column=0, columnspan=1,sticky="nswe")
        
        


        
        
        
app = App()
app.mainloop()

