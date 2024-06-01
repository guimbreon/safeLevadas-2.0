from devolveLista import *
from constants import * 
from readLN import * 

def fazerFuncionar(myStations, dig):
    todasOsCaminhos = []
    for pairOfStations in myStations:
        if pairOfStations != "out of network":
            todasOsCaminhos.append(search2(dig, pairOfStations[0], pairOfStations[1]))
        else:
            todasOsCaminhos.append("out of network")
    for caminho in range(len(todasOsCaminhos)):
        if not todasOsCaminhos[caminho]:
            todasOsCaminhos[caminho] = "do not communicate"
    return todasOsCaminhos
            
filePath = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/testSets - VI/testSet7/myStations.txt"
filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/testSets - VI/testSet7/myLevadasNetwork.txt"

dataLN = readLN(filePath2)
a = readMyStations(filePath)
dig = buildNetwork(dataLN)
b = findSrcDestNodes(a, dig)
#print(dataLN)
#print(a)
#print(c)
#print(dig)



todasOsCaminhos = fazerFuncionar(b, dig)

#print(fazerFuncionar(b, dig))

for caminho in todasOsCaminhos:
    count = 1
    if caminho != "out of network" and caminho != "do not communicate":
        for item in caminho:
            print("\n")
            print("path number: ", count)
            print(printPath(item[0]))
            print(item[1])
            count += 1
    else:
        print("\n")
        print(caminho)