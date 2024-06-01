from devolveLista import *
from constants import * 
from readLN import * 

def fazerFuncionar(myStations, dig):
    todasOsCaminhos = []
    for pairOfStations in myStations:
        if pairOfStations[0] != "out of network":
            todasOsCaminhos.append(search2(dig, pairOfStations[0], pairOfStations[1]))
        else:
            todasOsCaminhos.append("out of network")
    for caminho in range(len(todasOsCaminhos)):
        if not todasOsCaminhos[caminho]:
            todasOsCaminhos[caminho] = "do not communicate"
    return todasOsCaminhos