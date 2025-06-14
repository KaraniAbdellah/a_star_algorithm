# Oriented graph
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)]
}

# heuristic table 
H_table = {
    'S': 7, 
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0,
}

# helper function: Path F-cost
'''
    Between S and A:
        f(C) = g(C) + h(C)
        f(C) = (0 + 1 + 5) + 2
        f(C) = 8 --> tuple(8, 'C')
'''
def path_f_cost(path: list[tuple]) -> tuple:
    g_cost = 0
    for(node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = g_cost + h_cost
    return (f_cost, last_node)

path = [('S', 0), ('A', 1), ('C', 5)]
path_f_cost(path=path)


def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if (node == goal):
            return path
        else:
            adjacent_nodes = graph.get(node)
            for (node2, cost) in  adjacent_nodes:
                new_path = path.copy() # by reference
                new_path.append((node2, cost))
                queue.append(new_path)
    return visited


solution = a_star_search(graph=graph, start='S', goal='G')
print(solution)
print(f"Cost is ", path_f_cost(solution)[0])





