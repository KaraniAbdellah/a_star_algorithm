'''
    - You Need to make own components
    - We need to know "after method"
    - Widget can be updated in real time using
        either configure or the layout methods
    - important:
        when we want to animate widgets we can use place
        it is the only one that can change  values pixel by pixel
'''


import customtkinter as ctk;

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("The Animated Widgets")

        self.button = ctk.CTkButton(self, text="Click")
        self.button.pack()

app = App()
app.mainloop()




