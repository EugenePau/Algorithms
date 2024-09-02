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
    def __init__(self,aj_list):
        self.aj_list = aj_list

            
    ## contraction algorithm (merge, eliminate edge and self-loop)
    def find_min_cut(self):
        while len(self.aj_list.keys()) > 2: 
            u = random.choice(list(self.aj_list.keys()))                      ## random select a edge
            v = random.choice(self.aj_list[u]) 

            self.aj_list[u].extend(self.aj_list[v])
            del self.aj_list[v]                                         ## merge nodes (by removing v)            
                                           
            for v1,neighbours in list(self.aj_list.items()):            ## regrowing edges
                new_edges = []
                for v2 in neighbours:
                    if v2 == v : v2 = u
                    if v1 != v2 : new_edges.append(v2)                  ## remove self-loops ( will result in x = y after the previous two 'if)                 
                self.aj_list[v1] = new_edges

                 
        return len(list(self.aj_list.values())[0])                            ## both vertices must have same length => pick the first array-value
    



## input adjacency list from file
import tkinter.filedialog
import re

filename = tkinter.filedialog.askopenfilename()
file = open(filename,'r')

aj_list = dict()
for line in file:
    key = line[0]
    aj_list[key] = re.findall('.*?\s(\S),*',line)

file.close()

print(f'Input = {aj_list}')

## Trial Zone    
min_cut = float('inf')

for _ in range(200):
    graph = Graph(copy.deepcopy(aj_list))
    current_cut = graph.find_min_cut()
    min_cut = min(min_cut, current_cut)

print(min_cut)

        
