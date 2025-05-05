import customtkinter as ctk 

# Start Function
def show_logs():
    print("Hello Logs")

def show_adj_matrix():
    print("Hello Adjacency Matrix")


class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # Grid The Buttons Frame
        self.columnconfigure([0, 1], weight=1)
        self.rowconfigure([0, 1, 2, 3], weight=1)

        btns_values = [
            {"value": "Add Nodes", "column": 0, "row": 0, "color": "#328E6E"},
            {"value": "Add Arcs", "column": 1, "row": 0, "color": "#1B56FD"},
            {"value": "Define Start", "column": 0, "row": 1, "color": "#FF9B17"},
            {"value": "Define End", "column": 1, "row": 1, "color": "#F7374F"},
            {"value": "Launch", "column": 0, "row": 2, "color": "#9B59B6"},
            {"value": "Clear", "column": 1, "row": 2, "color": "#5F7A76"},
            {"value": "Save Graph", "column": 0, "row": 3, "color": "#8B4513"},
            {"value": "Load Graph", "column": 1, "row": 3, "color": "#1F7D53"}
        ]

        for btn_value in btns_values:
            btn = ctk.CTkButton(
                master=self, 
                fg_color=btn_value["color"], 
                text=btn_value["value"],
                height=45,
                corner_radius=8
            )
            btn.grid(column=btn_value["column"], row=btn_value["row"], padx=5, pady=5, sticky="nsew")


class Output(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        
        # Frame Configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        # Create tab buttons frame
        self.tab_buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.tab_buttons_frame.grid(row=0, column=0, pady=(5, 5), sticky="n")
        
        # Add buttons to tab frame
        self.adj_matrix_btn = ctk.CTkButton(
            master=self.tab_buttons_frame, 
            text="Adjacency Matrix", 
            command=show_adj_matrix, 
            fg_color="#5B9BD5",
            corner_radius=5,
            height=28,
            width=120
        )
        self.logs_btn = ctk.CTkButton(
            master=self.tab_buttons_frame, 
            text="Logs", 
            command=show_logs, 
            fg_color="#A0A0A0",
            corner_radius=5,
            height=28,
            width=80
        )
        
        # Place buttons side by side in the tab frame
        self.adj_matrix_btn.pack(side="left", padx=(0, 5))
        self.logs_btn.pack(side="left")

        # Create text box with white background
        self.text_box = ctk.CTkTextbox(self, fg_color="white", text_color="black", corner_radius=5)
        self.text_box.grid(column=0, row=1, sticky="nsew", pady=(0, 5))


class Mode(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        
        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Create status message at bottom
        self.mode_label = ctk.CTkLabel(
            master=self, 
            text="Mode: define_end",
            fg_color="transparent",
            text_color="black",
            anchor="w",
            font=("Arial", 12)
        )
        self.mode_label.grid(row=0, column=0, sticky="sw", padx=5)


class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="#E0E0E0", **kwargs)

        # Grid For Menu
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)  # Buttons
        self.rowconfigure(1, weight=1)  # Output/text area
        self.rowconfigure(2, weight=0)  # Mode label

        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, sticky="new", padx=10, pady=10)

        # Frame Contain Logs and Adj
        self.output_frame = Output(self)
        self.output_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 0))

        # Mode Element (status bar)
        self.mode_ele = Mode(self)
        self.mode_ele.grid(row=2, column=0, sticky="sw", padx=0, pady=(0, 5))


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

        # Set appearance mode and default color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Grid The Window
        self.columnconfigure(0, weight=1)  # Menu frame takes 1/3
        self.columnconfigure(1, weight=2)  # Grid takes 2/3
        self.rowconfigure(0, weight=1)
        
        # Make Left And Right Frames
        self.menu_frame = Menu(self)
        self.menu_frame.grid(column=0, row=0, sticky="nswe", pady=10, padx=10)
        
        self.grid = Grid(self, fg_color="#FFFFFF")
        self.grid.grid(column=1, row=0, sticky="nswe", pady=10, padx=10)


app = App()
app.mainloop()