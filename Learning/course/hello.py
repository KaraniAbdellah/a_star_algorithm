import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="darkly")
# window = ttk.Window(themename="journal")
window.title("Miles To Kilometer")
window.geometry("300x150")


# Function To Convert
def convert():
    print()
    km_output = entry_int.get() * 1.61
    output_string.set(f"Km = {km_output}")


# Widget 
title_label = ttk.Label(master=window, text="Miles To Kilometers", font="Calibri 24 bold")
title_label.pack()


# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="CLick Me", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
entry.pack()
input_frame.pack(pady=10)


# Output
output_string = tk.StringVar() 
output_label = ttk.Label(master=window,
        text='Output',
        font="Calibri 24 bold",
        textvariable=output_string)
output_label.pack(pady=5)


# run
window.mainloop()


