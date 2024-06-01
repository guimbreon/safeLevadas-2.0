from devolveLista import *
from constants import * 
from readLN import * 
from findAllStations import *




def writeMS(objeto, myStations, filePath):
    fp = open(filePath, "w")
    
    for i in range(len(objeto)):
        fp.write("#" + myStations[i][0] + " - " +  myStations[i][1])
        fp.write("\n")
        if objeto[i] != "out of network" and objeto[i] != "do not communicate": #TESTAR SE É OUT OF NETWORK OU N

            for caminho, tempo in objeto[i]:
                caminhoStr = str(tempo) +", "
                count = 1
                for item in caminho:
                    if len(caminho) > count:
                        caminhoStr += item.__str__() +   ", "
                    else:
                        caminhoStr += item.__str__()
                    count += 1
                    
                fp.write(caminhoStr)
                fp.write("\n")
        else:
            fp.write(objeto[i])
            fp.write("\n")
            

filePath = "l:/Aulas/Ano1/2Sem/ProgII/projeto2/test_set/myStations_A.txt"
filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/projeto2/test_set/myLevadasNetwork.txt"


dataLN = readLN(filePath2)
a = readMyStations(filePath)
dig = buildNetwork(dataLN)
b = findSrcDestNodes(a, dig)

todasOsCaminhos = fazerFuncionar(b, dig)


filePath3 = "l:/Aulas/Ano1/2Sem/ProgII/projeto2/teste.txt"
writeMS(todasOsCaminhos, a, filePath3)
"""for caminho in todasOsCaminhos:
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
        print(caminho)"""