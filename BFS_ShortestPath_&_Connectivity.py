## Explore nodes by layers ; explored nodes stored in FIFO Data Structure (e.g. Queue), queueing for search sequence

import copy

class Graph:
    ## initialise 
    def __init__(self,aj_list):
        self.aj_list = aj_list
        
    ## set local boolean for each of the nodes to indicate explored / unexplored & Queue List
    def reset(self):
        self.is_explored = { vertice : False for vertice in self.aj_list.keys() }
        self.queue = []
        

    def BFS(self,s):
        self.reset()
        self.is_explored[s] = True
        self.queue.append(s)
        while len(self.queue) != 0:
            v = self.queue[0]
            self.queue.remove(v)
            for neighbour in self.aj_list[v]:
                if self.is_explored[neighbour] == False:
                    self.queue.append(neighbour)
                    self.is_explored[neighbour] = True

                    
        return list(self.is_explored.items())

    def BFS_ShortestPath(self,s):
        self.reset()
        self.is_explored[s] = True
        self.distance = { vertice : 0 if vertice == s else float('inf') for vertice in self.aj_list.keys() }
        self.queue.append(s)
        while len(self.queue) != 0:
            v = self.queue[0]
            self.queue.remove(v)
            for neighbour in self.aj_list[v]:
                if self.is_explored[neighbour] == False:
                    self.distance[neighbour] = self.distance[v] + 1 
                    self.queue.append(neighbour)
                    self.is_explored[neighbour] = True

                    
        return list(self.distance.items())
        




aj_list = {'A': ['C', 'D', 'E'], 'B': ['D', 'F', 'G'], 'C': ['A', 'H', 'I'], 'D': ['A', 'B', 'J'], 'E': ['A', 'F', 'I'], 'F': ['B', 'E', 'J'], 'G': ['B', 'H', 'J'], 'H': ['C', 'G', 'I'], 'I': ['C', 'E', 'H'], 'J': ['D', 'F', 'G']}

G = Graph(copy.deepcopy(aj_list))
print(G.BFS_ShortestPath('A'))
print(G.BFS('A'))
