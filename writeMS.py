from devolveLista import *
from constants import * 
"""
recebe 
"""

    
def firstTest():
    """
    first Test out of the voices of my head
    """
    nodes =  []
    
    nodes.append(Node("A", "Lisboa")) #0
    nodes.append(Node("B", "Seixal")) #1
    nodes.append(Node("C", "Porto")) #2
    nodes.append(Node("D", "Pico Ruivo")) #3
    nodes.append(Node("E", "Coimbra")) #4
    nodes.append(Node("G", "Braga")) #5
    nodes.append(Node("F", "Faro")) #6

    
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
        
    g.addEdge(Edge(nodes[0], nodes[1], 2))
    g.addEdge(Edge(nodes[1], nodes[2], 4))
    g.addEdge(Edge(nodes[1], nodes[3], 5))
    g.addEdge(Edge(nodes[2], nodes[6], 2))
    g.addEdge(Edge(nodes[3], nodes[5], 12))
    g.addEdge(Edge(nodes[3], nodes[4], 3))
    g.addEdge(Edge(nodes[5], nodes[6], 4))
    g.addEdge(Edge(nodes[6], nodes[5], 4))
    
    print(g)
    # [0] -> lista e [1] -> tempo
    return search(g, nodes[0], nodes[5])
    

def writeMS(objeto, filePath):
    fp = open(filePath, "w")
    
    for item in objeto:
        last = len(item[LISTA]) - 1 # pegando no tamanho da lista subtrais 1 para obter o ultimo elemento
        print(item[LISTA][FIRST], item[LISTA][last])
        
        linha = "# " + item[LISTA][FIRST].getName() + " - " + item[LISTA][last].getName() + "\n"
        fp.write(linha)
        linha = str(item[TEMPO]) + ", "
        count = 1
        for elem in item[0]:
            if count == last:
                linha += elem.getName() + "\n"
                
            else:
                
                linha += elem.getName() + ", "
            count += 1
        fp.write(linha)
            

objeto = firstTest()
filePath = "l:/Aulas/Ano1/2Sem/ProgII/Projeto2/teste.txt"
writeMS(objeto, filePath)