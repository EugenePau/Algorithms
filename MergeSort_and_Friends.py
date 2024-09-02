## MergeSort, canoical Divide-and-Conquer Algorithm, with running time of mostly ( log(2,n)+1 )*(6n)
## ... note that for small input size, conventional sorting algorithm (with running time 0.5n^2) is faster than MergeSort; but this is not the domain where fast algorithm is interested
## ... turn-over point is at around input size of 90

import time
import tkinter.filedialog

filename = tkinter.filedialog.askopenfilename()
file = open(filename,'r')

array = []
for line in file:
    array.append(int(line))

visualisation_toggle = 0

## Assumption 1 : Input array size must be in multiples of 2 
## Assumption 1 Break Lemma: Any positive integers except 1 can be expressed by 2x + 3y
## Idea: Halve until an odd-length candidate; slice such candidate into one by //2 (smaller & even); and the remaining one (bigger & odd)
## ... The above division will eventually arrives a parent with child of size 2 and 3 (lemma)
## ... no modification is needed to generalise the algorithm's scope to any arbitary size

## Assumption 2: Discrete element in array
## Assumption 2 Break: The code simply does not rely discreteness of array values

def MergeSort(arr):
    n = len(arr)
    # Base Case: Size of child-array = 1
    if n == 1 :
        return arr
    # 'Divide' Step: Halve the parent array and recursive call the child arrays
    child_1 = MergeSort( arr[:(n//2)] )
    child_2 = MergeSort( arr[(n//2):] )
    # 'Conquer' Step: compare the left-most element from the two child list, write-in the smaller one into the parent
    # pointer proceed to next element of the list containing the winner 
    c1_counter = 0
    c2_counter = 0
    for i in range(len(arr)):
        ## Critical Line: A or ( B and C ) , where C is vulnerable
        ## ... therefore, use A , B as Guard signifying terminal conditions; i.e. +ve A guards A or ( B and C ), then -ve B guards ( B and C )  
        if  c2_counter == len(child_2) or ( not c1_counter == len(child_1)  and child_1[c1_counter] < child_2[c2_counter] ) :
            arr[i] = child_1[c1_counter]
            c1_counter += 1
        else:
            arr[i] = child_2[c2_counter]
            c2_counter += 1
    return arr

array_m = array.copy()

time_start = time.time()
Msort = MergeSort(array_m)
time_end = time.time()



print('By MergeSort: ' ,'\n',  Msort)
print(f"Execution time: {time_end - time_start} seconds \n")


###################

## Ordinary Algorithm: Selection Sort

def SelectionSort(arr):
    ## Construct a double nested loop i & j: j search and record the historical minimum canditate of the loop, the winner swaps position with i
    for i in range(len(arr)):
        min_value, min_index = arr[i], i 
        for j in range(i,len(arr)):
            if arr[j] < min_value:
                min_value, min_index = arr[j], j
        arr[min_index],arr[i] = arr[i],min_value
        if visualisation_toggle == True : print(i,arr)
    return arr

array_s = array.copy()

time_start = time.time()
SSort = SelectionSort(array_s)
time_end = time.time()

print('By Selection Sort:' ,'\n',  SSort)
print(f"Execution time: {time_end - time_start} seconds \n")


###################


## Ordinary Algorithm: Insertion Sort

def InsertionSort(arr):
    ## The algo compares i with its immediate predecessor. If the predecessor is greater than i, they swap with each other.
    ## Repeat until a failure of such condition; Proceed to the next i loop 
    for i in range(1,len(arr)):
        compare = i - 1
        while compare >= 0 and arr[compare] > arr[compare + 1]:
            arr[compare],arr[compare + 1] = arr[compare + 1],arr[compare]
            compare -= 1
        if visualisation_toggle == True: print(i,arr)
    return arr
            

array_i = array.copy()

time_start = time.time()
ISort = InsertionSort(array_i)
time_end = time.time()

print('By Insertion Sort:' ,'\n',  ISort)
print(f"Execution time: {time_end - time_start} seconds \n")

###################


## Ordinary Algorithm: Bubble Sort

def BubbleSort(arr):
    ## The algo compares i with its immediate successor. If the successor is greater than i, they swap with each other.
    ## Rinse and repeat until a loop with no swap occured; terminate function
    while True:
        sort = 'complete'
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort = False
        if visualisation_toggle == True: print(arr)
        if sort == 'complete': return arr

array_b = array.copy()

time_start = time.time()
BSort = BubbleSort(array_b)
time_end = time.time()

print('By Bubble Sort:' ,'\n',  BSort)
print(f"Execution time: {time_end - time_start} seconds \n")
