import sys
from MinHeap import MinHeap

# This class represents a directed graph. It can also work as an undirected graph by
# supplying edges from both directions
class Graph:
    # numberOfNodes: Represents nodes numbered from 1 to inputted number
    # edgeList: List<List<int>> 
    # [[Source,Target,Distance],...]
    # ex: [[1,2,1],[1,3,1],[2,4,2]]     
    def __init__(self,numberOfNodes,edgeList):
        self.numberOfNodes = numberOfNodes
        self.adjacencyList = {}      
        self.__populate_adjacency_list__(edgeList)  

    # populates the adjacency list with the inputted edge list
    def __populate_adjacency_list__(self,edgeList):
        for i in range(1,self.numberOfNodes+1):
            self.adjacencyList[i] = []
        for edge in edgeList:
            source,destination,weight = edge                           
            self.adjacencyList[source].append((destination,weight))

    def shortest_path_distance_to_all(self,startingNode):
        visited = [False for i in range(0,self.numberOfNodes+1)]
        distances = [sys.maxsize for i in range(0,self.numberOfNodes+1)]
        heapList = [(sys.maxsize,i) for i in range(1,self.numberOfNodes+1)]
        heapList[startingNode-1] = (0,startingNode)
        minheap = MinHeap(heapList)
        distances[startingNode] = 0
        while not minheap.is_empty():
            currentWeight,currentNode = minheap.extract_min()
            visited[currentNode] = True 
            for child in self.adjacencyList[currentNode]:        
                childNode,weight = child                
                if not visited[childNode]:
                    if distances[childNode] > distances[currentNode] + weight:
                        distances[childNode] = distances[currentNode] + weight
                        minheap.decrease_key(childNode,distances[childNode])

        for i in range(1,len(distances)):
            if i != startingNode:
                print('Node ',startingNode,'\'s shortest path distance to node ',i,' is ', distances[i])

    def shortest_path_to_specific_node(self,startingNode,endNode):
        route = {} # This is used to collect nodes on the path to the end node
        visited = [False for i in range(0,self.numberOfNodes+1)]
        distances = [sys.maxsize for i in range(0,self.numberOfNodes+1)] 
        heapList = [(sys.maxsize,i) for i in range(1,self.numberOfNodes+1)]
        heapList[startingNode-1] = (0,startingNode) # Initialize starting node distance to 0 in the list that will used to create the minheap
        minheap = MinHeap(heapList) # MinHeap creation
        distances[startingNode] = 0 # Initialize starting node distance to 0
        while not minheap.is_empty():
            # extract the node with minimum currently known distance to start node
            currentWeight,currentNode = minheap.extract_min()  
            visited[currentNode] = True # set as visited
            # if current visited node is end node, then path is complete
            if currentNode == endNode:
                print('Shortest Path Total Distance is ',distances[currentNode])
                break
            # Process each node that current node has an edge to
            for child in self.adjacencyList[currentNode]:        
                childNode,weight = child                                
                if not visited[childNode]:
                    # If child node's currently known shortest distance to start node
                    # is greater than current node's known shortest distance to start node
                    # plus the edge between them, then update child node's distance.                    
                    if distances[childNode] > distances[currentNode] + weight:
                        distances[childNode] = distances[currentNode] + weight
                        minheap.decrease_key(childNode,distances[childNode])                        
                        # Update current node as the previous node that is known to come 
                        # before child node on the shortest path from start node to child node
                        route[childNode] = currentNode 

        # Print the route from start to end node
        routeStr = ''
        routeList = []
        currentNode = endNode
        while route[currentNode] != startingNode:
            routeList.append(route[currentNode])
            currentNode = route[currentNode]
        routeStr += str(startingNode) + ' -> '
        for i in range(0,len(routeList)):            
            routeStr += str(routeList[i]) + ' -> '
        routeStr += str(endNode)                
        print(routeStr)
        
# g = Graph(4,[[1,2,1],[1,3,1],[2,4,2],[3,4,3]])
# g.shortest_path_to_specific_node(1,4)
