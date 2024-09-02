## The Algorithm is to find out the shortest-distance pair from a set of node, applicable to computer vision & graphics ; O(nlogn)
## ASSUMPTION all nodes are DISTINCT in x- & y-coordinate


## The input set of point P is preliminarily sorted into Px, Py which is in ascending order according to their x- & y-coordinate respectively
## ... Upon function call ClosestPair(Px, Py), Partition P into two groups: Left Half Q and Right Half R
## ... Relabel nodes in Q to Qx, Qy and nodes in R to Rx, Ry ; Recursive Call ClosestPair(Qx, Qy) & ClosestPair(Rx, Ry)
## ...... Base Case is reached to if Qx, Qy remains 2 or 3 nodes ; in such case solve by BruteForce (Euclidean Pythagorean)
## ... SplitClosesetPair(Px,Py,d) caters to cross-group shortest-distance pair ; d as the less of shortest-pair from R & Q
## ...... Rule 1: narrow down scope by filtering Px, Py to make Sy which only contains nodes in range [X-d, X+d] ; X as the rightmost mode in Q ; Sy sorted by y-coordinate
## ...... Rule 2: if closeset pair is split, then no pair in Q or R per se has distance smaller than d.
## ...... then all possibility of nodes in Sy are confined to an 8-mesh space spanning height of d and width of 2d [Rule 1], and each mesh hosts at most 1 node [Rule 2]
## ...... this concludes the closest pair at most differ by 7 in index of Sy ; s.t. a repeated scan of 8 consecutive nodes in Sy each time suffices and the historical lowest record is the anwser
## ... function returns min of { ClosestPair(Qx, Qy), ClosestPair(Rx, Ry), SplitClosesetPair(Px,Py,d) }

import tkinter.filedialog
import math

## Use Desmo to visualise nodes

