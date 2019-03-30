'''
Created on Mar 23, 2018

@author: Ale
'''
from Graph import Graph
from _collections import deque

class UI:
    def __init__(self, g):
        self.g = g
    
    def bfsBackward(self, start, end):
        visited = {end: None}
        queue = deque([end])
        while queue:
            node = queue.popleft()
            if node == start:
                path = []
                while node is not None:
                    path.append(node)
                    node = visited[node]
                return path
            for neighbour in self.g.dictIn[node]:
                if neighbour not in visited:
                    visited[neighbour] = node
                    queue.append(neighbour)
                    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in self.g.parseOut(start) - visited:
            self.dfs(next, visited)
        return visited
        
    def printMenu(self):
        """
        Prints out the menu 
        """
        print("1. Print the content of the file (the graph)")
        print("2. Get the number of vertices and edges")
        print("3. Check if there is an edge between two vertices")
        print("4. Get the IN degree and OUT degree of a vertex")
        print("5. Get the outbound neighbours of a vertex")
        print("6. Get the inbound neighbours of a vertex")
        print("7. Get the cost of an edge")
        print("8. Modify a cost of an edge")
        print("9. BONUS: Add an edge")
        print("10. BONUS: Remove an edge")
        print("11. BONUS: Add a vertex")
        print("12. BONUS: Remove a vertex")
        print("13. Get the lowest length path between two vertices (backward BFS from the ending vertex)")
        print("0. Exit the program")
        
    def printGraph(self):
        """
        Prints out the graph, each vertex with its inbound and outbound neighbours
        """
        print("The graph: ")
        for node in self.g.parseX():
            print(str(node) + " In: " + str(self.g.parseIn(node)) + " Out: " + str(self.g.parseOut(node)))
            
    def printCosts(self):
        """
        Prints out the edges and their cost
        """
        print("Costs: ")
        for (i,j) in self.g.parseC():
            if self.g.isEdge(i, j):
                print(str((i, j)) + " - " + str(self.g.dictOutCosts[(i, j)]))

    def start(self):
        """
        Starts the program
        """
        self.printMenu()
        while True:
            option = str(raw_input("Enter an option: "))
            
            if option == '1':
                self.printGraph()
                self.printCosts()
                
            elif option == '2':
                print("Number of vertices: " + str(self.g.getNrVertices()))
                print("Number of edges: " + str(self.g.getNrEdges()))
                
            elif option == '3':
                start = input("Enter the start vertex: ")
                end = input("Enter the end vertex: ")
                
                if self.g.isEdge(start, end) == True:
                    print("Yes, there is an edge between " + str(start) + " and " + str(end))
                else:
                    print("No, there is no edge between " + str(start) + " and " + str(end))
                    
            elif option == '4':
                x = input("Enter a vertex: ")
                
                if self.g.findVertex(x) == True:
                    print("IN degree: " + str(self.g.getInDegree(x)))
                    print("OUT degree: " + str(self.g.getOutDegree(x)))
                else:
                    print("No such vertex")
                
            elif option =='5':
                x = input("Enter a vertex: ")
                
                if self.g.findVertex(x) == True:
                    print("Outbound neighbours: ")
                    print(self.g.parseOut(x))
                else:
                    print("No such vertex")
                
            elif option =='6':
                x = input("Enter a vertex: ")
                
                if self.g.findVertex(x) == True:
                    print("Inbound neighbours: ")
                    print(self.g.parseIn(x))
                else:
                    print("No such vertex")
                
            elif option == '7':
                print("You chose to see a cost")
                start = input("Enter the start vertex: ")
                end = input("Enter the end vertex: ")
                if self.g.isEdge(start, end) == True:
                    print(str(start) + " - " + str(end) + " cost: " + str(self.g.getCost(start, end)))
                else:
                    print("No edge between them")
                    
            elif option == '8':
                print("You chose to modify a cost")
                start = input("Enter the start vertex: ")
                end = input("Enter the end vertex: ")
                if self.g.isEdge(start, end) == True:
                    cost = int(input("New cost: "))
                    self.g.setEdge(start, end, cost)
                else:
                    print("No edge between them")
                    
            elif option == '9':
                print("You chose to add an edge")
                
                start = input("Enter the start vertex: ")
                end = input("Enter the end vertex: ")
                cost = int(input("Enter the cost: "))
                
                if self.g.isEdge(start, end) == False and self.g.addEdge(start, end):
                    self.g.nrEdges +=1
                    self.g.setEdge(start, end, cost)
                    print("Edge added successfully")
                else:
                    print("Error. Edge not added")
                    
            elif option == '10':
                print("You chose to remove an edge")
                start = input("Enter the start vertex: ")
                end = input("Enter the end vertex: ")

                if self.g.removeEdge(start, end):
                    print("Edge removed successfully")
                else:
                    print("Error. Edge not removed")
                    
            elif option == '11':
                print("You chose to add a vertex")
                x = input("Enter the vertex: ")
                if self.g.addVertex(x) == True:
                    print("Vertex added successfully")
                else:
                    print("Error. Vertex already in graph")
                
            elif option == '12':
                print("You chose to remove a vertex")
                x = input("Enter the vertex: ")
                if self.g.removeVertex(x) == True:
                    print("Vertex removed successfully")
                else:
                    print("Error. Vertex not found")
                    
            elif option == '13':
                x = input("Enter starting vertex: ")
                y = input("Enter end vertex: ")
                
                print(self.bfsBackward(x, y))
                  
            elif option == '0':
                print("Exited the program")
                break
            
            else:
                print("Not a valid option")
            
G = Graph("graph1k.txt")
ui = UI(G)
ui.start()