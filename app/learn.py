# Import Required Module
from tkinter import *


# Create Object
root = Tk()
root.title("learn")
root.geometry("1000x600")


# Widgets
nodes_frame = Frame(root, bg='yellow')
matrix_frame = Label(root, text="label 2", background="blue")
button1 = Button(root, text="run")


# define grid
root.rowconfigure(0, minsize=30)  # First row 
root.rowconfigure(1, weight=1)  # Second row  
root.columnconfigure(0, weight=1)  # First column  
root.columnconfigure(1, weight=1)  # Second column  


# Place other widgets in the main grid
button1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
nodes_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
matrix_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)


# Create 20 button for nodes_frame
for i in range(20):
    nodes_frame.columnconfigure(i, weight=1)
    nodes_frame.rowconfigure(i, weight=1)


# Function For Change The Button Content
def changeContent():
    button1.config(text="Running")


button1.bind("<Button-1>", lambda event: changeContent())




# Execute Tkinter
root.mainloop()
