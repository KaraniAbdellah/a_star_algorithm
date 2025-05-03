# Make Frame That Has All Buttons
# Import Packages
import customtkinter as ctk;
import tkinter as tk;
from tkinter import ttk; # provide addition functionality

class Buttons(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
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


        
