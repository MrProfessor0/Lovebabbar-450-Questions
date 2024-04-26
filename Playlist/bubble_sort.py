from os import *
from sys import *
from collections import *
from math import *

def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    print("arr: ",end=" ")
    print(arr)
    count = 0
    for i in range(0,n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                count += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

        print(arr)
    print(count)

arr = [8, 22, 7, 9, 31, 5, 13]
bubbleSort(arr,len(arr))