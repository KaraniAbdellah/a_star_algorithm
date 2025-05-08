import customtkinter as ctk 

# Start Function
def show_logs():
    print("Hello Logs")

def show_adj_matrix():
    print("Hello Adjacency Matrix")



# Function Declaration
def add_node():
    # Mode().mode_value = "add_node"
    print("We Are In Add Node Mode")


def add_arcs():
    # Mode().mode_value = "add_arcs"
    print("We Are In Add Node Arcs")

def define_start():
    return
def define_end():
    return
def launch():
    return
def clear():
    return
def save_graph():
    return
def load_graph():
    return

class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid The Buttons Frame
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        btns_values = [
            {"value": "Add Nodes", "column": 0, "row": 0, "color": "#328E6E", "function": add_node},
            {"value": "Add Arcs", "column": 1, "row": 0, "color": "#1B56FD", "function": add_arcs},
            {"value": "Define Start", "column": 0, "row": 1, "color": "#FF9B17", "function": define_start},
            {"value": "Define End", "column": 1, "row": 1, "color": "#F7374F", "function": define_end},
            {"value": "Launch", "column": 0, "row": 2, "color": "#8B44AD", "function": launch},  # Changed color to purple
            {"value": "Clear", "column": 1, "row": 2, "color": "#5F7A76", "function": clear},   # Changed color to match design
            {"value": "Save Graph", "column": 0, "row": 3, "color": "#8B4513", "function": save_graph},  # Changed color to brown
            {"value": "Load Graph", "column": 1, "row": 3, "color": "#1F7D53", "function": load_graph},
        ]

        for btn_value in btns_values:
            self.btn = ctk.CTkButton(master=self, fg_color=btn_value["color"], 
                text=btn_value["value"], corner_radius=2, command=btn_value['function'])
            self.btn.grid(column=btn_value["column"], row=btn_value["row"], padx=4, pady=4, sticky="nsew")
        


class Output(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create text box
        self.text_box = ctk.CTkTextbox(self, text_color="black", corner_radius=5)
        self.text_box.pack(side="top", fill="both", expand=True)



class Mode(ctk.CTkFrame):
    mode_value = "null"
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

        self.logs_btn.grid(column=0, row=0, sticky="nse")
        self.adj_matrix_btn.grid(column=1, row=0, sticky="nsw")


class Menu(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Grid For Menu
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=2)
        self.rowconfigure((2), weight=5)
        self.rowconfigure((1, 3), weight=0)

        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")

        # Frame Contain Logs and Adjacency Matrix
        self.tabs_frame = Tabs(self, fg_color="#eee")
        self.tabs_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))

        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Output(self)
        self.output_frame.grid(row=2, column=0, sticky="nsew")

        # Mode Element [It Like Status Wich Is {add node, add arcs, ...}]
        self.mode_ele = Mode(self)
        self.mode_ele.grid(row=3, column=0, sticky="nsew", pady=(10, 10))


class Node:
    def __init__(self, canvas, x, y, node_value):
        # Le'ts Create A Circle
        canvas.create_oval(x - 25, y - 25, x + 25, y + 25, 
            fill="#1B56FD", outline="black")
        
        canvas.create_text(x, y, text=str(node_value), 
            font=("Arial", 12, "bold"), fill="white")


class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Node Value [Dynamic Valud]
        self.node_counter = 1
        # For Storing the positions for no duplicated
        self.node_positions = []

        self.canvas = ctk.CTkCanvas(self, width=800, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # Draw The Grid
        grid_size = 25
        for x in range(0, 1000, grid_size):
            self.canvas.create_line(x, 0, x, 1000, fill="#ddd")
        for y in range(0, 1000, grid_size):
            self.canvas.create_line(0, y, 1000, y, fill="#ddd")

        def add_node(event):
            # Check if position already has a node (within 50px radius)
            for pos in self.node_positions:
                distance = ((pos[0] - event.x)**2 + (pos[1] - event.y)**2)**0.5
                if distance < 50:
                    print(f"Position ({event.x},{event.y}) already has a node nearby")
                    return

            print(f"Drawing node {self.node_counter} at ({event.x},{event.y})")
            Node(self.canvas, event.x, event.y, self.node_counter)
            self.node_positions.append((event.x, event.y))
            self.node_counter += 1

        # Bind The Canvas
        self.canvas.bind("<Button-1>", add_node)



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

