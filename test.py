# repeat the graph also with adjacency list




def make_graph(src, dest, list):
    list[src].append(dest)
    list[dest].append(src)


# here we have just two nodes
list = [[], []]






