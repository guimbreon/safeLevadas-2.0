# 2023-2024 Programação 2 LTI
# Grupo 5
# 62372 Guilherme Soares
# 62211 Vitória Correia
from Digraph import Digraph
from Edge import Edge

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)