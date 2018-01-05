from itertools import chain
import AStar
from NodeHandler import NodeHandler as NH
import get_char_path as ch

nodes = []
full_path = []


def explore(start, grid):
    while 2 in chain(*grid):
        nh = NH(grid)
        node_i, walls = nh.get_next_node(start[0], start[1])
        if node_i == (-1, -1):
            break
        nodes.append(node_i)
    print "Number of Nodes"
    print str(len(nodes)+1)
    return nodes, walls


def sort(start, grid, walls, method):
    nh = NH(grid)
    if method == 1:
        return nodes
    elif method == 2:
        return nh.sorted_euclidean(start, nodes)
    elif method == 3:
        return nh.sorted_a_star(start, nodes, walls)
    elif method == 4:
        return nh.sorted_pos(start, nodes, walls)


def walk(start, sorted_nodes, walls):
    for end_i in sorted_nodes:
        # if end_i not in full_path:
        # if full_path.count(end_i) == 0:
            a = AStar.AStar()
            a.init_grid(25, 25, walls, start, end_i)
            path = a.solve()
            # print path
            for i in path:
                if path.index(i) < len(path)-1 or sorted_nodes.index(end_i) == len(sorted_nodes)-1:
                    full_path.append(i)
            start = end_i
    ch.get_char_from_path(full_path)


def act(start, grid, method):
    _, walls = explore(start, grid)
    sorted_nodes = sort(start, grid, walls, method)
    walk(start, sorted_nodes, walls)