### Function: Count number of inverted element, not necessarily neighbour, in a given array
### ... Divide-and-Conquer : Partition the array into segment L and R
### ... characterised inversion into three type (sub-problem): a) Inversion at L; b) SplitInversion ; c) Inversion at R
### ... a) & c) can be dissolved into recursive call ; to solve b) , we need to piggyback the MergeSort Algorithm
### ... i.e. during merge stage of MergeSort between sorted list A and B, the number of split inversion equals to the sum of remaining elements in array A upon removal of element in array B
### ... conquer by a) + b) + c) ; return sorted array and no. of inversion

array = [9,7,6,3,4,2,1,5,8]

def ArrayInversion(array):

    # Base Case: array length = 1
    if len(array) == 1 :
        return array, 0

    # Divide: Partion and characterise
    else:
        n = len(array)
        half = n // 2

        left_array = array[:half]
        right_array = array[half:]

        sorted_L, inversion_L = ArrayInversion(left_array)
        sorted_R, inversion_R = ArrayInversion(right_array)
        
    # Conquer: Process Sub-problem result and combine
        # Sorting & SplitInversion Count
        sorted_array = []
        split_inversion = 0
        for i in range(n):
            if len(sorted_L) != 0 and len(sorted_R) != 0:
                candidate = min(sorted_L[0],sorted_R[0])
                sorted_array.append(candidate)
                if candidate in sorted_L :
                    sorted_L.remove(candidate)
                else:
                    sorted_R.remove(candidate)
                    split_inversion += len(sorted_L)
            elif len(sorted_L) == 0:
                sorted_array.append(sorted_R[0])
                sorted_R.remove(sorted_R[0])
            elif len(sorted_R) == 0:
                sorted_array.append(sorted_L[0])
                sorted_L.remove(sorted_L[0])
    
        inversion = inversion_L + split_inversion + inversion_R
        print(inversion_L , split_inversion , inversion_R)
        return sorted_array, inversion

    

##---------------------------------

import time

time_start = time.time()
MS_inversion = ArrayInversion(array)
time_end = time.time()

print('By MergeSortInversion: ' ,'\n',  MS_inversion)
print(f"Execution time: {time_end - time_start} seconds \n")




time_start = time.time()
BS_inversion = 0
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            BS_inversion += 1
time_end = time.time()

print('By BruteForce: ' ,'\n',BS_inversion)
print(f"Execution time: {time_end - time_start} seconds \n")
