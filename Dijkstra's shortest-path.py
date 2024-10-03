### set each node i a three-item tuple (tail,weight,head) in heap to extra keep track of weight and tail of each V-X node
### important assumption : all edges must be non-negative


from collections import defaultdict
import math
import tkinter.filedialog


### Format of a heap node: (head, distance from source node, tail) ###
class MinHeap:
    def __init__(self,array,maxsize):
        self.heap = array
        self.max_size = maxsize
        self.cur_size = 0
        self.build_heap()

    

    ## transform array to heap ( = array that complies with heap properties) ; part of the __init__ method
    def build_heap(self):
        self.cur_size = len(self.heap)
        for i in range(len(self.heap)//2 -1,-1,-1):  # since all the leaves inherently (by definition )satify the heap property, it's only the non-leave nodes not satifying
                                                     # thus you only need to recurse on these nodes
            self.heapify(i)                          # i is the INDEX OF HEAP, not the node number of tail node


    ## check & restore the heap properties of the node i
    def heapify(self,i):
        ## no need to heapify if the heap is exhausted
        if len(self.heap) == 0 :
            print('heap exhausted, all nodes searched')
            return
        
        i_key = self.heap[i][1]

        l_child, r_child = self.child(i)

        ## compare the parents and the child ;
        ## if child is larger than the parent, heap properties are violated, need a swap and further checking
        min_node, min_val = i, i_key
        if l_child < self.cur_size and self.heap[l_child][1] < min_val :
            min_node, min_val = l_child, self.heap[l_child][1]
        if r_child < self.cur_size and self.heap[r_child][1] < min_val :
            min_node, min_val = r_child, self.heap[r_child][1]

        if min_node != i:
            self.heap[i], self.heap[min_node] = self.heap[min_node], self.heap[i]
            self.heapify(min_node)


    ## for insertion of nodes
    def bubble_up(self,i):
        i_weight = self.heap[i][1]
        
        parent = self.parent(i)
        if i > 0 and self.heap[parent][1] > i_weight:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubble_up(parent)

    ## for deletion of nodes
    def bubble_down(self,i):
        self.heapify(i)
            
        
    
    ## return the two childs of the given node i
    def child(self,i):
        l_child = 2*i + 1
        r_child = 2*i + 2
        return (l_child, r_child)

    ## return the parent of the given node i
    def parent(self,i):
        parent = (i-1) // 2
        return parent

    ## addition of one node ; achieved by adding to the bottom and bubble-up
    def insert_key(self,tuple_node):
        self.heap.append(tuple_node)
        self.cur_size +=1
        self.bubble_up(self.cur_size-1)

    ## deletion of one node ; achieved by switching with the bottom and bubble-down the new node at i 
    def delete_key(self,i):
        if i > self.cur_size - 1 : print ('To-be-deleted node does not exist!!!!')
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.cur_size -= 1
        self.heap.pop()
        self.bubble_down(i)

    ## modify the value of a node
    def modify_key(self,i,new_value):      
        if i > self.cur_size - 1 : print ('To-be-deleted node does not exist!!!!')
        old_node_tuple = self.heap[i]
        old_value = old_node_tuple[1]
        self.heap[i] = old_node_tuple[0],new_value,old_node_tuple[2]
        if new_value < old_value :
            self.bubble_up(i)
        if new_value > old_value :
            self.bubble_down(i)

    ## extract root
    def extract_min(self):
        root = self.heap[0]
        self.delete_key(0)
        return root

    ## return a boolean indicating if heap is empty
    def is_empty(self):
        if self.cur_size == 0: return True
        else: False

    ## for printing out the heap structure
    def print_heap(self):
        print(self.heap[:self.cur_size])


    

class DijkstraSP():
    def __init__(self,graph,s):                                  ## s = start node; the origin of the shortest path
        self.aj_list = graph
        self.processed_node = {s}                                ## set of X, containg nodes with guaranteed shortest path
        self.node_distance = defaultdict(lambda: math.inf)
        self.node_distance[s] = 0                                ## for storage of guaranteed shortest path, used for Dikstra's greedy Criterion 
        self.temp_distance = defaultdict(lambda: math.inf)       ## for temporary storage of unguaranteed shortest path during frontier expansion
        self.node_path = defaultdict(list)                       ## for bookkeeping the path to each node
        self.node_path[s].append(s)
        self.create_heap(s)
        
    ## create heap using MinHeap Class (part of initialization)
    def create_heap(self,s):
        array = []
        for neighbour,weight in self.aj_list[s]:
            array.append((neighbour, self.node_distance[s]+int(weight),s ))             ## format of a heap node: (head, distance from source node, tail)
        self.H = MinHeap(array,300)
        
        
    ## thanks to the minHeap properties, popping the root of self.Heap always give the minimium path edge lvw
    ## ... we can easily obtain the shortest edge by simply heapifying the heap after extract-min(root removal)
    ## ... which only costs O(m+n) time ; compared to the traditional Dijkastra's linear search of min. edge among all edges of every nodes O(mn)
    def add_new_min(self):
        min_node, min_path, tail = self.H.extract_min()                 ## v* = min_node ; w* = tail
        self.processed_node = self.processed_node | {min_node}
        self.node_distance[min_node] = min_path
        self.node_path[min_node] = self.node_path[tail]+[min_node]
        self.temp_distance[min_node] = float('inf')

        ## frontier expansion: update the 'frontier' by heap_inserting nodes with inbounding edges from w*
        for neighbour,weight in self.aj_list[min_node]:
            neighbour_path = self.node_distance[min_node] + int(weight)         ## Dijkstra's Greedy Criterion ##
            #print(f'new_distance:{neighbour_path}, old_distance:{self.temp_distance[neighbour]}')
            if neighbour not in self.processed_node and neighbour_path < self.temp_distance[neighbour]:     ## Local competition: only keep the min. path for each contested head
                self.temp_distance[neighbour] = neighbour_path
                self.H.insert_key((neighbour,neighbour_path,min_node))
            
    def main_algo(self):
        # keep extracting min until no more vertices can be extracted (i.e. V-X is exhausted (exckuding inaccessable nodes))
        while not self.H.is_empty():
            #self.H.print_heap()
            self.add_new_min()



### data input from .txt is in the format of (tail,weight)
def txt_to_aj_list():
    filename = tkinter.filedialog.askopenfilename()
    file = open(filename,'r')
    aj_list = defaultdict(list)
    count = 0
    for line in file:
        node_series = line.split('\t')
        tail = node_series[0] 
        for value in node_series[1:-1]:
            head, weight = value.split(',')
            aj_list[tail].append((head,weight))
        count += 1
        if count == 300 : break                              #### LIMITER ####
    file.close()
    return aj_list
        



    
    
aj_list = txt_to_aj_list()

Heap_real = DijkstraSP(aj_list,'1')
Heap_real.main_algo()

print('-'*50,'\n')
print(sorted(list(Heap_real.node_distance.values()),reverse=True)[:20])
print(Heap_real.node_path)

print('end')
