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
    1: [(3, 12), (2, 7)],
    2: [(3, 10)],
    3: [(4, 5)],
    4: [(1, 3)]
}



def heuristic(goal_node: int) -> dict:
    h_nodes = {}
    for node in nodes:
        x1 = nodes[node][0]
        y1 = nodes[node][1]
        x2_g = nodes[goal_node][0]
        y2_g = nodes[goal_node][0]
        euclidean_distance = sqrt(pow((x1 - x2_g), 2) + pow((y1 - y2_g), 2))
        h_nodes[node] = int(euclidean_distance)
    return h_nodes



def a_star_algo(start: int, goal: int) -> list[int]:
    h_list = heuristic(goal)
    print(h_list)

    # neighbers of node
    for neighber in edges[start]:
        cost = neighber[1] + h_list[neighber[0]]
        print(f"cost between {start} and {neighber[0]} is {cost}")

        
    
    return 1


a_star_algo(1, 4)
   

