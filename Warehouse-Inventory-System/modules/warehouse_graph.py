#Implements shortest path to an item (DIJKSTRA), Nodes=warehouse shelves, Edges=Paths between shelves
#We can fetch items from optimal paths using graph algorithms.

import heapq

class WarehouseGraph:
    def __init__(self): #initializes an empty warehouse graph
        self.graph={} #Adjacency list representation of graph
        
    def add_shelf(self, shelf): #adds a warehouse shelf (node) to the graph
        if shelf not in self.graph:
            self.graph[shelf]={} #each shelf has an adjacency list

    def add_path(self,shelf1,shelf2,distance):
        self.add_shelf(shelf1)
        self.add_shelf(shelf2)
        self.graph[shelf1][shelf2]=distance #path from shelf1 to shelf2
        self.graph[shelf2][shelf1]=distance #path from shelf2 to shelf1

    def dijkstra(self,start_shelf): #shortest path algo
        distances = {}
        for shelf in self.graph: #loops through all shelves or rather nodes in the graph
            distances[shelf]=float('inf') #initial distance infinity
        distances[start_shelf]=0 #start shelf distance is 0
        parents={} #dictionary to store parent shelves or rather shortest path tree
        for shelf in self.graph:
            parents[shelf]=None #no shelf has a parent initially
        priority_queue=[(0,start_shelf)] 
        while priority_queue:
            current_distance, current_shelf=heapq.heappop(priority_queue) #min extracted
            for neighbor,weight in self.graph[current_shelf].items(): #loop through connected shelves
                new_distance=current_distance+weight #new shorter paths
                if new_distance<distances[neighbor]:
                    distances[neighbor]=new_distance
                    parents[neighbor]=current_shelf #shortest path of parent is updated
                    heapq.heappush(priority_queue,(new_distance,neighbor))
        return distances,parents #return shortest path distances and parents
    
    def shortest_path(self,start_shelf,target_shelf):
        distances, parents= self.dijkstra(start_shelf)
        if distances[target_shelf]==float('inf'):
            return None, float('inf') #no valid path exists for this
        path=[]
        current=target_shelf
        while current is not None:
            path.insert(0,current) #build path backwards from target to start
            current=parents[current]
        return path,distances[target_shelf] #return the optimal path and distance
    def display_graph(self):
        print("\n Warehouse Graph (shelves and their paths)") #adjacency list representation
        for shelf,connections in self.graph.items():
            print(f"{shelf}:{connections}")
