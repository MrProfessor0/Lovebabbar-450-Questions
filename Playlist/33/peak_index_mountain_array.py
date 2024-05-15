from typing import List

def peak_index(arr,start,end):
    # print(start,end)
    if start>=end:
        return start

    mid = start+(int((end-start)/2))

    if arr[mid] < arr[mid+1]:
        return peak_index(arr,mid+1,end)
    else:
        return peak_index(arr,start,mid)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        print("Inside:",end=" ")
        print(arr)
        return peak_index(arr,0,len(arr)-1)



# arr = [0,10,5,2]
arr = [0,1,2,4,6,8,10,9]

print(Solution().peakIndexInMountainArray(arr))