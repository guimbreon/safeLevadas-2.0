class Node(object):
    def __init__(self, letter, name):
        """
        Requires: name is a string
        """
        self.name = name
        self._letter = letter
        
    def getName(self):
        return self.name
    
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

def DFS_mins(graph, start, end, path, shortest, totalMins, minTotal=float('inf')):
    """
    Depth first search in a directed graph with minutes accumulation

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph along with total minutes
    """
    # Accumulates; start node entered into the path
    path = path + [start]
    
    # Just to keep watching the recursion progressing
    print('Current DFS path:', printPath(path))

    # Recursion: base
    # Target node is reached (or initially start and end nodes are the same)
    if start == end: 
        return path, totalMins

    # Recursion: step
    # Target was not reached and start node is not a leaf (i.e. it has children)
    for node in graph.childrenOf(start):
        print(start, node)
        
        if node not in path: # To avoid cycles
            # Calculating total minutes for the current path
            mins = graph.getEdgesMins()[(start, node)]
            newTotalMins = totalMins + mins
            
            # Recursive call of DFS function to itself
            # If target was never reached yet before OR
            # this path is still the shortest so far
            if shortest is None or newTotalMins < minTotal: 
                newPath, newTotalMins = DFS_mins(graph, node, end, path, shortest, newTotalMins, minTotal)
                # If a new shortest path is found
                if newPath is not None and (shortest is None or len(newPath) < len(shortest)):
                    shortest = newPath
                    minTotal = newTotalMins
    
    # The shortest path found so far after running the for cycle
    return shortest, minTotal


def search(graph, start, end):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """

    # fourth param: accumulator of nodes (to define path)
    # fifth param: witness: keeps best path found so far

    #return DFS(graph, start, end, [], None, 0)
    return DFS_mins(graph, start, end, [], None, 0)



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
    
    print(g)

    sp, mins = search(g, nodes[0], nodes[5])
    
    print('Shortest path found by DFS:', printPath(sp))
    print(mins)
    
firstTest()