from util import Stack, Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
    for pair in ancestors:
        g.add_edge(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in g.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor