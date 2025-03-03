import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttk

'''
    Widgets is Buttons, text, checkboxes, menus, frames, etc
    
    Tkinter has 2 set of widgets:
        tk widget were the original ones
        ttk widgets were added later on (these are much more modern)
    
    Widgets has config method to update widget
        Label.config(text='some new text')
        Label['text'] = 'Some new text'
    
    mainloop():
        update the gui
        checks for events (button clicks, mouse mouvments, closing window)
'''


def button_disabled_fun():
    # get the content of entry
    print(myEntry.get())
    # update label
    # myLabel.configure(text="New Title")
    myLabel['text'] = "Another New Title"
    myEntry['state'] = "disabled"
    print(myLabel.configure())

def button_enbaled_fun():
    myEntry["state"] = 'enabled'

def button_disabled_fun():
    myEntry["state"] = 'disabled'


# Create Window
myWindow = ttk.Window(title="Widgets and Window", themename="darkly")
myWindow.geometry("200x200")


# Create Label
myLabel = ttk.Label(master=myWindow, font='Calibri 24 bold', text="This is a test")   
myLabel.pack(pady=5)

# Create TextArea
myText = ttk.Text(master=myWindow, bg="#eee", width=100, height=10, padx=3, pady=3)
myText.pack(pady=5)


# Create Entry or Input
myEntry = ttk.Entry(master=myWindow)
myEntry.pack(pady=5)


# Create A Button
myButton = ttk.Button(master=myWindow, text="A Button", command=button_disabled_fun)
myButton.pack(pady=5)

# Create A Button
myButton = ttk.Button(master=myWindow, text="Enabled", command=button_enbaled_fun)
myButton.pack(pady=5)

# Run
myWindow.mainloop()



# Old Method with tk
# root = tk.Tk()
# root.title("myWindow")
# root.geometry("200x400")

# text = tk.Text(master=root)
# text.pack()


# root.mainloop()