'''
    - You Need to make own components
    - We need to know "after method"
    - Widget can be updated in real time using
        either configure or the layout methods
    - important:
        when we want to animate widgets we can use place
        it is the only one that can change  values pixel by pixel
    
    - After is method of Tk that can call a function after some time:
        window.after(1000, func)
        def func():
            print("Hello, See You After 1 Second")
            window.after(1000, func)
'''



import customtkinter as ctk;
from random import choice;


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)
        # general attributes
        self.start_pos = start_pos - 0.3
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # Animation Logic
        self.pos = self.start_pos
        self.in_start_pos = True
        # Layout
        self.place(relx=self.start_pos,rely=0,
            relwidth=self.width, relheight=1)
    def animate(self):
        print("Hello")
        if(self.in_start_pos): 
            self.animate_forward()
        else: self.animate_backwards()
        
    def animate_forward(self):
        print("Animate For Ward")
        if (self.pos < 0):
            self.pos += 0.01
            self.place(relx=self.pos,rely=0,
            relwidth=self.width, relheight=1)
            self.after(10, self.animate_forward)
        else: self.in_start_pos = False
        
    def animate_backwards(self):
        print("Animate For Ward")
        if (self.pos >= self.start_pos):
            self.pos -= 0.01
            self.place(relx=self.pos,rely=0,
            relwidth=self.width, relheight=1)
            self.after(10, self.animate_backwards)
        else: self.in_start_pos = True
        
class App(ctk.CTk):
    button_x = 0.5
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Animated Widgets")

        def move_btn(): 
            self.button_x += 0.001
            print(self.button_x)
            self.button.place(anchor="center",
                relx=self.button_x, rely=0.5)
            # self.after(10, move_btn)
            # # Configure
            # colors = ['red', "green", "yellow", "pink"]
            # color = choice(colors)
            # self.button.configure(fg_color=color)

        def infinite_print():
            print("Infinite")
            self.after(1000, move_btn)

        self.animated_panel = SlidePanel(self, 0, -0.3)
        self.label = ctk.CTkLabel(self.animated_panel, text="Logs").pack()
        self.label = ctk.CTkLabel(self.animated_panel, text="Adjacency Matrix").pack()
        
        self.button = ctk.CTkButton(master=self, 
            text="Show Logs",
            command=self.animated_panel.animate)
        self.button.place(anchor="sw",
                relx=0, rely=1)
        

window = App()
window.mainloop()
