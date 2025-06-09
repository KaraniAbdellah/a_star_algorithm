import math
import customtkinter as ctk
from tkinter import simpledialog, messagebox, filedialog
from models.Node import Node
from models.Arc import Arc
from algo_func.func import a_star_algo
from helper_func.helper import set_content, content

class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.node_counter = 1
        self.nodes = [] # for store nodes (x, y)
        grid_size = 25
        self.selected_nodes = []  # for arc drawing
        self.arcs = []  # store arcs and weights between nodes
        self.start_node = 0
        self.end_node = 0

        self.canvas = ctk.CTkCanvas(self, width=800, bg="white")
        self.canvas.pack(expand=True, fill="both")

        for x in range(0, 1000, grid_size):
            self.canvas.create_line(x, 0, x, 1000, fill="#ddd")
        for y in range(0, 1000, grid_size):
            self.canvas.create_line(0, y, 1000, y, fill="#ddd")


        def on_canvas_click(event):
            from helper_func.helper import current_mode
            if current_mode == "Add Node":
                self.add_node(event)
            if current_mode == "Add Arcs":
                self.add_arc(event)
            if current_mode == "Define Start":
                self.define_start(event)
            if current_mode == "Define End":
                self.define_end(event)
            if current_mode == "Launch":
                self.launch_graph()
            if current_mode == "Clear":
                self.clear_canvas(event)
            if current_mode == "Save":
                self.save_logs()
        self.canvas.bind("<Button-1>", on_canvas_click)

    def add_node(self, event):
        for node in self.nodes:
            distance = ((node.x - event.x) ** 2 + (node.y - event.y) ** 2) ** 0.5
            if distance < 50:
                print(f"Position ({event.x},{event.y}) already has a node nearby")
                return

        new_node = Node(self.canvas, event.x, event.y, self.node_counter)
        self.nodes.append(new_node)
        self.node_counter += 1

    def add_arc(self, event):
        node_found = False
        for node in self.nodes:
            distance = ((node.x - event.x)**2 + (node.y - event.y)**2)**0.5
            if distance < 25:
                node_found = True
                self.selected_nodes.append(node)
                if len(self.selected_nodes) == 2:
                    n1, n2 = self.selected_nodes

                    # Check if arc already exists
                    arc_exists = False
                    for arc in self.arcs:
                        if (arc.n1 == n1 and arc.n2 == n2):
                            arc_exists = True
                            break
                    
                    if arc_exists:
                        messagebox.showwarning("Warning", "Arc Already Exists")
                        self.selected_nodes = []
                        return

                    # Get weight from user
                    try:
                        weight = 0
                        while weight == 0:
                            weight_str = simpledialog.askstring(
                                "Arc Weight",
                                f"Enter weight != 0 between Node {n1.value} and Node {n2.value}:"
                            )
                            
                            if weight_str is None:  # User clicked cancel
                                self.selected_nodes = []
                                return
                                
                            weight = int(weight_str)
                            
                    except (ValueError, TypeError):
                        messagebox.showerror("Error", "Please enter a valid integer")
                        self.selected_nodes = []
                        return

                    # Create the arc
                    new_arc = Arc(self.canvas, n1, n2, weight=weight)

                    # Save arc info
                    self.arcs.append(new_arc)
                    
                    # Reset selected nodes
                    self.selected_nodes = []
                break

        if not node_found:
            messagebox.showinfo("Info", "Please select a node")

    def define_start(self, event):
        if (len(self.nodes) == 0):
            messagebox.showinfo("Info", "Please select a node")
            return
        for node in self.nodes:
            distance = ((node.x - event.x)**2 + (node.y - event.y)**2)**0.5
            if distance < 25:
                if (self.start_node == 0):
                    self.canvas.itemconfig(node.oval, fill="#ACC572")
                    self.start_node = node

    def define_end(self, event):
        if (len(self.nodes) == 0):
            messagebox.showinfo("Info", "Please select a node")
            return
        for node in self.nodes:
            distance = ((node.x - event.x)**2 + (node.y - event.y)**2)**0.5
            if distance < 25:
                if (self.end_node == 0):
                    self.canvas.itemconfig(node.oval, fill="#CB0404")
                    self.end_node = node

    def clear_canvas(self, event):
        if (len(self.nodes) == 0):
            messagebox.showinfo("Info", "Please select a node")
            return

        # Delete all nodes
        for node in self.nodes:
            self.canvas.delete(node.oval)
            self.canvas.delete(node.text)

        # Delete all arcs
        for arc in self.arcs:
             self.canvas.delete(arc.line)
             self.canvas.delete(arc.rect)
             self.canvas.delete(arc.text)
            

        # Reset all Variables
        self.nodes = []
        self.arcs = []
        self.selected_nodes = []
        self.node_counter = 1
        self.start_node = 0
        self.end_node = 0
        
        set_content("")

    def draw_arcs(self, node_sequence):
        for i in range(len(node_sequence) - 1):
            for arc in self.arcs:
                if (str(arc.n1.value) == node_sequence[i] and 
                    str(arc.n2.value) == node_sequence[i + 1]):
                    self.canvas.itemconfig(arc.line, fill="red", width=4)

    def launch_graph(self):
        if (self.start_node == 0 or self.end_node == 0 or len(self.arcs) == 0):
            messagebox.showinfo("Info", "Select Start Node and End Node and Arcs")
        elif (self.start_node == self.end_node):
            messagebox.showinfo("Info", "Start and End nodes cannot be the same")
        else:
            try:
                result = a_star_algo(nodes=self.nodes, arcs=self.arcs,
                    start_node=self.start_node, end_node=self.end_node)
                if result is None:
                    messagebox.showinfo("Info", f"No path found between {self.start_node.value} and {self.end_node.value}")
                else:
                    node_sequence, h_table, graph, total_cost = result
                    self.draw_arcs(node_sequence=node_sequence)
                    set_content(f"""Algorithm Results:\n
                    ** Heuristic Table:
                    {h_table}:\n
                    ** Graph [Adjacency List]:
                    {graph}\n
                    ** Node Sequence:
                    {' → '.join(map(str, node_sequence))}\n
                    ** Total Path Cost From {self.start_node.value} to {self.end_node.value}: {total_cost}\n
                    """)
                    
            except Exception as e:
                print(f"Error running A* algorithm: {e}")
                messagebox.showerror("Error", f"Algorithm failed: {str(e)}")

    def save_logs(self):
        if (content != ""):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                with open(file_path, "w") as file:
                    file.write(content)
        else:
            messagebox.showwarning("Warning", "Draw Your Graph First")