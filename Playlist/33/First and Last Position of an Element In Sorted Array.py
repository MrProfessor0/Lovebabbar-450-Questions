"""
Sample Input 1:
8 2
0 0 1 1 2 2 2 2

Sample output 1:
4 7

Explanation of Sample output 1:

For this testcase the first occurrence of 2 in at index 4 and last occurrence is at index 7.
"""


from os import *
from sys import *
from collections import *
from math import *

def first_occurance(arr,start,end,k,ans):
    # ans = -1
    if start>end:
        return ans
    
    mid = start + int((end-start)/2)
    # print(mid,start,end,k,ans)

    if arr[mid] == k:
        ans = mid
        return first_occurance(arr,start,mid-1,k,ans)
    if arr[mid] < k:
        return first_occurance(arr,mid+1,end,k,ans)
    if arr[mid] > k:
        return first_occurance(arr,start,mid-1,k,ans)

def last_occurance(arr,start,end,k,ans):
    if start>end:
        return ans
    
    mid = start + int((end-start)/2)

    if arr[mid] == k:
        ans = mid
        return last_occurance(arr,mid+1,end,k,ans)
    if arr[mid] < k:
        return last_occurance(arr,mid+1,end,k,ans)
    if arr[mid] > k:
        return last_occurance(arr,start,mid-1,k,ans)

def firstAndLastPosition(arr, n, k):

    # Write your code here
    first = first_occurance(arr,0,n,k,-1)
    # last = last_occurance(arr,n,k)
    last = last_occurance(arr,0,n,k,-1)

    print(first,last)





arr = [0,0,1,1,2,2,2,2]
k = 2

# arr = [1,3,3,5]
# k = 2

firstAndLastPosition(arr,len(arr)-1,k)
