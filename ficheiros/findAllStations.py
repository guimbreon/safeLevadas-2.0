from devolveLista import *
from constants import * 
from readLN import * 

def findAllStations(myStations, dig):
    """
     Find paths between all pairs of stations using a specified search function.

    Parameters:
    - myStations (list of lists): A list of list, where each list contains two stations.
    - dig (function): Digraph

    Returns:
    - list: A list of paths between the stations.
    """
    todasOsCaminhos = []
    for pairOfStations in myStations:
        if pairOfStations[0] != "out of network":
            todasOsCaminhos.append(search(dig, pairOfStations[0], pairOfStations[1]))
        else:
            todasOsCaminhos.append("out of network")
    for caminho in range(len(todasOsCaminhos)):
        if not todasOsCaminhos[caminho]:
            todasOsCaminhos[caminho] = "do not communicate"
    return todasOsCaminhos