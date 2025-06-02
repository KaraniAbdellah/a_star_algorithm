import customtkinter as ctk 

# Output inherits from CTkFrame
# parent is Menu Frame
# self is Output instance [a CTkFrame]

class Output(ctk.CTkFrame): 
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        global output_instance

        # Create text box
        output_instance = ctk.CTkTextbox(self, text_color="black", corner_radius=5, font=("JetBrains Mono", 16))
        output_instance.pack(side="top", fill="both", expand=True)
        output_instance.insert("0.0", "content")

class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Output(self)
        self.output_frame.grid(row=2, column=0, sticky="nsew")


