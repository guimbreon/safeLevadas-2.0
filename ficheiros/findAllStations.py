# 2023-2024 Programação 2 LTI
# Grupo 5
# 62372 Guilherme Soares
# 62211 Vitória Correia
from devolveLista import *
from constants import * 
from readFiles import * 

def findAllStations(myStations, dig):
    """
     Find paths between all pairs of stations using a specified search function.

    Parameters:
    - myStations (list of lists): A list of list, where each list contains two stations.
    - dig (function): Digraph

    Returns:
    - list: A list of paths between the stations.
    """
    allThePaths = []
    for pairOfStations in myStations:
        if pairOfStations[0] != "out of the network":
            allThePaths.append(search(dig, pairOfStations[0], pairOfStations[1]))
        else:
            allThePaths.append("out of the network")
    for caminho in range(len(allThePaths)):
        if not allThePaths[caminho]:
            allThePaths[caminho] = "do not communicate"
    return allThePaths