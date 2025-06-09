import math

class Arc:
    def __init__(self, canvas, n1, n2, weight):
        self.canvas = canvas
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

        # Find angle between nodes
        angle = math.atan2(n2.y - n1.y, n2.x - n1.x)
        
        # Start point (edge of first node)
        start_x = n1.x + 25 * math.cos(angle)
        start_y = n1.y + 25 * math.sin(angle)

        # End point (edge of second node)
        end_x = n2.x - 25 * math.cos(angle)
        end_y = n2.y - 25 * math.sin(angle)

        # Draw arrow line
        self.line = self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            width=2, fill="black", arrow="last"
        )
        
        # Draw weight in middle
        mid_x = (n1.x + n2.x) / 2
        mid_y = (n1.y + n2.y) / 2
        
        # White background for weight text
        self.rect = self.canvas.create_rectangle(
            mid_x - 15, mid_y - 10, mid_x + 15, mid_y + 10,
            fill="white", outline="gray"
        )

        # Weight text
        self.text = self.canvas.create_text(
            mid_x, mid_y, text=str(weight),
            font=("Arial", 10, "bold"), fill="blue"
        )