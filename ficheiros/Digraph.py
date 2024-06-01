class Digraph(object):
    """
    Class for Directed Graphs.
    """

    def __init__(self):
        """
        Initializes an empty Directed Graph.
        """
        self._nodes = []
        self._edges = {}
        self._edgesMins = {}

    def getNodes(self):
        """
        Returns the list of nodes.
        """
        return self._nodes
    
    def getNode(self, id):
        """
        Returns the node with the given id, or None if not found.
        """
        for node in self._nodes:
            if node._id == id:
                return node
        return None

    def getEdges(self):
        """
        Returns the dictionary of edges.
        """
        return self._edges
    
    def getEdgesMins(self):
        """
        Returns the dictionary of edge 'mins' values.
        """
        return self._edgesMins
    
    def addNode(self, node):
        """
        Adds a node to the graph. Raises ValueError if node already exists.
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        """
        Adds an edge to the graph. Raises ValueError if nodes not in graph.
        """
        src = edge.getSource()
        dest = edge.getDestination()
        mins = edge.getMins()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(dest)
        self._edgesMins[(src, dest)] = mins

    def childrenOf(self, node):
        """
        Returns the list of children for a given node.
        """
        return self._edges[node]

    def hasNode(self, node):
        """
        Checks if a node is in the graph.
        """
        return node in self._nodes

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result += f"{src.getName()} <- {self._edgesMins[(src, dest)]} -> {dest.getName()}\n"
        return result
