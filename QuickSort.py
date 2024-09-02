## Compared to MergeSort, QuickSort requires much less memory space, since sorting is directly done at the divide stage instead of at the conquer step
## ... it also showcases with the involvement of randomization ; the expected value of running time is still O(nlogn)

## QuickSort partition the input array with a randomly chosen pivot
## ... then do a linear scan [O(n)] across the array to compare & swap elements with value smaller than pivot to be located at left of the pivot (L) , and those with larger values to be at right of the pivot (R)
## ... pivot is immediately at the correct position at the end of the current call ; then recursively call the L & R sub-array until base case (n=1) is reached
## ... no computation in combine / conquer step is needed ; this is the biggest difference with the MergeSort
## ...... the best case is that the pivot is magically always the median of the input array [theta(nlogn)], the worst case is that always the 1st element is chosen as the pivot [theta(n^2)]
## ...... with a randonly chosen pivot during each call, the expected value of 'no. of comparison' is upper-bounded by 2n*ln(n) [proof relies on Linearity of Expectation, Indicator Random Variable, Inequality, Integration by definition]
## ...... since running time in QuickSort is dominated by 'no. of comparison', so the running time is also O(nlogn) in average


def QuickSort(array):

    n = len(array)
    
    ## base case
    if n <= 1: return array

    ## general case
    else:
        ## choose pivot case
        pivot_case = 'median'
        
        if pivot_case == '1st' : pivot_pos = 0
        if pivot_case == 'last' : pivot_pos = -1
        if pivot_case == 'median' :
            candidate = [ array[0],array[-1],array[(n-1)//2] ]
            candidate.remove(max(candidate))
            candidate.remove(min(candidate))
            pivot_pos = array.index(candidate[0])

        ## put pivot to be the first element of array, then partition around p
        array[0], array[pivot_pos] = array[pivot_pos], array[0]
        pivot = array[0]
        i = 1
        for j in range(1,n):
            if array[j] < pivot :
                array[j],array[i] = array[i],array[j]
                i += 1
        array[0],array[i-1] = array[i-1],array[0]

        ## recursive call L & R
        print(array[:i-1],[pivot],array[i:])
        sorted_array = QuickSort(array[:i-1]) + [pivot] + QuickSort(array[i:])
        return sorted_array

array = [7,9,1,3,4,6,2,5,8]
sol = QuickSort(array)
print(sol)



