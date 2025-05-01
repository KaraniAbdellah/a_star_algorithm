import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Grid")

        # Create Frame
        self.frame = ctk.CTkFrame(master=self, width=10, height=20)
        self.frame.pack(side="top", fill="both", expand=True)
        self.frame.configure(fg_color="grey")

        # Create Labels
        self.button1 = ctk.CTkLabel(master=self.frame, text="button1", fg_color="red")
        self.button2 = ctk.CTkLabel(master=self.frame, text="button2", fg_color="red")

        # define grid --> columnconfigure() --> create columns
        # weight of column if weight big he take more space
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        # We Have Two Columns and One Row
        
        # Place Label in Grid Layout 
        self.button1.grid(row=0, column=0, sticky="nswe", rowspan=1)
        self.button2.grid(row=0, column=1, sticky="n", columnspan=1)

        
app = App()
app.mainloop()
        
