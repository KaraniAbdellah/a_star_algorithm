from collections import namedtuple

Graph = namedtuple("myGraph", ["nodes", "edges", "is_directed"])

nodes = range(4) # list with 4 ele
edges = [
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 3],
    [3, 3]
]
myGraph = Graph(nodes, edges, is_directed=True)
# print(myGraph)

def adjacency_matrix(graph):
    '''
        return the adjacency matrix of the graph
        Assumes that graph.nodes is equivalent  to range(len(graph.node))
    '''
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    print(adj)
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    print(adj)
    return adj

adjacency_matrix(myGraph)






























# Graph With Adjacency List
'''
Graph = namedtuple("myGraph", ["nodes", "edges", "is_directed"])
nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("B", "A"),
    ("C", "D"),
    ("A", "C"), 
    ("D", "A"), 
]
myGraph = Graph(nodes, edges, is_directed=True)
print(myGraph)
print(myGraph.nodes)
print(myGraph.edges)
# Create graph with Adjacency list
def adjacency_dict(graph):
    # return the adjacency list representation of the graph
    adj = {node: [] for node in graph.nodes} # {'A': [], 'B': [], 'C': [], 'D': []}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj
print(adjacency_dict(myGraph))
'''

