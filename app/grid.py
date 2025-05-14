import customtkinter as ctk 


class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.node_counter = 1
        self.nodes = [] # nodes that we draw
        grid_size = 25
        self.selected_nodes = []  # for arc drawing

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
                distance = ((node.x - event.x) ** 2 + (node.y - event.y) ** 2) ** 0.5
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
                print(f"Selected node {node.value} for arc")

                if len(self.selected_nodes) == 2:
                    n1, n2 = self.selected_nodes
                    self.canvas.create_line(n1.x, n1.y, n2.x, n2.y, width=2, fill="black")
                    print(f"Arc added between Node {n1.value} and Node {n2.value}")
                    self.selected_nodes = []  # reset for next arc
                break
