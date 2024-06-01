from devolveLista import *
from constants import * 
from readLN import * 
from findAllStations import *

def writeMS(objeto, myStations, allStations, filePath):
    lines = []

    for i in range(len(objeto)):
        lines.append("# " + myStations[i][0] + " - " + myStations[i][1])
        if objeto[i] != "out of network" and objeto[i] != "do not communicate":
            for caminho, tempo in objeto[i]:
                caminhoStr = str(tempo) + ", "
                count = 1
                for item in caminho:
                    if len(caminho) > count:
                        caminhoStr += item.__str__() + ", "
                    else:
                        caminhoStr += item.__str__()
                    count += 1

                lines.append(caminhoStr)
        elif objeto[i] == "out of network":
            if allStations[i][1] == "sour":  # source doesn't exist
                lines.append(myStations[i][0] + " " + objeto[i])
            else:
                lines.append(myStations[i][1] + " " + objeto[i])
        elif objeto[i] == "do not communicate":
            lines.append(myStations[i][0] + " and " + myStations[i][1] + " " + objeto[i])

    with open(filePath, "w") as fp:
        fp.write("\n".join(lines))
            
            

#filePath = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myStations_A.txt"
#filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myLevadasNetwork.txt"


filePath = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myStations_B.txt"
filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myLevadasNetwork.txt"

dataLN = readLN(filePath2)
a = readMyStations(filePath)
dig = buildNetwork(dataLN)
b = findSrcDestNodes(a, dig)

todasOsCaminhos = fazerFuncionar(b, dig)

filePath3 = "teste.txt"
writeMS(todasOsCaminhos, a, b, filePath3)
