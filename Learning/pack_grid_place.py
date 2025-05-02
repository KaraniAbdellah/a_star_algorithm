import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Grid")

        self.menu_frame = ctk.CTkFrame(master=self, fg_color="grey")
        self.main_frame = ctk.CTkFrame(master=self, fg_color="grey")

        self.menu_frame.pack(side="left", expand=True, fill="both")
        self.main_frame.pack(side="right", expand=True, fill="both")
        
        # Grid The Menu Frame
        self.menu_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.menu_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')


        self.button1 = ctk.CTkButton(master=self.menu_frame,
                                    fg_color="#f1f1f1", text_color="black")
        self.button1.grid(row=0, column=0, sticky='nswe', columnspan=2)
        self.button2 = ctk.CTkButton(master=self.menu_frame,
                                    fg_color="#eee", text_color="black")
        self.button2.grid(row=0, column=2, sticky='nswe', columnspan=1)
        self.button3 = ctk.CTkButton(master=self.menu_frame,
                                    fg_color="#444", text_color="black")
        self.button3.grid(row=1, column=0, sticky='nswe',columnspan=3)
        
        self.slider1 = ctk.CTkSlider(master=self.menu_frame, from_=0, to=100)
        self.slider1.grid(row=2, column=0)
        self.slider2 = ctk.CTkSlider(master=self.menu_frame, from_=0, to=100)
        self.slider2.grid(row=2, column=2)

        self.bottom_frame = ctk.CTkFrame(master=self.menu_frame)
        self.bottom_frame.grid(column=0, row=3, columnspan=3, sticky="nswe")
        self.bottom_frame.rowconfigure((0, 1), weight=1)
        self.bottom_frame.columnconfigure((0, 1), weight=1)
        
        self.radio_var = tk.IntVar(value=0)
        self.radiobutton_1 = ctk.CTkRadioButton(self.bottom_frame, text="CTkRadioButton 1", variable= self.radio_var, value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self.bottom_frame, text="CTkRadioButton 2", variable= self.radio_var, value=2)
        self.entry = ctk.CTkEntry(master=self.bottom_frame)
        
        self.radiobutton_1.grid(row=0, column=0, sticky="ns")
        self.radiobutton_2.grid(row=0, column=1, sticky="ns")
        self.entry.grid(row=1, column=0, columnspan=2, sticky="nswe")
        
        # Grid The Main Frame
        self.main_frame.columnconfigure((0, 1), weight=1, uniform='a')
        self.main_frame.rowconfigure((0, 1), weight=1, uniform='a')

        self.label1 = ctk.CTkLabel(master=self.main_frame, text="Label1", bg_color="red")
        self.label2 = ctk.CTkLabel(master=self.main_frame, text="Label2", bg_color="green")
        self.label3 = ctk.CTkLabel(master=self.main_frame, text="Label3", bg_color="yellow")
        self.label4 = ctk.CTkLabel(master=self.main_frame, text="Label4", bg_color="orange")
        
        self.label1.grid(row=0, column=0, sticky="nswe")
        self.label2.grid(row=0, column=1, sticky="nswe")
        self.label3.grid(row=1, column=0, sticky="nswe")
        self.label4.grid(row=1, column=1, sticky="nswe")

        
        
app = App()
app.mainloop()

