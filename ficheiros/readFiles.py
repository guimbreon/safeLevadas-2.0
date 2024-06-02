# 2023-2024 Programação 2 LTI
# Grupo 5
# 62372 Guilherme Soares
# 62211 Vitória Correia
from devolveLista import *
def readLN(filePath):
    """
    Read and process a file to extract lines of data.

    Parameters:
    - filePath (str): The path to the input file containing the data.

    Returns:
    - list: A list of processed lines, where each line is split into components.
    """
    fp = open(filePath, 'r')
    lines = []
    for item in fp:
        if not item.startswith("#"):  # Check if the line has an #
            lines.append(item.strip().split(", ", 2))  # Split with a maximum of 2 to avoid splitting lists
    return lines


def readMyStations(fileMyStations):
    """
    Extract source and destination stations from a file.

    Parameters:
    - fileMyStations (str): The path to the file containing the station data.

    Returns:
    - list: A list of lists, where each sublist contains the source and destination station names.
    """
    srcs_and_dests = []
    with open(fileMyStations, "r") as file:
        for line in file:
            src_name, dest_name = line.strip().split("-")
            srcs_and_dests.append([src_name.strip(), dest_name.strip()])
    return srcs_and_dests


def buildNodes(dataLN):
    """
    Build nodes from the provided data.

    Parameters:
    - dataLN (list): A list of data where each item contains node information.

    Returns:
    - dict: A dictionary of nodes, where keys are node names and values are Node objects.
    """
    nodes = {}
    for item in dataLN:
        nodes[item[0]] = Node(item[0], item[1])
    return nodes


def findSrcDestNodes(srcs_and_dests, network):
    """
    Find source and destination nodes in the network.

    Parameters:
    - srcs_and_dests (list): A list of pairs (src, dest) representing source and destination names.
    - network (object): An object containing the network nodes.

    Returns:
    - list: A list of lists, where each sublist contains two Node objects representing the source and destination.
    """
    paired_nodes = []
    
    for src_name, dest_name in srcs_and_dests:
        src_node = None
        dest_node = None
        
        for node in network._nodes:
            if node.getName() == src_name:
                src_node = node
            if node.getName() == dest_name:
                dest_node = node
                
        if src_node and dest_node:
            paired_nodes.append([src_node, dest_node])
        else:
            if not src_node:
                paired_nodes.append(["out of the network", "sour"])
            if not dest_node:
                paired_nodes.append(["out of the network", "dest"])
    return paired_nodes


def isEdgeBi(inFileSrc, inFileDest, edges):
    """
    Check if an edge is bidirectional.

    Parameters:
    - inFileSrc (Node): The source node from the file.
    - inFileDest (Node): The destination node from the file.
    - edges (list): A list of edges to check against.

    Returns:
    - bool: True if a bidirectional edge exists, False otherwise.
    """
    for edge in edges:
        if edge.getSource() == inFileDest and edge.getDestination() == inFileSrc:
            return True
    return False


def buildEdges(dataLN, nodes):
    """
    Build edges from the provided data.

    Parameters:
    - dataLN (list): A list of data where each item contains edge information.
    - nodes (dict): A dictionary of nodes where keys are node names and values are Node objects.

    Returns:
    - list: A list of Edge objects including bidirectional edges.
    """
    edges = []
    
    for item in dataLN:
        item[2] = item[2].strip("[]")
        for pair in item[2].split("), "):
            node_info = pair.strip("()").split(", ")
            if node_info[0]:
                source_node = nodes[item[0]]
                dest_node = nodes[node_info[0]]
                weight = int(node_info[1])
                edges.append(Edge(source_node, dest_node, weight))
    
    biedge = []
    
    for edge in edges:
        if not isEdgeBi(edge.getSource(), edge.getDestination(), edges):
            biedge.append(Edge(edge.getDestination(), edge.getSource(), edge.getMins()))
    
    return edges + biedge


def buildNetwork(dataLN):
    """
    Build a network (directed graph) from the provided data.

    Parameters:
    - dataLN (list): A list of data where each item contains information to build the network.

    Returns:
    - Digraph: A directed graph containing the nodes and edges from the data.
    """
    g = Digraph()
    nodes = buildNodes(dataLN)
    edges = buildEdges(dataLN, nodes)
    
    for node in nodes:
        g.addNode(nodes[node])
        
    for edge in edges:
        g.addEdge(edge)
    
    return g
