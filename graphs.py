# Create Graph With namedtuple
'''
    G = (V, E)
    V: Vertex
    E: edges
    Example: 
        V = {0, 1, 2, 3}
        G = {(0, 1), (0, 2), (1, 3), (1, 4)}
    
    # this is not good method for present the graph    
'''

# G = (V, E)
from collections import namedtuple

Graph = namedtuple("myGraph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("B", "A"),
    ("B", "D"),
    ("D", "B"),
    ("D", "A"),
    ("A", "D"),
    ("A", "C"),
    ("C", "A"),
]

G = Graph(nodes, edges)
print(G.edges)
print(G.nodes)


# Create graph with Adjacency list

def adjacency_dict(graph):
    '''
    return the adjacency list representation of the graph
    '''
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj

print(adjacency_dict(G))


# Create graph With Adjacency Matrix







