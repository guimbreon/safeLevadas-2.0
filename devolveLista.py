class Node(object):
    def __init__(self, id, name):
        """
        Requires: name is a string
        """
        self.name = name
        self._id = id
        
    def getName(self):
        return self.name
    
    def getId(self):
        return self._id
    
    def __str__(self):
        return self.name



class Edge(object):
    def __init__(self, src, dest, mins):
        """
        Requires: src and dst Nodes
        """
        self.src = src
        self.dest = dest
        self._mins = mins
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def getMins(self):
        return self._mins 
    
    def __str__(self):
            """
            String representation
            """
            return self._src.getName() +'<-' + self.getMins() + '->' + self._dest.getName()
    



class Digraph(object):
    """
    Class of Directed Graphs
    """


    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        """
        Constructs a Directed Graph
        
        Ensures:
        empty Digraph, i.e.
        Digraph such that [] == self.getNodes() and {} == self.getEdges() 
        """
        self._nodes = []
        self._edges = {}
        self._edgesMins = {}
        


    def getEdges(self):
        return self._edges
    
    def getEdgesMins(self):
        return self._edgesMins
    
    
    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the digraph yet
        Ensures:
        getNodes() == getNodes()@pre.append(node)
        getEdges[node] == [] 
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        mins = edge.getMins()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(dest)
        self._edgesMins[(src, dest)] = mins
        

        
    def childrenOf(self, node):
        return self._edges[node]

    
    def hasNode(self, node):
        return node in self._nodes

    
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() +' <- ' + str(self._edgesMins[(src, dest)])  +' -> ' + dest.getName() + '\n'
        return result




class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        

def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def DFS(graph, start, end, path, shortest):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def DFS_mins(graph, start, end, path, shortest_paths, totalMins, minTotal=float('inf')):
    """
    Depth first search in a directed graph with minutes accumulation

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph along with total minutes
    """
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        shortest_paths.append((path, totalMins))
        return shortest_paths

    for node in graph.childrenOf(start):
        if node not in path:
            mins = graph.getEdgesMins()[(start, node)]
            new_total_mins = totalMins + mins
            if len(shortest_paths) < 3 or new_total_mins < shortest_paths[-1][1]:
                shortest_paths = DFS_mins(graph, node, end, path, shortest_paths, new_total_mins, minTotal)
                shortest_paths.sort(key=lambda x: x[1])
                shortest_paths = shortest_paths[:3]
    return shortest_paths


def search(graph, start, end):
    shortest_paths = []
    shortest_paths = DFS_mins(graph, start, end, [], shortest_paths, 0)
    return shortest_paths




def testSP():
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', printPath(sp))


#testSP()

    
    

    
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

    sp= search(g, nodes[0], nodes[5])
    count = 1
    for item in sp:
        print("\n")
        print("path number: ", count)
        print(printPath(item[0]))
        print(item[1])
        count += 1
    #print('Shortest path found by DFS:', printPath(sp))
    #print(mins)
    
firstTest()


def bigTest():
    """
    tests all
    """

    nodes = []

    nodes.append(Node("A", "Lisboa")) #0
    nodes.append(Node("B", "Portalegre")) #1
    nodes.append(Node("C", "Coimbra")) #2
    nodes.append(Node("D", "Beja")) #3
    nodes.append(Node("E", "Setúbal")) #4
    nodes.append(Node("F", "Évora")) #5
    nodes.append(Node("G", "Bragança")) #6
    nodes.append(Node("H", "Loures")) #7
    nodes.append(Node("I", "Leiria")) #8
    nodes.append(Node("J", "Porto")) #9
    nodes.append(Node("K", "Fátima")) #10
    nodes.append(Node("L", "Tomar")) #11
    nodes.append(Node("M", "Espinhos")) #12
    nodes.append(Node("N", "Barreiro")) #13
    nodes.append(Node("O", "Santa Cruz")) #14
    nodes.append(Node("P", "Penafiel")) #15
    nodes.append(Node("Q", "Chaves")) #16
    nodes.append(Node("R", "Almada")) #17
    nodes.append(Node("S", "Queluz")) #18
    
    g = Digraph()

    for n in nodes:
        g.addNode(n)

    g.addEdge(Edge(nodes[0], nodes[1], 3))
    g.addEdge(Edge(nodes[1], nodes[2], 3))
    g.addEdge(Edge(nodes[1], nodes[3], 3))
    g.addEdge(Edge(nodes[1], nodes[4], 5))
    g.addEdge(Edge(nodes[3], nodes[5], 6))
    g.addEdge(Edge(nodes[4], nodes[5], 4))
    g.addEdge(Edge(nodes[4], nodes[15], 40))
    g.addEdge(Edge(nodes[4], nodes[14], 10))
    g.addEdge(Edge(nodes[5], nodes[6], 2))
    g.addEdge(Edge(nodes[5], nodes[10], 50))
    g.addEdge(Edge(nodes[6], nodes[7], 6))
    g.addEdge(Edge(nodes[7], nodes[8], 3))
    g.addEdge(Edge(nodes[8], nodes[9], 3))
    g.addEdge(Edge(nodes[10], nodes[11], 4))
    g.addEdge(Edge(nodes[10], nodes[12], 1))
    g.addEdge(Edge(nodes[12], nodes[14], 2))
    g.addEdge(Edge(nodes[14], nodes[13], 2))
    g.addEdge(Edge(nodes[14], nodes[15], 10))
    g.addEdge(Edge(nodes[15], nodes[16], 2))
    g.addEdge(Edge(nodes[16], nodes[17], 5))
    g.addEdge(Edge(nodes[17], nodes[18], 4))

    print(g)

    sp= search(g, nodes[1], nodes[17])
    count = 1
    for item in sp:
        print("\n")
        print("path number: ", count)
        print(printPath(item[0]))
        print(item[1])
        count += 1
    #print('Shortest path found by DFS:', printPath(sp))
    #print(mins)
    
bigTest()
