import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Title Here")
        self.button = ctk.CTkButton(master=self, text="Test")
        self.button.pack(side="top", fill="both", expand=False)
        
        self.frame = ctk.CTkFrame(master=self, width=10, height=20)
        self.frame.pack(side="top", fill="both", expand=True)
        self.frame.pack_propagate(False)
        self.frame.configure(border_width=2, fg_color="grey")
        
        self.label1 = ctk.CTkLabel(master=self.frame, text="I am Lebel in Frame", fg_color='green')
        self.label1.pack(pady=10, padx=10)
        
        self.label2 = ctk.CTkLabel(master=self, text="I am Lebel in Window", fg_color='green')
        self.label2.pack(pady=10, padx=10)
                
        
app = App()
app.mainloop()
        
