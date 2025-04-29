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

        self.button1 = ctk.CTkButton(master=self.frame_left, text="Button1")
        self.button2 = ctk.CTkButton(master=self.frame_left, text="Button2")
        self.button3 = ctk.CTkButton(master=self.frame_left, text="Button3")
        self.button1.pack(side="right")
        self.button2.pack(side="left")
        self.button3.pack(side="top")

        self.radio1 = ctk.CTkRadioButton(master=self.frame_left)
        self.radio2 = ctk.CTkRadioButton(master=self.frame_left)
        self.radio1.pack()
        self.radio2.pack()
        
        self.checkbox1 = ctk.CTkCheckBox(master=self.frame_left)
        self.checkbox2 = ctk.CTkCheckBox(master=self.frame_left)
        self.checkbox1.pack()
        self.checkbox2.pack()

        self.sub_frame_right1 = ctk.CTkFrame(master=self.frame_right, fg_color="red")
        self.sub_frame_right2 = ctk.CTkFrame(master=self.frame_right, fg_color="blue")
        self.sub_frame_button1 = ctk.CTkFrame(master=self.frame_right, text="Button 3")
        self.sub_frame_button2 = ctk.CTkFrame(master=self.frame_right, text="Button 4")
        self.sub_frame_right1.pack()
        self.sub_frame_right2.pack()
        self.sub_frame_button1.pack()
        self.sub_frame_button2.pack()
        
        
        
        
        
app = App()
app.mainloop()

