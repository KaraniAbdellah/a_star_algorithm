import customtkinter as ctk 

# Start Function
def show_logs():
    print("Hello Logs")

def show_adj_matrix():
    print("Hello Adjacency Matrix")


class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid The Buttons Frame
        self.columnconfigure([0, 1], weight=1)
        self.rowconfigure([0, 1, 2, 3], weight=1)

        btns_values = [
            {"value": "Add Nodes", "column": 0, "row": 0, "color": "#328E6E"},
            {"value": "Add Arcs", "column": 1, "row": 0, "color": "#1B56FD"},
            {"value": "Define Start", "column": 0, "row": 1, "color": "#FF9B17"},
            {"value": "Define End", "column": 1, "row": 1, "color": "#F7374F"},
            {"value": "Launch", "column": 0, "row": 2, "color": "#8B44AD"},  # Changed color to purple
            {"value": "Clear", "column": 1, "row": 2, "color": "#5F7A76"},   # Changed color to match design
            {"value": "Save Graph", "column": 0, "row": 3, "color": "#8B4513"},  # Changed color to brown
            {"value": "Load Graph", "column": 1, "row": 3, "color": "#1F7D53"}
        ]

        for btn_value in btns_values:
            self.btn = ctk.CTkButton(master=self, fg_color=btn_value["color"], 
                text=btn_value["value"], height=20, corner_radius=2)
            self.btn.grid(column=btn_value["column"], row=btn_value["row"], padx=5, pady=5, sticky="nsew")


class Output(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create text box
        self.text_box = ctk.CTkTextbox(self, fg_color="white", text_color="black")
        self.text_box.pack(side="top", fill="both", expand=True)


class Mode(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        
        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create status message at bottom
        self.mode_label = ctk.CTkLabel(master=self, text="Mode: define_end", fg_color="transparent",
            text_color="black", anchor="w", font=("Arial", 16))
        self.mode_label.grid(row=0, column=0, sticky="sw", padx=5)


class Tabs(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        # Create tab buttons
        self.logs_btn = ctk.CTkButton(master=self, text="Logs", 
            command=show_logs, fg_color="#4682B4", corner_radius=2)
        self.adj_matrix_btn = ctk.CTkButton(master=self, text="Adjacency Matrix", 
            command=show_adj_matrix, fg_color="#5F7A76", corner_radius=2)

        self.logs_btn.grid(column=0, row=0, sticky="ns")
        self.adj_matrix_btn.grid(column=1, row=0, sticky="ns")


class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Grid For Menu
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 15))

        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Tabs(self, height=20)
        self.output_frame.grid(row=1, column=0, pady=(0, 15))
    
        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Output(self)
        self.output_frame.grid(row=2, column=0, sticky="nsew")

        # Mode Element [It Like Status Wich Is {add node, add arcs, ...}]
        self.mode_ele = Mode(self, height=5)
        self.mode_ele.grid(row=3, column=0, sticky="nsew", padx=0, pady=0)


class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.canvas = ctk.CTkCanvas(self, width=800, bg="white")
        self.canvas.pack(expand=True, fill="both")

        grid_size = 25
         # draw horizontal lines
        for x in range(0, 1000, grid_size):
            self.canvas.create_line(x, 0, x, 1000, fill="#ddd")

        # draw horizontal lines
        for y in range(0, 1000, grid_size):
            self.canvas.create_line(0, y, 1000, y, fill="#ddd")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title("A* Pathfinding Algorithm")

        # Grid The Window
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        
        # Make Left And Right Frames
        self.menu_frame = Menu(self, fg_color="#EEEEEE")
        self.menu_frame.grid(column=0, row=0, sticky="nswe", pady=10, padx=10)
        
        self.grid = Grid(self, fg_color="#FFFFFF")
        self.grid.grid(column=1, row=0, sticky="nswe", pady=10, padx=10)


app = App()
app.mainloop()

