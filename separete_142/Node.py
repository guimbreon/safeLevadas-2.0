class Node(object):
    """
    Class of Nodes
    """

    def __init__(self, letter, name):
        """
        Constructs a Node
        
        Requires:
        name is a string
        Ensures:
        node such that name == self.getName()
        """
        self._name = name
        self._letter = letter

        
    def getName(self):
        """
        Gets the name
        """
        return self._name

    
    def __str__(self):
        """
        String representation
        """
        return self._name
