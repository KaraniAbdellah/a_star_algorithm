# https://www.datacamp.com/tutorial/a-star-algorithm

'''
    A* based in this formula:
        f(n) = g(n) + h(n)
            --> wich is g(n) is actual cost between each node.

    this algorithm use Heuristic function h(n)
        it is like function that provide estimate cost 
        for each node (from initial node to goal).

    The A* algorithm maintains two essential lists:
        Open list:
            Contains nodes that need to be evaluated
            Sorted by f(n) value (lowest first)
            New nodes are added as they're discovered
        Closed list:
            Contains already evaluated nodes
            Helps avoid re-evaluating nodes
            Used to reconstruct the final path

    A* selects the node with the lowest f(n) value 
    from the open list, and moves it to the closed list
    until it reaches the goal node or determines no path exists.
'''


# heuristic function
def heuristic(start, goal):
    return 0

# Algorithmic Solution
def a_star_algo(start, goal):
    openList = [start] # Nodes to be evaluated
    closedList = [] # Nodes already evaluate

    start.g = 0 # Cost from start to start is 0
    start.h = heuristic(start, goal) # Estimate to goal
    start.parent = None # For path reconstruction
    
    while (openList is not empty):
        # Get node with lowest f value - implement using a priority queue
        # for faster retrieval of the best node
        current = node in openList with lowest f value

        
        
         
    
    



# Python code



