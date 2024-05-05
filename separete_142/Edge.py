class Edge(object):
    """
    Class of Edges
    """
    
    def __init__(self, src, dest, mins):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        Ensures:
        Edge such that src == self.getSource() and dest == self.getDestination() 
        """
        self._src = src
        self._dest = dest
        self._mins = mins

        
    def getSource(self):
        """
        Gets the source Node
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Node
        """
        return self._dest
    
    def getMins(self):
        return self._mins


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()

