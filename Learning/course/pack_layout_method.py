# Start Learning Pack
import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenwidth()
        self.geometry(f"{screen_width}x{screen_height}")
        self.title("The Packet Layout")

        # add Widgets like (buttons, labels, ...)
        self.button = ctk.CTkButton(self, command=self.button_click)
        self.lable1 = ctk.CTkLabel(master=self, text="First Label", bg_color='red')
        self.lable2 = ctk.CTkLabel(master=self, text="Second Label", bg_color='blue')
        self.lable3 = ctk.CTkLabel(master=self, text="Thirth Label", bg_color='green')

        # Layout
        '''
            Expand: True --> will occupay all space
            fill: both --> fill x and y spaces
        '''
        self.lable1.pack(side='top', expand=True, fill="both", pady=10, padx=10)
        self.lable2.pack(side='left', expand=True, fill="both")
        self.lable3.pack(side='top', expand=True, fill="both")
        self.button.pack(side='top', expand=True, fill="both")

    def button_click(self):
        print("Hello World")

app = App()
app.mainloop()

