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
        return str(self.src.getName()) +'<-' + str(self.getMins()) + '->' + str(self.dest.getName())