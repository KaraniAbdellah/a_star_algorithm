# Start Implement a Graph
from collections import namedtuple

Graph = namedtuple("MyGraph", ["nodes", "edges", "is_directed"])
nodes = ["A", "B", "C", "D", "E", "F", "G"]
edges = [
    ("A", "B", 4), ("B", "A", 4),
    ("A", "C", 3), ("C", "A", 3),
    ("A", "E", 7), ("E", "A", 7),
    ("B", "C", 6), ("C", "B", 6),
    ("B", "D", 5), ("D", "B", 5),
    ("C", "D", 11), ("D", "C", 11),
    ("C", "E", 8), ("E", "C", 8),
    ("D", "E", 2), ("E", "D", 2),
    ("D", "F", 2), ("F", "D", 2),
    ("D", "G", 10), ("G", "D", 10),
    ("E", "G", 5), ("G", "E", 5),
    ("F", "G", 3), ("G", "F", 3)
]
G = Graph(nodes, edges, is_directed=False)

def adjacency_list(graph):
    '''
        return adjacency list representation of graph
    '''
    adj = {node: [] for node in graph.nodes}
    print(adj)
    for edge in graph.edges:
        node1, node2, weight = edge[0], edge[1], edge[2]
        print(node1, node2)
        adj[node1].append((node2, weight))
        if graph.is_directed:
            adj[node2].append((node1, weight))
    print(adj)
    return adj

adjacency_list(G)












