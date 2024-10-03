## example : Entered 6 keys: 3, 10, 12, 8, 2, 14
## max heap or min heap


class MaxHeap:
    def __init__(self,array,maxsize):
        self.heap = array
        #self.heap = self.build_heap(array)
        self.max_size = maxsize
        self.cur_size = 0
        self.build_heap()

    

    ## transform array to heap ( = array that complies with heap properties) ; part of the __init__ method
    def build_heap(self):
        self.cur_size = len(self.heap)
        for i in range(len(self.heap)//2 -1,-1,-1):  # since all the leaves satify the heap property, it's only the non-leave nodes not satifying
                                                     # thus you only need to recurse on these nodes
            self.heapify(i)

    ## for printing out the heap structure
    def print_heap(self):
        print(self.heap[:self.cur_size])

    ## check & restore the heap properties of the node i
    def heapify(self,i):
        l_child, r_child = self.child(i)

        ## compare the parents and the child ;
        ## if child is larger than the parent, heap properties are violated, need a swap and further checking
        max_node, max_val = i, self.heap[i]
        if l_child < self.cur_size and self.heap[l_child] > max_val :
            max_node, max_val = l_child, self.heap[l_child]
        if r_child < self.cur_size and self.heap[r_child] > max_val :
            max_node, max_val = r_child, self.heap[r_child]

        if max_node != i:
            self.heap[i], self.heap[max_node] = self.heap[max_node], self.heap[i]
            self.heapify(max_node)

    ## for insertion of nodes
    def bubble_up(self,i):
        parent = self.parent(i)
        if i > 0 and self.heap[parent] < self.heap[i]:
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
    def insert_key(self,value):
        self.heap.append(value)
        self.cur_size +=1
        self.bubble_up(self.cur_size-1)

    ## deletion of one node ; achieved by switching with the bottom and bubble-down the new node at i 
    def delete_key(self,i):
        if i > self.cur_size - 1 : print ('To-be-deleted node does not exist!!!!')
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.cur_size -= 1
        self.bubble_down(i)

    ## modify the value of a node
    def modify_key(self,i,new_value):
        if i > self.cur_size - 1 : print ('To-be-deleted node does not exist!!!!')
        old_value = self.heap[i]
        self.heap[i] = new_value
        if new_value > old_value :
            self.bubble_up(i)
        if new_value < old_value :
            self.bubble_down(i)

## class inheritance
class MinHeap(MaxHeap):
    def heapify(self,i):
        l_child, r_child = self.child(i)

        ## compare the parents and the child ;
        ## if child is larger than the parent, heap properties are violated, need a swap and further checking
        min_node, min_val = i, self.heap[i]
        if l_child < self.cur_size and self.heap[l_child] < min_val :
            min_node, min_val = l_child, self.heap[l_child]
        if r_child < self.cur_size and self.heap[r_child] < min_val :
            min_node, min_val = r_child, self.heap[r_child]

        if min_node != i:
            self.heap[i], self.heap[min_node] = self.heap[min_node], self.heap[i]
            self.heapify(min_node)

    ## for insertion of nodes
    def bubble_up(self,i):
        parent = self.parent(i)
        if i > 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubble_up(parent)

        
    def modify_key(self,i,new_value):
        if i > self.cur_size - 1 : print ('To-be-deleted node does not exist!!!!')
        old_value = self.heap[i]
        self.heap[i] = new_value
        if new_value < old_value :
            self.bubble_up(i)
        if new_value > old_value :
            self.bubble_down(i)
    


array = [3, 10, 12, 8, 2, 14]
print(array)
H = MaxHeap(array,10)
H.print_heap()
print(f'Current Size: {H.cur_size} ; Max size : {H.max_size}')
print('now insert 20....')
H.insert_key(20)
H.print_heap()
print('now delete node 1....')
H.delete_key(1)
H.print_heap()
print('now modify node 1 to be 5....')
H.modify_key(1,5)
H.print_heap()
