from devolveTamanho import *
def readLN(filePath):
    fp = open(filePath, 'r')
    lines = []
    for item in fp:
        if not item.startswith("#"):#assim sabemos q é a linha do comentário
            lines.append(item.strip().split(", ", 2))  #com 2 splits maximos, para ele n bugar com os ", " das listas
    return lines
    

def buildNodes(dataLN):
    nodes = {}
    for item in dataLN:
        nodes[item[0]] = Node(item[0],item[1])
    return nodes



def buildEdges(dataLN, nodes):
    edges = []
    for item in dataLN:
        item[2] = item[2].replace("[", "")
        item[2] = item[2].replace("]", "")
        for i in item[2].split("), "):
            i = i.split(", ")
            if i[0].replace("(","") != '':
                #Edge -> nodes[i[0].replace("(","")]: para onde vai,  nodes[item[0]]: origem, i[1].replace(")",""):tempo
                edges.append(Edge(nodes[item[0]], nodes[i[0].replace("(","")], i[1].replace(")","")))
    return edges


def buildNetwork(dataLN):
    g = Digraph()
    nodes = buildNodes(dataLN)
    edges = buildEdges(dataLN, nodes)
    
    for node in nodes:
        g.addNode(nodes[node])
        
    for edge in edges:
        g.addEdge(edge)
    
    return g  



#filePath = "l:/Aulas/Ano1/2Sem/ProgII/Projeto2/testSets/testSet1/myLevadasNetwork.txt"
filePath = "C:/Users/vitor/Downloads/Git/prog2_Proj2_LTI/testSets/testSet1/myLevadasNetwork.txt"

dataLN = readLN(filePath)
dig = buildNetwork(dataLN)

print(dig)