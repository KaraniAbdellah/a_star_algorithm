# Start Implement a Graph
from collections import namedtuple

Graph = namedtuple("MyGraph", ["nodes", "edges", "is_directed"])
nodes = ["A", "B", "C", "D", "E", "F", "G"]
edges = [
    ("A", "B", 4),
    ("A", "C", 3),
    ("A", "E", 7),
    ("B", "C", 6),
    ("B", "D", 5),
    ("C", "D", 11),
    ("C", "E", 8),
    ("D", "E", 2),
    ("D", "F", 2),
    ("D", "G", 10),
    ("E", "G", 5),
    ("F", "G", 3)
]
G = Graph(nodes, edges, is_directed=True)


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

adj_list = adjacency_list(G)


# Make Heristic Graph
'''
    H(n) = node_ele(n) * 2
'''
print("------------")
def heristic_Graph(graph, adj_list):
    H = {node: 0 for node in graph.nodes}
    # print(H)
    for ele in adj_list:
        # print(adj_list[ele])
        s = 0
        for t in adj_list[ele]:
            s += t[1]
        H[ele] = s * 2
    # print(H)
    return H

H = heristic_Graph(G, adj_list)
print(H)


# Find The Shortest Path Between (A --> F) With a* algorithm
path = []
def a_start_algorithm(path, adj_list, H, start, end):
    print(adj_list['A'])
    minEle, temp = 0, 0
    node = adj_list[start][0][0]
    for ele in adj_list['A']:
        if (minEle == 0):
            temp = ele[1] + H[ele[0]]
        else:
            if minEle < temp:
                node = ele[0]
                temp = minEle
        minEle = ele[1] + H[ele[0]]
    print(temp)
    print(node)
        
        
a_start_algorithm(path, adj_list, H, 'B', 'F')






