# Try Implement the A* Algorithm

'''

    The a* algorithm need the heirstic graph (proposition)
        --> h(n) = node_level * 2
        --> node_level(n) is sum of all connect edges to n

    the algorithm use f(n)=g(n)+h(n) to find the shortest path
    g(n): The cost from the start node to the current node.
    h(n): The heuristic estimate from the current node to the goal.

    I need in implement to use:
        Graph, (Min-Heap), Set, Map
'''

# this is undirected graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # add ele to graph
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def display(self):
        print("hi")
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
            
        
myGraph = Graph()
myGraph.add_node("A", "B", 2)
myGraph.add_node("B", "C", 2)
myGraph.display()



