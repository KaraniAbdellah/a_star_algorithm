class Node:
    def __init__(self, canvas, x, y, node_value):
        self.x = x
        self.y = y
        self.value = node_value
        self.canvas = canvas
        self.oval = canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#1B56FD", outline="black")
        self.text = canvas.create_text(x, y, text=str(node_value), font=("Arial", 12, "bold"), fill="white")
