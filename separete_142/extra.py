from Digraph import Digraph
from Edge import Edge
from Graph import Graph
from Node import Node

def printPath(path):
    """
    String representation of a path
    
    Requires:
    path a list of nodes
    Ensures:
    string whith nodes' names concatenated by '->'
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# DFS function as in the book (i.e. without comments):

##def DFS(graph, start, end, path, shortest):
##    path = path + [start]
##    print('Current DFS path:', printPath(path))
##    if start == end:
##        return path
##    for node in graph.childrenOf(start):
##        if node not in path:
##            if shortest == None or len(path) < len(shortest):
##                newPath = DFS(graph, node, end, path, shortest)
##                if newPath != None:
##                    shortest = newPath
##    return shortest
##
##
## # as in the book
##
##def search(graph, start, end):
##    return DFS(graph, start, end, [], None)


# commented (to help students better understand it)

def DFS(graph, start, end, path, shortest):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """

    # accumulates; start node entered into the path
    path = path + [start]
    
    # just to keep watching the recursion progressing
    print('Current DFS path:', printPath(path))

    # recursion: base
    # target node is reached (or initially start and end nodes are the same)
    if start == end: 
        return path

    # recursion: step
    # target was not reached and start node is not a leaf (i.e. it has children)
    for node in graph.childrenOf(start):
        
        if node not in path: # to avoid cycles

            # recursive call of DFS function to itself
            # if target was never reached yet before OR
            # this path is still the shortest so far
            if shortest == None or len(path) < len(shortest): 
                newPath = DFS(graph, node, end, path, shortest)
                
                if newPath != None: # if target node was reached
                    shortest = newPath
                    
    # the shortest path found so far after running the for cycle
    return shortest
def DFS_mins(graph, start, end, path, shortest, minTotal, totalMins = 0):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    # To get all the times in the edges
    edgesMins = graph.getEdgesMins()
    # Accumulates; start node entered into the path
    path = path + [start]
    
    # Just to keep watching the recursion progressing
    print('Current DFS path:', printPath(path))

    # Recursion: base
    # Target node is reached (or initially start and end nodes are the same)
    if start == end: 
        return path, minTotal

    # Recursion: step
    # Target was not reached and start node is not a leaf (i.e. it has children)
    for node in graph.childrenOf(start):
        
        if node not in path: # To avoid cycles
            if node in edgesMins: # If the node exists in edgeMins a.k.a if it has any follow-up node
                mins = graph.getEdgesMins()[node]
                print(mins, node)
                # Increment total minutes
                totalMins += mins
            # Recursive call of DFS function to itself
            # If target was never reached yet before OR
            # this path is still the shortest so far
            if shortest is None or totalMins < minTotal: 
                newPath, newTotalMins = DFS_mins(graph, node, end, path, shortest, totalMins)
                # If a new shortest path is found
                if newPath is not None and (shortest is None or len(newPath) < len(shortest)):
                    shortest = newPath
                    minTotal = newTotalMins
    
    # The shortest path found so far after running the for cycle
    return shortest, minTotal





# commented

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
    """
    Function to test search in a graph with a specific example
    """
    
    nodes = []
    
    for name in range(7): #Create 7 nodes
        nodes.append(Node(str(name)))
        
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
        
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[6]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[5]))
    g.addEdge(Edge(nodes[4],nodes[6]))
    g.addEdge(Edge(nodes[6],nodes[5]))
    
    print(g)
    """
    sp = search(g, nodes[0], nodes[5])
    
    print('Shortest path found by DFS:', printPath(sp))"""


#testSP()

    
    
def firstTest():
    """
    first Test out of the voices of my head
    """
    nodes =  []
    
    nodes.append(Node("A", "Lisboa"))
    nodes.append(Node("B", "Seixal"))
    nodes.append(Node("C", "Porto"))
    nodes.append(Node("D", "Pico Ruivo"))
    nodes.append(Node("E", "Coimbra"))
    nodes.append(Node("F", "Braga"))
    nodes.append(Node("G", "Faro"))

    
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
        
    g.addEdge(Edge(nodes[0], nodes[1], 2))
    g.addEdge(Edge(nodes[1], nodes[2], 5))
    g.addEdge(Edge(nodes[1], nodes[4], 7))
    g.addEdge(Edge(nodes[2], nodes[6], 2))
    g.addEdge(Edge(nodes[6], nodes[5], 4))
    g.addEdge(Edge(nodes[5], nodes[4], 9))
    g.addEdge(Edge(nodes[3], nodes[4], 3))
    
    print(g)

    sp, mins = search(g, nodes[0], nodes[2])
    
    print('Shortest path found by DFS:', printPath(sp))
    print(mins)
    
firstTest()