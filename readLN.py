from devolveLista import *

def readLN(filePath):
    fp = open(filePath, 'r')
    lines = []
    for item in fp:
        if not item.startswith("#"):#assim sabemos q é a linha do comentário
            lines.append(item.strip().split(", ", 2))  #com 2 splits maximos, para ele n bugar com os ", " das listas
    return lines

           
def readMyStations(fileMyStations):
    """
    Esta função serve para extrair as estações de origem e destino contidas no arquivo fileMyStations.
    Retorna uma lista de listas, onde cada lista contem os nomes dos nodes
    de origem e destino
    """
    srcs_and_dests = []
    with open(fileMyStations, "r") as file:
        for line in file:
            src_name, dest_name = line.strip().split("-")
            srcs_and_dests.append([src_name.strip(), dest_name.strip()])
    return srcs_and_dests
    

def buildNodes(dataLN):
    nodes = {}
    for item in dataLN:
        nodes[item[0]] = Node(item[0],item[1])
    return nodes


def findSrcDestNodes(srcs_and_dests, network):
    """
    Esta função recebe uma lista de pares (src, dest) e um objeto network que contém nós.
    Retorna uma lista de listas, onde cada sublista contém dois objetos Node que representam a origem e o destino.
    """
    paired_nodes = []
    
    # Iterar sobre cada par
    for src_name, dest_name in srcs_and_dests:
        src_node = None
        dest_node = None
        
        # Procurar os nós correspondentes na rede
        for node in network._nodes:
            if node.getName() == src_name:
                src_node = node
            if node.getName() == dest_name:
                dest_node = node
                
        # Adicionar o par (src_node, dest_node) à lista se ambos forem encontrados
        if src_node and dest_node:
            paired_nodes.append([src_node, dest_node])
    return paired_nodes


def isEdgeBi(inFileSrc, inFileDest, edges):
    for edge in edges:
        if edge.getSource() != inFileSrc and edge.getDestination() != inFileDest:
            return False
    return True


def buildEdges(dataLN, nodes):
    edges = []
    for item in dataLN:
        item[2] = item[2].replace("[", "")
        item[2] = item[2].replace("]", "")
        for i in item[2].split("), "):
            i = i.split(", ")
            if i[0].replace("(","") != '':
                #Edge -> nodes[i[0].replace("(","")]: para onde vai,  nodes[item[0]]: origem, i[1].replace(")",""):tempo
                edges.append(Edge(nodes[item[0]], nodes[i[0].replace("(","")], int(i[1].replace(")",""))))
                if isEdgeBi(item[0], i[0], edges) == False:
                    edges.append(Edge(nodes[i[0].replace("(","")], nodes[item[0]], int(i[1].replace(")",""))))

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

    
    
    