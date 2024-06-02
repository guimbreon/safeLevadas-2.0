# 2023-2024 Programação 2 LTI
# Grupo 5
# 62372 Guilherme Soares
# 62211 Vitória Correia
class Node(object):
    def __init__(self, id, name):
        """
        Initialize a Node object.

        Parameters:
        - id (int): The unique identifier for the node.
        - name (str): The name of the node. Requires that name is a string.
        """
        self._name = name
        self._id = id
        
    def getName(self):
        """
        Get the name of the node.

        Returns:
        - str: The name of the node.
        """
        return self._name
    
    def getId(self):
        """
        Get the unique identifier of the node.

        Returns:
        - int: The unique identifier of the node.
        """
        return self._id
    
    def __str__(self):
        """
        Get the string representation of the node.

        Returns:
        - str: The name of the node.
        """
        return self._name