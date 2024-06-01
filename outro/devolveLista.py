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
        return self._src.getName() +'<-' + self.getMins() + '->' + self._dest.getName()
    



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




class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        

def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def DFS(graph, start, end, path, shortest):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def DFS_mins_print(graph, start, end, path, shortest_paths, totalMins, minTotal=float('inf')):
    """
    Depth first search in a directed graph with minutes accumulation

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph along with total minutes
    """
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        shortest_paths.append((path, totalMins))
        return shortest_paths

    for node in graph.childrenOf(start):
        if node not in path:
            mins = graph.getEdgesMins()[(start, node)]
            new_total_mins = totalMins + mins
            if len(shortest_paths) < 3 or new_total_mins < shortest_paths[-1][1]:
                shortest_paths = DFS_mins(graph, node, end, path, shortest_paths, new_total_mins, minTotal)
                shortest_paths.sort(key=lambda x: x[1])
                shortest_paths = shortest_paths[:3]
    return shortest_paths

def DFS_mins(graph, start, end, path, shortest_paths, totalMins, minTotal=float('inf')):
    """
    Depth first search in a directed graph with minutes accumulation

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph along with total minutes
    """
    path = path + [start]
    if start == end:
        shortest_paths.append((path, totalMins))
        return shortest_paths

    for node in graph.childrenOf(start):
        if node not in path:
            mins = graph.getEdgesMins()[(start, node)]
            new_total_mins = totalMins + mins
            if len(shortest_paths) < 3 or new_total_mins < shortest_paths[-1][1]:
                shortest_paths = DFS_mins(graph, node, end, path, shortest_paths, new_total_mins, minTotal)
                shortest_paths.sort(key=lambda x: x[1])
                shortest_paths = shortest_paths[:3]
    return shortest_paths


def searchMins(graph, start, end):
    shortest_paths = []
    shortest_paths = DFS_mins(graph, start, end, [], shortest_paths, 0)
    if shortest_paths == []:    
        return "do not communicate"
    else:
        return shortest_paths

