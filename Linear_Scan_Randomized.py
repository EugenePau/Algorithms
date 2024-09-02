## Find the ith smallest element of an input array under O(n) running time
## ... this algo simply piggybacks the partitioning method from QuickSort: after each round of sorting, the pivot must be at the right position
## ... if i < pivot_pos => call the L sub-array ; if i > pivot_pos => call the R sub-array
## ... similar to QuickSort, best partitioning is to have the median as pivot O(n) [Case 2] ; worst case is to have 1st / last element as pivot O(n^2)
## ...... randomization of pivot choice indeed yields an average O(n) running time, similar to how randomization benefits QuickSort
## ...... key idea of the proof is to compute the number of recursive calls needed until the input array size decreases to < 75% ; denote a completion as ending of a phase j
## ...... such number is the expected value of a geometric random variable
## ...... summation of (operation in each call)*(no. of call for each phase)*(no. of phase) gives the total running time


def LinearSelect(array,i):

    n = len(array)

    ## base case
    if n <= 1 :
        return array[0]

    ## general case
    else:
        ## choose pivot
        candidate = [array[0], array[(n-1)//2], array[-1]]
        candidate.remove(max(candidate))
        candidate.remove(min(candidate))
        pivot = candidate[0]
        
        pivot_pos = array.index(pivot)

        ## swap pivot to be 1st element
        array[0], array[pivot_pos] = array[pivot_pos], array[0]

        ## partitioning
        print(array)
        R_boundary = 1
        for j in range(1,n):
            if array[j] < pivot:
                array[j],array[R_boundary] = array[R_boundary], array[j]
                R_boundary += 1

        ## swap pivot to be between L & R
        array[0], array[R_boundary-1] = array[R_boundary-1], array[0]
        print(array[:R_boundary-1],[pivot],array[R_boundary:])

        ## Check if pivot is the target
        pivot_order = R_boundary - 1
        target = i-1

        if pivot_order == target : return pivot
        elif target < pivot_order : return LinearSelect(array[:pivot_order],i)
        elif target > pivot_order : return LinearSelect(array[(pivot_order+1):],target-pivot_order)                


array = [43, 98, 55, 74, 81, 40, 67, 26, 87, 96, 53, 94, 58, 22, 37, 13, 73, 79, 91, 59, 27, 42, 10, 90, 44, 1, 24, 28, 6, 61, 19, 5, 41, 51, 78, 76, 30, 11, 66, 56, 54, 89, 84, 82, 38, 60, 93, 95, 21, 62, 75, 23, 25, 50, 46, 70, 16, 35, 20, 68, 85, 52, 39, 83, 64, 7, 45, 0, 92, 12, 77, 15, 63, 57, 47, 32, 17, 4, 3, 34, 33, 31, 9, 14, 72, 2, 69, 88, 80, 97, 65, 86, 29, 36, 18, 71, 8, 99, 49, 48]
sol = LinearSelect(array,64)
print(sol)
