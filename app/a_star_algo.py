# oriented graph
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
    Between S and A --> 8
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

# path = [('S', 0), ('A', 1), ('C', 5)]



def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        print(f"old queue: {queue}")
        # [(8,'B'), (8,'C'), (13,'G'), ('C', 7)]
        queue.sort(key=path_f_cost) # sort by f_cost
        print(f"sorted queue: {queue}")
        path = queue.pop(0) # get least f_cost
        node = path[-1][0]
        print(f"// Selected Node is {node}")
        if node in visited:
            print(f"// {node} Already Visited")
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
        print(f"new queue: {queue}")
        print(f"visited: {visited}")
        print("----------------------------")
        print("----------------------------")
        print("----------------------------")


solution = a_star_search(graph=graph, start='S', goal='G')
print(solution)
print(f"Cost of Solution is ", path_f_cost(solution)[0])





