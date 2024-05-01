from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    arr_swap = list(arr)
    start = m+1
    end = len(arr)-1
    
    while(start<end):
        arr_swap[start],arr_swap[end] = arr_swap[end], arr_swap[start]
        start += 1
        end -= 1
    
    print(arr_swap)



# arr = [1, 4, 5, 6, 6, 7, 7 ]
# m = 3
# 1 4 5 6 7 7 6 

arr = [10, 4, 5, 2, 3, 6, 1, 3, 6]
m = 3
# 10 4 5 2 6 3 1 6 3 
reverseArray(arr,m)