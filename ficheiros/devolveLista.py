from Edge import Edge
from Graph import Graph
from Node import Node
from Digraph import Digraph
from constants import *
def DFS(graph, start, end, path, shortest_paths, totalMins, minTotal=float('inf')):
    """
    Perform a depth-first search in a directed graph to find the shortest paths.

    Parameters:
    - graph (Digraph): The directed graph to search.
    - start (Node): The starting node for the search.
    - end (Node): The target node to reach.
    - path (list): The current path of nodes being traversed.
    - shortest_paths (list): The list of shortest paths found so far.
    - totalMins (int): The total minutes accumulated along the current path.
    - minTotal (float): The minimum total minutes for a path found so far (default is infinity).

    Returns:
    - list: A list of tuples, each containing a path (list of nodes) and the total minutes for that path.
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
                shortest_paths.sort(key=lambda x: (x[TIME], -len(x[PATH]), x[PATH][1]._name))
                shortest_paths = shortest_paths[:3]
    return shortest_paths


def search(graph, start, end):
    """
    Find the three shortest paths from the start node to the end node in the graph.

    Parameters:
    - graph (Digraph): The directed graph to search.
    - start (Node): The starting node for the search.
    - end (Node): The target node to reach.

    Returns:
    - list: A list of the three shortest paths found, each path is a tuple containing a list of nodes and the total minutes for that path.
    """
    shortest_paths = []
    shortest_paths = DFS(graph, start, end, [], shortest_paths, 0)
    return shortest_paths
