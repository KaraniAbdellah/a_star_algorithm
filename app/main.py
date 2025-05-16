import customtkinter as ctk 
from tkinter import simpledialog # for popups
from tkinter import messagebox

# Start Function
def show_logs():
    print("Hello Logs")

def show_adj_matrix():
    print("Hello Adjacency Matrix")


# Define Global Variables For Mode
current_mode = "null"


def set_mode(new_mode):
    global current_mode
    current_mode = new_mode

    if 'mode_label' in globals() and mode_label is not None:
        mode_label.configure(text=f"Mode: {new_mode}")


class Buttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid The Buttons Frame
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        def add_node():
            set_mode("Add Node")

        def add_arcs():
            set_mode("Add Arcs")

        def define_start():
            set_mode("Define Start")

        def define_end():
            set_mode("Define End")

        def launch():
            set_mode("Launch")

        def clear():
            set_mode("Clear")
 
        def save_graph():
            set_mode("Save")

        def load_graph():
            set_mode("Load")

        btns_values = [
            {"value": "Add Nodes", "column": 0, "row": 0, "color": "#328E6E", "function": add_node},
            {"value": "Add Arcs", "column": 1, "row": 0, "color": "#1B56FD", "function": add_arcs},
            {"value": "Define Start", "column": 0, "row": 1, "color": "#FF9B17", "function": define_start},
            {"value": "Define End", "column": 1, "row": 1, "color": "#F7374F", "function": define_end},
            {"value": "Launch", "column": 0, "row": 2, "color": "#8B44AD", "function": launch},
            {"value": "Clear", "column": 1, "row": 2, "color": "#5F7A76", "function": clear},
            {"value": "Save Graph", "column": 0, "row": 3, "color": "#8B4513", "function": save_graph},
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
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        global mode_label

        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        mode_label = ctk.CTkLabel(master=self, text=f"Mode: {current_mode}",
            fg_color="transparent", text_color="black", anchor="w", font=("Arial", 16))

        mode_label.grid(row=0, column=0, sticky="sw", padx=5)


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

        # Mode Element [It Like Status Which Is {add node, add arcs, ...}]
        self.mode_ele = Mode(self)
        self.mode_ele.grid(row=3, column=0, sticky="nsew", pady=(10, 10))

        # Frame Contain Buttons
        self.buttons_frame = Buttons(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")

        # Frame Contain Logs and Adjacency Matrix
        self.tabs_frame = Tabs(self, fg_color="#eee")
        self.tabs_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))

        # Frame Contain Logs and Adjacency Matrix
        self.output_frame = Output(self)
        self.output_frame.grid(row=2, column=0, sticky="nsew")


class Node:
    def __init__(self, canvas, x, y, node_value):
        self.x = x
        self.y = y
        self.value = node_value
        self.canvas = canvas
        self.oval = canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#1B56FD", outline="black")
        self.text = canvas.create_text(x, y, text=str(node_value), font=("Arial", 12, "bold"), fill="white")

class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.node_counter = 1
        self.nodes = [] # for store nodes (x, y)
        grid_size = 25
        self.selected_nodes = []  # for arc drawing
        self.arcs = []  # store arcs and weights between nodes

        self.canvas = ctk.CTkCanvas(self, width=800, bg="white")
        self.canvas.pack(expand=True, fill="both")

        for x in range(0, 1000, grid_size):
            self.canvas.create_line(x, 0, x, 1000, fill="#ddd")
        for y in range(0, 1000, grid_size):
            self.canvas.create_line(0, y, 1000, y, fill="#ddd")

        def on_canvas_click(event):
            if current_mode == "Add Node":
                self.add_node(event)
            if current_mode == "Add Arcs":
                self.add_arc(event)
            

        def on_canvas_double_click(event):
            for node in self.nodes:
                distance = ((node.x - event.x) ** 2 + (node.y - event.y) ** 2) ** 0.5 # ((x1 - x2)^2 + (y1 - y2)^2)^1/2
                if distance < 25:
                    print(f"Deleting node {node.value}")
                    self.canvas.delete(node.oval)
                    self.canvas.delete(node.text)
                    self.nodes.remove(node)
                    break

        self.canvas.bind("<Button-1>", on_canvas_click)
        self.canvas.bind("<Double-Button-1>", on_canvas_double_click)


    def add_node(self, event):
        for node in self.nodes:
            distance = ((node.x - event.x) ** 2 + (node.y - event.y) ** 2) ** 0.5
            if distance < 50:
                print(f"Position ({event.x},{event.y}) already has a node nearby")
                return

        print(f"Drawing node {self.node_counter} at ({event.x},{event.y})")
        new_node = Node(self.canvas, event.x, event.y, self.node_counter)
        self.nodes.append(new_node)
        self.node_counter += 1

    def add_arc(self, event):            
        for node in self.nodes:
            distance = ((node.x - event.x)**2 + (node.y - event.y)**2)**0.5
            if distance < 25:
                self.selected_nodes.append(node)
                if len(self.selected_nodes) == 2:
                    n1, n2 = self.selected_nodes

                    # check if n1 already exit in self.arcs
                    for arc in self.arcs:
                        if arc["n1"].x == n1.x and arc["n2"].x == n2.x:
                        # or arc["n2"].x == n1.x and arc["n1"].x == n2.x:
                            messagebox.showwarning("Warnning", "Arcs Already Exit")
                            print("The Arcs Already Exit")
                            self.selected_nodes = []
                            return

                    weight = 0
                    while (weight == 0):
                        weight = simpledialog.askstring(
                            "Arc Weight",
                            f"Enter weight != 0 between Node {n1.value} and Node {n2.value}:"
                        )
                        weight = int(weight)
                         

                    # Create line between two node
                    self.canvas.create_line(
                        n1.x + 25, n1.y, n2.x - 25, n2.y,
                        width=2, fill="black", arrow="last", arrowshape=(10, 12, 5)
                    )

                    # get mid distance between n1 and n2
                    mid_x = (n1.x + n2.x) / 2
                    mid_y = (n1.y + n2.y) / 2

                    # Create Weight
                    temp_text = self.canvas.create_text(
                        mid_x, mid_y, text=weight,
                        font=("Arial", 12, "bold")
                    )
                    bbox = self.canvas.bbox(temp_text)
                    self.canvas.delete(temp_text)

                    # Add a rectangle background to weight
                    padding = 4
                    self.canvas.create_rectangle(
                        bbox[0] - padding, bbox[1] - padding,
                        bbox[2] + padding, bbox[3] + padding,
                        fill="white", outline=""
                    )

                    # Draw text on top
                    self.canvas.create_text(
                        mid_x, mid_y, text=weight,
                        fill="blue", font=("Arial", 12, "bold")
                    )

                    # Save arc info
                    self.arcs.append({"n1": n1, "n2": n2, "weight": weight})
                    print(self.arcs[0]["n1"].x)
                    print(self.arcs[0]["n1"].y)
                    self.selected_nodes = []
                break




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


