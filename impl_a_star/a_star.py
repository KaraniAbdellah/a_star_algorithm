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
    for edge in graph.edges:
        node1, node2, weight = edge[0], edge[1], edge[2]
        adj[node1].append((node2, weight))
        if graph.is_directed:
            adj[node2].append((node1, weight))
    return adj

adj_list = adjacency_list(G)
print(adj_list)


# Make Heristic Graph
'''
    H(n) = node_ele(n) * 2
'''
print("------------")
def heristic_Graph(graph, adj_list):
    H = {node: 0 for node in graph.nodes}
    for ele in adj_list:
        s = 0
        for t in adj_list[ele]:
            s += t[1]
        H[ele] = s * 2
    return H

H = heristic_Graph(G, adj_list)
print(H)


# Find The Shortest Path Between (A --> F) With a* algorithm
from heapq import heappop, heappush

def a_star_algorithm(adj_list, H, start, end):
    open_set = [(0 + H[start], 0, start, [])]  # (f, g, node, path)
    print(open_set)
    visited = set()
    print(visited)
    while open_set:
        _, g, node, path = heappop(open_set)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == end:
            return path, g  # Return path and total cost
        for neighbor, cost in adj_list.get(node, []):
            if neighbor not in visited:
                heappush(open_set, (g + cost + H[neighbor], g + cost, neighbor, path))
    return None, float("inf")  # No path found

# Exemple d'utilisation
path, cost = a_star_algorithm(adj_list, H, 'A', 'F')
print("Shortest path:", path, "with cost:", cost)




