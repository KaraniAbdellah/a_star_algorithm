from collections import namedtuple


Graph = namedtuple("myGraph", ["nodes", "edges", "is_directed"])

nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("B", "A"),
    ("C", "D"),
    ("A", "C")
]

myGraph = Graph(nodes, edges, is_directed=True)
# print(myGraph)


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

adjacency_dict(myGraph)



