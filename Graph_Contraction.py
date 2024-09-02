## Objective: To find the minimum cut of a graph (i.e. a partition into non-empty sub-graph A & B s.t. no. of crossing edge is minimum)
## ... randomised algorithm (on choice of edge) + randomised sampling (i.e. n^2ln(n) trials to find the lowest result)

## Idea: Randomly choose an edge, 'contract' the edge such that the two endpoint vertices merge into one and the edge joining them disappears, also eliminates any self-loop
## ... rinse and repeat until only two vertices left, return the no. of crossing links
## ... it is not guaranteed that the no. of crossing links is minimum in this trial (indeed the success chance is merely 1/n^2),
## ... therefore we iterate it by n^2ln(n) times (failure chance = 1/n ) ; although not optimum but definitely better than the brute-force 2^n

import random
import copy

class Graph:
    ## initialise graph and all of its vertices
    def __init__(self,verrtices,edges):
        self.vertices = vertices
        self.edges = edges

            
    ## contraction algorithm (merge, eliminate edge and self-loop)
    def find_min_cut(self):
        while len(vertices) > 2: 
            u,v = random.choice(self.edges)                             ## random select a edge
            
            self.vertices.remove(v)                                     ## merge nodes (by removing v) & regrowing edges
            new_edges = []
            for x,y in self.edges:
                if x == v : x = u
                elif y == v : y = u
                
                if x != y : new_edges.append((x,y))                     ## remove self-loops ( will result in x = y after the previous two 'if)                 
            self.edges = new_edges
        return len(self.edges)
    def display(self):
        print(self.vertices,self.edges)



vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'),('A', 'C'),('B', 'C'),('B', 'D'),('C', 'D')]        ## = K4 complete graph - 1 diagonal edge
min_cut = float('inf')

for _ in range(200):
    graph = Graph(copy.deepcopy(vertices),copy.deepcopy(edges))
    current_cut = graph.find_min_cut()
    min_cut = min(min_cut, current_cut)

print(min_cut)

        
