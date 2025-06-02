import tkinter as tk;
from tkinter import ttk;

def button_sending():
    print("Sending ...")


# Create a window
window = tk.Tk()
window.title("Leanrning Widgets")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")

# Create Widgets
text = tk.Text(master=window)
text.pack()

label = ttk.Label(master=window, text="Click to send")
label.pack()

ex_label = ttk.Label(master=window, text="My Label")
ex_label.pack() 

# ttk button
button = ttk.Button(master=window, text="Send", command=button_sending)
button.pack()

ex_button = ttk.Button(master=window, text="Click Here", command= lambda: print("Hello"))
ex_button.pack()


# main loop --> update widgets
window.mainloop()



