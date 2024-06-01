from Edge import Edge
from Graph import Graph
from Node import Node
from Digraph import Digraph
def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest_paths, totalMins, minTotal=float('inf')):
    """
    Depth first search in a directed graph with minutes accumulation

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph along with total minutes
    """
    path = path + [start]
    if start == end:
        shortest_paths.append((path, totalMins))
        return shortest_paths

    for node in graph.childrenOf(start):
        if node not in path:
            mins = graph.getEdgesMins()[(start, node)]
            new_total_mins = totalMins + mins
            if len(shortest_paths) < 3 or new_total_mins <= shortest_paths[-1][1]:
                shortest_paths = DFS(graph, node, end, path, shortest_paths, new_total_mins, minTotal)
                shortest_paths.sort(key=lambda x: (x[1], -len(x[0]), x[0][1].name))
                shortest_paths = shortest_paths[:3]
    return shortest_paths


def search2(graph, start, end):
    shortest_paths = []
    shortest_paths = DFS(graph, start, end, [], shortest_paths, 0)
    return shortest_paths