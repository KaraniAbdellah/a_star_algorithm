# Import Required Module
from tkinter import *


# Create Object
root = Tk()
root.title("learn")


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


# Create 10 row and column for nodes_frame
for i in range(10):
    nodes_frame.columnconfigure(i, weight=1)
    nodes_frame.rowconfigure(i, weight=1)


# Function For Change The Button Content
def changeContent(btn, row, col):
    btn.config(bg="#FF7F50", font = ('Sans','10','bold'), fg="white", text=f"{row * 10 + col}")


# Update the binding to pass the row and column
for row in range(10):
    for col in range(10):
        button = Button(nodes_frame, width=2, height=2, bg="white")
        button.grid(row=row, column=col, sticky="nsew")
        button.bind("<Button-1>", lambda event, btn=button, row=row, col=col: changeContent(btn, row, col))



# Execute Tkinter
root.mainloop()