input_node = [(417, 312), (469, 185), (459, 143), (471, 118), (50, 470), (404, 52), (258, 381), (434, 79), (48, 274), (240, 42), (285, 407), (322, 64), (255, 284), (165, 14), (315, 360), (2, 365), (85, 208), (222, 222), (455, 42), (172, 0), (341, 421), (204, 78), (359, 97), (101, 405), (272, 319), (472, 6), (406, 325), (123, 64), (12, 33), (477, 172), (219, 44), (415, 106), (478, 113), (170, 89), (156, 401), (310, 271), (330, 274), (67, 390), (261, 465), (268, 314), (488, 244), (105, 280), (177, 391), (382, 231), (436, 153), (479, 459), (357, 11), (279, 15), (366, 26), (310, 148), (392, 419), (415, 164), (317, 312), (340, 310), (423, 31), (351, 251), (400, 151), (308, 81), (257, 237), (337, 495), (223, 372), (175, 367), (23, 173), (353, 472), (375, 85), (87, 489), (354, 276), (266, 116), (446, 448), (235, 251), (284, 391), (495, 145), (288, 101), (478, 158), (368, 322), (265, 121), (122, 350), (323, 132), (161, 266), (226, 428), (218, 470), (84, 183), (344, 198), (91, 192), (338, 134), (272, 100), (342, 237), (492, 197), (30, 104), (320, 214), (198, 388), (162, 328), (100, 85), (438, 404), (182, 412), (63, 331), (144, 263), (324, 436), (17, 355), (96, 424), (428, 342), (204, 437), (362, 178), (474, 467), (277, 291), (330, 85), (253, 98), (386, 181), (212, 159), (335, 161), (381, 366), (417, 101), (122, 47), (180, 56), (148, 159), (368, 201), (276, 408), (167, 248), (113, 440), (281, 347), (120, 223), (311, 297), (130, 354), (69, 141), (105, 335), (96, 208), (225, 4), (78, 40), (292, 429), (325, 297), (26, 360), (5, 399), (301, 253), (158, 369), (283, 263), (144, 321), (62, 62), (412, 427), (22, 4), (173, 380), (497, 436), (421, 429), (130, 202), (379, 378), (414, 163), (172, 351), (210, 496), (184, 180), (475, 448), (376, 299), (426, 28), (92, 9), (101, 440), (357, 328), (109, 495), (282, 224), (393, 63), (387, 239), (147, 6), (46, 304), (469, 80), (49, 207), (318, 320), (426, 74), (35, 137), (154, 56), (335, 367), (47, 87), (241, 149), (199, 218), (380, 313), (335, 176), (308, 320), (331, 437), (39, 73), (410, 181), (162, 137), (451, 360), (169, 496), (0, 48), (141, 239), (421, 125), (95, 100), (375, 198), (159, 67), (305, 394), (4, 102), (340, 101), (472, 194), (350, 410), (17, 460), (140, 30), (465, 341), (346, 402), (122, 473), (284, 291), (109, 96), (251, 118), (431, 336), (448, 302)


## Support: MergeSort Algorithm (catered to tuple)

def MergeSort_tuple_x(array):
    
    ## Base Case
    if len(array) == 1:
        return array
    ## Recursive
    else:
        n = len(array)
        half = n//2
        left_array = array[:half]
        right_array = array[half:]

        sorted_L = MergeSort_tuple_x(left_array)
        sorted_R = MergeSort_tuple_x(right_array)

        sorted_array = []
        i,j = 0, 0
        ## i for sorted_L ; j for sorted_R ; [0] for x-coodinate
        for k in range(len(array)):
            if i == len(sorted_L):
                sorted_array.append(sorted_R[j])
                j += 1
            elif j == len(sorted_R):
                sorted_array.append(sorted_L[i])
                i += 1
            elif sorted_L[i][0] < sorted_R[j][0]:
                    sorted_array.append(sorted_L[i])
                    i += 1
            elif sorted_L[i][0] >= sorted_R[j][0]:
                    sorted_array.append(sorted_R[j])
                    j += 1

        return sorted_array

def MergeSort_tuple_y(array):
    
    ## Base Case
    if len(array) == 1:
        return array
    ## Recursive
    else:
        n = len(array)
        half = n//2
        left_array = array[:half]
        right_array = array[half:]

        sorted_L = MergeSort_tuple_y(left_array)
        sorted_R = MergeSort_tuple_y(right_array)

        sorted_array = []
        i,j = 0, 0
        ## i for sorted_L ; j for sorted_R ; [1] for y-coodinate
        for k in range(len(array)):
            if i == len(sorted_L):
                sorted_array.append(sorted_R[j])
                j += 1
            elif j == len(sorted_R):
                sorted_array.append(sorted_L[i])
                i += 1
            elif sorted_L[i][1] < sorted_R[j][1]:
                    sorted_array.append(sorted_L[i])
                    i += 1
            elif sorted_L[i][1] >= sorted_R[j][1]:
                    sorted_array.append(sorted_R[j])
                    j += 1

        return sorted_array
            
            
        

## Preliminary Sorting of Px, Py

Px = MergeSort_tuple_x(input_node)
Py = MergeSort_tuple_y(input_node)
print(f"Px: {Px}\nPy: {Py}")
    
            
## Function

def ClosestPair(Px,Py):

    n = len(Px)

    ## Base Case
    if n == 2 or n ==3 :
        lowest_pair = None
        lowest_record = float('inf')
        for i in range(n-1):
            for j in range(i+1,n):
                current_distance = math.hypot((Px[i][0] - Px[j][0]),(Px[i][1] - Px[j][1]))
                if current_distance < lowest_record:
                    lowest_pair = (Px[i],Px[j])
                    lowest_record = current_distance


    ## Partition into Qx, Qy & Rx, Ry for recursive calling
    else:
        half = n // 2
        Qx = Px[:half]
        Rx = Px[half:]
        Qy = [i for i in Py if i in Qx]
        Ry = [i for i in Py if i in Rx]

        Q_pair, Q_record = ClosestPair(Qx,Qy)
        R_pair, R_record = ClosestPair(Rx,Ry)

        ## Split-Pair Px, Py, d, x_pivot
        d = min(Q_record, R_record)
        x_pivot = Qx[-1][0]

        ## Select Sy by filtering Py with [x_pivot - d, x_pivot + d]
        Sy = []
        for i in Py:
            if x_pivot - d <= i[0] <= x_pivot + d:
                Sy.append(i)
                
        ## Split-pair by most differ from 7 in index of Sy
        ## i as start of the at-most-8-consecutive 'cell' , j as 2nd-to-last of the at-most-8-consecutive 'cell' ; if no. of cell is lower than 8, i = 1 , j = 2nd-to-last 'cell'
        ## ... i should stop at the penultimate 'cell' so that every 2-pair has been gone through
        ## ... although a nested 2 for-loop is used here, it is still considered O(n) since the inner loop is a small constant loop compared to a n-length of loop
        ## ... such effect is more prominent for large n
        split_pair = None
        split_record = float('inf')
        for i in range(len(Sy)-1):
            for j in range(i+1,i+min(8,len(Sy)-i)):
                current_distance = math.hypot((Sy[i][0] - Sy[j][0]),(Sy[i][1] - Sy[j][1]))
                if current_distance < split_record:
                    split_pair = (Sy[i],Sy[j])
                    split_record = current_distance

        ## Return min of {Q_pair, R_pair, split_pair} (and optionally the value)
        checklist = [(Q_pair, Q_record),(R_pair, R_record),(split_pair, split_record)]      
        lowest_record = min(Q_record, R_record, split_record)
        for i in checklist:
            if lowest_record == i[1]:
                lowest_pair = i[0]
                
    return lowest_pair,lowest_record

    
ans = ClosestPair(Px,Py)
print(ans)
