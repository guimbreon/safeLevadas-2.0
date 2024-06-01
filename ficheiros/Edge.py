class Edge(object):
    def __init__(self, src, dest, mins):
        """
        Initializes an edge from src to dest with a given mins value.
        Requires: src and dest are Nodes.
        """
        self.src = src
        self.dest = dest
        self._mins = mins
        
    def getSource(self):
        """
        Returns the source node.
        """
        return self.src
    
    def getDestination(self):
        """
        Returns the destination node.
        """
        return self.dest
    
    def getMins(self):
        """
        Returns the mins value.
        """
        return self._mins 
    
    def __str__(self):
        """
        Returns a string representation of the edge.
        """
        return f"{self.src.getName()} <- {self.getMins()} -> {self.dest.getName()}"
