'''
Created on Mar 23, 2018

@author: Ale
'''

class Graph:
    def __init__(self, filename):
        """
        Initializes a directed graph with data from a file
        Input: filename - name of the file
        
        """
        self.dictIn={}
        self.dictOut={}
        self.dictInCosts={}
        self.dictOutCosts={}
        self.filename = filename
        self.nrVertices = 0
        self.nrEdges = 0
        self.loadFromFile()

    def loadFromFile(self):
        """
        Loads data from a file
        """
        file = open(self.filename, "r")
        line = file.readline().strip().split()
        self.nrVertices = int(line[0])
        self.nrEdges = int(line[1])
        
        for i in range(0, int(line[0])):
            self.dictOut[i] = []
            self.dictIn[i] = []
            
        for i in range(0, int(line[0])):
            for j in range(0, int(line[0])):
                self.dictOutCosts[(i, j)] = 0
                self.dictInCosts[(j, i)] = 0
            
        for line in file:
            attributes = line.split(" ")
            if len(attributes) != 3:
                continue
            self.addEdge(int(attributes[0]), int(attributes[1]))
            self.setEdge(int(attributes[0]), int(attributes[1]), int(attributes[2]))
        
        file.close()
    
    def setEdge(self, start, end, cost):
        """
        Sets the cost to an edge given by start and end
        Input: start - vertex
                end - vertex
                cost - integer
        Output: the cost is set
        """
        self.dictOutCosts[(start, end)] = cost 
        self.dictInCosts[(end, start)]= cost 
        
    def getNrVertices(self):
        """
        Gets the number of vertices in the graph
        Returns an integer
        """
        return self.nrVertices
    
    def getNrEdges(self):
        """
        Gets the number of edges in the graph
        Returns an integer
        """
        return self.nrEdges

    def findVertex(self, x):
        """
        Checks if a vertex exists
        Input: x - vertex
        Output: True if it does, False otherwise
        """
        if x in self.parseX():
            return True
            
        return False
        
    def addEdge(self, start, end):
        """
        Adds the edge going from start to end to the graph
        Input: start - the starting vertex
               end - the ending vertex
        Output: True if it was added, False otherwise
        Precondition: the vertices are valid in the graph
        """
        if start not in self.parseX() or end not in self.parseX():
            return False
        
        if end in self.dictOut[start]:
            return False

        self.dictIn[end].append(start)
        self.dictOut[start].append(end)
        return True
    
    def removeEdge(self, start, end):
        """
        Removes an edge from start to end, and the cost attached to it
        Input: start - vertex
                end - vertex
        Output: True if it was removed, False otherwise
        Precondition: the edge from start to end exists in the graph
        """
        if self.isEdge(start, end) == True:
            self.dictOut[start].remove(end)
            self.dictIn[end].remove(start)
            self.dictOutCosts[(start, end)] = 0
            self.dictInCosts[(end, start)] = 0
            self.nrEdges -=1
            return True
        
        return False
    
    def addVertex(self, x):
        """
        Adds a vertex
        Input: x - vertex
        Output: None
        """
        if x in self.parseX():
            return False
        
        self.dictIn[x] = []
        self.dictOut[x] = []
        self.nrVertices += 1
        
        return True
        
        
    def removeVertex(self, x):
        """
        Removes a vertex, and all the edges that contained it
        Input: x - vertex
        Output: None
        """
        if x not in self.parseX():
            return False

        for y in self.parseOut(x):
            self.parseIn(y).remove(x)
            
        for y in self.parseIn(x):
            self.parseOut(y).remove(x)
        
        
        del self.dictIn[x]
        del self.dictOut[x]
    
        
        self.nrVertices -= 1
        
        return True
        
        
    def parseX(self):
        """
        Returns an iterable object containing all the vertices of the graph
        """
        return self.dictIn.keys()

    def parseOut(self, x):
        """
        Returns an iterable object containing all the outbound neighbours of the given vertex
        """
        return self.dictOut[x]

    def parseIn(self, x):
        """
        Returns an iterable object containing all the inbound neighbours of the given vertex
        """
        return self.dictIn[x]
    
    def parseC(self):
        """
        Returns an iterable object containing all the costs of the graph
        """
        return self.dictOutCosts.keys()

    def isEdge(self, x, y):
        """
        Returns True if there is an edge from x to y
        """
        if x in self.parseX() and y in self.parseX():
            return y in self.dictOut[x] 
        
        return False
    
    def getInDegree(self, x):
        """
        Gets the in degree of a vertex x
        Input: x - vertex
        Output: an integer
        """
        return len(self.dictIn[x])
    
    def getOutDegree(self, x):
        """
        Gets the out degree of a vertex x
        Input: x - vertex
        Output: an integer
        """
        return len(self.dictOut[x])
    
    def getCost(self, start, end):
        """
        Gets the cost of an edge given by start and end
        Input: start - vertex
                end - vertex
        Output: an integer
        """
        return self.dictOutCosts[(start, end)]
