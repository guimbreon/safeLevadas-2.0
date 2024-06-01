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