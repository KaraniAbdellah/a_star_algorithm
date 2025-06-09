def path_f_cost(path: list[tuple], h_table: dict) -> tuple:
    g_cost = 0
    for(node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = h_table[str(last_node)]
    f_cost = g_cost + h_cost
    return (f_cost, last_node)


def find_shortest_path(graph, start, goal, h_table):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=lambda x: path_f_cost(x, h_table)) # sort by f_cost
        path = queue.pop(0) # get least f_cost
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(f'{node}')
        if (node == goal):
            return path
        else:
            adjacent_nodes = graph.get(f'{node}')
            if (adjacent_nodes):
                for (node2, cost) in  adjacent_nodes:
                    new_path = path.copy() # Shallow Copy
                    new_path.append((node2, cost))
                    queue.append(new_path)
    return None


def a_star_algo(nodes, arcs, start_node, end_node):
    h_table = {}
    graph = {}

    # make heuristic table
    for node in nodes:
        x1 = node.x
        y1 = node.y
        xf = end_node.x
        yf = end_node.y
        Euclidean_Distance = 0
        h_table[f'{node.value}'] = Euclidean_Distance

    # make graph
    for arc in arcs:
        node1 = str(arc.n1.value)
        node2 = str(arc.n2.value)
        weight = arc.weight
        if graph.get(node1) == None: 
            graph[node1] = []
        graph[node1].append((node2, weight))

    shortest_path = find_shortest_path(graph=graph, start=str(start_node.value),
        goal=str(end_node.value), h_table=h_table)

    if shortest_path is None:
        return None
    else:
        total_cost = sum(cost for node, cost in shortest_path)
        node_sequence = [node for node, cost in shortest_path]
        return node_sequence, h_table, graph, total_cost