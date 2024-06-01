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
        


    def getNodes(self):
        return self._nodes
    
    def getNode(self, id):
        for node in self._nodes:
            if node._id == id:
                return node
        return None

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