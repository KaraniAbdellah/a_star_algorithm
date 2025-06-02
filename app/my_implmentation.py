# https://www.datacamp.com/tutorial/a-star-algorithm

from math import sqrt, pow

'''
    A* based in this formula:
        f(n) = g(n) + h(n)
            --> wich is g(n) is actual cost between each node.

    this algorithm use Heuristic function h(n)
        it is like function that provide estimate cost 
        for each node (from initial node to goal).

    For Calculate The Heuristic we can user:
        - Manhattan distance
        - Euclidean distance
    
   Steps:
        - make Heuristic function for each node --> node(x, y)
        - 
'''

'''
nodes = [
    {"value": 0, "coord": (34, 23)}, {"value": 1, "coord": (56, 98)},
    {"value": 2, "coord": (62, 1)},  {"value": 3, "coord": (233, 34)}
]
arcs = [
    {"nodes": (0, 2), "weight": 12}, {"nodes": (0, 1), "weight": 12},
    {"nodes": (0, 3), "weight": 12}
]

print(neighber)
    print(h_list[edge])
    print(neighber)
    print(cost)
    print(f"cost between {edge} and {neighber[0]} is {cost}")
    print("-----")
'''


# each nodes has tuple is coordinates
nodes = {
    1: (34, 23), 2: (56, 98),
    3: (62, 1), 4: (233, 34)
}

# each node link with another node with weight
edges = {
    1: [(3, 12), (2, 7)], 2: [(3, 10)],
    3: [(4, 5)], 4: [(1, 3)]
}


# Please use Adjacency list and PILE
def heuristic(goal_node: int) -> dict:
    h_nodes = {}
    for node in nodes:
        x1 = nodes[node][0]
        y1 = nodes[node][1]
        x2_g = nodes[goal_node][0]
        y2_g = nodes[goal_node][1]
        euclidean_distance = sqrt(pow((x1 - x2_g), 2) + pow((y1 - y2_g), 2))
        h_nodes[node] = int(euclidean_distance)
    return h_nodes

heuristic(4)


        

def a_star_algo(start: int, goal: int, selected_nodes: list[int], old_node_costs: list[dict]) -> list[int]:
    if (start == goal): return []
    h_list = heuristic(goal)
    print("heuristic: ", h_list)

    if (len(selected_nodes) == 0): selected_nodes.append(start)
    selected_node = selected_nodes[len(selected_nodes) - 1]

    node_costs = []
    for neighber in edges[selected_node]:
        cost_from_start_to_neighber = 0 # I have a problem here
        cost = neighber[1] + h_list[neighber[0]] + cost_from_start_to_neighber
        print(f"cost between {selected_node} and {neighber[0]} is {cost}")
        node_costs.append({"cost": cost, "node": neighber[0]})
    print("node_costs: ", node_costs)

    # get the old node_costs
    print("old_node_costs: ", old_node_costs)
    for old_node_cost in old_node_costs:
        node_costs.append(old_node_cost)
    print("node_costs: ", node_costs)


    # Get The Node That Have A Small Cost
    selected_node = node_costs[0]["node"]
    cost_of_selected_node = node_costs[0]["cost"]
    check = False
    for node_with_cost in node_costs:
        if (cost_of_selected_node > node_with_cost["cost"]):
            selected_node = node_with_cost["node"]
            cost_of_selected_node = node_with_cost["cost"]
            node_costs.pop(node_costs.index(node_with_cost))
            check = True
    if (check == False): node_costs.pop(0)
    
    selected_nodes.append(selected_node)
    print("selected_nodes: ", selected_nodes)
    
    print(f"We Select Node {selected_node}")
    print(node_costs)
    print("----------------------------")

    if (goal != selected_node):
        a_star_algo(selected_node, goal=goal,
            selected_nodes=selected_nodes,
            old_node_costs=node_costs)
    


start = 1
goal = 4
selected_nodes = []
old_node_costs = []
a_star_algo(start=start, goal=goal,
    selected_nodes=selected_nodes,
    old_node_costs=old_node_costs
)


   

