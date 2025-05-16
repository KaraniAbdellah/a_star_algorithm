class Grid(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.node_counter = 1
        self.nodes = [] # for store nodes (x, y)
        grid_size = 25
        self.selected_nodes = []  # for arc drawing
        self.dragged_node = None # no node want to move
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

            if current_mode == "Move Node":
                self.move_node(event)
            
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

        def on_canvas_move(event):
            if self.dragged_node:
                # Update position of the dragged node
                dx = event.x - self.dragged_node.x
                dy = event.y - self.dragged_node.y
                self.canvas.move(self.dragged_node.oval, dx, dy)
                self.canvas.move(self.dragged_node.text, dx, dy)
                self.dragged_node.x = event.x
                self.dragged_node.y = event.y

                # Update arcs connected to the moved node
                for arc in self.arcs:
                    if arc["n1"] == self.dragged_node or arc["n2"] == self.dragged_node:
                        # Update line coordinates
                        x1, y1 = arc["n1"].x, arc["n1"].y
                        x2, y2 = arc["n2"].x, arc["n2"].y
                        self.canvas.coords(arc["line"], x1, y1, x2, y2)

                        # Update text position (weight label)
                        mid_x = (x1 + x2) / 2
                        mid_y = (y1 + y2) / 2
                        self.canvas.coords(arc["text"], mid_x, mid_y)

                        # Update background for text
                        bbox = self.canvas.bbox(arc["text"])
                        self.canvas.coords(arc["bg"], bbox[0] - 4, bbox[1] - 4, bbox[2] + 4, bbox[3] + 4)

        def on_canvas_release(event):
            self.dragged_node = None

        self.canvas.bind("<Button-1>", on_canvas_click)
        self.canvas.bind("<Double-Button-1>", on_canvas_double_click)

        self.canvas.bind("<B1-Motion>", on_canvas_move)
        self.canvas.bind("<ButtonRelease-1>", on_canvas_release)


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
                    weight = simpledialog.askstring(
                        "Arc Weight",
                        f"Enter weight between Node {n1.value} and Node {n2.value}:"
                    )

                    # Create line between two node
                    line = self.canvas.create_line(
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
                    rect = self.canvas.create_rectangle(
                        bbox[0] - padding, bbox[1] - padding,
                        bbox[2] + padding, bbox[3] + padding,
                        fill="white", outline=""
                    )

                    # Draw text on top
                    text = self.canvas.create_text(
                        mid_x, mid_y, text=weight,
                        fill="blue", font=("Arial", 12, "bold")
                    )

                    # Save arc info
                    self.arcs.append({"n1": n1, "n2": n2, "line": line, "text":
                        text, "bg": rect})
                    print(self.arcs)
                    self.selected_nodes = []
                break

    def move_node(self, event):
        for node in self.nodes:
            distance = ((node.x - event.x) ** 2 + (node.y - event.y) ** 2) ** 0.5
            if distance < 25:
                self.dragged_node = node
                break
