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

Graph = namedtuple("myGraph", ["nodes", "edges", "is_directed"])
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
G = Graph(nodes, edges, is_directed=True)
# print(G.edges)
# print(G.nodes)


# Create graph with Adjacency list
def adjacency_dict(graph):
    '''
    return the adjacency list representation of the graph
    '''
    adj = {node: [] for node in graph.nodes}
    print(adj) # {'A': [], 'B': [], 'C': [], 'D': []}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj

# adjacency_dict(G)


# Create graph With Adjacency Matrix
nodes = range(4)
edges = [
    (0, 1),
    (1, 1),
    (0, 2),
    (2, 0),
    (0, 3),
    (3, 0),
    (3, 1),
    (3, 2)
]
G = Graph(nodes, edges, is_directed=True)
def adjacency_matrix(graph):
    '''
    return the adjacency matrix of the graph
    Assumes that graph.nodes is equivalent  to range(len(graph.node))
    '''
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # print(adj)
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj

print(adjacency_matrix(G))


'''
    Adjacency List:
        can be use in defferent type of data
        uses less memory and good for graph with few edges
    
    Adjacency Matrix:
        only works for graphs whose nodes are integers
        not a good choice for space graphs, use most memory
'''




