from devolveLista import *
from constants import * 
from readLN import * 

def fazerFuncionar(myStations, dig):
    todasOsCaminhos = []
    for pairOfStations in myStations:
        todasOsCaminhos.append(search2(dig, pairOfStations[0], pairOfStations[1]))
    return todasOsCaminhos

#filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/Projeto2/testSets/testSet1/myLevadasNetwork.txt"

#filePath = "l:/Aulas/Ano1/2Sem/ProgII/Projeto2/testSets/testSet1/myStations.txt"


filePath = "C:/Users/vitor/Downloads/Git/prog2_Proj2_LTI/testSets/testSet1/myStations.txt"
filePath2 = "C:/Users/vitor/Downloads/Git/prog2_Proj2_LTI/testSets/testSet1/myLevadasNetwork.txt"

dataLN = readLN(filePath2)
a = readMyStations(filePath)
dig = buildNetwork(dataLN)
b = findSrcDestNodes(a, dig)
#print(dataLN)
#print(a)
#print(c)
#print(dig)



todasOsCaminhos = fazerFuncionar(b, dig)


print(todasOsCaminhos)
for caminho in todasOsCaminhos:
    count = 1
    for item in caminho:
        print("\n")
        print("path number: ", count)
        print(printPath(item[0]))
        print(item[1])
        count += 1
