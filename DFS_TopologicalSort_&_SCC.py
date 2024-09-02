## Explore nodes aggressively ; LIFO data structure, but in this case we use recursion to do the same stuff
import copy

class Graph():
    def __init__(self,aj_list):
        self.aj_list = aj_list
        self.set_zero()

    def set_zero(self):
        self.is_explored = {vertex : False for vertex in self.aj_list.keys()}

    def new_vertex_dict(self):
        return {vertex:[] for vertex in self.aj_list.keys()}

    def DFS(self,graph,s,version=None):
        self.is_explored[s] = True
        if version == 'SCC_ver':
            self.SCC_group[s] = self.leader_vertex
        for neighbour in graph[s]:
            if self.is_explored[neighbour] == False:
                self.DFS(graph,neighbour,version)
        if version == 'Topo_ver':
            self.topo_order[s] = self.label
            self.label -= 1
        if version == 'SCC_ver':
            self.finish_order_list[s] = self.finish_order
            self.finish_order += 1


    def DFS_TopoOrder(self):
        self.set_zero()
        self.topo_order = {}
        self.label = len(self.aj_list)
        for vertex in self.aj_list.keys():
            if self.is_explored[vertex] == False:
                self.DFS(self.aj_list,vertex,'Topo_ver')
        return self.topo_order.items()


    def Kosaraju_two_pass_SCC(self):
        self.finish_order_list = self.new_vertex_dict()
        self.SCC_group = self.new_vertex_dict()
        self.reverse_graph()
        self.DFS_Loop(self.Raj_list,'1st')
        self.DFS_Loop(self.aj_list,'2nd')
        return self.SCC_group

    
    def DFS_Loop(self,graph,trial):
        self.set_zero()
        self.finish_order = 1
        self.leader_vertex = None
        if trial == '1st':
            process_order_list = {i : vertex for i,vertex in enumerate(graph.keys(),1) }
        if trial == '2nd':
            process_order_list = {order : vertex for vertex,order in self.finish_order_list.items() }
        for i in range(len(graph)):
            current_vertex = process_order_list[len(graph)-i]
            if self.is_explored[current_vertex] == False:
                self.leader_vertex = current_vertex
                self.DFS(graph,current_vertex,'SCC_ver')
        print(process_order_list)
        
    
    def reverse_graph(self):
        self.Raj_list = self.new_vertex_dict()
        for key,value_list in self.aj_list.items():
            for vertex in value_list:
                if key not in self.Raj_list[vertex]:
                    self.Raj_list[vertex].append(key)
        return self.Raj_list


aj_list = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['E', 'F'], 'E': ['D'], 'F': ['G'], 'G': ['H', 'J'], 'H': ['I', 'G'], 'I': ['J', 'H'], 'J': ['G', 'I']}
G = Graph(copy.deepcopy(aj_list))


print(G.Kosaraju_two_pass_SCC())


